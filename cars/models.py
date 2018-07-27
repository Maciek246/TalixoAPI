from django.db import models

CATEGORY = [
    ('E', 'Economical'),
    ('B', 'Business'),
    ('F', 'First Class'),
]

ENGINE_TYPE = [
    ('CB', 'Combustion'),
    ('HB', 'Hybrid'),
    ('EL', 'Electric'),
]


class Producer(models.Model):
    name = models.CharField(max_length=80, primary_key=True)

    class Meta:
        db_table = 'Producers'
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class CarType(models.Model):
    name = models.CharField(max_length=80, primary_key=True)

    class Meta:
        db_table = 'Car_Types'

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    registration = models.CharField(max_length=9, unique=True)
    max_passengers = models.PositiveIntegerField()
    year_of_production = models.PositiveSmallIntegerField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    model = models.CharField(max_length=60)
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    category = models.CharField(max_length=1, choices=CATEGORY)
    engine = models.CharField(max_length=2, choices=ENGINE_TYPE, default=ENGINE_TYPE[0])

    class Meta:
        db_table = 'Cars'

    def __str__(self):
        return f"{self.producer.name} {self.model}({self.year_of_production}) [{self.registration}]"
