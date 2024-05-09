from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva
import random
from datetime import datetime, timedelta
from django.utils import timezone

fake = Faker()

class Command(BaseCommand):
    help = 'Creates fake data for the application'

    def handle(self, *args, **options):
        self.create_fake_data()

    def create_fake_data(self):
        for _ in range(10):
            Automobil.objects.create(
                marca=fake.company(),
                model=fake.catch_phrase(),
                matricula=fake.bothify(text='??###', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            )

        users = User.objects.all()
        automobils = Automobil.objects.all()
        for _ in range(20):
                    data_inici_naive = fake.date_time_between(start_date='-1y', end_date='now')
                    data_fi_naive = fake.date_time_between(start_date='now', end_date='+1y')

                    data_inici_aware = timezone.make_aware(data_inici_naive, timezone.get_default_timezone())
                    data_fi_aware = timezone.make_aware(data_fi_naive, timezone.get_default_timezone())

                    Reserva.objects.create(
                        automobil=random.choice(automobils),
                        usuari=random.choice(users),
                        data_inici=data_inici_aware,
                        data_fi=data_fi_aware
                    )