from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def secureQR(request,QR):
    from pyaadhaar.deocde import AadhaarSecureQr
    obj  = AadhaarSecureQr(QR)
    print(obj.decodeddata())
    return JsonResponse(obj.decodeddata())


