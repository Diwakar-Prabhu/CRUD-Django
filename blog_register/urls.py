from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.blog_form,name='blog_insert'),
    path('<int:id>',views.blog_form,name='blog_update'),
    path('delete/<int:id>/',views.blog_delete,name='blog_delete'),
    path('list/',views.blog_list,name='blog_list')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)