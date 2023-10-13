from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT, STATIC_ROOT, STATIC_URL

urlpatterns = [path('admin/', admin.site.urls),
               path('', include('catalog.urls')),
               path('', include('account.urls')),
               path('', include('blog.urls')),
               path('', include('cart.urls'))
               ] \
              + static(MEDIA_URL, document_root=MEDIA_ROOT) \
              + static(STATIC_URL, document_root=STATIC_ROOT)
