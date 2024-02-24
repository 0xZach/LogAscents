from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Ascent
from .forms import AscentForm



def Index(request):
    template = "ascents/index.html"
    context={}
    return render(request,template,context)


class AscentDetailsView(generic.DetailView):
    model = Ascent
    template_name = "ascents/ascent_details.html"


class AscentDeleteView(generic.edit.DeleteView):
    model = Ascent
    success_url = "/logAscents/"
    template_name = "ascents/delete_ascent.html"


def ascent_list(request):
    template = "ascents/list.html"

    if request.GET.get("query"):
        query = '%'+request.GET.get("query")+'%'
        theList = Ascent.objects.filter(name__icontains=query)
    else:
        theList = Ascent.objects.order_by("-date_uploaded")[:15]
    
    context = {
        'latest_ascents_list':theList,
    }
    return render(request,template,context)


def upload_ascent(request):

    if request.method == 'POST':
        form = AscentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form,
            }
            return render(request,'ascents/upload_ascent.html',context)

    context = {
        'form':AscentForm(),
    }
    return render(request,'ascents/upload_ascent.html',context)
