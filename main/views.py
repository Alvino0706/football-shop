from django.shortcuts import render

def show_main(request):
    context = {
        'title' : 'Football Shop',
        'name' : 'Alvino Revaldi',
        'class' : 'PBP E'
    }
    return render(request, "main.html", context)
