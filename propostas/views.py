from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Proposta
from .serializers import PropostaSerializer


class PropostaViewSet(ViewSet):
    permission_classes = (AllowAny, )

    @action(detail=False, methods=['GET'], url_path="propostas")
    def get_propostas(self, request):
        try:
            propostas = Proposta.objects.all()
            serializer = PropostaSerializer(propostas, many=True)
            return Response(
                data={"data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                data={"detail": str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['GET'], url_path="proposta_detail")
    def get_proposta_detail(self, request):
        try:
            propostas = Proposta.objects.get(id=request.data.get("id", None))
            serializer = PropostaSerializer(propostas)
            return Response(
                data={"data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                data={"detail": str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['POST'], url_path='nova_proposta')
    def post_nova_proposta(self, request):
        try:
            proposta = PropostaSerializer(data=request.data)
            proposta.is_valid()
            proposta.save()
            return Response(
                data={"proposta": proposta.data},
                status=status.HTTP_201_CREATED
            )
        except Exception as error:
            return Response(
                data={"detail": error},
                status=status.HTTP_400_BAD_REQUEST
            )
