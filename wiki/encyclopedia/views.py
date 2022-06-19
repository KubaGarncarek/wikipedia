from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def greet(request,name):
    name = name.lower()
    entries = util.list_entries()
    for entry in range(len(entries)):
        entries[entry] = entries[entry].lower()
    if name in entries:
        return render(request, "encyclopedia/greet.html", {
            "entry" : util.get_entry(name),
            "title" : name
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message" : f"page {name} does not exist"
        })

