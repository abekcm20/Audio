from django.shortcuts import render,redirect
from .models import Song,Podcast,Audiobook
# Create your views here.
def songprofile(request,pk):
    songprofile = Song.objects.get(id=pk)
    return render(request,'#.html',{'songprofile ': songprofile })

def addsong(request):
    if request.method == 'POST':
        new_song = Song(
          ID =request.POST['ID'],
          Name_of_the_song =request.POST['Name_of_the_song'],
          Duration_in_sec =request.POST['Duration_in_sec'],
          uploaded_time =request.POST['uploaded_time']
        )
        new_song.save()
        return redirect('/')
    return render(request, '#.html')


def editsong(request,pk):
    songprofile = Song.objects.get(id=pk)
    if request.method == 'POST':
        songprofile.ID = request.POST['ID']
        songprofile.Name_of_the_song = request.POST['Name_of_the_song']
        songprofile.Duration_in_sec = request.POST['Duration_in_sec']
        songprofile.uploaded_time = request.POST['uploaded_time']
        songprofile.save()
        return redirect('/profile/'+str(songprofile.id))
    return render(request,'#.html',{'songprofile': songprofile})

def deletesong(request,pk):
    songprofile = Song.objects.get(id=pk)
    if request.method == 'POST':
        songprofile.delete()
        return redirect('/')
    return render(request,'#.html',{'songprofile': songprofile})

def podcastprofile(request,pk):
    podcastprofile = Podcast.objects.get(id=pk)
    return render(request,'#.html',{'podcastprofile ': podcastprofile})

def addpodcast(request):
    if request.method == 'POST':
        new_podcast = Podcast(
          ID =request.POST['ID'],
          Name_of_the_podcast =request.POST['Name_of_the_podcast'],
          Duration_in_sec =request.POST['Duration_in_sec'],
          uploaded_time =request.POST['uploaded_time'],
          Host =request.POST['Host'],
          Participants =request.POST['Participants']
        )
        new_podcast.save()
        return redirect('/')
    return render(request, '#.html')


def editpodcast(request,pk):
    podcastprofile = Podcast.objects.get(id=pk)
    if request.method == 'POST':
        podcastprofile.ID = request.POST['ID']
        podcastprofile.Name_of_the_podcast = request.POST['Name_of_the_song']
        podcastprofile.Duration_in_sec = request.POST['Duration_in_sec']
        podcastprofile.uploaded_time = request.POST['uploaded_time']
        podcastprofile.Host = request.POST['Host']
        podcastprofile.Participants = request.POST['Participants']
        podcastprofile.save()
        return redirect('/profile/'+str(podcastprofile.id))
    return render(request,'#.html',{'podcastprofile': podcastprofile})

def deletepodcast(request,pk):
    podcastprofile = Podcast.objects.get(id=pk)
    if request.method == 'POST':
        podcastprofile.delete()
        return redirect('/')
    return render(request,'#.html',{'podcastprofile': podcastprofile})

def audiobookprofile(request,pk):
    audiobookprofile = Audiobook.objects.get(id=pk)
    return render(request,'#.html',{'audiobookprofile ': audiobookprofile})

def addaudiobooks(request):
    if request.method == 'POST':
        new_audiobook = Audiobook(
          ID =request.POST['ID'],
          Title_of_the_audiobook =request.POST['Title_of_the_audiobook'],
          Author =request.POST['Author'],
          Narrator =request.POST['Narrator'],
          Duration_in_sec =request.POST['Duration_in_sec'],
          uploaded_time =request.POST['uploaded_time']
        )
        new_audiobook.save()
        return redirect('/')
    return render(request, '#.html')


def editaudiobook(request,pk):
    audiobookprofile = Audiobook.objects.get(id=pk)
    if request.method == 'POST':
        podcastprofile.ID = request.POST['ID']
        podcastprofile.Title_of_the_audiobook = request.POST['Title_of_the_audiobook']
        podcastprofile.Author = request.POST['Author']
        podcastprofile.Narrator = request.POST['Narrator']
        podcastprofile.Duration_in_sec = request.POST['Duration_in_sec']
        podcastprofile.uploaded_time = request.POST['uploaded_time']

        podcastprofile.save()
        return redirect('/profile/'+str(audiobookprofile.id))
    return render(request,'#.html',{'audiobookprofile': audiobookprofile})

def deleteaudiobook(request,pk):
    audiobookprofile = Podcast.objects.get(id=pk)
    if request.method == 'POST':
        audiobookprofile.delete()
        return redirect('/')
    return render(request,'#.html',{'audiobookprofile': audiobookprofile})

