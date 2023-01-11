from rest_framework import status
from .models import Breed,Dog
from .serializers import BreedSerializers,DogSerializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import random

# Create your views here.
#def index(request):
    #return render(request, 'home.html')

class Breedviewset(viewsets.ModelViewSet):
    queryset=Breed.objects.all()
    serializer_class=BreedSerializers

class DogViewset(viewsets.ModelViewSet):
    queryset=Dog.objects.all()
    serializer_class=DogSerializers


class RandomDogByCategory(APIView):
    def get(self, request, breed):
        try:
            breed = Breed.objects.get(name = breed)
        except Breed.DoesNotExist:
            return Response("Please provide valid breed", status=status.HTTP_400_BAD_REQUEST)
        doogs = list(Dog.objects.filter(breedId = breed.id))
        doogsLength = len(doogs) - 1
        randomId = random.randint(0, doogsLength)
        serializeDoog = DogSerializers(doogs[randomId])
        return Response(serializeDoog.data, status=status.HTTP_200_OK)






