from django.http import HttpResponse

def home(request):
    return HttpResponse("This is Home page")

def about(request):
    return HttpResponse("this is about section")

def cart(request):
    return HttpResponse("this is cart section")

def read_one(reqest):
    with open ("one.txt","r") as f:
        s = f.readlines()
    for index, line in enumerate(s): 
        return HttpResponse(line)  

print(read_one)