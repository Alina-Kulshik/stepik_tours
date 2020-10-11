from random import sample

from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render

from tours import data


def index(request):
    title = data.title
    subtitle = data.subtitle
    description = data.description
    departures = data.departures
    tours = {i: data.tours[i] for i in sample(range(1, 17), 6)}
    return render(request, 'index.html', context={
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'departures': departures,
        'tours': tours,
    })


def departure(request, departure):
    tours = {i: data.tours[i] for i in data.tours if data.tours[i]['departure'] == departure}
    price = [tours[i]['price'] for i in tours]
    min_price = min(price)
    max_price = max(price)
    nights = [tours[i]['nights'] for i in tours]
    min_nights = min(nights)
    max_nights = max(nights)
    departure = data.departures.get(departure)
    departures = data.departures
    if departure is None:
        raise Http404
    return render(request, 'departure.html', context={
        'departure': departure,
        'departures': departures,
        'tours': tours,
        'min_price': min_price,
        'max_price': max_price,
        'min_nights': min_nights,
        'max_nights': max_nights,
    })


def tour(request, tour_id):
    tour = data.tours.get(tour_id)
    departure = data.tours[tour_id]['departure']
    departure = data.departures[departure]
    departures = data.departures
    if tour is None:
        raise Http404
    return render(request, 'tour.html', context={
        'tour': tour,
        'departure': departure,
        'departures': departures,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')
