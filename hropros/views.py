from django.shortcuts import redirect

def redirect_polls(request):
    return redirect('polls:index', permanent=True)