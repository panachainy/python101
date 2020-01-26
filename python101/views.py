from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response as response


@api_view(['GET'])
@permission_classes([AllowAny])
def health(request):
    if request.method == 'GET':
        return response(status=status.HTTP_200_OK)
