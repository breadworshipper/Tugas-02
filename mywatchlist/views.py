from django.shortcuts import render
from mywatchlist.models import WatchListItem
from django.http import HttpResponse
from django.core import serializers
from django.template import loader

watch_list_data = WatchListItem.objects.all()

context = {
    'watch_list' : watch_list_data, # data untuk HTML
    'nama' : 'Azhra Yashna Azka',
    'npm' : 2106705291,
}
# Create your views here.
def show_watch_list(request):
    return render(request, 'watchlist.html', context)

# Show data dalam format html
def show_html(request):
    return render(request, 'watchlist.html', context)

# Show data dalam format xml
def show_xml(request):
    return HttpResponse(serializers.serialize("xml", watch_list_data), content_type="application/xml")

# Show data dalam format json
def show_json(request):
    return HttpResponse(serializers.serialize("json", watch_list_data), content_type="application/json")


