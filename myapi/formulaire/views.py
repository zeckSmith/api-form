from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Client, FormulaireClient
from .serializers import ClientSerializer, FormulaireClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class FormulaireClientViewSet(viewsets.ModelViewSet):
    queryset = FormulaireClient.objects.all()
    serializer_class = FormulaireClientSerializer

    def create(self, request, *args, **kwargs):
        client_code = request.data.get("code_client")
        
        try:
            client = Client.objects.get(code_client=client_code)
        except Client.DoesNotExist:
            return Response({"error": "Client non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        if FormulaireClient.objects.filter(client=client).exists():
            return Response({"error": "Formulaire déjà soumis pour ce client"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(client=client)
        client.statut = True
        client.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
