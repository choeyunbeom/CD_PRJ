from django.urls import path
from crime import views

app_name = 'crime'
urlpatterns = [
    path('bulk/region/', views.region, name='region'),
    path("place/<str:category_name>/<str:year>/", views.place, name='place'),
    path("time/<str:category_name>/", views.time, name='time'),
    path("seoul/<str:category_name>/<str:year>/", views.seoul, name='seoul'),
    path("landing/", views.landing, name = "landing"),
    path("gu_post/", views.gu_post, name = "gu_post"),
    path("post_add/", views.post_add, name = "post_add"),
    path("post_edit/<int:pk>/", views.post_edit, name = "post_edit"),
    path("post_delete/<int:pk>/", views.post_delete, name = "post_delete"),
    path("post_detail/<int:pk>/", views.post_detail, name = "post_detail"),
]