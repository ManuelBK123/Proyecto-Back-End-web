from rest_framework import serializers  

#----------------MODELOS----------------
from Profile.models import ProfileModel 

class ProfileModelSerializer(serializers.ModelSerializer ):
    class Meta:
        model = ProfileModel
        fields = ('__all__')