import json
 
# Opening JSON file
json_object = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

with open("./TASK1/assets/multiple-choice/b.json", "w") as outfile:
    outfile.write(json_object)