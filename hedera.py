import json
import requests

# Set the base URL for the mirror node based on the network (e.g., MAINNET, TESTNET, PREVIEWNET)
base_url = "https://testnet.mirrornode.hedera.com"

# Specify the account ID or alias for which you want to retrieve information
account_id_or_alias = "0.0.4537110"  # Replace with the desired account ID or alias

def getHederaAccountInfo(account_id_or_alias):
    # Create the URL for the account information request
    url = f"{base_url}/api/v1/accounts/{account_id_or_alias}"

    # Make the GET request to retrieve account information
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        account_info = response.json()

        # You can now access different fields in the account_info dictionary
        # For example, to access the account balance and alias:
        balance = account_info["balance"]["balance"]
        alias = account_info["alias"]

        print(f"Account Alias: {alias}")
        print(f"Account Balance: {balance}")

        pretty_json = json.dumps(account_info, indent=2)

        print(pretty_json)

        return pretty_json
    else:
        print(f"Failed to retrieve account information. Status Code: {response.status_code}")
        print(response.text)  # Print the error message if available

getHederaAccountInfo(account_id_or_alias)