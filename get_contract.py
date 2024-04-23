from web3 import Web3
import requests

# Connect to an Ethereum node
Web3_api_key = "ad1054980384489c913bffc868148a05"
web3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{Web3_api_key}"))


def get_source_code(hash_code):
    etherScan_api_key = "HMZ5ZMCX861D1Z9SH7VUHYRFQSUV1R4MAX"
    api_url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={hash_code}&{etherScan_api_key}"

    response = requests.get(api_url)
    data = response.json()

    if data["status"] == "1":
        print("Smart contract is verified!")

        source_code = data["result"][0]["SourceCode"]
        return source_code
    else:
        print("Smart contract is not verified.")
