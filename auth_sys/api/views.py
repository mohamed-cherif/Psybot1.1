from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import fasttext


words = []
model = fasttext.load_model(r"C:\Users\LENOVO\Desktop\Using AI to prevent mental illness\Psybot1.1\backend\auth_sys\api\depression.bin")


@api_view(['POST'])
@permission_classes([AllowAny])
def sendData(request):
    test = model.predict(str(request.data))
    return Response(test)
