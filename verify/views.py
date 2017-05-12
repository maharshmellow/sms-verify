from django.shortcuts import render
from django.http import HttpResponse
import random
import hashlib
import os
import requests

def index(request):
    """Displays the page that asks for the phone number"""
    return render(request, "verify/sms.html")

def verify(request):
    """Displays the page that asks for the verification code"""
    # if the form wasn't submitted properly, then go to index page
    try:
        phoneNumber = request.POST['phonenumber']
    except:
        return render(request, "verify/sms.html")

    verificationCode = str(random.randint(1000000, 9999999))

    # the check sequence is sent to the next page to verify if the code entered is correct
    checkSequence = hashlib.sha1((verificationCode+str(os.environ.get("SEED"))).encode("utf-8")).hexdigest()

    sendVerificationCode(phoneNumber, verificationCode)
    return render(request, "verify/verification.html", {"code": checkSequence})

def checkCode(request):
    """Checks if the verification code entered is correct"""
    try:
        verificationCode = request.GET['verification']
        correctCheckSequence = request.GET['code']
    except:
        return render(request, "verify/sms.html")

    # check the correct check sequence against the check sequence based on the verification code provided
    checkSequence = hashlib.sha1((verificationCode+str(os.environ.get("SEED"))).encode("utf-8")).hexdigest()
    if checkSequence == correctCheckSequence:
        return HttpResponse("1")
    else:
        return HttpResponse("0")

def sendVerificationCode(phoneNumber, verificationCode):
    """Sends the verification code to the provided phone number using TILL API"""
    if len(phoneNumber) < 10:
        return              # doesn't give the user an error message - just doesn't send the message

    TILL_URL = os.environ.get("TILL_URL")
    requests.post(TILL_URL, json={"phone":[phoneNumber], "text": "Verication code: " + str(verificationCode)})
