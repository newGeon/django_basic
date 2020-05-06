from django.shortcuts import render

# Create your views here.
def photo_list(request):
    return render(request, 'marker/photo_list.html', {})