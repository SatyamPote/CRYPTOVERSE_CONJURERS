# myapp/ipfs_utils.py
import ipfshttpclient

def save_to_ipfs(file):
    # Connect to the local IPFS node
    client = ipfshttpclient.connect()
    
    # Add the file to IPFS
    res = client.add(file)
    
    # Return the IPFS hash
    return res['Hash']