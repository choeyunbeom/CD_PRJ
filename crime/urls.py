from django.urls import path
from crime import views

app_name = 'crime'
urlpatterns = [
    path('crime/bulk/region/', views.region, name='region'),
    path("crime/place/<str:category_name>/<str:year>/", views.place, name='place'),
    path("crime/time/<str:category_name>/", views.time, name='time'),
    path("crime/seoul/<str:category_name>/<str:year>/", views.seoul, name='seoul'),
    path("", views.landing, name = "landing"),
    path("crime/gu_post/", views.gu_post, name = "gu_post"),
    path("crime/post_add/", views.post_add, name = "post_add"),
    path("crime/post_edit/<int:pk>/", views.post_edit, name = "post_edit"),
    path("crime/post_delete/<int:pk>/", views.post_delete, name = "post_delete"),
    path("crime/post_detail/<int:pk>/", views.post_detail, name = "post_detail"),
]