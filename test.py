import pandas as pd
import json

def get_location_data(tmp_data):
	station_id = tmp_data["station_code"]
	position = (tmp_data["lat"], tmp_data["lon"])
	name_tw = tmp_data["station_name_tw"]
	name_en = tmp_data["station_name_en"]
	color = tmp_data["line_code"]
	# return {"id":station_id, "position":position, "name_tw":name_tw, "name_en":name_en, "color": color}
	return {"id":station_id, "position":position, "color": color}

data = pd.read_csv("./data/northern-taiwan.csv") 
result = []

for index, row in data.iterrows():
    result.append(get_location_data(row))

file_object = open("./data/mrt.json", 'w')
json.dump(result, file_object)
