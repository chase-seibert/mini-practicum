import string, random
from framework import require_post, reverse, send_email, HttpResponseRedirect
from myapp.models import User


@require_post
def create_user(request):
    if request.method == 'POST':
        username, password = request.POST.get('username'), request.POST.get('password')
        user = User.create(username, password)
        return HttpResponseRedirect(reverse('user', args=(user.id, )))


def view_reset_all(request, message):
    for user in list(User.all()):
        user.password = ''.join(random.choice(string.ascii) for _ in range(8))
        user.save()
        send_email(user.email, subject='Hello, {0}'.format(user.get_first_name()),
            body=message, content_type='text/html')
    return "OK"
