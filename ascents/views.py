from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from .models import Ascent
from .forms import AscentForm



class IndexView(generic.ListView):
    template_name = "ascents/index.html"
    context_object_name = "latest_ascents_list"
    
    def get_queryset(self):
        return Ascent.objects.order_by("-date_uploaded")[:15]


class AscentDetailsView(generic.DetailView):
    model = Ascent
    template_name = "ascents/ascent_details.html"


class AscentDeleteView(generic.edit.DeleteView):
    model = Ascent
    success_url = "/logAscents/"
    template_name = "ascents/delete_ascent.html"


def upload_ascent(request):
    title="add an ascent"

    if request.method == 'POST':
        form = AscentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form,
                'title': title,
            }
            return render(request,'ascents/upload_ascent.html',context)

    context = {
        'form':AscentForm(),
        'title':title,
    }
    return render(request,'ascents/upload_ascent.html',context)
