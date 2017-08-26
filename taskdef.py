import jsontree
from pprint import pprint

with open('describe_taskdefinition.json', 'r') as myfile:
    data2=myfile.read().replace('\n', '')

je = jsontree.JSONTreeDecoder().decode(data2)
je = je.taskDefinition
od = jsontree.jsontree()
od.containerDefinitions = je.containerDefinitions
if (je.has_key("networkMode")):
    od.networkMode = je.networkMode
od.family = je.family
od.volumes = je.volumes

#pprint(jsontree.JSONTreeEncoder().encode(od))

taskDefinition = je["taskDefinitionArn"].split("/",1)[1]
newTaskDefinitionNum = taskDefinition.split(":",1)[1]
fileName = "describe_taskdefinition_" + taskDefinition + ".json"
f = open(fileName,"w")
f.write(jsontree.JSONTreeEncoder().encode(od))
