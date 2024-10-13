from django.http import HttpResponse

def yt(request):
    return HttpResponse('''<div><h1>Yt link is below</h1><a href="https://www.youtube.com/" target="_main">yt links</a> </div> 
                        <div><h1>Docker links is</h1><a href="https://hub.docker.com/"> docker_link</a> </div>
                        <div><a href="http://127.0.0.1:8000/" style="display: inline-block; padding: 10px 20px; background-color: red; color: white; text-decoration: none; border-radius: 5px; text-align: center; cursor: pointer;">Home</a></div>
                        <div><a href="../">Back</a></div>''')

def home(request):
    return HttpResponse('''<div><a href="http://127.0.0.1:8000/">Home</a></div>
                        <div><a href="http://127.0.0.1:8000/yt">yt</a></div>''')


#def docker(response):
#    return HttpResponse('''<h1>Docker links is</h1><a href="https://hub.docker.com/"> docker_link</a>''')