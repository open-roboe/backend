""" All the websocket apis and the connection manager are defined here

Usage:
from app.routers.websocket import manager
manager.broadcast_room("room_name", "message json string")

"""
from typing import Any
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.logger import logger
from app.models.api import WsAPIError, WsAPIRequest, WsApiResponse
from pydantic import ValidationError
import json
import pprint

router = APIRouter(prefix='/api/websocket', tags=['websocket'])


class ConnectionManager:
    # default room assigned to all new websocket connections
    DEFAULT_ROOM = "default"

    def __init__(self):
      # rooms, that a websocket connection can subscribe to
      self.rooms: dict[str, list[WebSocket]] = {}
      #initialize the default room
      self.rooms[self.DEFAULT_ROOM] = []

    def get_info(self):
      ret = {}
      for room_name, room_content in list(self.rooms.items()):
        ret[room_name] = [pprint.pformat(x) for x in room_content]
      return ret

    def _remove_from_all_rooms(self, websocket: WebSocket):
      for room_name, room_content in list(self.rooms.items()):
        self.unsubscribe(websocket, room_name)

    async def connect(self, websocket: WebSocket):
        """ accept the websocket, and Start tracking it by subscribing it to
            the default room
        """
        await websocket.accept()
        self.rooms[self.DEFAULT_ROOM].append(websocket)

    def disconnect(self, websocket: WebSocket):
        """ Stop tracking a websocket connection
        """
        self._remove_from_all_rooms(websocket)

    async def send_personal_message(self, message: Any, websocket: WebSocket):
        """ Send a message to a specific connection
        """
        await websocket.send_json(message, mode="text")

    async def broadcast_default(self, message: Any):
        """ Send a message to all the connections that are not subscribed to a room
        """
        self.broadcast_room(self.DEFAULT_ROOM, message)

    async def broadcast_room(self, room_name: str, message: Any):
        """ Send a message to all the connections that are subscribed to a specific room
        """
        if room_name in self.rooms:
          for connection in self.rooms[room_name]:
            await connection.send_json(message, mode="text")

    def subscribe(self, websocket: WebSocket, room_name: str):
      """ Subscribe a connection to a room. This won't unsubscribe from other rooms
      """
      #create room if it does not exist
      if room_name not in self.rooms:
        self.rooms[room_name] = []
      #subscribe to the room
      self.rooms[room_name].append(websocket)

    def unsubscribe(self, websocket: WebSocket, room_name: str):
      if room_name in self.rooms:
        try:
          self.rooms[room_name].remove(websocket)
          # remove the room if it's empty
          if len(self.rooms[room_name]) == 0 and room_name is not self.DEFAULT_ROOM:
            self.rooms.pop(room_name, None)
        except:
          # the object is not in this room
          pass


    def unsubscribe_all(self, websocket: WebSocket):
      """ Unsubscribe a connection from any kind of room, but keep tracking it
      """
      self._remove_from_all_rooms(websocket)
      self.rooms[self.DEFAULT_ROOM].append(websocket)

manager = ConnectionManager()



@router.get("/info")
async def get_info():
  return manager.get_info()


@router.get("/test_client")
async def test_client():
  html = """
  <!DOCTYPE html>
  <html>
      <head>
          <title>Chat</title>
      </head>
      <body>
          <h1>WebSocket Chat</h1>
          <form action="" onsubmit="sendMessage(event)">
              <input type="text" id="messageText" autocomplete="off"/>
              <button>Send</button>
          </form>
          <ul id='messages'>
          </ul>
          <script>
              var ws = new WebSocket("ws://localhost:8080/ws");
              ws.onmessage = function(event) {
                  var messages = document.getElementById('messages')
                  var message = document.createElement('li')
                  var content = document.createTextNode(event.data)
                  message.appendChild(content)
                  messages.appendChild(message)
              };
              function sendMessage(event) {
                  var input = document.getElementById("messageText")
                  ws.send(input.value)
                  input.value = ''
                  event.preventDefault()
              }
          </script>
      </body>
  </html>
  """
  return HTMLResponse(html)



# for some reason, this websocket is accessible at
# python3 -m websockets ws://localhost:8080/ws
# even though the @router has a path of /api/websocket
# this could be a bug in FastAPI
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            #receive a message
            raw_msg = await websocket.receive_text()

            # Try to parse it as json
            try:
              parsed_msg = json.loads(raw_msg)
            except:
              resp = WsAPIError(
                error="invalid_schema",
                description="received data is not json"
              ).dict()
              await manager.send_personal_message(resp, websocket)
              continue

            # make sure the decoded data is a dict
            #TODO: don't allow lists
            if not isinstance(parsed_msg, dict):
              resp = WsAPIError(
                error="invalid_schema",
                description="received json should be a dict"
              ).dict()
              await manager.send_personal_message(resp, websocket)
              continue

            # parse the data against a pydantic model
            try:
              ws_api_request = WsAPIRequest(
                **parsed_msg
              )
            except ValidationError as err:
              resp = WsAPIError(
                error="invalid_schema",
                description=str(err)
              ).dict()
              await manager.send_personal_message(resp, websocket)
              continue

            # listen to commands
            command = ws_api_request.command
            data = ws_api_request.data

            # Request to subscribe to a room
            # example payload:
            # {"command": "subscribe", "data": {"room": "testroom"}}
            if command == 'subscribe':
              if not 'room' in data:
                resp = WsAPIError(
                  error="invalid_schema",
                  description="data.room required"
                ).dict()
                await manager.send_personal_message(resp, websocket)
                continue
              else:
                manager.subscribe(websocket, data['room'])
                await manager.send_personal_message(
                  WsApiResponse().dict(), websocket)

            # Request to subscribe to a room
            # example payload:
            # {"command": "unsubscribe", "data": {"room": "testroom"}}
            if command == 'unsubscribe':
              if not 'room' in data:
                resp = WsAPIError(
                  error="invalid_schema",
                  description="data.room required"
                ).dict()
                await manager.send_personal_message(resp, websocket)
                continue
              else:
                manager.unsubscribe(websocket, data['room'])
                await manager.send_personal_message(
                  WsApiResponse().dict(), websocket)

            #request to unsubscribe from all rooms
            if command == 'unsubscribe_all':
              manager.unsubscribe_all(websocket)
              await manager.send_personal_message(
                WsApiResponse().dict(), websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
