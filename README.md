
# Zendesk Bulk Ticket Importer

## Overview

The Zendesk Bulk Ticket Importer is a Python-based tool designed to automate the process of importing support tickets into Zendesk in bulk. This tool reads data from CSV files, generates JSON files compatible with the Zendesk API, and imports the tickets into Zendesk.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/squishell/zendesk-bulk-ticket-importer.git
    cd zendesk-bulk-ticket-importer
    ```

2. **Set Up Virtual Environment**:
    Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**:
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Your Environment**:
    Update `config.py` with your Zendesk credentials and other settings:
    ### Explanation of Configuration Fields
    - **ZENDESK_URL**: Your Zendesk subdomain API endpoint.
    - **EMAIL_ADDRESS**: The email address associated with your Zendesk account.
    - **API_TOKEN**: Your Zendesk API token for authentication.
    - **ASSIGNEE_ID**: The ID of the user to whom the tickets should be assigned.
    - **AUTHOR_ID**: The ID of the user who appears to have created the ticket.
    - **TICKET_FORM_ID**: The ID of the form template to use for the tickets.
    - **CUSTOM_FIELDS**: A dictionary mapping field IDs to either fixed values or CSV column names for dynamic values.

## Usage

1. **Prepare Your CSV Files**:
    Ensure your CSV files are placed in the `CSV Files` directory. After the initial setup run, place any additional CSV files in this directory. The script will iterate through all CSV files present.

2. **Run the Script**:
    Execute the import script:
    ```bash
    ./run_zendesk_import.sh
    ```
    This script sets up the environment, installs dependencies, and runs the main import script. It will process all CSV files in the `CSV Files` directory and generate corresponding JSON files in the `JSON Files` directory.

3. **Review Logs**:
    Logs will provide information on the import process, any errors, and the job status URL to track the import.

## Customization

- **Modify Ticket Fields**:
  Adjust the `config.py` and `main.py` to customize the ticket creation process, including which fields to use from your CSV files.s