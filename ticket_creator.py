import json
import logging
from datetime import datetime
import math
from config import ASSIGNEE_ID, AUTHOR_ID

def create_ticket_json(csv_rows, output_filename, subject_fields, description_fields, max_tickets=100):
    """
    Creates JSON files from CSV data, split into batches of 100 tickets.
    """
    tickets = []
    for row in csv_rows:
        subject = " - ".join([row.get(field, 'Unknown') for field in subject_fields])
        description = " - ".join([row.get(field, 'Unknown') for field in description_fields])
        
        date_value = datetime.now().strftime('%Y-%m-%d')
        
        ticket = {
            "subject": subject,
            "assignee_id": ASSIGNEE_ID,
            "comments": [
                {
                    "author_id": AUTHOR_ID,
                    "public": False,
                    "value": f"{subject} - Imported to Zendesk on {date_value}"
                }
            ],
            "description": description,
            "requester_id": AUTHOR_ID,
            "tags": [
                "ap_-_accounting",
                "invoices"
            ]
        }
        tickets.append(ticket)

    num_batches = math.ceil(len(tickets) / max_tickets)
    for i in range(num_batches):
        batch_tickets = tickets[i*max_tickets:(i+1)*max_tickets]
        batch_filename = f"{output_filename.split('.json')[0]}_batch_{i+1}.json"
        with open(batch_filename, 'w') as json_file:
            json.dump({"tickets": batch_tickets}, json_file, indent=4)
        logging.info(f"JSON file '{batch_filename}' created successfully.")
