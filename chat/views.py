from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    conversation = Conversation.objects.filter(receiver=request.user.id)
    context = {'conversations':conversation}
    
    return render(request, 'index.html', context)




def chat(request, id):
    messages = Conversation.objects.get(id=id)
    if request.method == 'POST':
        sender = User.objects.get(id=request.user.id)
        message = request.POST['message']
        chat = Chat.objects.create(sender=sender, message=message)
        messages.messages.add(chat)
        messages.save()


    print(messages.id)
    
   
    context = {'messages': messages.messages.all(), 'room_name': messages.id}
    return render(request, 'chat.html', context)
