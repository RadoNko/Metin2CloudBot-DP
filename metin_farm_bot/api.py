from flask import Flask, request
from metin_farm_bot import main, captureAndDetect
app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    print("/login called")
    # Get username and password from request body
    username = request.get_json()['username']
    password = request.get_json()['password']
    pin = request.get_json()['pin']
    main.loginGUI(username, password,pin)
    return 'Logged in successfully'


@app.route('/start', methods=['POST'])
def start():
    print("/start called")
    # Handle start logic here
    main.cleanupGUI()
    main.main()
    return 'Started successfully'


@app.route('/stop', methods=['POST'])
def stop():
    print("/stop called")
    main.exitGame()
    return 'Stopped successfully'


@app.route('/restart', methods=['POST'])
async def restart():
    print("/restart called")
    await main.exitGame()
    username = (await request.get_json())['username']
    password = (await request.get_json())['password']
    await main.loginGUI(username, password)
    await main.cleanupGUI()
    main.main()
    return 'Restarted successfully'


if __name__ == '__main__':
    app.run(debug=True)
