from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from gestion_tk.models import Ticket 

class ReportesTicketsView(APIView):
    def get(self, request):
        # Inicializar contadores
        estados = {
            'PENDIENTE': 0,
            'EN_PROGRESO': 0,
            'RESUELTO': 0
        }
        categorias = {
            'HARDWARE': 0,
            'SOFTWARE': 0,
            'PERIFERICO': 0,
        }
        
        # Obtener todos los tickets
        tickets = Ticket.objects.all() 
        
        # Contar los tickets por estado y categoría
        for ticket in tickets:
            estado = ticket.estado
            categoria = ticket.categoria
            
            if estado in estados:
                estados[estado] += 1
            
            if categoria in categorias:
                categorias[categoria] += 1
        
        # Crear la respuesta con los contadores
        resultado = {
            'estados': estados,
            'categorias': categorias
        }
        
        return Response(resultado, status=status.HTTP_200_OK)
