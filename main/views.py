from django.shortcuts import render, redirect
from main.models import About, Post, What, Categoriya, Project
from main.forms import PostForms
from django.contrib import messages

def index(request):
    module = Post()
    form = PostForms(request.POST, instance=module)
    print(request.POST)
    if form.is_valid():
        print("asas")
        form.save()
        messages.success(request, f"Sms malumotingiz ketdi!")
        return redirect("main:index")

    about = About.objects.all()
    what = What.objects.all()
    categoriya = Categoriya.objects.all()
    project = Project.objects.all()


    ctx = {
        "about": about,
        "what": what,
        "categoriya": categoriya,
        'project': project,
        "form": form
    }

    return render(request, 'main/index.html', ctx)


#
# def project(request, id):
#     categoriya = Categoriya.objects.all()
#     project = Project.objects.filter(categoriya_id=id)
#
#     ctx = {
#         'project': project,
#         'categoriya': categoriya
#     }
#
#     return render(request, 'main/index.html', ctx)
