from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "verify/sms.html")

def verify(request):
    print("verify")
    phoneNumber = request.POST['phonenumber']
    
    return render(request, "verify/verification.html")
