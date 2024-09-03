import os

# Zendesk API credentials and endpoint
ZENDESK_URL = os.getenv('ZENDESK_URL', 'https://pegdev.zendesk.com/api/v2/imports/tickets/create_many')
EMAIL_ADDRESS = os.getenv('ZENDESK_EMAIL', 'jcedeno@pegcompanies.com')
API_TOKEN = os.getenv('ZENDESK_API_TOKEN', 'IVGDSNHrNzR79oiCPnLCu6tOvyvmyjRBsqE0ma07')

# Who the tickets should be assigned to
ASSIGNEE_ID = os.getenv('ZENDESK_ASSIGNEE_ID','1900636157647')

# Who the tickets should appear to be written by
AUTHOR_ID = os.getenv('21970550332173')

# Ticket form ID, can be changed here if needed
TICKET_FORM_ID = os.getenv('ZENDESK_TICKET_FORM_ID', '29808498387981')

CUSTOM_FIELDS = {
    'AP_Forms': {
        'id': 16055787532557,
        'value': 'invoices'  # Static value as per your requirement
    },
    'Invoice_Register_ID': {
        'id': 7825258962189,
        'value': None  # Placeholder; set dynamically in the script
    },
    'Batch_ID': {
        'id': 9300644316301,
        'value': None  # Placeholder; set dynamically in the script
    }
}