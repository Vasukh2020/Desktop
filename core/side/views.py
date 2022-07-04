from django.shortcuts import render
from django.http import JsonResponse

from django.http import JsonResponse
from django.shortcuts import render
#the thierd parties import
# Create your views here.


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
class TestView(APIView):
    permission_classes= (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        data={
            'name':'john','age': 44
        }
        return Response(data)

    def post (self, request,*args,**kwargs):
        serializer= PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        return Response(serializer.errors)   
        
    def get (self, request, *args, **kwargs):
        qs= Post.objects.all()
        serializer= PostSerializer(qs,many= True)
        return Response(serializer.data) 
        
'''
def test_view(request):
    data ={
        'name':'joh',
        'age': 23
    }
    return JsonResponse(data)
'''