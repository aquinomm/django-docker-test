from django.urls import path
from test.views import index
app_name = 'blog'

urlpatterns = [
    path('', index, name="index"),
]
