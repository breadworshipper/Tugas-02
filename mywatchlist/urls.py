from django.urls import path
from mywatchlist.views import show_watch_list
from mywatchlist.views import show_xml, show_json, show_html

app_name = 'watchlist'

urlpatterns = [
    path('', show_watch_list, name='show_watch_list'),
    path('html', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
