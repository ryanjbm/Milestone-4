from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to renders the shoping bag contents """
    
    return render(request, 'bag/bag.html')