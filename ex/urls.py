from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',views.UrlView.as_view()),
    path('<path:p>',views.CatchView.as_view()),

]
