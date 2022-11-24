# https://www.starlette.io/testclient/#testing-websocket-sessions
from app.routers.websocket import manager

def test_websocket_rooms(client):
    with client.websocket_connect('/ws') as websocket:
        # the testclient is connected via ws. therefore a request to 
        # websocket/info should show one client connected
        response_get_info = client.get("/api/websocket/info")
        assert response_get_info.status_code == 200 
        assert len(response_get_info.json()['default']) == 1

        #invalid json
        data = "notjson"
        websocket.send_text(data)
        resp = websocket.receive_json(mode='text')
        assert resp['success'] == False
        assert resp['error'] == "invalid_schema"
        assert "not json" in resp['description']

        #json that is not a dict
        data = [1,3,3,7]
        websocket.send_json(data, mode='text')
        resp = websocket.receive_json(mode='text')
        assert resp['success'] == False
        assert resp['error'] == "invalid_schema"
        assert "dict" in resp['description']

        #invalid data in dict json
        data = {
            "invalid": "data"
        }
        websocket.send_json(data, mode='text')
        resp = websocket.receive_json(mode='text')
        assert resp['success'] == False
        assert resp['error'] == "invalid_schema"

        #connect to new room A
        data = {
            "command": "subscribe",
            "data": {
                "room": "room_a"
            }
        }
        websocket.send_json(data, mode='text')
        resp = websocket.receive_json(mode='text')
        assert resp['success'] == True

        # websocket/info should show one client connected to default,
        # and one client connected to room_a
        response_get_info = client.get("/api/websocket/info")
        assert response_get_info.status_code == 200 
        assert len(response_get_info.json()['default']) == 1
        assert len(response_get_info.json()['room_a']) == 1

        #broadcast to new room A
        #TODO: test reponse, hard without asyncio

        #leave all rooms
        data = {
            "command": "unsubscribe_all",
        }
        websocket.send_json(data, mode='text')
        resp = websocket.receive_json(mode='text')
        assert resp['success'] == True

        #leave a random room we are not even subscribed to
        #should return success
        data = {
            "command": "unsubscribe",
            "data": {
                "room": "a_random_room"
            }
        }
        websocket.send_json(data, mode='text')
        resp = websocket.receive_json(mode='text')
        assert resp['success'] == True

        #close connection
        websocket.close()

    #no connection should be registered
    response_get_info = client.get("/api/websocket/info")
    assert response_get_info.status_code == 200 
    assert len(response_get_info.json()['default']) == 0