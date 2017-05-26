Skip to content
This repository
Search
Pull requests
Issues
Marketplace
Gist
 @vgaivoronskyi
 Sign out
 Watch 6
  Star 0
 Fork 0 pdffiller/teamcity-update-service
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Settings Insights 
Tree: 79181364cf Find file Copy pathteamcity-update-service/taskdef.py
7918136  on 28 Mar
@vgaivoronskyi vgaivoronskyi fix for volumes
1 contributor
RawBlameHistory     
93 lines (73 sloc)  2.31 KB
import json
import jsonpickle
from pprint import pprint

with open('describe_taskdefinition.json') as data_file:
    data = json.load(data_file)
data = data['taskDefinition']

class host:
    def __init__(self):
        self.sourcePath = ""

class volume:
    def __init__(self):
        self.name = ""
        self.host = host()

class portMappings:
    def __init__(self):
        self.protocol = ""
        self.containerPort = 0
        self.hostPort = 0

class env:
    def __init__(self):
        self.name = ""
        self.value = ""

class mountPoint:
    def __init__(self):
        self.containerPath = ""
        self.sourceVolume = ""

class containerDefinitions:
    def __init__(self):
        self.environment = []
        self.name = ""
        self.mountPoints = []
        self.image = ""
        self.cpu = 0
        self.memory = 0
        self.essential = False
        self.volumesFrom = []
        self.portMappings = []

class deploymentConfiguration:
    def __init__(self):
        self.minimumHealthyPercent = 0
        self.maximumPercent = 100

class outData:
    def __init__(self):
        self.family = ""
        #self.networkMode = ""
        #self.taskDefinition = ""
        self.containerDefinitions = []
        self.volumes = []

cd = containerDefinitions()
od = outData()
od.family = data["family"]
#od.networkMode = data["networkMode"]
taskDefinition = data["taskDefinitionArn"][data["taskDefinitionArn"].find("/")+1:data["taskDefinitionArn"].rfind(":"):]

for vol in data["volumes"]:
    v = volume()
    v.host.sourcePath = vol["host"]["sourcePath"]
    v.name = vol["name"]
    od.volumes.append(v)

cd.name = data["containerDefinitions"][0]["name"]
cd.image = data["containerDefinitions"][0]["image"]
cd.cpu = data["containerDefinitions"][0]["cpu"]
cd.memory = data["containerDefinitions"][0]["memory"]
cd.essential = data["containerDefinitions"][0]["essential"]

for mpN in data["containerDefinitions"][0]["mountPoints"]:
    cd.mountPoints.append(mpN)

for env0 in data["containerDefinitions"][0]["environment"]:
    cd.environment.append(env0)

for pm in data["containerDefinitions"][0]["portMappings"]:
    cd.portMappings.append(pm)

od.containerDefinitions.append(cd)

fileName = "describe_taskdefinition_" + taskDefinition + ".json"
f = open(fileName,"w")
f.write(jsonpickle.encode(od, unpicklable=False))


Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
