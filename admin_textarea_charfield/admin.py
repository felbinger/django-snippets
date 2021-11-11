from django.forms import ModelForm, Textarea, CharField


class CategoryAdminForm(ModelForm):
    """
    show textarea instead of text input for the description field
    """
    description = CharField(widget=Textarea, required=False)
    model = Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
