import json
import logging
from datetime import datetime
import math
from config import ASSIGNEE_ID, AUTHOR_ID, CUSTOM_FIELDS, TICKET_FORM_ID

def create_ticket_json(csv_rows, output_filename, subject_fields, description_fields, max_tickets=100):
    """
    Creates JSON files from CSV data, split into batches of 100 tickets.
    Adds validation and parsing for data consistency.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    tickets = []
    for row in csv_rows:
        try:
            # Validate and clean data for subject
            subject_parts = [row.get(field, '').strip() for field in subject_fields]
            if not all(subject_parts):
                logging.warning(f"Skipping row due to missing data for subject fields: {row}")
                continue
            subject = " - ".join(subject_parts)

            # Validate and clean data for description
            description_parts = [row.get(field, '').strip() for field in description_fields]
            if not all(description_parts):
                logging.warning(f"Skipping row due to missing data for description fields: {row}")
                continue
            description = " - ".join(description_parts)

            # Dynamically set custom fields based on config
            custom_fields = []
            for field_id, default_value in CUSTOM_FIELDS.items():
                value = row.get(default_value.get('csv_field', ''), '').strip() if default_value.get('csv_field') else default_value['value']
                custom_fields.append({"id": field_id, "value": value})

            # Construct ticket dictionary
            date_value = datetime.now().strftime('%Y-%m-%d')
            ticket = {
                "subject": subject,
                "assignee_id": ASSIGNEE_ID,
                "comments": [
                    {
                        "author_id": AUTHOR_ID,
                        "public": False,
                        "value": f"Imported to Zendesk on {date_value}"
                    }
                ],
                "requester_id": AUTHOR_ID,
                "tags": [
                    "ap_-_accounting",
                    "invoices"
                ],
                "ticket_form_id": TICKET_FORM_ID,
                "custom_fields": custom_fields
            }
            tickets.append(ticket)
        except KeyError as e:
            logging.error(f"Missing expected column in CSV: {e}")
            continue
        except Exception as e:
            logging.error(f"Unexpected error processing row: {e}")
            continue

    if not tickets:
        logging.info("No tickets were created. Check the CSV file for data consistency.")
        return
    
    num_batches = math.ceil(len(tickets) / max_tickets)
    logging.info(f"Number of ticket batches to be created: {num_batches}")
    
    for i in range(num_batches):
        batch_tickets = tickets[i*max_tickets:(i+1)*max_tickets]
        batch_filename = f"{output_filename.split('.json')[0]}_batch_{i+1}.json"
        try:
            with open(batch_filename, 'w') as json_file:
                json.dump({"tickets": batch_tickets}, json_file, indent=4)
            logging.info(f"JSON file '{batch_filename}' created successfully.")
        except Exception as e:
            logging.error(f"Failed to write JSON file '{batch_filename}': {e}")
