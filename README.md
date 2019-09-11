# OpenSource-Lichess-Bot

This Bot can help you playing on lichess during real time games with a real time graphic interface with the best moves
according to the newest stockfish chess engine

# Requirements

- python >= 3

- look at the requirements.txt for the python libraries

- registered DeveloperApp (see how to create one in the section below)

- Lichess account

# Create a Lichess webApp

1) go to https://lichess.org/account/oauth/app/create
2) create a webApp setting Callback URL to http://127.0.0.1:8080

 <p align="center">
  <img src="https://i.ibb.co/tKrTCfw/Annotazione-2019-09-10-113314.png" alt="logo">
</p>
3) copy and paste client id and client secret in the src/create_unlimited_session.py file

 <p align="center">
  <img src="https://i.ibb.co/cr68MN5/Annotazione-2019-09-10-113903.png" alt="logo">
</p>

# Save your session and use it whenever you want

you can now run src/create_unlimited_session.py
it will create a .bin file in the bin directory with the session of your logged lichess account
and now running src/use_id_session.py you can get all information about your logged account

# Next implementations

- Graphic interface
- Connect stockfish backend engine with the interface
