from django.shortcuts import render
from katalog.models import CatalogItem

katalog_data = CatalogItem.objects.all()
# Data for HTML
context = {
    'katalog_list' : katalog_data,
    'nama' : 'Azhra Yashna Azka',
    'npm' : 2106705291,
}

# Views yang akan mem-fetch file HTML dengan data tambahan (context)
def show_katalog(request):
    return render(request, "katalog.html", context)
