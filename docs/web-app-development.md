# Web app development

You will only need basic knowledge javascript, html and css.o

The webapp is based on [Github's primer css](https://primer.style/css) desing system,
and the Solid.js framework

The api server runs with docker-compose, but knowledge on this technology is not required

## Setting up your local development environment

> This documentation assumes that you already have git installed on your device,
> configured with your github credentials

Install the following software, if you don't have it already

- docker [Download docker desktop](https://docs.docker.com/get-docker/)
- nodejs & npm [windows](https://nodejs.org/en/download/) [linux](https://github.com/nodesource/distributions)

### clone the repository

Execute the command `git clone https://github.com/open-roboe/backend.git`

A `/backend` folder will be generated. You can navigate into it with the command
`cd /backend`


### Initialize the environment variables

Copy the content of the `.env.example` file and paste it into a new `.env` file.
On a terminal this can be done with the command `cp .env.example .env`

This was the last step of the setup. You are now ready to start developing

### Run the api server

- Make sure that your terminal is in the `/backend` folder, where the
docker-compose.yml file is located.
- If you are using windows, make sure the docker desktop app is running

- Execute the command `docker-compose up` to start the app.
  The first time this command may require a couple of minutes.
  
  When completed, the api server will be available at http://localhost:8080.
  The web app is already configured to communicate with it.

  To stop the api server, execute the command `docker-compose down`
