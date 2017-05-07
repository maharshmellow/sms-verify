from django.shortcuts import render
import random
import hashlib
import os
# Create your views here.
def index(request):
    return render(request, "verify/sms.html")

def verify(request):
    print("verify")
    # if the form wasn't submitted properly, then go to index page
    try:
        phoneNumber = request.POST['phonenumber']
    except:
        return render(request, "verify/sms.html")

    verificationCode = getVerificationCode(phoneNumber)

    # send the sms to the user with the verification code
    sendVerificationCode(verificationCode)

    return render(request, "verify/verification.html", {"phone": phoneNumber})


def getVerificationCode(phoneNumber):
    return(hashlib.sha512((phoneNumber+str(os.environ.get("SEED"))).encode("utf-8")).hexdigest()[:5])

def sendVerificationCode(verificationCode):
    print("Verification Code: ", verificationCode)
    # TODO put the api call for sending the verification code here
