from django.urls import path


from package_app.views import First

urlpatterns = [
    path("first/", First.as_view(), name="first"),
]
