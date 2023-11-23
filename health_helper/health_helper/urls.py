from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diabetes/', include('diabetes.urls')),
    path('heart/', include('heart.urls')),
    path('', include('start_app.urls')),
]

