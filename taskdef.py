import json
import jsonpickle
from pprint import pprint

with open('taskdef.json') as data_file:
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
        #self.taskDefinition = ""
        self.containerDefinitions = []
        self.volumes = []

cd = containerDefinitions()
od = outData()
od.family = data["family"]
taskDefinition = data["taskDefinitionArn"][data["taskDefinitionArn"].find("/")+1:data["taskDefinitionArn"].rfind(":"):]

v = volume()
for vol in data["volumes"]:
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

pprint(jsonpickle.encode(od, unpicklable=False))

fileName = "taskdef_" + taskDefinition + ".json"
f = open(fileName,"w")
f.write(jsonpickle.encode(od, unpicklable=False))


