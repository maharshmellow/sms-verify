from django.shortcuts import render
from django.http import HttpResponse
import random
import hashlib
import os
import requests

def index(request):
    return render(request, "verify/sms.html")

def verify(request):
    print("verify")
    # if the form wasn't submitted properly, then go to index page
    try:
        phoneNumber = request.POST['phonenumber']

    except:
        return render(request, "verify/sms.html")

    # sent to the user - what the user has to type in
    verificationCode = hashlib.sha512((phoneNumber+str(random.randint(1,1000))+str(os.environ.get("SEED"))).encode("utf-8")).hexdigest()[:5]
    # sent to next page for the get request instead of phone number - to prevent brute forcing the validation
    # verificatoinCode that the user types in will be hashed and checked against the checkSequence
    checkSequence = hashlib.sha512((verificationCode+str(os.environ.get("SEED"))).encode("utf-8")).hexdigest()[:100]
    # send the sms to the user with the verification code
    sendVerificationCode(phoneNumber, verificationCode)
    return render(request, "verify/verification.html", {"code": checkSequence})

def checkCode(request):
    try:
        verificationCode = request.GET['verification']
        correctCheckSequence = request.GET['code']
    except:
        return render(request, "verify/sms.html")

    # check the correct check sequence against the check sequence based on the verification code provided
    checkSequence = hashlib.sha512((verificationCode+str(os.environ.get("SEED"))).encode("utf-8")).hexdigest()[:100]
    if checkSequence == correctCheckSequence:
        return HttpResponse("1")
    else:
        return HttpResponse("0")

def sendVerificationCode(phoneNumber, verificationCode):
    if len(phoneNumber) < 10:
        return              # doesn't give the user an error message - just doesn't send the message

    TILL_URL = os.environ.get("TILL_URL")
    requests.post(TILL_URL, json={"phone":[phoneNumber], "text": "Verication code: " + str(verificationCode)})

    print("Verification Code: ", verificationCode)
