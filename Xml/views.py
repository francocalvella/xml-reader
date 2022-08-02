from django.shortcuts import redirect, render
from .models import AlbumXml
from .forms import XmlForm
import xml.dom.minidom as xmldom

# Create your views here.

def xml(request):
    albums_array = AlbumXml.objects.all()
    if request.method == 'POST':
        form = XmlForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            domtree = xmldom.parse(data['xml'])    
            group = domtree. documentElement    
            albums = group.getElementsByTagName('album')
            for album in albums:
                title = album.getElementsByTagName('title')[0].childNodes[0].nodeValue
                date = album.getElementsByTagName('release')[0].childNodes[0].nodeValue
                author = album.getElementsByTagName('author')[0].childNodes[0].nodeValue
                best_song = album.getElementsByTagName('best_song')[0].childNodes[0].nodeValue
                newAlbum = AlbumXml(title=title, release_year=date, author=author, best_song=best_song, xml=data['xml'])
                newAlbum.save()
            return redirect('xml')
    form = XmlForm()
    return render(request, 'xml/index.html', {'albums_array': albums_array, 'form': form})