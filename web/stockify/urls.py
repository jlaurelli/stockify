from django.conf.urls import url
from django.contrib import admin

from stockify.apps.market_analyzer.views import HomeView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),
]
