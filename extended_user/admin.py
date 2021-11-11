from django.contrib import admin
from django.forms import ModelForm, TextInput, IntegerField

from .models import User


class UserAdminForm(ModelForm):
    """
    show normal input field instead of integer input for the discord id field
    """
    example_int_value = IntegerField(widget=TextInput, required=False)
    model = User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
