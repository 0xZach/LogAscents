from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic

from itertools import chain

from .models import Ascent
from .forms import AscentForm



def Index(request):
    context={}
    template = "ascents/index.html"
    
    """
    if request.method == 'POST':
        query = request.POST['search_query']
        # context['query'] = query
        return redirect("list/?query="+query) # TODO: This sounds like a very junky idea
    else:"""
    
    return render(request,template,context)


def ascent_list(request):
    template = "ascents/list.html"

    if request.GET.get("query"):
        query = request.GET.get("query")
        nameList = Ascent.objects.filter(name__icontains=query)
        gradeList = Ascent.objects.filter(grade__name=query)
        userList = Ascent.objects.filter(user__icontains=query)
        resultList = list(chain(nameList,gradeList,userList))
        
    else:
        resultList = Ascent.objects.order_by("-date_uploaded")[:15]
    
    context = {
        'latest_ascents_list':resultList,
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




class AscentDetailsView(generic.DetailView):
    model = Ascent
    template_name = "ascents/ascent_details.html"


class AscentDeleteView(generic.edit.DeleteView):
    model = Ascent
    success_url = "/logAscents/"
    template_name = "ascents/delete_ascent.html"
