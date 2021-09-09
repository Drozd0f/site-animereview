from .models import Genre

menu = [{'title': "Главна страница", 'url_name': 'index'},
        {'title': "Добавить статью", 'url_name': 'add_post'},
        # {'title': "Профиль", 'url_name': 'profile_update'},
        ]


class DataMixin:  # read about context_processors
    paginate_by = 3

    def get_user_contex(self, **kwargs):
        context = kwargs
        genre = Genre.objects.all()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['genres'] = genre
        if 'genre_selected' not in context:
            context['genre_selected'] = 0
        return context
