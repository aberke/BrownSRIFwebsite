# Create your views here.

from django.http import HttpResponse, Http404

from django.shortcuts import render_to_response, render

from models import Stock, Pitch, SemesterPitch, EducationPageSection, GuidePageSection

def serve_index(request):
	return render(request, "home.html",{'page':'index'})

def serve_portfolio(request):
	context = {}
	last_updated_list = Stock.objects.all().order_by('last_updated')
	num_holdings = len(last_updated_list)
	if num_holdings > 0 :
		last_updated = last_updated_list[0].last_updated
		stocks = Stock.objects.all().order_by('purchase_date')
		context = {'page':'portfolio','last_updated': last_updated, 'stocks': stocks}
	
	context['num_holdings'] = num_holdings
	return render(request, "portfolio.html", context)


def serve_education(request):
	items = EducationPageSection.objects.all()
	return render(request, 'education.html', {'page':'education', 'items': items})


def serve_guide(request):
	items = GuidePageSection.objects.all()
	return render(request, 'guide.html', {'page':'guide', 'items': items})


def serve_pitches(request):
	# if no semester specified, take most recent semester
	return serve_pitches_by_id(request, -1)

def serve_pitches_by_id(request, semester_id):
	semesters = SemesterPitch.objects.all().order_by('-year')
	if len(semesters) == 0:
		return render(request, 'pitches.html', {'page':'pitches'})
	else:
		# if no semester specified, take most recent semester
		if semester_id < 0:
			selected_semester = semesters[0]
		else:
			try:
				selected_semester = SemesterPitch.objects.get(pk=semester_id)
			except SemesterPitch.DoesNotExist:
				raise Http404
		pitches = selected_semester.pitch_set.all().order_by('pitch_date')
		context = {'page':'pitches', 'semesters': semesters, 'selected_semester': selected_semester, 'pitches': pitches}
		return render(request, 'pitches.html', context)




