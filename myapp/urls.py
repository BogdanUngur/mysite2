from django.urls import path
from . import views
from mysite import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='myapp'
urlpatterns = [
    path('',views.IndexView.as_view(),name='main'),
    path('create/',views.MovieCreate.as_view(),name='create'),
    path('update/<int:pk>/',views.MovieUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.MovieDelete.as_view(),name='delete'),
    path('details/<int:pk>/',views.MovieDetails.as_view(),name='details')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
