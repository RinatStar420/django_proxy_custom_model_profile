from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic import FormView
from .models import Person

# класс для отображения главной страницы
class Index(TemplateView):
    template_name = 'index.html'

# класс для создания пользователя
class CreatUser(FormView):
    form_class = UserCreationForm
    template_name = 'singup.html'
    success_url = '/'

    # валидация для создания нового пользователя
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(CreatUser, self).form_valid(form)

# клас для отображения всех пользователей
class ALLUsers(TemplateView):
    template_name = 'all_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['users'] = Person.people.get_staff_user()
        return context