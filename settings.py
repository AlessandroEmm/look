import os

appPath = os.path.abspath(os.path.dirname(__file__)) 
configPath = os.path.abspath(os.path.dirname(__file__)) + '/look.conf'
databaseUrl = appPath + '/db/look.db'
loginDBUrl = appPath + '/db/login.db'
# 1. "simple" means file handling yourself  2. "web" handle files and channels through web interface

presentHandling = "simple"

channelPath="./channels"