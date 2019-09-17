# TOB
 
TOB is the reverse of BOT and stands for:

Too
Obvius
Bitch

TOB is a lichess Bot that can help you playing (cheating) on lichess during real time games with a real time graphic interface with the best moves
according to the newest stockfish chess engine

- TOB INTERFACE
 <p align="center">
  <img src="https://i.ibb.co/z8g1rqz/tob.png" alt="logo">
</p>

# Requirements

- python >= 3

- look at the requirements.txt for the python libraries

- registered DeveloperApp (see how to create one in the section below)

- Lichess account

- scrot (used by opencv-python) library

# Run

1) From source code, go to src directory and:

```
python3 interface.py
```

2) From Binary, go to prog directory and click 2 times on BOT

# Create a Lichess webApp

1) run interface.py and click on "create a web Application"

2) you need to put the callback url as the one in the image below

 <p align="center">
  <img src="https://i.ibb.co/tKrTCfw/Annotazione-2019-09-10-113314.png" alt="logo">
</p>

# Select the Area of the Chess board:

1) Click "Take a Screenshot of Lichess Board" button from interface.py

2) TOB is gonna take a screenshot, so you have to  make visible in your desktop the lichess board when you click that button

3) select the chess board from the saved image

4) press "c" to save the chess area, press "r" to reset the chess area

# How to Use it

You can play only 1 game each time.
When you click "take screenshot of lichess board" and you save the board area
you can't move that chessboard if you want that TOB works perfectly,
otherwise you have to reclick the button.

Once You have selected the engine level the engine depth and the engine time out seconds, if you click the button "load lichess account" you cannot change
the TOB setup anymore. if you want to rechange the setup you have to close TOB and run it again

Videos:

- How to use it:
 
https://www.youtube.com/watch?v=TG-pWUXUjqs

- How to be a chess cancer:

https://youtu.be/4D_4-AwHzEY


# How To avoid Ban for Cheating

Here you can see the conditions necessary to be considered cheater (directly from lichess opensource repo):

 <p align="center">
  <img src="https://i.ibb.co/jvmP5MR/Schermata-del-2019-09-15-23-48-45.png" alt="logo">
</p>

For These Reasons Stockfish < 10 engine, stockfish Depth parameter, and Maximum random time waiting parameter have been added.
Furthemore TOB doesn't click 2 differents squares when it has to move the pieces but it holds the mouse
from Point A to B. The best setting up until now seems to be:
- Stockfish 5 
- depth 3 
- secs = 1 
- time waiting = 5.

with these conditions TOB can play bullets with minimum +1 increments and is also able to beat 2300 elo masters
(  and you will never be banned for cheating ;)  ).

# Executable Files

- At The Moment TOB is available only for Linux_x86_64 and Windows_x86_64

You can find TOB for linux in the Linux_X86_64/prog directory. Don't move from there! just run it! 
You can find TOB for windows in the Windows_x64/prog directory. Don't move from there! just run it! 
