from django.shortcuts import render

def home(request):
    print(request.user)
    return render(request, 'travel/home.html', {'current_user': request.user})
