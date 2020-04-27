from django.db import models


class Artist(models.Model):
    Name = models.CharField(max_length=120)

    def __str__(self):
        return self.Name


class Album(models.Model):
    Title = models.CharField(max_length=160)
    artist = models.ForeignKey('Artist', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Title


class Track(models.Model):
    Name = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.DO_NOTHING)
    Composer = models.CharField(max_length=220)
    Milliseconds = models.TextField()
    Bytes = models.IntegerField()
    UnitPrice = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.Name
