from django.contrib import admin
from django.urls import path, include

from blog import views as blog_view
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static
import account.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_view.blog, name='blog'),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('account/', include('account.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)