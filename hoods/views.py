from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render

# Create your views here.
def hood(request):
    return render(request,'index.html')

def search_results(request):

    if 'hood' in request.GET and request.GET["hood"]:
        search_term = request.GET.get("hood")
        searched_hoods = Hood.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"hoods": searched_hoods})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})