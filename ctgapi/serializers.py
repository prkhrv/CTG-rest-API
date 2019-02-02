from rest_framework import serializers
from .models import getintouch

class GetintouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = getintouch
        fields = ('id','first_name','last_name','company','phone','email','website','comments')
