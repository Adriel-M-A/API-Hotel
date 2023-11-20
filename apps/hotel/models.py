from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.core.models import Direccion, TipoHabitacion, Vendedor


class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    tipos_habitacion = models.ManyToManyField(
        TipoHabitacion, through="PrecioPorTipo", related_name="hoteles"
    )
    # Revisar
    habilitado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    numero = models.PositiveIntegerField()
    piso = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Habitacion {self.numero} ({self.tipo})"


class Paquete(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="paquetes")
    nombre = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    coeficiente_descuento = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    habitaciones = models.ManyToManyField(Habitacion, related_name="paquetes")
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
