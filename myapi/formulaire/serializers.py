
from rest_framework import serializers
from .models import Client, FormulaireClient

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['code_client', 'statut']


class FormulaireClientSerializer(serializers.ModelSerializer):
    code_client = serializers.ReadOnlyField(source='client.code_client')

    class Meta:
        model = FormulaireClient
        fields = [
            'code_client', 'q1', 'q2', 'q3', 
            'q1', 'q2', 'q3', 'q4', 'q5', 
            'q6', 'q7', 'q8', 'q9', 'q10', 
            'q11', 'q12', 'q13', 'q14', 'q15', 
            'q16', 'q17', 'q19', 'q19', 'date_soumission', 
                  ]
        # extra_kwargs = {
        #     'client': {'write_only': True}
        # }
