from web3 import Web3
import json

# Set up the connection to the local Ganache blockchain
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load the contract ABI and address
with open('path_to_abi.json') as f:
    contract_abi = json.load(f)
contract_address = 'your_contract_address_here'
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def create_content(ipfs_hash, user_address):
    tx_hash = contract.functions.createContent(ipfs_hash).transact({'from': user_address})
    web3.eth.waitForTransactionReceipt(tx_hash)

def upvote_content(content_id, user_address):
    tx_hash = contract.functions.upvoteContent(content_id).transact({'from': user_address})
    web3.eth.waitForTransactionReceipt(tx_hash)

def downvote_content(content_id, user_address):
    tx_hash = contract.functions.downvoteContent(content_id).transact({'from': user_address})
    web3.eth.waitForTransactionReceipt(tx_hash)