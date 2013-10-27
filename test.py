#!/usr/bin/env python
import bottlesession
import bottle
import redis
import json
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
    return bottle.static_file(path, root="JS")

@bottle.route('/CSS/<path:path>')
def callback(path):
    return bottle.static_file(path, root="CSS")

@bottle.route('/pix/<path:path>')
def pix(path):
    return bottle.static_file(path, root="pix")

@bottle.route('/HTML/partials/<path:path>')
def callback(path):
    return bottle.static_file(path, root="HTML/partials")

    

#############
#   AppIndex
#      Serve Application Body
#
@bottle.get('/')
@bottle.get('/look')
def appIndex():
    return bottle.static_file("/look.html", root="HTML")


##########
# Works
#
@bottle.get('/works/<client>')
def works(client):
        js = app.r.lrange(client, 0, 10)
        # Build JSON from List with join and string concat to save time
        js = "[" + ",".join(js) + "]"
        return js

@bottle.post('/works/<client>/<tasks>')
def works(client, tasks):
        app.r.lpush(client, tasks)
        counter = app.r.hincrby('version', client, 1)
        return counter


bottle.debug(True)
bottle.run(app=app,host='localhost',port=8888,reloader=True)

