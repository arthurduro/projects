from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductoSerializer
from .models import Categoria, Producto
from rest_framework.parsers import FileUploadParser
import os
from django.conf import settings

class ProductoList(generics.ListCreateAPIView):
  queryset = Producto.objects.order_by('-id').all()
  serializer_class = ProductoSerializer
  


  def post(self, request, format=None):

    print 'sssssssss'
    serializer = ProductoSerializer(data=request.data)
    
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    print serializer.errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class CompaniDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = compani.objects.all()
#   serializer_class = CompaniSerializer



class ProductoDetail(APIView):
  """
  Retrieve, update or delete a snippet instance.
  """
  def get_object(self, pk):
    try:
      return Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = ProductoSerializer(snippet)
    return Response(serializer.data)

  # def put(self, request, pk, format=None):
  #   snippet = self.get_object(pk)
  #   print request.data
  #   serializer = CompaniEditSerializer(snippet, data=request.data)
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data)
  #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    snippet = self.get_object(pk)
    print snippet.foto
    os.unlink("%s/%s"%(settings.MEDIA_ROOT,snippet.foto))
  
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
