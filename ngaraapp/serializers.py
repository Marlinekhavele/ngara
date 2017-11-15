from .models import Index
from .models import About
from .models import Service
from .models import Contact
from rest_framework import serializers
class IndexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Index
        fields = ('service','timestamp','picture')
        
        
class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = ('service','timestamp')
        

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('service','timestamp')
        
        
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('service','timestamp')