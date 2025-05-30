from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="indie"),
    path("<int:ques_id>/", views.ques_page, name="ques"),
    path("post-html/<int:num>/", views.post_html, name="htmltest")
]