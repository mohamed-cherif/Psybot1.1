from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'depressive', 'suicide', 'cyberbullying', 'total', 'time',
                  'graph_home', 'graph_dep', 'graph_sui', 'graph_cyb')
