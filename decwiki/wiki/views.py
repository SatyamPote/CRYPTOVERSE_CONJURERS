from django.shortcuts import render, redirect
from .models import Content
from services.blockchain import create_content, upvote_content, downvote_content
from .ipfs_utils import save_to_ipfs

def index(request):
    contents = Content.objects.all()
    return render(request, 'index.html', {'contents': contents})

def create_content_view(request):
    if request.method == 'POST':
        file = request.FILES['file']
        ipfs_hash = save_to_ipfs(file)  # Implement IPFS saving logic
        create_content(ipfs_hash, request.user.address)
        Content.objects.create(author=request.user, ipfs_hash=ipfs_hash)
        return redirect('index')
    return render(request, 'create_content.html')

def content_detail(request, content_id):
    content = Content.objects.get(id=content_id)
    return render(request, 'content_detail.html', {'content': content})

def upvote_content_view(request, content_id):
    content = Content.objects.get(id=content_id)
    upvote_content(content_id, request.user.address)
    content.upvotes += 1
    content.save()
    return redirect('content_detail', content_id=content_id)

def downvote_content_view(request, content_id):
    content = Content.objects.get(id=content_id)
    downvote_content(content_id, request.user.address)
    content.downvotes += 1
    content.save()
    return redirect('content_detail', content_id=content_id)