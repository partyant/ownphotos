from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models import User
from api.directory_watcher import scan_photos
from rest_framework.response import Response

class Command(BaseCommand):
    help = 'Scans directories of all users'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        user = User.objects.get(username='admin')
        self.stdout.write("%s Starting photo scan for user %s" % (time, user))
        res = scan_photos.delay(user)
        print("Job status: %s" % Response({'status': True, 'job_id': res.id}))

        


