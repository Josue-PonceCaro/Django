from django.contrib import admin
from django.urls import path, include

def testerPerson(self):
    print('Testing person ======================++++++++++')

urlpatterns = [
    path('persona/', testerPerson),
]
