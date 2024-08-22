import json
import logging
from requests.auth import HTTPBasicAuth
import requests
from config import ZENDESK_URL, EMAIL_ADDRESS, API_TOKEN

def ticket_import(json_file):
    """
    Sends the generated JSON payload to the Zendesk API to create tickets.
    Tracks the job status and reports success or failure.
    """
    try:
        with open(json_file, 'r') as file:
            payload = json.load(file)

        headers = {
            "Content-Type": "application/json",
        }

        auth = HTTPBasicAuth(f'{EMAIL_ADDRESS}/token', API_TOKEN)

        response = requests.post(
            ZENDESK_URL,
            auth=auth,
            headers=headers,
            json=payload
        )

        if response.status_code == 201:
            job_status_url = response.json()['job_status']['url']
            logging.info(f"Import job submitted successfully. Track the status here: {job_status_url}")
        else:
            logging.error(f"Failed to import tickets: {response.text}")

    except json.JSONDecodeError:
        logging.error("Error: The JSON structure could not be parsed.")
    except requests.RequestException as e:
        logging.error(f"Error: There was a problem with the request - {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
