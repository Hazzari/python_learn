from django.urls import path
from .views import AnimalListView, AnimalDetailView, \
    AnimalCreateView, AnimalUpdateView, \
    status_view, ContactFormView, AnimalDeleteView, UserCreateView, \
    LoginUserView, LogoutUserView

app_name = 'animals'

urlpatterns = [
    path('', AnimalListView.as_view(), name='index'),
    path('create/', AnimalCreateView.as_view(), name='create'),
    path('animal/<int:pk>/', AnimalDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', AnimalUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AnimalDeleteView.as_view(), name='delete'),
    path('status/', status_view, name='status'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('registration/', UserCreateView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
