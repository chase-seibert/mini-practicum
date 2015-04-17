from framework import require_post, reverse, HttpResponseRedirect
from myapp.models import User


@require_post
def create_user(request):
    if request.method == 'POST':
        username, password = request.POST.get('username'), request.POST.get('password')
        user = User.create(username, password)
        return HttpResponseRedirect(reverse('user', args=(user.id, )))
