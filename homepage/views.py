from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def v_index(request):
    context = {
        "providers": [
            {
                "first_name": "Pepito",
                "last_name": "Rojas"
            },
            {
                "first_name": "Felipe",
                "last_name": "Iero"
            }, 
            {   "first_name": "Amanda",
                "last_name": "Miguel"
            }, 
            {   "first_name": "Carlos",
                "last_name": "Mueres"
            }, 
            {   "first_name": "Pablo",
                "last_name": "Horrores"
            }, 
            {   "first_name": "Felicita",
                "last_name": "Bonita"}
        ]
    }
    return render(request, "homepage/index.html", 
                  context)
