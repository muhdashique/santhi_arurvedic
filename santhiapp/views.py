from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')




def about(request):
    return render(request,'about.html')
    



def facilities(request):
    return render(request,'facilities.html')    



def gallery(request):
    return render(request,'gallery.html')      





def treatment(request):
    return render(request,'treatment.html')




def advtreatment(request):
    return render(request,'advtreatment.html')



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json

@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            mobile = data.get('mobile')
            message = data.get('message')

            subject = " Website Assistant Chatbot"
            full_message = f"""
            Name: {name}
            Email: {email}
            Mobile: {mobile}
            
            Message:
            {message}
            """

            send_mail(
                subject,
                full_message,
                'youremail@example.com',  # Replace with your Django 'EMAIL_HOST_USER'
                ['shanthihospital2004@gmail.com'],  # Recipient
                fail_silently=False,
            )

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

