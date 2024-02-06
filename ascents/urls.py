from django.urls import path

from . import views

# urls inside the app
urlpatterns = [
    # when using a class, need to call the as_view method as we don't use a simple view function
    path("", views.IndexView.as_view(), name="index"), 
    path("ascent_details/<int:pk>/", views.AscentDetailsView.as_view(), name="ascent-details"),
    path("upload/", views.upload_ascent, name="upload-ascent"),
]
