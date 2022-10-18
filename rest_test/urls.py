from django.urls import include, path
from rest_framework import routers
from entidades import views as eviews
from bodegas import views as bviews
from solicitudes import views as sviews

router = routers.DefaultRouter()
router.register(r'entidades/users', eviews.UserViewSet)
router.register(r'entidades/groups', eviews.GroupViewSet)
router.register(r'entidades/customers', eviews.CustomerViewSet)
router.register(r'entidades/products', eviews.ProductViewSet)
router.register(r'bodegas/warehouses', bviews.WarehouseViewSet)
router.register(r'bodegas/racks', bviews.RackViewSet)
router.register(r'bodegas/levels', bviews.LevelViewSet)
router.register(r'bodegas/spaces', bviews.SpaceViewSet)
router.register(r'bodegas/sections', bviews.SectionViewSet)
router.register(r'bodegas/pallets', bviews.PalletViewSet)
router.register(r'bodegas/palletproducts', bviews.PalletProductViewSet)
router.register(r'bodegas/inventories', bviews.InventoryViewSet)
router.register(r'solicitudes/requests', sviews.RequestViewSet)
router.register(r'solicitudes/requestproducts', sviews.RequestProductViewSet)
router.register(r'solicitudes/inputs', sviews.InputViewSet)
router.register(r'solicitudes/inputpallets', sviews.InputPalletViewSet)
router.register(r'solicitudes/outputs', sviews.OutputViewSet)
router.register(r'solicitudes/outputpallets', sviews.OutputPalletViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
