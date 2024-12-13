# Create yfrom django.db import models
# from django.contrib import admin
# from django.utils.translation import gettext_lazy as _
#
# # Clase Zoologico
# class Zoologico(models.Model):
#     nombre = models.CharField(max_length=100)
#     horario = models.CharField(max_length=50)
#     telefono = models.CharField(max_length=15)
#     capacidad_maxima = models.IntegerField()
#     direccion = models.TextField()
#
#     def abrir(self):
#         pass
#
#     def cerrar(self):
#         pass
#
#     def asignar_cuidador(self):
#         pass
#
#     def registrar_animal(self):
#         pass
#
#     def __str__(self):
#         return self.nombre
#
# # Clase Jaula
# class Jaula(models.Model):
#     capacidad = models.IntegerField()
#     ubicacion = models.CharField(max_length=100)
#     zoologico = models.ForeignKey(Zoologico, on_delete=models.CASCADE, related_name="jaulas")
#
#     def asignar_animal(self, animal):
#         pass
#
#     def limpiar_jaula(self):
#         pass
#
#     def verificar_capacidad(self):
#         return True
#
#     def __str__(self):
#         return f"Jaula en {self.ubicacion} con capacidad {self.capacidad}"
#
# # Clase Animal
# class Animal(models.Model):
#     nombre = models.CharField(max_length=100)
#     nombre_cientifico = models.CharField(max_length=100)
#     edad = models.IntegerField()
#     estado_salud = models.CharField(max_length=50)
#     jaula = models.ForeignKey(Jaula, on_delete=models.CASCADE, related_name="animales")
#
#     def __str__(self):
#         return self.nombre
#
# # Clases específicas para tipos de animales
# class Carnivoro(Animal):
#     def come_carne(self):
#         pass
#
# class Omnivoro(Animal):
#     def come_variado(self):
#         pass
#
# class Herbivoro(Animal):
#     def comer_planta(self):
#         pass
#
# class Insectivoro(Animal):
#     def come_insecto(self):
#         pass
#
# # Clase Persona
# class Persona(models.Model):
#     nombre = models.CharField(max_length=100)
#     cedula = models.CharField(max_length=20)
#     fecha_nacimiento = models.DateField()
#     telefono = models.CharField(max_length=15)
#
#     def __str__(self):
#         return self.nombre
#
# # Clase Cuidador
# class Cuidador(Persona):
#     def alimentar(self, animal):
#         pass
#
#     def limpiar_jaula(self, jaula):
#         pass
#
#     def agregar_animal(self, animal):
#         pass
#
#     def consultar_historial_salud(self):
#         pass
#
# # Clase Veterinario
# class Veterinario(Persona):
#     especialidad = models.CharField(max_length=100)
#
#     def realizar_chequeo(self):
#         pass
#
#     def prescribir_tratamiento(self):
#         pass
#
#     def consultar_historial_salud(self):
#         pass
#
# # Clase HistorialSalud
# class HistorialSalud(models.Model):
#     fecha = models.DateField()
#     diagnostico = models.TextField()
#     tratamiento = models.TextField()
#     observacion = models.TextField()
#     animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="historiales_salud")
#
#     def registrar_diagnostico(self):
#         pass
#
#     def registrar_tratamiento(self):
#         pass
#
#     def __str__(self):
#         return f"Historial de {self.animal.nombre} - {self.fecha}"
#
# # Clase Boleteria
# class Boleteria(models.Model):
#     entradas_disponibles = models.IntegerField()
#
#     def vender_entrada(self):
#         pass
#
# # Clase Cliente
# class Cliente(models.Model):
#     entradas_adquiridas = models.IntegerField()
#     boleteria = models.ForeignKey(Boleteria, on_delete=models.CASCADE, related_name="clientes")
#
# # Configuración de admin
# class JaulaInline(admin.TabularInline):
#     model = Jaula
#     extra = 1
#
# class HistorialSaludInline(admin.TabularInline):
#     model = HistorialSalud
#     extra = 1
#
# @admin.register(Zoologico)
# class ZoologicoAdmin(admin.ModelAdmin):
#     list_display = ("nombre", "horario", "telefono", "capacidad_maxima")
#     search_fields = ("nombre", "direccion")
#     inlines = [JaulaInline]
#
# @admin.register(Animal)
# class AnimalAdmin(admin.ModelAdmin):
#     list_display = ("nombre", "nombre_cientifico", "edad", "estado_salud", "jaula")
#     list_filter = ("estado_salud", "jaula")
#     search_fields = ("nombre", "nombre_cientifico")
#     inlines = [HistorialSaludInline]
#
# @admin.register(Cuidador)
# class CuidadorAdmin(admin.ModelAdmin):
#     list_display = ("nombre", "cedula", "telefono")
#     search_fields = ("nombre", "cedula")
#
# @admin.register(Boleteria)
# class BoleteriaAdmin(admin.ModelAdmin):
#     list_display = ("entradas_disponibles",)
#
# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
#     list_display = ("entradas_adquiridas", "boleteria")
#     search_fields = ("boleteria__entradas_disponibles",)our models here.
