from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "OOOOOOOOH YEEEEEEAH"
    return HttpResponse(response)


from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
   
    random = get_random_string(length=14)
    context = {
        "random": random
    }
    
    if 'num' not in request.session:
        request.session['num'] = 0
    request.session['num'] += 1

    return render(request, 'random_word/index.html', context)


def create(request):
    return redirect('/')

def reset(request):
    request.session['num'] = 0
    return redirect('/random_word')
