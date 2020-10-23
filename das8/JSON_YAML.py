import json
import yaml

with open("sample_json.json", "r") as file_json:
	data = json.load(file_json)
	for i in data["items"]:
		del i["married"]
print(data["items"][1]["name"], data["items"][1]["surname"])

with open("new_sample_json.json", 'w') as changed_json:
	json.dump(data, changed_json, indent = 2)


with open("json_to_text.txt", "w") as json_txt:
	json_txt.write(str(data))


with open("sample_json.json", "r") as file1_json:
	data1 = json.load(file1_json)
print(data)


with open("json_YAML.yaml", "w") as file:
	yaml = yaml.dump(data1, file)

with open("test.yml", "r") as file_yaml:
	new_yaml = yaml.load(file_yaml)
print(new_yaml)

with open("new_sample_json.json", "a") as y_j:
	json.dump(new_yaml, y_j, indent = 2)

with open("yml_text.txt", "w") as y_t:
	y_t.write(str(new_yaml))