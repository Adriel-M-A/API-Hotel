from rest_framework.routers import DefaultRouter
from api.core.views.ubicacion import (
    PaisViewSet,
    ProvinciaViewSet,
    CiudadViewSet,
    DireccionViewSet,
)
from api.core.views.persona import (
    VendedorViewSet,
    EncargadoViewSet,
    ClienteViewSet,
)
from api.core.views.otro import (
    TipoHabitacionViewSet,
    CategoriaViewSet,
    ServicioViewSet,
)

router = DefaultRouter()

# Ubicacion
router.register(r"paises", PaisViewSet, basename="pais")
router.register(r"provincias", ProvinciaViewSet, basename="provincia")
router.register(r"ciudades", CiudadViewSet, basename="ciudad")
router.register(r"direcciones", DireccionViewSet, basename="direccion")

# Persona
router.register(r"vendedores", VendedorViewSet, basename="vendedores")
router.register(r"encargados", EncargadoViewSet, basename="encargados")
router.register(r"clientes", ClienteViewSet, basename="clientes")

# Otros
router.register(
    r"tiposhabitaciones", TipoHabitacionViewSet, basename="tiposhabitaciones"
)
router.register(r"servicios", ServicioViewSet, basename="servicio")
router.register(r"categorias", CategoriaViewSet, basename="categorias")


urlpatterns = router.urls
