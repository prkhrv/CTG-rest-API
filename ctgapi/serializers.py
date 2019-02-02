from rest_framework import serializers
from .models import getintouch

class GetintouchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = getintouch
        fields = ('url','id','first_name','last_name','company','phone','email','website','comments')
