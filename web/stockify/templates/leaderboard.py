from django.views import View
from django.shortcuts import render


class Leaderboard(View):
    title = 'Leaderboard'
    template = 'ui/react_base.html'
    component = 'pages/leaderboard.js'

    def get(self, request):
        # gets passed to react via window.props
        props = {
            'users': [
                {'username': 'alice'},
                {'username': 'bob'},
            ]
        }

        context = {
            'title': self.title,
            'component': self.component,
            'props': props,
        }

        render(request, self.template, context)
