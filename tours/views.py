from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

from tours import data


def index(request):
    title = data.title
    subtitle = data.subtitle
    description = data.description
    return render(request, 'index.html', context={
        'title': title,
        'subtitle': subtitle,
        'description': description,
    })


def departure(request, departure):
    departure = data.departures.get(departure)
    if departure is None:
        raise Http404
    return render(request, 'departure.html', context={'departure': departure})


def tour(request, tour_id):
    tour = data.tours.get(tour_id)
    if tour is None:
        raise Http404
    return render(request, 'tour.html', context={'tour': tour})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
