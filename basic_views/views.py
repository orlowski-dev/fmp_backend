from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from oauth2_provider.models import AccessToken


@login_required()
def home_view(request):
    tokens = None
    if request.user.is_superuser:
        tokens = AccessToken.objects.all()
    else:
        tokens = AccessToken.objects.all().filter(user=request.user)
    return render(request, "basic_views/home-page.html", {"tokens": tokens})
