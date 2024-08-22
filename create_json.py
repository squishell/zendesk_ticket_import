import csv
import json

url += "/api/v2/imports/tickets/create_many"

def createjson(csvFilePath, jsonFilePath):
	
	data = {}
	
	with open(csv_file, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		for rows in csvReader:
			key = rows['No']
			data[key] = rows

	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
csvFilePath = r'input.csv'
jsonFilePath = r'output.json'

make_json(csvFilePath, jsonFilePath)
