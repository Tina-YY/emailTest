from django.core.mail import send_mail

def send_custom_email(request):
    email_address = request.GET.get('emailAddress', None)
    is_linux = request.GET.get('isLinux', None)

    print(email_address, is_linux)
    
    subject = 'Low disk space warning'
    message = 'Your usage on Linux machine is over 80%, please delete files or apply for more spaces.'
    if not is_linux:
            message = 'Your usage on Windows machine is over 80%, please delete files or apply for more spaces.'
    
    from_email = '18721812130@163.com'  # Replace with the specified email address
    recipient_list = [email_address]  # Replace with the recipient's email address

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    # Optionally, you can return a response or redirect to another page
    # return HttpResponse('Email sent successfully!')