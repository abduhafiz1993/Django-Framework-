from django.shortcuts import render, redirect
from django.http import Http404
from django import forms
from markdown2 import Markdown
from django.contrib import messages

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Title", "class": "mb-4"}
        ),
    )
    content = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "Content (markdown)",
                "id": "new_content",
            }
        ),
    )

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, entry):
    if entry not in util.list_entries():
        raise Http404
    content = util.get_entry(entry)
    return render(
        request,
        "encyclopedia/wiki.html",
        {"title": entry, "content": Markdown().convert(content)
        },
    )


def search(request):
    query = request.GET.get("q", "")
    if query is None or query == "":
        return render(
            request,
            "encyclopedia/search.html",
            {"found_entries": "", "query": query},
        )
    
    entries = util.list_entries()
    found_entries = [
        valid_entry
        for valid_entry in entries
        if query.lower() in valid_entry.lower()
    ]

    return render(
            request,
            "encyclopedia/search.html",
            {"found_entries": found_entries, "query": query},
        )

def new(request):
    if request.method == 'POST':

        form = NewEntryForm(request.POST)

        if form.is_valid():


            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
            
            if title.lower() in [entry.lower() for entry in util.list_entries()]:
                messages.add_message(
                    request,
                    messages.WARNING,
                    message=f'Entry "{title}" already exists',
                )
            else:
                util.save_entry(title=title, content=content)
                return redirect("wiki", title)
        else:
            messages.add_message(
            request, messages.WARNING, message="Invalid request form"
            )
    elif request.method == 'GET':

        return render(request, "encyclopedia/new.html", {
            "form": NewEntryForm()
        })
    

    return render(request, "encyclopedia/new.html",{
                "form": form
            })


def edit(request, entry):
    if request.method == "GET":
        title = entry
        content = util.get_entry(title)
        form = NewEntryForm({"title": title, "content": content})
        return render(
            request,
            "encyclopedia/edit.html",
            {"form": form, "title": title},
        )

    form = NewEntryForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")

        util.save_entry(title=title, content=content)
        return redirect("wiki", title)
            

