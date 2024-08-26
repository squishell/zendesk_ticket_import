import os

# Zendesk API credentials and endpoint
ZENDESK_URL = os.getenv('ZENDESK_URL')
EMAIL_ADDRESS = os.getenv('ZENDESK_EMAIL')
API_TOKEN = os.getenv('ZENDESK_API_TOKEN')

# Who the tickets should be assigned to
ASSIGNEE_ID = os.getenv('ASSIGNEE_ID')

# Who the tickets should appear to be written by
AUTHOR_ID = os.getenv('AUTHOR_ID')

# Ticket form ID, can be changed here if needed
TICKET_FORM_ID = os.getenv('TICKET_FORM_ID')

# Custom fields with their respective IDs and default values
CUSTOM_FIELDS = {
    # Custom Field Format #
    ## ID: {type: value},
}
