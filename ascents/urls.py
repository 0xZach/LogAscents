from django.urls import path

from . import views

# urls inside the app
urlpatterns = [
    # when using a class, need to call the as_view method as we don't use a simple view function
    path("", views.Index, name="index"), 
    path("ascent_details/<int:pk>/", views.AscentDetailsView.as_view(), name="ascent-details"),
    path("<int:pk>/delete/",views.AscentDeleteView.as_view(), name="ascent-delete"),
    path("list/", views.ascent_list, name="list"),
    path("upload/", views.upload_ascent, name="upload-ascent"),
]
