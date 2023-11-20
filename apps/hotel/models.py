from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.core.exceptions import ValidationError
from apps.core.models import Direccion, Vendedor, Encargado, TipoHabitacion, Categoria


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

    def vendedores(self):
        return [hv.vendedor for hv in self.hotelvendedor_set.all()]

    def descuentos_disponibles(self, habitaciones):
        return self.descuentos.filter(cantidad_habitaciones__lte=habitaciones).order_by(
            "-cantidad_habitaciones"
        )

    def temporadas_disponibles(self, inicio, fin, flexible=False):
        qs = self.temporadas.filter(fecha_inicio__lte=inicio, fecha_fin__gte=fin)
        if flexible:
            # TODO: Flexibilidad al seleccionar alquileres, si se superpone con
            # alquileres por unos dias pero no el total del rango inicio fin retornar True
            pass
        return qs

    def paquetes_disponibles(self, habitaciones, inicio, fin, flexible=False):
        qs = self.paquetes.filter(fecha_inicio__gte=inicio, fecha_fin__lte=fin)
        if flexible:
            # TODO: Flexibilidad al seleccionar alquileres, si se superpone con
            # alquileres por unos dias pero no el total del rango inicio fin retornar True
            pass
        return qs

    def verificar_disponibilidad(self, habitaciones, desde, hasta, flexible=False):
        if len(habitaciones) == 0:
            raise ValidationError("Debe ingresar habitaciones")
        if len(set([h.hotel.pk for h in habitaciones])) != 1:
            raise ValidationError("Las habitaciones deben ser del mismo hotel")
        descuentos = self.descuentos_disponibles(len(habitaciones))
        paquetes = self.paquetes_disponibles(
            habitaciones, desde, hasta, flexible=flexible
        )
        temporadas = self.temporadas_disponibles(desde, hasta, flexible=flexible)
        total = sum([h.precio for h in habitaciones])
        return {
            "precio": total,
            "temporadas": temporadas,
            "paquetes": paquetes,
            "descuentos": descuentos,
        }


class Habitacion(models.Model):
    numero = models.PositiveIntegerField()
    piso = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Habitacion {self.numero} ({self.tipo})"


class Paquete(models.Model):
    nombre = models.CharField(max_length=200)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="paquetes")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    coeficiente_descuento = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    habitaciones = models.ManyToManyField(
        Habitacion, through="PaqueteHabitacion", related_name="paquetes"
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


class PrecioPorTipo(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="tarifas")
    tipo_habitacion = models.ForeignKey(
        TipoHabitacion, on_delete=models.CASCADE, related_name="tarifas"
    )
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )

    def __str__(self):
        return f"Hotel: {self.hotel.nombre} - Tipo Habitacion: {self.tipohabitacion.nombre}"


class HotelVendedor(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hotel.nombre} - {self.vendedor.nombre}"


class PaqueteHabitacion(models.Model):
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.paquete.nombre} - Habitacion: {self.habitacion.numero}"
