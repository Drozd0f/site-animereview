from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
import pdb

from .forms import AddPostForm, RegisterUserForm, LoginUserForm
from .models import *
from .utils import *

# Create your views here.


class ReviewsHome(DataMixin, ListView):
    model = Posts
    template_name = 'reviews/index.html'
    context_object_name = 'posts'

    def post(self, *args, **kwargs):
        print('Что-то происходит))')

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Posts.objects.filter(title__icontains=search_query)
        else:
            return Posts.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title="Главная страница")
        context.update(c_def)
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


@csrf_exempt
def temp(request):
    print(request.POST)
    print(request.body)
    return HttpResponse('{"message": "Что-то происходит))"}')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'reviews/addreviews.html'
    success_url = reverse_lazy('index')
    login_url = "/admin/"
    # reverse_lazy('login')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # or
        # context.update({
        #     'title': 'Добавить статью',
        #     'menu': menu
        # })
        c_def = self.get_user_contex(title="Добавить статью")
        context.update(c_def)
        return context


class UserUpdateProfile(DataMixin, UpdateView):
    model = User
    template_name = 'reviews/profile.html'
    fields = ['avatar']
    success_url = '/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # if 'form' not in kwargs:  # ??? это делается по умолчанию
        #     kwargs['form'] = self.get_form()
        c_def = self.get_user_contex(title="Обновить профиль")
        context.update(c_def)
        return context

    def form_valid(self, form):
        # pdb.set_trace()
        return super().form_valid(form)


class ShowPost(DataMixin, DetailView):
    model = Posts
    template_name = 'reviews/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title=context['post'])
        context.update(c_def)
        return context


class PostGenre(DataMixin, ListView):
    model = Posts
    template_name = 'reviews/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.filter(genre__id=self.kwargs['genre_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title='Категория - ' + Genre.objects.get(id=self.kwargs.get('genre_id')).name,
                                     genre_selected=context['posts'][0].genre)
        context.update(c_def)
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'reviews/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title="Регистрация")
        context.update(c_def)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'reviews/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title="Авторизация")
        context.update(c_def)
        return context

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')