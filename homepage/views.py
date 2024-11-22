from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def v_index(request):
    context = {
        "providers": [
            {
                "first_name": "Thomas",
                "last_name": "Reed",
                "photo": "https://images-assets.nasa.gov/image/iss072e145396/iss072e145396~medium.jpg"
            },
            {
                "first_name": "Mark",
                "last_name": "Iero",
                "photo": "https://images-assets.nasa.gov/image/iss072e145408/iss072e145408~medium.jpg"
            }, 
            {   "first_name": "Andy",
                "last_name": "Warhol",
                "photo": "https://images-assets.nasa.gov/image/iss072e188539/iss072e188539~medium.jpg"
            }, 
            {   "first_name": "Holden",
                "last_name": "Hands",
                "photo": "https://images-assets.nasa.gov/image/iss072e189176/iss072e189176~medium.jpg"
            }, 
            {   "first_name": "Pablo",
                "last_name": "Honey",
                "photo": "https://images-assets.nasa.gov/image/KSC-20241107-PH-KLS01_0011/KSC-20241107-PH-KLS01_0011~medium.jpg"
            }, 
            {   "first_name": "Phillip",
                "last_name": "Bells",
                "photo": "https://images-assets.nasa.gov/image/JPL-20170821-SUNs-000C-Eclipse3/JPL-20170821-SUNs-000C-Eclipse3~medium.jpg"
            }
                
        ]
    }
    return render(request, "homepage/index.html", 
                  context)
def v_feedback_gracias(request):
    return render(request, "homepage/feedback_gracias.html")

from django.shortcuts import redirect
def v_feedback_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print("++", data)
        ##Guardar base de datos
        return redirect("/feedback/gracias")
    
    return redirect("/")


