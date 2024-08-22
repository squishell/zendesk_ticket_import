import os
import csv
import logging
from ticket_creator.py import create_ticket_json
from zendesk_import.py import ticket_import

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    cwd = os.getcwd()
    csv_file = os.path.join(cwd, 'data.csv')
    json_file = os.path.join(cwd, 'data.json')

    if not os.path.isfile(csv_file):
        logging.error(f"CSV file not found: {csv_file}")
    else:
        columns = ['Control', 'Batch', 'Person', 'Property', 'Reference']
        with open(csv_file, mode='r') as file:
            csvReader = csv.DictReader(file)
            rows = [row for row in csvReader if all(col in row for col in columns)]
            create_ticket_json(rows, json_file, subject_fields=['Person', 'Property', 'Batch'], description_fields=['Control', 'Person', 'Property', 'Reference'])

        json_files = [f for f in os.listdir(cwd) if f.startswith(json_file.split('.json')[0])]
        for jf in json_files:
            ticket_import(jf)
