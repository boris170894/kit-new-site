from django.shortcuts import render
from .models import CollegeContactModel


def contacts(request):
    contacts = CollegeContactModel.objects.filter(public=True).last()

    return render(request, 'contacts/contacts.html', {
        "contacts": contacts
    })