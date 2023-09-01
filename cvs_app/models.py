from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(null=True, blank=True)
    prefijo_cuil = models.IntegerField(null=True, blank=True)
    sufijo_cuil = models.IntegerField(null=True, blank=True)
    cod_area = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    domicilio = models.CharField(max_length=100, null=True, blank=True)
    localidad = models.CharField(max_length=60, null=True, blank=True)
    provincia = models.CharField(max_length=60, null=True, blank=True)
    nacionalidad = models.CharField(max_length=60, null=True, blank=True)
    genero = models.CharField(max_length=50, null=True, blank=True)
    day = models.IntegerField(null=True, blank=True,)
    month = models.IntegerField(null=True, blank=True,)
    year = models.IntegerField(null=True, blank=True,)
    foto = models.ImageField(default='default.jpg', upload_to='profile_images')
    estado_civil = models.CharField(max_length=40, null=True, blank=True)
    imprime_estado_civil = models.BooleanField(default=True)
    cantidad_hijos = models.CharField(max_length=10, null=True, blank=True, default="0")
    imprime_cantidad_hijos = models.BooleanField(default=True)
    editar_cv = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

class Academic_Level(models.Model):
    level = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.level
    

class Status(models.Model):
    status = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.status


class Academic_Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Academic_Level, on_delete=models.CASCADE)
    estado = models.ForeignKey(Status, on_delete=models.CASCADE)
    escuela = models.CharField(max_length=80, null=True, blank=True)
    titulo = models.CharField(max_length=150, null=True, blank=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    year_inicio = models.CharField(max_length=4, null=True, blank=True)
    year_fin = models.CharField(max_length=4, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'{self.escuela} - {self.nivel} - {self.estado}'
    

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100, null=True, blank=True)
    puesto = models.CharField(max_length=180, null=True, blank=True)
    month_inicio = models.CharField(max_length=2, null=True, blank=True)
    year_inicio = models.CharField(max_length=4, null=True, blank=True)
    month_fin = models.CharField(max_length=2, null=True, blank=True)
    year_fin = models.CharField(max_length=4, null=True, blank=True)
    referencia_nombre = models.CharField(max_length=50, null=True, blank=True)
    referencia_puesto = models.CharField(max_length=180, null=True, blank=True)
    referencia_cod_area = models.CharField(max_length=5, null=True, blank=True)
    referencia_telefono = models.CharField(max_length=30, null=True, blank=True)
    trabaja_actualmente = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.empresa} - {self.puesto}'
    

class About_Me(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    objetivo = models.CharField(max_length=500, null=True, blank=True)
    objetivo_imp = models.BooleanField(default=True)
    aptitudes = models.CharField(max_length=500, null=True, blank=True)
    aptitudes_imp = models.BooleanField(default=True)
    habilidades = models.CharField(max_length=500, null=True, blank=True)
    habilidades_imp = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
    

class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_curso = models.CharField(max_length=100, null=False, blank=False)
    institucion = models.CharField(max_length=100, null=False, blank=False)
    duracion = models.CharField(max_length=30, null=True, blank=True)
    year_egreso = models.CharField(max_length=4, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre_curso} - Usuario: {self.user}'