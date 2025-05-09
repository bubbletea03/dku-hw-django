from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Project, Rating
from django.urls import reverse


def index(request):
    project_list = Project.objects.order_by('-pub_date')
    template = loader.get_template('index.html')
    context = {
        'project_list': project_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'detail.html', {'project': project, 'ratings': [1,2,3,4,5]})

def rate(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.rating_set.create(rating=request.POST['rating'])
    return HttpResponseRedirect(reverse('PortfolioApp:index'))