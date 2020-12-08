from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


from . import views

app_name = "polls"
urlpatterns = [
    path('login/', views.login, name='login'),  
	path('logout/', views.logout, name='logout'), 
    path('', views.IndexView.as_view(), name='index'),
    path('votes', views.VotesView.as_view(), name='votes'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('create/question', views.QuestionCreate.as_view(), name="question_create"),
    path('create/question/<int:pk>', views.create_question_finish, name="question_create_finish"),
]