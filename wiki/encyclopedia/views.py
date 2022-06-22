from django.shortcuts import redirect, render
from django import forms
from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title of Page")
    

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
    if name.lower() in lowercase_entries():
        return render(request, "encyclopedia/greet.html", {
            "entry" : util.get_entry(name),
            "title" : name
        })

    else:
        return render(request, "encyclopedia/greet.html", {
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

def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if title.lower() in lowercase_entries():
                return render(request,"encyclopedia/index.html", {
                    "message": "this title already exists"
                })

            content = request.POST.get("page_content")
            util.save_entry(title, content)

            return render(request, "encyclopedia/greet.html", {
                "entry" : util.get_entry(title),
                "title" : title
                
            })

    return render(request, "encyclopedia/new_page.html", {
        "form": NewPageForm(),
        "new_page" : True
        
    })

def edit_page(request):
    title = request.POST['title']
    content = request.POST['content']
    print(title)    
    return render(request, "encyclopedia/new_page.html", {
            "content" : content,
            "title" : title      
        })
def save_changes(request):
    title = request.POST['title']
    content = request.POST.get('page_content')
    util.save_entry(title, content)
    return render(request, "encyclopedia/greet.html", {
        "entry" : util.get_entry(title),
        
    })