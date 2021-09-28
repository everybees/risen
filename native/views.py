from django.shortcuts import render

from native.models import Native


def hello_world(request):
    return render(request, "hello_world.html")


def create_page(request):
    return render(request, "some.html")


def get_all_natives(request):
    natives = Native.objects.all()
    context = {
        "natives": natives
    }
    return render(request, "natives.html", context)
