import sys
import jsontree

if len(sys.argv) < 2:
        with open('img.json', 'r') as data_file:
                data = data_file.read().replace('\n','')

        data = jsontree.JSONTreeDecoder().decode(data)
        data = data.imageIds
        for img in data:
                if img.imageTag == "latest":
                        hash = img.imageDigest

        for img in data:
                if (img.imageDigest == hash) and (img.imageTag!="latest") :
                        number = img.imageTag
else:
        number = sys.argv[1]

        
with open('describe_taskdefinition.json', 'r') as myfile:
    data2=myfile.read().replace('\n', '')

je = jsontree.JSONTreeDecoder().decode(data2)
je = je.taskDefinition
od = jsontree.jsontree()
od.containerDefinitions = je.containerDefinitions
if od.containerDefinitions[0].image.rfind(':') > 0 :
        od.containerDefinitions[0].image = od.containerDefinitions[0].image[0:od.containerDefinitions[0].image.rfind(':')+1:] + number
else:
        od.containerDefinitions[0].image += ':' + number

print number        
        
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

#print(jsontree.JSONTreeEncoder().encode(od))
