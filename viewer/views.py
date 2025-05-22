from django.shortcuts import render

def pano_view(request):
    return render(request, 'viewer/pano.html')
