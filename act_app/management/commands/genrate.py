from django.core.management.base import BaseCommand
from django.db.models.base import ObjectDoesNotExist
import sys, random, string, pytz
from random import randint
from ...models import activity, member

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Command(BaseCommand):
    help = 'Populating the random data though this genrate command'

    def add_arguments(self, parser):
        parser.add_argument('numberofdata', type=int)

    def handle(self, *args, **kwargs):
        arg = kwargs['numberofdata']
        if arg == None:
            sys.stdout.write('You must specify a number of data needs to feed\n')
            sys.exit(1)

        for i in range(arg):
            id = self.random_id()
            real_name = self.random_name()
            timezone = self.random_tz()
            start_time = self.random_time()

            end_time = self.random_time()
            b = member(id=id, real_name=real_name, timezone=timezone)
            a = activity(id=id, start_time=start_time, end_time=end_time)
            a.save()
            b.save()


    def random_id(self):
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return res

    def random_name(self):
        res = ''.join(random.choices(string.ascii_uppercase, k=10))
        return res

    def random_tz(self):
        value = randint(1, 593)
        bit = randint(0, 1)
        return TIMEZONES[value][bit]

    def random_time(self):
        hour = randint(0, 23)
        minute = randint(0, 59)
        sec = randint(0, 59)
        return str(hour) + ':' + str(minute) + ':' + str(sec)
