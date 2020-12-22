from django.shortcuts import render
from .forms import UserInfoIDForm
from .models import UserInfoID, PartyVotes
import tkinter as tk
import socket
from django.http import HttpResponseRedirect
from django.urls import reverse
vl = True
# Create your views here.
def startServer(request):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('122.176.22.64',1024))
    return HttpResponseRedirect(reverse('index'))
def index(request):
    return render(request, "index.html", {})
def pollLogin(request):
    not_registered = True
    party_form = PartyVotes()
    if request.method == "POST":
        user_form = UserInfoIDForm(data=request.POST)
        if user_form.is_valid():
            global party1,party2,party3,party4
            party = request.POST['party']
            user = user_form.save()
            party_form.person = user
            party_form.party = party
            party_form.save()
            s.send(party.encode('ascii'))
            not_registered = False
    else:
        user_form = UserInfoIDForm()
    return render(request, 'polling.html', {'userf':user_form, 'not_registered':not_registered})
def closeServer(request):
    s.close()
    return HttpResponseRedirect(reverse('index'))
