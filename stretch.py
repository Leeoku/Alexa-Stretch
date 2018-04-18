from flask import Flask
from flask_ask import (Ask, statement,session)
import time, threading,boto3,logging

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger('flask_ask').setLevel(logging.INFO)

#Initialize Time/game
TIME = 0
GAME = 0


@ask.launch
def launchRequest():
    return statement('You have started the stretch reminder')


@ask.intent('AddStretchAfter')
# User asks Alexa to set a reminder to stretch after {Time} minutes or {Game} games
def addStretchAfter(TIME,GAME):
    if (TIME == 0 and GAME == 0):
        return statement(f"Please specify time or number of games")
    elif TIME !=0:
        #Add code to use timer and remind after {TIME}
        return statement(f"Reminding to stretch after {TIME} minutes")
    elif GAME != 0:
        #Add code to use timer and remind after fixed interval of time to see if game is done
        return statement(f"Reminding to stretch after {GAME} games")
    



app.run(debug=True)