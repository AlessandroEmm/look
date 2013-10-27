#!/usr/bin/env python
import cherrypy
import settings
import loginController 
import loginView
import dbsqlite
import json

class login(object):
    def index(self):
        view = loginView.loginView()
        return view.login()
    index.exposed = True



### Login Call
    def login(self, login="", password="", error=""):
        controller = loginController.loginController()
        path ="/"
        if (controller.verifyUserPassword(login, password)):
            cherrypy.session['roles'] = 'view';
            cherrypy.session['username'] = login;
            path="/roles"
        view = loginView.loginView()
        return view.forwarder(path)
    login.exposed = True


    def roles(self):
        view = loginView.loginView()
        roleView = ""
        if cherrypy.session.get('username') is None:
            roleView  = view.forwarder("/")
        else:
            roleView  = view.roleView(cherrypy.session.get('username'))
        return roleView 
    roles.exposed = True


class look(object):
	def __init__(self):
		pass
	def index(self):
		""" Show chooser Menu """

		return "Template.render(channelList=List)"
	index.exposed = True


class works(object):
	def __init__(self):
		self.db = dbsqlite.dbsqlite("db/look.db")

	def default(self, client=None):
		""" Show works """
		if client is None:
			return "Supply a client"
		auth = self.db.select("authorization ", "where username = '" + cherrypy.session.get('username') + "'" );
		print(auth)
		works = self.db.select("works ", "where clientId = (select id from clients where client = '" + client + "')" );
		return json.dumps(works)
	default.exposed = True


cherrypy.tree.mount(login(), '/', settings.configPath)
cherrypy.tree.mount(look(), '/look', settings.configPath)
cherrypy.tree.mount(works(), '/works', settings.configPath)

cherrypy.engine.start()
cherrypy.engine.block()