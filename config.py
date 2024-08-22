import os

# Zendesk API credentials and endpoint
ZENDESK_URL = os.getenv('ZENDESK_URL', 'https://your_zendesk_subdomain.zendesk.com/api/v2/imports/tickets/create_many')
EMAIL_ADDRESS = os.getenv('ZENDESK_EMAIL', 'your_email@domain.com')
API_TOKEN = os.getenv('ZENDESK_API_TOKEN', 'your_api_token')

# Common static values specific to the company (if any)
ASSIGNEE_ID = ""
AUTHOR_ID = ""
