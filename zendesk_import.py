import json
import logging
import time
from requests.auth import HTTPBasicAuth
import requests
from config import ZENDESK_URL, EMAIL_ADDRESS, API_TOKEN

def ticket_import(json_file):
    """
    This function sends the generated JSON payload to the Zendesk API to create tickets.
    It handles the bulk import and tracks the job status.
    """
    try:
        with open(json_file, 'r') as file:
            payload = json.load(file)

        headers = {
            "Content-Type": "application/json",
        }

        auth = HTTPBasicAuth(f'{EMAIL_ADDRESS}/token', API_TOKEN)

        # Log the payload being sent to Zendesk
        logging.info(f"Sending payload to Zendesk: {json.dumps(payload, indent=4)}")

        response = requests.post(
            ZENDESK_URL,
            auth=auth,
            headers=headers,
            json=payload
        )

        # Log the full API response
        logging.info(f"API Response: {response.status_code} - {response.text}")

        if response.status_code == 201:
            job_status_url = response.json()['job_status']['url']
            logging.info(f"Import job submitted successfully. Checking job status: {job_status_url}")
            check_job_status(job_status_url, auth, headers)
        else:
            logging.error(f"Failed to import tickets: {response.text}")

    except json.JSONDecodeError:
        logging.error("Error: The JSON structure could not be parsed.")
    except requests.RequestException as e:
        logging.error(f"Error: There was a problem with the request - {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def check_job_status(job_status_url, auth, headers):
    """
    Checks the job status for the ticket import to Zendesk.
    """
    while True:
        response = requests.get(job_status_url, auth=auth, headers=headers)

        if response.status_code == 200:
            job_status = response.json()['job_status']
            status = job_status['status']
            logging.info(f"Job Status: {status}")

            if status == "completed":
                logging.info("Ticket import completed successfully.")
                break
            elif status == "failed":
                logging.error(f"Ticket import failed: {job_status.get('message')}")
                if job_status.get('results'):
                    for result in job_status['results']:
                        logging.error(f"Error: {result}")
                break
            elif status == "queued":
                logging.info("Job is still queued. This could be due to high load on Zendesk servers or rate limiting.")
                time.sleep(10)  # Adjust this sleep time as necessary
            else:
                # If still in progress, wait and retry
                logging.info("Job still in progress. Waiting for 10 seconds before checking again.")
                time.sleep(10)
        else:
            logging.error(f"Failed to check job status: {response.text}")
            break