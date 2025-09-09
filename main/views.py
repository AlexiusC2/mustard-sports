from django.shortcuts import render
def show_main(request):
    context = {
        
        'name': 'Alexius Christhoper Wijaya',
        'class': 'PBP B',
    }

    return render(request, "main.html", context)
# Create your views here.
