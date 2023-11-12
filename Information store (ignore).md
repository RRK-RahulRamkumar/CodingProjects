To pull projects from github to visual studio code
https://www.youtube.com/watch?v=_ynMa2XlRgk

To push changes from visual studio code to github
https://www.youtube.com/watch?v=LxkXT9WD7yk

---------------------------------------------
Working with JSON in python
https://www.youtube.com/watch?v=-51jxlQaxyA

Serialize - Converting data into a format which can be stored or transferred over a network
Deserialize - Converting the serialized format back into its original form

import json

# When the json is in form of a string
json_data = """...."""
<object_name> = json.loads(json_data) # Deserialization
<object_name> = json.dumps(json_data) # Serialization

# When the json is in a file
with open(<json_file>, "r") as <file_name>: # Deserialization
  <object_name> = json.load(<file_name>)

with open(<json_file>, "w") as <file_name>: # Serialization
  json.dump(json_data, <file_name>)
