from django.urls import path
from .views import index, ad_list, AdCreateView

# Not /app

app_name = 'ads'

urlpatterns = [
    path('<uuid:pk>/detail/', index, name='ad_detail'), # /1 /2 /101241
    path('ad/create/', AdCreateView.as_view(), name='create_ad'),
    path('', ad_list),
    path('<str:name>/<int:pk>/', index, name='index') # http://127.0.0.1:8000/app/random_str/,
]

