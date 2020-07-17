#!/usr/bin/env python
from flask import Flask, render_template, session, request, flash
from flask_socketio import SocketIO, emit 
from random import random
import time
app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

my_value = 5278

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('client_event')
def client_msg(msg):
    while True:
        if (msg['data']=='start'):
            time.sleep(2)
            emit('server_response', {'data': random()})
        if (msg['data']=='end'):
            # time.sleep(1)
            emit('server_response', {'data': 'end'})
            flash

@socketio.on('connect_event')
def connected_msg(msg):
    print 'yooooooooooo'
    emit('server_response', {'data': msg['data']})

@socketio.on('my_event')
def new_msg(msg):
    print 'my event triggered'
    while True:
        emit('my_response',{'data':my_value})

@app.route('/update')
def update():
    global my_value
    my_value = request.args.get('value')
    print 'get value' + my_value
    return 'success'

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')