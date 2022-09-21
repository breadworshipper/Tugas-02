from django.db import models

# Model DataBase lokal watchlist
class WatchListItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=255) # DateField() ngga bisa :(
    review = models.TextField()
