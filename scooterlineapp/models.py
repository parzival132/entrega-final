# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Modelo(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'modelo'
    def __str__ (self):
        return self.descripcion


class Usuarios(models.Model):
    username = models.CharField(max_length=45, verbose_name="Nombre")
    last_name = models.CharField(max_length=45, verbose_name="Apellido")
    email = models.CharField(max_length=45, verbose_name="Correo")
    modelo = models.ForeignKey(Modelo, models.DO_NOTHING, verbose_name="Modelo de Scooter")
    zona = models.ForeignKey('Zona', models.DO_NOTHING, verbose_name="Zona de Desplazamiento")
    activo = models.BooleanField(default=True, verbose_name="Scooter activo")

    class Meta:
        managed = False
        db_table = 'usuarios'
        unique_together = (('id', 'modelo', 'zona'),)


class Zona(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'zona'
    def __str__ (self):
        return self.descripcion
