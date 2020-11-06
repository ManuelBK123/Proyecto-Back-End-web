from django.urls import path, re_path
from Profile import views 
urlpatterns = [
    re_path('^profileModel_url',views.ProfileModelView.as_view())
]