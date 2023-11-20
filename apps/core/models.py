from django.db import models

# -------------------- Ubicacion --------------------


class Pais(models.Model):
    codigo = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo}, {self.nombre}"


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}, {self.pais}"


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20, primary_key=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre}, {self.provincia}"


class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.calle} {self.numero}"


# -------------------- Otros ----------------------


class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    capacidad = models.IntegerField()

    def __str__(self):
        return f"Tipo de Habitacion {self.nombre}"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"Servicio {self.nombre}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    servicios = models.ManyToManyField(Servicio)
    estrellas = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return f"Categoria {self.nombre}"


# -------------------- Personas ---------------------


class Persona(models.Model):
    DNI = 0
    PASAPORTE = 1
    LIBRETA = 2
    TIPOS_DOCUMENTO = ((DNI, "DNI"), (PASAPORTE, "PASAPORTE"), (LIBRETA, "LIBRETA"))
    tipo_documento = models.PositiveSmallIntegerField(choices=TIPOS_DOCUMENTO)
    documento = models.CharField(max_length=13, primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.EmailField(max_length=254)
    telefono = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.capitalize()
        super().save(*args, **kwargs)

    def tipo_documento_display(self):
        return self.get_tipo_documento_display()


class Vendedor(Persona):
    pass


class Encargado(Persona):
    asignado = models.BooleanField(default=False)


class Cliente(Persona):
    puntos = models.PositiveIntegerField(default=0)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, null=True)
