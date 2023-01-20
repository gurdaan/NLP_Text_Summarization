from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from WebsiteTextParser import TextParser
from SummarizingModel import summarizer
import json
from django.http import JsonResponse

# Create your views here.

def index(request):
    context={
        'variable':"Gurdaan Walia "
    }
    return render(request,'index.html',context)

def url(request):
        
    context={'parsedText':'','summarizedText':''}  
    if request.method == 'POST':
        submit_values = request.POST.getlist('submit_button')
        if 'Submit 1' in submit_values:
            # Do something when 'Submit 1' is clicked
            urlData=request.POST.get('urlName')
            #messages.success(request, 'Extracting Text')
            soupObject=TextParser.parser(urlData)
            context['parsedText']=soupObject.get_text()
            dummyText=context['parsedText']
        else:
            data = json.loads(request.body)
            p_text = data['p_text']
            # Do something with the data
            summarizedData=summarizer.summarize(p_text)
            data = {'summarizedData': summarizedData}
            json_data = json.dumps(data)
            return JsonResponse(json_data, safe=False)
    return render(request,'url.html',context)


def text(request):
    return render(request,'text.html')

def fileUpload(request):
    return render(request,'fileUpload.html')

def contactUs(request):
    if request.method=="POST":
        # Request.POST gives the dictionary
        email=request.POST.get('email')
        text=request.POST.get('text')
        date=datetime.now()
        contact=Contact(email=email,text=text,date=date)
        contact.save()
        messages.success(request, 'Profile details updated.')
    
    return render(request,'contactUS.html')

def textFromImage(request):
    return render(request,'textFromImage.html')


    #return HttpResponse("This is a ContactUs string")