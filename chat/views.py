from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name  
})


# check if is loggedin user
# def room(request, room_name):
#     return render(request, 'chat/room.html', {
#         'room_name': room_name,
#         'username': request.user.username
#     })




def unauthorized(request ) :
    pass