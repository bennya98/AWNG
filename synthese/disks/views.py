from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from disks.models import Artist, Album, Track


def home(request):
    albums = Album.objects.all()

    return render(request, 'disks/home.html', {'albums': albums})


def albumview(request, id):
    albums = Album.objects.all()
    album = get_object_or_404(Album, id=id)
    tracks = album.track_set.all()

    return render(request, 'disks/album.html', {'tracks': tracks, 'album': album, 'albums': albums})


def search(request):
    query = request.GET.get('q', '')
    # The empty string handles an empty "request"
    if query:
        queryset = Q(Title__icontains=query)
        # I assume "text" is a field in your model
        # i.e., text = model.TextField()
        # Use | if searching multiple fields, i.e.,
        # queryset = (Q(text__icontains=query))|(Q(other__icontains=query))
        results = Album.objects.filter(queryset).distinct()
    else:
        results = []
    return render(request, 'disks/home.html', {'albums': results})
