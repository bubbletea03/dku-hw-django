from django.http import HttpResponse, Http404
from django.template import loader
from .models import Project


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
    return HttpResponse("Hello, world. You're at the polls detail.")