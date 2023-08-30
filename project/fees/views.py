from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User


# Create your views here.
def profile_page(request):
    return render(request, 'feesone.html')

def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if not request.user.following.filter(id=user_id).exists():
        Follow.objects.create(follower=request.user, following=user_to_follow)
    return redirect('profile_page')


def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    request.user.following.filter(id=user_id).delete()
    return redirect('profile_page')
