from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import UserModel

def ForbiddenUsernamesValidator(value):
    forbidden_usernames = ['admin', 'settings', 'news', 'about', 'help',
                           'signin', 'signup', 'signout', 'terms', 'privacy',
                           'cookie', 'new', 'login', 'logout', 'administrator',
                           'join', 'account', 'username', 'root', 'blog',
                           'user', 'users', 'billing', 'subscribe', 'reviews',
                           'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                           'home', 'job', 'jobs', 'contribute', 'newsletter',
                           'shop', 'profile', 'register', 'auth',
                           'authentication', 'campaign', 'config', 'delete',
                           'remove', 'forum', 'forums', 'download',
                           'downloads', 'contact', 'blogs', 'feed', 'feeds',
                           'faq', 'intranet', 'log', 'registration', 'search',
                           'explore', 'rss', 'support', 'status', 'static',
                           'media', 'setting', 'css', 'js', 'follow',
                           'activity', 'questions', 'articles', 'network',
                           'speechacademia', 'jeanluc kabulu','sql' ]

    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')

def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User With This Email Already exist')

def UniqueUsernameIgnoreCaseValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')


class UserSignUpForm(ModelForm):
    """
    User Signup Form Modified
    """

    username = forms.CharField(widget=forms.TextInput(),
    max_length=30,
    required=True,
    help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters')
    password = forms.CharField(
        widget= forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label = 'Confirm your password',
        required = True
    )
    email = forms.CharField(
        widget = forms.EmailInput(),
        required = True,
        max_length= 75
    )

    class Meta:
        model = UserModel
        exclude = ['last_login', 'date_joined']
        fields = ['username','first_name','last_name', 'email', 'password', 'confirm_password', ]

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsernamesValidator)
        self.fields['username'].validators.append(
            UniqueUsernameIgnoreCaseValidator
            )
        self.fields['email'].validators.append(UniqueEmailValidator)

    def clean(self):
        super(UserSignUpForm,self).clean() #call the really class
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(
                ['Password don\'t match']

            )

        return self.cleaned_data
