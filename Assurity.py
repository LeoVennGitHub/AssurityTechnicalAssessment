import json, sys

#Check if JSON file is passed
if len(sys.argv) == 0:
    print("Please pass the path to a JSON file")
    exit(0)

#Check if the path and corresponding JSON file is valid
try:
    json_file = open(sys.argv[1])
    json_object = json.load(json_file, strict=False)
except FileNotFoundError:
    print("JSON file could not be opened")
    exit(0)
except:
    print("JSON format invalid")
    exit(0)


#Check if the Name element is 'Badges'
name_Is_Badges = (json_object["Name"] == "Badges")
if not name_Is_Badges:
    print("API not accepted: Name field is '" + json_object["Name"] +"'")
    exit(0)

#Check if the CanRelist element is 'true'
can_Relist = json_object["CanRelist"]
if not can_Relist:
    print("API not accepted: Can Relist field is false")
    exit(0)

#Check if there is a Promotions element with Name = 'Feature' and Description = 'Better position in category'
for x in json_object["Promotions"]:
    if (x["Name"] == "Feature" and x['Description'] == 'Better position in category'):
        print("API Accepted")
        exit(0)
print("No Promotions element with Name = 'Feature' and Description = 'Better position in category' found. API not accepted.")