from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

 
def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))

def about(request):
    return HttpResponse("This is the about page")
