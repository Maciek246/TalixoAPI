from rest_framework.routers import DefaultRouter

from cars import views as cars_views

router = DefaultRouter()
router.register('cars', cars_views.CarViewSet, 'cars')
