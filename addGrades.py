from ascents.models import Grade
import json

# Opening JSON file
f = open('grades.json')
 
# returns JSON object as a dictionary
data = json.load(f)
 
# Iterating through the json list and adding the grades
for i in data['grades']:
    grade = Grade(name=i['fields']['name'],value=int(i['fields']['value']))
    grade.save()
 
# Closing file
f.close()