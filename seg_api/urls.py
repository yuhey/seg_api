from django.contrib import admin
from django.conf.urls import url, include
from api.urls import router as api_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_router.urls)),
]
