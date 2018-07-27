import django
import os
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TalixoAPI.settings")
django.setup()
from cars.models import Producer, CarType

producers = set()
types = set()

with open('cars.csv', 'r+', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for i in reader:
        try:
            producers.add(i[0])
            types.add(i[2])
        except:
            pass

Producer.objects.bulk_create([Producer(name) for name in producers])
CarType.objects.bulk_create([CarType(name) for name in types])
