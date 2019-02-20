from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def project(request):
	return render(request, 'projects.html')

def project_detail(request):
	return render(request, 'project_detail.html')

def blog(request):
	return render(request, 'blog.html')

def blog_detail(request):
	return render(request, 'blog_detail.html')