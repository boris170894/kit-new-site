from django.shortcuts import render, get_object_or_404
from .models import (
    GroupModel, CMCModel, PersonModel, PositionModel
)


def staff(request):
    cmcs = CMCModel.objects.all()

    return render(request, 'staff/staff.html', {
        "cmcs": cmcs
    })

# """ Show one """
def staff_one(request, slug):
    person = get_object_or_404(PersonModel, slug=slug)

    return render(request, 'staff/object.html', {
        'person': person
    })

    