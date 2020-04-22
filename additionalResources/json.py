import simplejson as json
import os

route = "E:\\Desarrollo\\PROGRAMMING COURSES\\PYTHON\\UDEMY\\additionalResources\\"
path = route+"ages.json"

# validate if exist a file and if its value is diferent of 0
if os.path.isfile(path) and os.stat(path).st_size != 0:
    old_file = open(path, "r+")
    # load the string from the file
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file = open(path, "w+")
    data = {"name": "Nick", "age": 27}
    print("No file found setting default age to", data["age"])

# this will seek for a file, if it exist it's going to append data
# else it's going to create it
old_file.seek(0)
old_file.write(json.dumps(data))
