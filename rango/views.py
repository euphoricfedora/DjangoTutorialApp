from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world! <br><br><a href='/rango/about'>About</a>" )

def about( request ):
	return HttpResponse( "Rango says: Here is the About page. <br><br><a href='/rango/'>Index</a>" )
