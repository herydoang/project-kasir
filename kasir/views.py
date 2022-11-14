from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {
        'title' : 'Home',
        'welcome' : 'Halaman Index',
    }
    # return HttpResponse(<h1> my home </h1>) #pilih apakah ingin menggunakan HttpResponse atau render
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title' : 'Halaman About',
    }
    return render(request, template_name, )
