import os
import csv
import logging
from ticket_creator import create_ticket_json
from zendesk_import import ticket_import

# Set up logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_directories():
    """
    Creates 'CSV Files' and 'JSON Files' directories if they do not exist.
    """
    csv_dir = os.path.join(os.getcwd(), 'CSV Files')
    json_dir = os.path.join(os.getcwd(), 'JSON Files')
    
    # Create directories if they don't exist
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)
        logging.info("Created 'CSV Files' directory.")

    if not os.path.exists(json_dir):
        os.makedirs(json_dir)
        logging.info("Created 'JSON Files' directory.")

    # Check if this is the first run
    if not os.listdir(csv_dir):
        logging.info("Setup complete. Please add your CSV files to the 'CSV Files' directory and run the script again.")
        return False
    
    return True

if __name__ == "__main__":
    # Initial setup
    if not setup_directories():
        exit()

    csv_dir = os.path.join(os.getcwd(), 'CSV Files')
    json_dir = os.path.join(os.getcwd(), 'JSON Files')

    # Process each CSV file in the 'CSV Files' directory
    for csv_filename in os.listdir(csv_dir):
        if csv_filename.endswith('.csv'):
            csv_file_path = os.path.join(csv_dir, csv_filename)
            json_filename = csv_filename.replace('.csv', '.json')
            json_file_path = os.path.join(json_dir, json_filename)
            
            columns = ['Control', 'Batch', 'Person', 'Property', 'Reference']  
            with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
                csvReader = csv.DictReader(file)
                headers = csvReader.fieldnames
                logging.info(f"Processing CSV file '{csv_filename}' with headers: {headers}")
                
                rows = [row for row in csvReader if all(col in row for col in columns)]
                if not rows:
                    logging.info(f"No valid rows found in '{csv_filename}'. Skipping.")
                    continue

                logging.info(f"Number of valid rows found: {len(rows)}")
                create_ticket_json(rows, json_file_path, subject_fields=['Person', 'Property', 'Reference'], description_fields=['Control', 'Person', 'Property', 'Batch'])

    # Import each JSON file in the 'JSON Files' directory
    for json_filename in os.listdir(json_dir):
        if json_filename.endswith('.json'):
            json_file_path = os.path.join(json_dir, json_filename)
            logging.info(f"Importing tickets from JSON file '{json_filename}'.")
            ticket_import(json_file_path)