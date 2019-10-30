from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from users.models import User
from users.forms import CreateUserForm


class CreateUserView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('users:list')
    template_name = 'users/user_form.html'


class UserListView(ListView):
    model = User
    paginate_by = 4
    template_name = 'users/user_list.html'
