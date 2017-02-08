from django.shortcuts import render


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
