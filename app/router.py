from dogapi.views import DogViewset,Breedviewset
from rest_framework import routers

router =routers.DefaultRouter()
router.register('dog',DogViewset)
router.register('breed',Breedviewset)