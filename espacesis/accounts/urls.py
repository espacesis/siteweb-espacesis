from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url, include

from .views import Profile
from .views import Signup

urlpatterns = [
    url(r'^$' , Profile.as_view(), name="profile"),
    url(r'^login/$', LoginView.as_view(
        redirect_authenticated_user = True,
        template_name="accounts/login.html" ),
        name='login'
    ),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^signup/$', Signup.as_view(), name="signup"),
]
