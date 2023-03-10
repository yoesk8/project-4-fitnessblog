from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('donation/', views.donation, name='donation'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error'),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('products/', include('products.urls')),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('', article_views.article_list, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
