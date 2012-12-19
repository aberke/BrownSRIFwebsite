# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render_to_response

def server_index(request):
	return render_to_response("home.html")

def server_portfolio(request):
	return render_to_response("portfolio.html")
