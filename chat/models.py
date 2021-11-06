from django.db import models
from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=1000)


def get_profile_image_filepath(self, filename):
    return 'media/images/' + str(self.pk) + '/20200807_131537_resized_resized.png'


def get_default_profile_image():
    return "media/images/20200807_131537_resized_resized.png"


class Message(models.Model):
    value = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath,
                                      null=True, blank=True,
                                      default=get_default_profile_image)
    room = models.CharField(max_length=10000000)
    user = models.CharField(max_length=10000000)

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('media/images/' + str(self.pk) + "/"):]


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
