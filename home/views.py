from django.shortcuts import render
from django.shortcuts import redirect

from home.models import Log

def index(request):
	for name in request.GET:
		log = Log()
		log.log_type = 'GET'
		log.log_name = name
		log.log_value = request.GET[name]
		log.save()
	for name in request.POST:
		log = Log()
		log.log_type = 'POST'
		log.log_name = name
		log.log_value = request.POST[name]
		log.save()

	return render(request,'home.html');

def log(request, n=2):

	page = request.GET.get('page', 1)
	offset = (int(page) - 1) * int(n)
	last_index = int(offset) + int(n)

	page_count = ((Log.objects.count() - 1) / int(n)) + 1

	logs = Log.objects.all().order_by('-id')[offset:last_index]
	data = {
		'n': n,
		'logs': logs,
		'page_range': range(1, page_count + 1)
	}
	return render(request,'log.html', data);

def delete(request, log_id):
	log = Log.objects.get(id=log_id)
	log.delete()
	return redirect('/log/5')