from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from .models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= Categoria
		fields= ('nombre')

class ProductoSerializer(serializers.ModelSerializer):
	
	foto = serializers.ImageField(
        max_length=None, use_url=True,
    )


	class Meta:
		model= Producto
		fields= ('nombre', 'descripcion', 'categoria', 'marca', 'modelo', 'foto', 'nro_serie', 'stock', 'costo', 'precio_unitario')

# class CompaniEditSerializer(serializers.ModelSerializer):
# 	telefono = serializers.IntegerField(
# 		error_messages={
# 			"invalid": "Se requiere un numero entero valido.",
# 		},
# 	)
	

	

# 	class Meta:
# 		model= compani
# 		fields= ('id','name', 'email', 'telefono')

