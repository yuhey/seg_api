from rest_framework import routers
from api.views.greeting_view import GreetingViewSet

router = routers.DefaultRouter()
router.register(r'greeting', GreetingViewSet)