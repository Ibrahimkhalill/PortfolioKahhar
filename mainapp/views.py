from django.shortcuts import redirect, render
from .models import *
# Create your views here.
from django.contrib import messages

def home(request):
  images= Image.objects.all()
  videos= Video.objects.all()
  context={
    "images": images,
    "videos":videos
  }
  return render(request, 'index.html',context)


<<<<<<< HEAD

=======
>>>>>>> bf0b16546991b0c6323ec3eb7ac49eb1cbbd0a1e
def message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_content = request.POST['message-content']

        new_message = Message(name=name, email=email, subject=subject, message=message_content)
        new_message.save()

        messages.success(request, "Message Sent Successfully!")
<<<<<<< HEAD
        return redirect('')
    # Handle the case when the request method is not "POST"
    else:
        messages.error(request, "Invalid Request Method")
        return redirect('')
=======
        return redirect('home')
    # Handle the case when the request method is not "POST"
    else:
        messages.error(request, "Invalid Request Method")
        return redirect('home')
>>>>>>> bf0b16546991b0c6323ec3eb7ac49eb1cbbd0a1e

