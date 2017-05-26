import jsontree
from pprint import pprint

with open('describe_taskdefinition.json', 'r') as myfile:
    data2=myfile.read().replace('\n', '')

je = jsontree.JSONTreeDecoder().decode(data2)
je = je.taskDefinition

od = jsontree.jsontree()
od.containerDefinitions = je.containerDefinitions
od.networkMode = je.networkMode
od.family = je.family
od.volumes = je.volumes

#pprint(jsontree.JSONTreeEncoder().encode(od))

taskDefinition = je["taskDefinitionArn"][je["taskDefinitionArn"].find("/")+1:je["taskDefinitionArn"].rfind(":"):]
fileName = "taskdef_" + taskDefinition + ".json"
f = open(fileName,"w")
f.write(jsontree.JSONTreeEncoder().encode(od))
