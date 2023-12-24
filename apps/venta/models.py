from django.db import models

# from apps.hotel.models import Habitacion, Paquete
from apps.core.models import Cliente


# Habitacion, Paquete y todo lo relacionado con estos dos
# estan comentados por que se genera un bucle de importacion
# el modelo de hotel importa el de venta y este mismo importa el de hotel
# ver como solucionar


class Alquiler(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pasajeros = models.IntegerField()
    # habitaciones = models.ManyToManyField(
    # Habitacion, related_name="alquileres", blank=True
    # )
    # paquetes = models.ManyToManyField(Paquete, blank=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.importe


class Factura(models.Model):
    fecha = models.DateField()
    numero = models.IntegerField()
    tipo_factura = models.CharField(max_length=1)
    importe_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.numero} con total de: {self.importe_total}"


class DetalleFactura(models.Model):
    descripcion = models.CharField(max_length=80)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    alquiler = models.ForeignKey(Alquiler, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)


class Liquidacion(models.Model):
    numero = models.IntegerField()
    fecha_emision = models.DateField()
    fecha_pago = models.DateField(null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    detalle_factura = models.ForeignKey(
        DetalleFactura, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"Liquidacion {self.numero} con fecha {self.fecha_emision}"


class Pago(models.Model):
    CONTADO = 0
    PUNTOS = 1
    TARJETA = 2
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    TIPOS_PAGO = ((CONTADO, "CONTADO"), (PUNTOS, "PUNTOS"), (TARJETA, "TARJETA"))
    tipo_pago = models.PositiveSmallIntegerField(choices=TIPOS_PAGO)

    def __str__(self):
        return f"Pago {self.importe} abonado con {self.tipo_pago}"
