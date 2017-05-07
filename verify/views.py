from django.shortcuts import render
import random
import hashlib
import os
# Create your views here.
def index(request):
    return render(request, "verify/sms.html")

def verify(request):
    print("verify")
    phoneNumber = request.POST['phonenumber']
    randomNumber = str(random.randint(1, 1000))
    verificationCode = getVerificationCode(phoneNumber, randomNumber)

    sendVerificationCode(verificationCode)

    return render(request, "verify/verification.html", {"phone": phoneNumber, "random": randomNumber})


def getVerificationCode(phoneNumber, randomNumber):
    return(hashlib.sha512((phoneNumber+randomNumber+str(os.environ.get("SEED"))).encode("utf-8")).hexdigest()[:5])

def sendVerificationCode(verificationCode):
    print("Verification Code: ", verificationCode)
    # TODO put the api call for sending the verification code here
