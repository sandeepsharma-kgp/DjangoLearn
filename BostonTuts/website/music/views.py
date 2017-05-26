from django.views import generic
from .models import Album

class IndexView(generic.ListView):
	template_name = 'music/index.html'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/index.html'
	"""docstring for DetailView"generic.DetailViewf 
	model = Album
	template_name = 'music/index.html'__init__(self, arg):
		super(DetailView,generic.DetailView._
		model = Album
		template_name = 'music/index.html'_init__()
		self.arg = arg
		

# # from django.http import Http404
# # from django.shortcuts import render
# from django.shortcuts import render , get_object_or_404
# from .models import Album
# # Create your views here.


# def index(request) :
# 	all_albums = Album.objects.all()
# 	return render(request,'music/index.html',{'all_albums':all_albums})

# def detail(request , album_id):
# 	# try :
# 	# 	album = Album.objects.get(pk=album_id)
# 	# except :
# 	# 	raise Http404("Album doesn't exist!")
# 	album = get_object_or_404(Album,pk= album_id)
# 	return render(request,'music/detail.html',{'album':album})

# def favourite(request,album_id):
# 	album = get_object_or_404(Album,pk = album_id)
# 	try:
# 		selected_song = album.song_set.get(pk=request.POST['song'])
# 	except (KeyError, Song.DoesNotExist):
# 		return render(request, 'music/detail.html',{
# 			'album':album,
# 			'error_message':"You didn't select a valid song"
# 			})
# 	else:
# 		selected_song.is_favourite = True
# 		selected_song.save()
# 		return render(request,'music/detail.html',{'album':album})