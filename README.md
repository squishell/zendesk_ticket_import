# Zendesk Bulk Ticket Importer

## Overview

The Zendesk Bulk Ticket Importer is a Python-based tool designed to automate the process of importing support tickets into Zendesk in bulk. This tool reads data from a CSV file, generates JSON files compatible with the Zendesk API, and imports the tickets into Zendesk while adhering to API constraints.

## Features

- **Batch Processing**: Automatically splits tickets into batches of 100 to comply with Zendesk's bulk import limits.
- **Configurable**: Adaptable to various datasets through customizable subject and description fields.
- **Error Handling**: Includes comprehensive error handling and logging for better traceability.
- **Job Status Tracking**: Tracks the status of ticket import jobs and logs the results.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/zendesk-bulk-ticket-importer.git
    cd zendesk-bulk-ticket-importer
    ```

2. **Install Dependencies**:
    Make sure you have Python 3.x installed. Then, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Configuration**:
    Update `config.py` with your Zendesk credentials and any other static values specific to your environment:
    ```python
    ZENDESK_URL = 'https://your_zendesk_subdomain.zendesk.com/api/v2/imports/tickets/create_many'
    EMAIL_ADDRESS = 'your_email@domain.com'
    API_TOKEN = 'your_api_token'
    ```

    ### How to Find Your Zendesk Credentials

    - **Zendesk Subdomain**: Your Zendesk subdomain is typically the part of your Zendesk URL that comes before `.zendesk.com`. For example, if your Zendesk URL is `https://company.zendesk.com`, then your subdomain is `company`.

    - **Email Address**: Use the email address associated with your Zendesk account. This is the same email address you use to log in to Zendesk.

    - **API Token**:
        1. Log in to your Zendesk account.
        2. Go to the **Admin Center** by clicking the **Admin** icon (gear icon) in the sidebar.
        3. Navigate to **Apps and Integrations** > **APIs** > **Zendesk API**.
        4. Ensure the **Token Access** is enabled.
        5. If you don’t have an API token yet, click on **Add API Token** to create one. You will see the token only once, so make sure to copy it and store it securely.
        6. Use this token in your `config.py` file under `API_TOKEN`.

## Usage

1. **Prepare Your CSV File**:
   Ensure your CSV file (`data.csv`) is in the root directory of the project. The file should contain the necessary columns based on your subject and description field requirements.

2. **Run the Script**:
   You have two options to run the script:

    **Option 1: Direct Execution**:
    - After cloning the repository, simply run the following command:
    ```bash
    ./run_zendesk_import.sh
    ```
    This assumes that the script has executable permissions, which it should if you've cloned the repository from GitHub.

    **Option 2: Using `bash`**:
    - If you encounter any issues with executable permissions or prefer an alternative method, you can run the script directly with `bash`:
    ```bash
    bash run_zendesk_import.sh
    ```

3. **Review Logs**:
   Logs will provide information on the progress of the import, any errors encountered, and the job status URL to track the import process.

## Customization

- **Modify Subject and Description Fields**:
  In `main.py`, you can specify which CSV columns to use for the subject and description of the tickets:
    ```python
    create_ticket_json(rows, json_file, subject_fields=['Person', 'Property', 'Batch'], description_fields=['Control', 'Person', 'Property', 'Reference'])
    ```

- **Credentials**:
  The script pulls credentials and API details from `config.py`. Make sure these are correctly set for your Zendesk account.

## Contributing

If you wish to contribute, please fork the repository and submit a pull request. We welcome improvements, bug fixes, and new features.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
