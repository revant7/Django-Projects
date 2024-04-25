from django.shortcuts import render
from contact.models import Contact

# Create your views here.


def contact(request):
    if request.method == "post":
        name = request.post.get('name')
        email = request.post.get('email')
        mobile = request.post.get('mobile')
        message = request.post.get('message')
        contact = Contact(name = name, email = email, mobile = mobile, message = message, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')

