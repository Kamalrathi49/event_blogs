from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    events = Event.objects.all()
    ctx = {'events':events}
    return render(request, 'home.html', ctx)

@login_required
def AddEvent(request):
    if request.method  == 'POST':
        form  = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.creater = request.user
            event.save()
            return redirect('/')
        else:
            return redirect('/event')
            
    else:
        form = EventForm()
        ctx = {'form':form}
        return render(request, 'addevent.html', ctx)