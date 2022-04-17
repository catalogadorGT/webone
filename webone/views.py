from django.http import HttpResponse


def saludo(request):
#views que regrese un saludo

	return HttpResponse('Hola Fernanda, Benjamin y Susana, saludos a todos')
