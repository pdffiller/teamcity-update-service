import sys
import jsontree

docker_image = sys.argv[1]
tag = sys.argv[2]

        
with open('describe_taskdefinition.json', 'r') as myfile:
    data2=myfile.read().replace('\n', '')

je = jsontree.JSONTreeDecoder().decode(data2)
je = je.taskDefinition
od = jsontree.jsontree()
od.containerDefinitions = je.containerDefinitions
od.containerDefinitions[0].image = docker_image + ':' + tag

print od.containerDefinitions[0].image        
        
od.family = je.family
od.volumes = je.volumes
if isinstance(je.networkMode, basestring) :
    od.networkMode = je.networkMode
if isinstance(je.taskRoleArn, basestring) :
    od.taskRoleArn = je.taskRoleArn

taskDefinition = je["taskDefinitionArn"][je["taskDefinitionArn"].find("/")+1:je["taskDefinitionArn"].rfind(":"):]
fileName = "describe_taskdefinition_" + taskDefinition + ".json"
f = open(fileName,"w")
f.write(jsontree.JSONTreeEncoder().encode(od))
