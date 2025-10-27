from django.shortcuts import render
from .models import Restaurant,MenuCategory
from django.http import HttpResponse
import datetime
from rest_framework.generics import ListAPIView
from .serializers import MenuCategorySerializer

# Create your views here.
def homepage(request):
    try:
        # Fetch the first restaurant from DB (or you can filter by ID)
        restaurant = Restaurant.objects.first()

        if not restaurant:
            # If no restaurant is found, show a fallback
            return HttpResponse(
                "<h1>No restaurant found. Please register a restaurant.</h1>",
                status=404
            )

        context = {
            "restaurant_name": restaurant.name,
            "phone_number": restaurant.phone_number,
            "current_year": datetime.datetime.now().year
        }
        return render(request, "home/index.html", context)

    except Exception as e:
        print(f"Error loading homepage: {e}")  # In production → use logging
        return HttpResponse(
            "<h1>Oops! Something went wrong.</h1><p>Please try again later.</p>",
            status=500
        )

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer