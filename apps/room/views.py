from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from room.models import Room
from store.models import Store

def room(request, slug):
    if Room.objects.filter(slug=slug).exists():
        print('sala existe')
        room = get_object_or_404(Room, slug=slug)
    else:
        print('sala criada')
        client = request.user

        store = request.GET.get('store')
        store = get_object_or_404(Store, pk=store)

        slug = f'{store.user.username}-{client.username}'

        room = Room(
            slug=slug,
            client=client,
            store=store,
        )

        room.save()

    context = {
        'room': room,
    }

    return render(request, 'room/room.html', context)
