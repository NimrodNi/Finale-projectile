from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('', views.index, name="home"),
    path('about-us', views.about, name="about"),
    path('create', views.create, name="create"),
    path('delete/<int:tasks_id>/', views.delete_task, name='delete_task')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
