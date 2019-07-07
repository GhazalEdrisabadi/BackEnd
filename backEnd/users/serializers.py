from rest_framework import serializers
from users.models import Design


class UploadDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = 'title'