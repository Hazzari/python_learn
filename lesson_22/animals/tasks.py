from celery import shared_task

from animals.models import Animal


@shared_task
def save_animals():
    animals = Animal.objects.all()
    with open('result.txt', 'a', encoding='utf-8') as f:
        for animal in animals:
            f.write(f'{animal}\n')
