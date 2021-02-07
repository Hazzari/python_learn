from django.core import serializers
from django.shortcuts import render
from .models import Animal
from .tasks import save_animals


def index_view(request):
    animals = Animal.objects.select_related('kind').all()

    if request.method == "POST":

        save_animals.delay()  # НЕ ВЫЗЫВАЕТСЯ НА ПРЯМУЮ А через .delay(param)

    # animals = Animal.objects.prefetch_related('foods').all()

    return render(request, 'animals/index.html', {'animals': animals})
