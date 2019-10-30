from django.forms import fields
from django.contrib.auth.forms import UsernameField, UserCreationForm

# from ZimadTest.utils import save_compressed
from users.models import User
from users.tasks import save_compressed


class CreateUserForm(UserCreationForm):
    # image_origin = fields.ImageField(label=_('Your'))

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            user.save()
            save_compressed.delay(user.pk)
            # save_compressed()
        return user

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'parent_name',
            'password1', 'password2', 'image_origin'
        )
        field_classes = {'username': UsernameField}
