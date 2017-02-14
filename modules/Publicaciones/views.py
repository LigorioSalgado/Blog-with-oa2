from django.shortcuts import render,redirect
from .models import TAGS,Publicacion
from .functions import handle_uploaded_file
def Index(request):

	public = [
		{	"Nombre":"Mi primer Proyecto en Django",
			"Autor":"Edwin Salgado",
			"Fecha":"7-02-2017",
			"Rating":5
		},

		{	"Nombre":"API Rest",
			"Autor":"Paco Ocampo",
			"Fecha":"7-02-2017",
			"Rating":1

		},

		{	"Nombre":"Angular for noobs",
			"Autor":"Uriel Torres",
			"Fecha":"7-02-2017",
			"Rating":4
		},
	]

	return render(request,'Publicaciones/index.html',{ "publicaciones":public })



def Add(request):

	if request.method == 'POST':
		if request.user.is_authenticated():
			types = {'image/jpeg':'.jpg','image/png':'.png','image/gif':'.gif'}
			image_name = request.FILES['imagen'].name+types[request.FILES['imagen'].content_type]
			publicacion = Publicacion()

			publicacion.nombre = request.POST['nombre']
			publicacion.contenido = request.POST['contenido']
			publicacion.tags = request.POST['tag']
			publicacion.autor = request.user
			publicacion.imagen = handle_uploaded_file(request.FILES['imagen'],image_name)

			publicacion.save()

			return redirect('Publicaciones:index-publicacion')

	else:
		dict_tags = dict((x,y) for x,y in TAGS)
		return render(request,'Publicaciones/add.html',{"tags":dict_tags})
