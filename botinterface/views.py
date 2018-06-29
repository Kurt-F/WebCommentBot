from django.shortcuts import HttpResponse, HttpResponseRedirect
from .messagehandling import *


# Handles messages sent from websites
def comments(request, site_id):
    # Make sure it's a POST request
    if request.method == 'GET':
        return(HttpResponse(request.build_absolute_uri()))
        # If the website of origin is not registered, return a 405
        return HttpResponse(status=200)
    # If it isn't, return a 405 error
    else:
        return HttpResponse(status=405)

# Webhook view for telegram
def messages(request):
    # Sort based on type
    # If not a "configuration" message, send back an error.
    pass