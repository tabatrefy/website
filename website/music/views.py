from django.http import HttpResponse
from .models import Album

def index(request):
    all_albums=Album.objects.all()
    html=''
    for album in all_albums:
        url'/music/' + str(album.id)+'/'
        html +='<a href="' + url +'">' + album.abum_title + '</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("details for album id:" + str(ablbum_id))
