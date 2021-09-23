from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import reverse, HttpResponse

def home(request):
    string = "我在自强学堂学习Django，用它来建网站"
    info_dict = {'site': '自强学堂', 'content': '各种IT技术教程'}
    return render(request, 'learn/home.html',{'info_dict':info_dict})


def firstView(request):
    return HttpResponse("helloword!")


def add1(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = str(int(a) + int(b))
    return HttpResponse(c)

def add2(request,a,b):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = str(int(a) + int(b))
    return HttpResponse(c)



def index(request):
    return render(request, 'learn/home.html')

def url_test(request):
    url = reverse('namesp1:add2')
    print(url)
    return HttpResponse("OK")



# Create your views here.
