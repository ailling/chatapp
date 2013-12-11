from django.core.management.base import BaseCommand
from django_socketio import broadcast, broadcast_channel, NoSocket

from chat.models import ChatRoom

import requests

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        rooms = ChatRoom.objects.all()
        print 'found %d rooms' % rooms.count()

        message = 'test message'
        url = 'http://localhost:9000/chat/system_message/'
        # url = 'http://ec2-50-19-156-150.compute-1.amazonaws.com:9000/chat/system_message/'
        requests.post(url, data={'message': message})
#        data = {'action': 'system', 'message': message}
#        broadcast(data)
#
#        for room in rooms:
#            channel = 'room-' + room.name
#            broadcast_channel(data, channel=channel)
        print 'finished'
