from django.shortcuts import render
from django.http import Http404
from django import forms

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
        {"title": entry, "content": content
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
    
    entry = util.list_entries()
    found_entries = []
    valid_entries = []
    for valid in entry:
        valid_entries.append(valid.lower())

    if query.lower() in valid_entries:
        found_entries.append(query)

    return render(
            request,
            "encyclopedia/search.html",
            {"found_entries": found_entries, "query": query},
        )