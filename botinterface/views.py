from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from botinterface.models import UserSite
from django.core.exceptions import ObjectDoesNotExist
from json import dumps
from .messagehandling import *

# Handles messages sent from websites
@csrf_exempt
def comments(request, site):
    # Make sure it's a POST request
    if request.method == 'POST':
        print(request.body)
        # If the website of origin is not registered, return a 405
        try:
            s = UserSite.objects.get(pk=site)
        except ObjectDoesNotExist:
            return HttpResponse(status=405)
        if s.url != request.META['HTTP_HOST']:
            return HttpResponse(status=405)
        # Finally, form the message into a JSON and send it to the telegram bot
        # (Test ver)
        return HttpResponse(str(dumps(request.POST.dict())))
    # If it isn't, return a 405 error
    else:
        return HttpResponse(status=405)


# Webhook view for telegram
def messages(request):
    # Sort based on type
    # If not a "configuration" message, send back an error.
    pass


def test(request):
    return HttpResponse("<b>test</b>")
