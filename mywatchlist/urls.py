from django.urls import path
from mywatchlist.views import show_watch_list
from mywatchlist.views import show_xml
from mywatchlist.views import show_json

app_name = 'watchlist'

urlpatterns = [
    path('', show_watch_list, name='show_watch_list'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
