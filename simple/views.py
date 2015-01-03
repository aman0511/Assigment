from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html','')

  
def wall_post(request,id=None):  
    fb = get_persistent_graph(request)  
  
    message = request.POST.get('message')  
    fb.set('me/feed', message=message)  
  
    messages.info(request, 'Posted the message to your wall')  
  
    return redirect('wall_post') 