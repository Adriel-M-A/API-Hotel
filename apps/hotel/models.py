from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.core.exceptions import ValidationError
from apps.core.models import Direccion, Vendedor, Encargado, TipoHabitacion, Categoria


class HotelManager(models.Manager):
    def verificar_disponibilidad(self, desde, hasta, localidad):
        qs = self.get_queryset()
        qs = qs.filter(direccion__ciudad=localidad)

        hoteles_disponibles = qs.exclude(
            habitaciones__alquileres__fecha_inicio__lte=hasta,
            habitaciones__alquileres__fecha_fin__gte=desde,
        )

        return hoteles_disponibles


class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    tipos_habitacion = models.ManyToManyField(
        TipoHabitacion, through="PrecioPorTipo", related_name="hoteles"
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    encargado = models.OneToOneField(Encargado, on_delete=models.SET_NULL, null=True)
    habilitado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def descuentos_disponibles(self, habitaciones):
        return self.descuentos.filter(cantidad_habitaciones__lte=habitaciones).order_by(
            "-cantidad_habitaciones"
        )

    def temporadas_disponibles(self, inicio, fin, flexible=False):
        temporadas = self.temporadas.filter(fecha_inicio__lt=inicio, fecha_fin__gt=fin)
        if flexible:
            # TODO: Flexibilidad al seleccionar alquileres, si se superpone con
            # alquileres por unos dias pero no el total del rango inicio fin retornar True
            pass
        return temporadas

    def paquetes_disponibles(self, inicio, fin, flexible=False):
        qs = self.paquetes.filter(fecha_inicio__gt=inicio, fecha_fin__lt=fin)
        if flexible:
            # TODO: Flexibilidad al seleccionar alquileres, si se superpone con
            # alquileres por unos dias pero no el total del rango inicio fin retornar True
            pass
        return qs

    def get_vendedores(self):
        vendedores = HotelVendedor.objects.filter(hotel=self).values_list(
            "vendedor__documento", flat=True
        )
        return Vendedor.objects.filter(documento__in=vendedores)

    def habitaciones_disponibles(self, desde, hasta):
        habitaciones = self.habitaciones.all()
        habitaciones_disponibles = [
            habitacion
            for habitacion in habitaciones
            if habitacion.habitacion_disponible(desde, hasta)
        ]
        return habitaciones_disponibles


class Habitacion(models.Model):
    numero = models.PositiveIntegerField()
    piso = models.PositiveIntegerField()
    hotel = models.ForeignKey(
        Hotel, related_name="habitaciones", on_delete=models.CASCADE
    )
    tipo = models.ForeignKey(
        TipoHabitacion, related_name="habitaciones", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Habitacion {self.numero} ({self.tipo})"

    @property
    def precio(self):
        # TODO: Que pasa si el hotel no tiene tarifa para el precio del tipo de habitacion
        qs = self.hotel.tarifas.filter(tipohabitacion=self.tipo_habitacion)
        if qs.exists():
            return qs.first().precio
        return Decimal("0.0")

    def habitacion_disponible(self, inicio, fin, flexible=False):
        disponible = not self.alquileres.filter(
            fecha_fin__lt=inicio, fecha_inicio__gt=fin
        ).exists()
        if flexible:
            # TODO: Flexibilidad al seleccionar alquileres, si se superpone con
            # alquileres por unos dias pero no el total del rango inicio fin retornar True
            pass
        return disponible


class Paquete(models.Model):
    nombre = models.CharField(max_length=200)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="paquetes")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    coeficiente_descuento = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    habitaciones = models.ManyToManyField(
        Habitacion, related_name="paquetes", through="PaqueteHabitacion"
    )
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Descuento(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="descuentos"
    )
    cantidad_habitaciones = models.IntegerField()
    porcentaje = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return f"Hotel {self.hotel.nombre} - Cant. Habitaciones {self.cantidad_habitaciones} - Porcentaje {self.porcentaje}"


class Temporada(models.Model):
    ALTA = 0
    BAJA = 1
    TIPOS_TEMPORADA = ((ALTA, "Alta"), (BAJA, "Baja"))
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name="temporadas"
    )
    tipo = models.PositiveSmallIntegerField(choices=TIPOS_TEMPORADA)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    porcentaje = models.DecimalField(
        max_digits=5, decimal_places=2
    )  # Si es menor a 1 es un descuento aplicable, sino corresponde a aumento

    def __str__(self):
        return f"Hotel {self.hotel} - Temporada {self.tipo} - Desde dia {self.fecha_inicio} hasta {self.fecha_fin}"


# Modelo intermedio para representar el precio por tipo de habitación en un hotel
class PrecioPorTipo(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="tarifas")
    tipo_habitacion = models.ForeignKey(
        TipoHabitacion, on_delete=models.CASCADE, related_name="tarifas"
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Hotel: {self.hotel.nombre} - Tipo Habitacion: {self.tipohabitacion.nombre}"


# Modelo intermedio para representar la relación entre un hotel y un vendedor
class HotelVendedor(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hotel.nombre} - {self.vendedor.nombre}"


# Modelo intermedio para representar la relación entre un paquete y una habitación
class PaqueteHabitacion(models.Model):
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.paquete.nombre} - Habitacion: {self.habitacion.numero}"
