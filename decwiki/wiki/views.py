from web3 import Web3
import json

ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load the contract ABI and address
with open('path/to/ArticleRegistry.json') as f:
    contract_abi = json.load(f)

contract_address = "YOUR_CONTRACT_ADDRESS"
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    articles = []
    article_count = contract.functions.articleCount().call()
    for i in range(1, article_count + 1):
        article = contract.functions.getArticle(i).call()
        articles.append(article)
    return render(request, 'home.html', {'articles': articles})

@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        tx_hash = contract.functions.createArticle(title, content).transact({
            'from': web3.eth.accounts[0],
            'gas': 3000000
        })
        web3.eth.waitForTransactionReceipt(tx_hash)
        return redirect('home')
    return render(request, 'article_form.html')

@login_required
def edit_article(request, article_id):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        tx_hash = contract.functions.updateArticle(article_id, title, content).transact({
            'from': web3.eth.accounts[0],
            'gas': 3000000
        })
        web3.eth.waitForTransactionReceipt(tx_hash)
        return redirect('home')
    article = contract.functions.getArticle(article_id).call()
    return render(request, 'article_form.html', {'article': article, 'edit': True})
