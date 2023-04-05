import os

import psycopg2
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
db_url = os.environ.get('DATABASE_URL')


@app.route('/login', methods=['POST'])
def login():
    print("/login called")
    # Get username and password from request body
    username = request.get_json()['username']
    password = request.get_json()['password']
    pin = request.get_json()['pin']
    # main.loginGUI(username, password, pin)
    return 'Logged in successfully'


@app.route('/start', methods=['POST'])
def start():
    print("/start called")
    # Handle start logic here
    # main.cleanupGUI()
    # main.main()
    return 'Started successfully'


@app.route('/stop', methods=['POST'])
def stop():
    print("/stop called")
    # main.exitGame()
    return 'Stopped successfully'


@app.route('/restart', methods=['POST'])
async def restart():
    print("/restart called")
    #  await main.exitGame()
    username = (await request.get_json())['username']
    password = (await request.get_json())['password']
    # await main.loginGUI(username, password)
    # await main.cleanupGUI()
    # main.main()
    return 'Restarted successfully'


@app.route('/setNextState', methods=['POST'])
def setNextState():
    print("/setNextState called")
    nextState = request.get_json()['nextState']
    conn = psycopg2.connect(db_url)
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS StateTable (id serial PRIMARY KEY, next_state varchar(255), created_at timestamp)')
    query = "INSERT INTO StateTable (next_state, created_at) VALUES (%s, %s)"

    cur.execute(query, (nextState, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()

    return "Next state is:" + nextState


@app.route('/', methods=['GET'])
def default():
    return "Hello word!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
