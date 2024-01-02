
# from django.contrib import admin
# from django.urls import include, path, re_path
# from django.conf.urls.static import static 
# from .views import manifest, offline, service_worker
# from . import settings


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("accounts/", include("django.contrib.auth.urls")),
#     path('profiles/', include('profiles.urls')),  
#     path('fixtures/', include('fixtures.urls')),  
#     path('clubs/', include('club.urls')),  
#     path('', include('world.urls')),
#     path('', include('pwa.urls')),
#     re_path(r"^serviceworker\.js$", service_worker, name="serviceworker"),
#     re_path(r"^manifest\.json$", manifest, name="manifest"),
#     path("offline/", offline, name="offline"),
    
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import include, path
from . import settings
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('profiles/', include('profiles.urls')),  
    path('fixtures/', include('fixtures.urls')),  
    path('clubs/', include('club.urls')),    
    path('', include("pwa.urls")),
    path('', include('world.urls')),
] 
