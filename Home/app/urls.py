from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('base/', base, name='base'),
                  path('', home, name='home'),
                  path('login/', login, name='login'),
                  path('registration/', registration, name='registration'),
                  path('logout/', logout, name='logout'),
                  path('create/', create, name='create'),
                  path('update/<int:id>', update, name='update'),
                  path('view/<int:id>', view_cv, name='view_cv'),
                  path('delete/<int:id>', delete, name='delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
