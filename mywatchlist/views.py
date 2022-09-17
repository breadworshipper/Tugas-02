from django.shortcuts import render
from mywatchlist.models import WatchListItem
from django.http import HttpResponse
from django.core import serializers

watch_list_data = WatchListItem.objects.all()

context = {
    'watch_list' : watch_list_data, # data untuk HTML
    'nama' : 'Azhra Yashna Azka',
    'npm' : 2106705291,
}
# Create your views here.
def show_watch_list(request):
    return render(request, 'watchlist.html', context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", watch_list_data), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", watch_list_data), content_type="application/json")


