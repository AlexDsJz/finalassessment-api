"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Process
from app.models import User

class ProcessSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        source='user', queryset=User.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Process
        fields = (
            'id',
            'created_at',
            'hash',
            'input',
            'k',
            'output',
            'user_id',  
        )