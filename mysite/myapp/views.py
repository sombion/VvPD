from django.shortcuts import render

def home(request):
  data = {
		"title": "Главная"
	}
  return render(request, 'myapp/index.html', data)