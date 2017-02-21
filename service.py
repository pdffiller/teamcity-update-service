import json
import jsonpickle

with open('describe_service.json') as data_file:
    data = json.load(data_file)
data = data["services"][0]

class deploymentConfiguration:
    def __init__(self):
        self.minimumHealthyPercent = 0
        self.maximumPercent = 100

class outData:
    def __init__(self):
        self.taskDefinition = ""
        self.cluster = ""
        self.service = ""
        self.desiredCount = 0
        self.deploymentConfiguration = deploymentConfiguration()

dc = deploymentConfiguration()
od = outData()
od.taskDefinition = data["taskDefinition"][data["taskDefinition"].find("/")+1:data["taskDefinition"].rfind(":"):]
od.cluster = data["clusterArn"][data["clusterArn"].find("/")+1::]
od.service = data["serviceName"]
od.desiredCount = data["desiredCount"]
dc.minimumHealthyPercent = data["deploymentConfiguration"]["minimumHealthyPercent"]
dc.maximumPercent = data["deploymentConfiguration"]["maximumPercent"]
od.deploymentConfiguration = dc

fileName = "describe_service_" + od.service + ".json"
f = open(fileName,"w")
f.write(jsonpickle.encode(od, unpicklable=False))
