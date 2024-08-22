import requests
import json
from requests.auth import HTTPBasicAuth
import credentials

def ticket_import(x):
	payload = json.loads(x)
	headers = {
		"Content-Type": "application/json",
	}

	auth = HTTPBasicAuth(f'{email_address}/token', api_token)

	response = requests.request(
		"POST",
		url,
		auth=auth,
		headers=headers,
		json=payload
	)

	print(response.text)