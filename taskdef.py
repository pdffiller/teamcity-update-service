import json
import jsonpickle
from pprint import pprint

with open('describe_taskdefinition.json') as data_file:
    data = json.load(data_file)
data = data["taskDefinition"]

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

class logOptions:
    def __init__(self):
        self.max_size = "1m"
        self.max_file = 1

class logConfiguration:
    def __init__(self):
        self.logDriver = "json-file"
        self.options = []

class env:
    def __init__(self):
        self.name = ""
        self.value = ""

class mountPoint:
    def __init__(self):
        self.containerPath = ""
        self.sourceVolume = ""

class ulimits:
    def __init__(self):
        self.name = ""
        self.softLimit = 0
        self.hardLimit = 0

class containerDefinitions:
    def __init__(self):
        self.environment = []
        self.name = ""
        self.mountPoints = []
        self.image = ""
        self.cpu = 0
        self.memory = 0
        self.essential = False
        self.user = ""
        self.volumesFrom = []
        self.portMappings = []
        self.logConfiguration = ""
        self.ulimits = []
        self.dnsServers = []
        self.hostname = ""

class deploymentConfiguration:
    def __init__(self):
        self.minimumHealthyPercent = 0
        self.maximumPercent = 100

class outData:
    def __init__(self):
        self.family = ""
        self.networkMode = ""
        #self.taskDefinition = ""
        self.containerDefinitions = []
        self.volumes = []

cd = containerDefinitions()
od = outData()
od.family = data["family"]

taskDefinition = data["taskDefinitionArn"][data["taskDefinitionArn"].find("/")+1:data["taskDefinitionArn"].rfind(":"):]
if ("networkMode" in data):
    od.networkMode = data["networkMode"]
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
if ("hostname" in data["containerDefinitions"][0]):
    cd.hostname = data["containerDefinitions"][0]["hostname"]
if ("user" in data["containerDefinitions"][0]):
    cd.user = data["containerDefinitions"][0]["user"]
cd.logConfiguration = logConfiguration()
cd.logConfiguration.options = logOptions()
if ("logConfiguration" in data["containerDefinitions"][0]):
    cd.logConfiguration.logDriver = data["containerDefinitions"][0]["logConfiguration"]["logDriver"]
    cd.logConfiguration.options.max_file = data["containerDefinitions"][0]["logConfiguration"]["options"]["max-file"]
    cd.logConfiguration.options.max_size = data["containerDefinitions"][0]["logConfiguration"]["options"]["max-size"]

if ("dnsServers" in data["containerDefinitions"][0]):
    cd.dnsServers = data["containerDefinitions"][0]["dnsServers"]

if ("ulimits" in data["containerDefinitions"][0]):
    cd.ulimits = ulimits()
    for ul in data["containerDefinitions"][0]["ulimits"]:
        cd.mountPoints.append(ul)

for mpN in data["containerDefinitions"][0]["mountPoints"]:
    cd.mountPoints.append(mpN)

for env0 in data["containerDefinitions"][0]["environment"]:
    cd.environment.append(env0)

for pm in data["containerDefinitions"][0]["portMappings"]:
    cd.portMappings.append(pm)

od.containerDefinitions.append(cd)

pprint(jsonpickle.encode(od, unpicklable=False))

fileName = "describe_taskdefinition_" + taskDefinition + ".json"
f = open(fileName,"w")
f.write(jsonpickle.encode(od, unpicklable=False))


