from django.shortcuts import redirect, render
from django import forms
from . import util

def lowercase_entries():
    entries = util.list_entries()
    for entry in range(len(entries)):
        entries[entry] = entries[entry].lower()
    return entries


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })
def greet(request,name):
    name = name.lower()
    if name in lowercase_entries():
        return render(request, "encyclopedia/greet.html", {
            "entry" : util.get_entry(name),
            "title" : name
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message" : f"page {name} does not exist"
        })

def search(request):
    if request.method == "POST":
        searched_entry = request.POST.get('q').lower()
        
        if searched_entry in lowercase_entries():
            return render(request,"encyclopedia/greet.html",{
                "entry" : util.get_entry(searched_entry),
                "title" : searched_entry
            })
        entries = []
        for entry in lowercase_entries():
            if searched_entry in entry:
                entries.append(entry)
        if entries:
            return render(request, "encyclopedia/index.html", {
                "entries": entries,
            })
        return render(request, "encyclopedia/index.html")
