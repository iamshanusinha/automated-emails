from django.shortcuts import render
from automatedemail.tasks import send_automated_email

def send_email_view(request):
    send_automated_email.delay()  # Call the task asynchronously
    return render(request, 'email_sent.html')



# Render home.html from the templates folder
def home_view(request):
    return render(request, 'home.html')  
