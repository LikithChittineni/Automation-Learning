import json
python_dict={
    'name':'Wintox',
    'status':'Active'
}
json_script=json.dumps(python_dict,indent=4)
print(json_script)
print(type(json_script))
playername=python_dict['name']
print(playername)

js_2='{"Name":"Punkk","Role":"IGL","is_playing":true}'
py_dict=json.loads(js_2)

print(py_dict)

js_3='{"person": {"name": "Likith", "age": 19, "city": "Hyderabad"}}'
pyt_dict=json.loads(js_3)
person_data=pyt_dict["person"]
name=person_data["name"]
city=person_data["city"]
print(f"Name:{name}")
print(f"City:{city}")
