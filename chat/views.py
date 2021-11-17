from django.shortcuts import render, redirect
from .models import Room, Message, NewUserForm
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@login_required()
def home(request):
    return render(request, 'home.html')


def room_(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    private = request.POST.get('private', False)

    if Room.objects.filter(name=room).exists():
        room_details = Room.objects.get(name=room)
        print(room_details.private + " ---------------")
        if room_details.private == "on":
            print("private -------------- and exists")
            if room_details.membersNo < 2:
                print("private , exists and not enough members ----------")
                room_details.membersNo += 1
                room_details.save()
                return redirect('/'+room+'/?username='+username)
            else:
                print("private exists enough members ----------")
                return redirect('/home')
        else:
            print("not private ----------- but exists")
            room_details = Room.objects.get(name=room)
            room_details.membersNo += 1
            room_details.save()
            return redirect('/' + room + '/?username=' + username)
    else:
        print("room does not exist ---------------",private)
        new_room = Room.objects.create(name=room)
        new_room.private = private
        new_room.membersNo += 1
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    profile_image = request.POST['profile_image']

    new_message = Message.objects.create(
        value=message, user=username, room=room_id, profile_image=profile_image
    )
    new_message.save()
    return HttpResponse("Hi, Message Sent Successfully!")


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'home.html')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrations successful!")
            return render(request, 'home.html')
        messages.error(request, "Unsuccessful registration.")
    form = NewUserForm()
    return render(request, 'register.html', context={"register_form": form})
