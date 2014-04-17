from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    print "4"
    if request.method=="POST":
        form = AuthenticationForm(request.POST)
        print "1"
        print form
        print form.is_bound
        if form.is_valid():
            print "2"
            return redirect("/dashboard/")
    elif request.method=="GET":
        print "3"
        form = AuthenticationForm()
    
    context = {
               "example_attribute": "Hello, world",
               "form":form,
               }
    
    return render(request, "promotion/index.html", context)
