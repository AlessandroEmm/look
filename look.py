#!/usr/bin/env python

import bottle
import plyvel
import json
import redis
from datetime import datetime
import settings

app = bottle.app()

app.r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


####################### 
## HTTP-Methods
# Static Files
@bottle.route('/JS/<path:path>')
def callback(path):
    print(path)
    return bottle.static_file(path, root="UI/JS")

@bottle.route('/CSS/<path:path>')
def callback(path):
    return bottle.static_file(path, root="UI/CSS")

@bottle.route('/PIX/<path:path>')
def pix(path):
    return bottle.static_file(path, root="UI/PIX")

@bottle.route('/HTML/partials/<path:path>')
def callback(path):
    return bottle.static_file(path, root="UI/HTML/partials")

    

#############
#   AppIndex
#      Serve Application Body
#
@bottle.get('/')
@bottle.get('/look')
def appIndex():
    return bottle.static_file("UI/HTML/look.html", root="")


##########
# Works
#

# get works for client
@bottle.get('/works/<client>')
def works(client):
        js = app.r.lrange(client, 0, 1000)
        # Build JSON from List with join and string concat to save time
        js = "[" + ",".join(js) + "]"
        return js

# add work
@bottle.get('/works/<client>/<tasks>')
def works(client, tasks):
        app.r.lpush(client, tasks)
        #counter = app.r.hincrby('version', client, 1)
        return "Worked!"

# add work
@bottle.post('/works/<client>/<tasks>')
def works(client, tasks):
        app.r.lpush(client, tasks)
        #counter = app.r.hincrby('version', client, 1)
        return counter


bottle.debug(True)
bottle.run(app=app,host='localhost',port=8888,reloader=True)
