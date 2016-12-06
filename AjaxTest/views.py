from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

def data(request, id):
    rlist = [['Jack', 'Chinese'], ['Mike', 'English'], ['Bob', 'Math'], ['Frank', 'Art'], ['Lucy', 'Music']]
    rlist2 = []
    rlist2.append({"name" : rlist[int(id)][0], "subject" : rlist[int(id)][1]})
    rjson = json.dumps(rlist2)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(rjson)
    return response
    
def update(request):
    return render_to_response('update.html')