from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Proposta
from .serializers import PropostaSerializer
from .proposta_utils import formata_cpf


class PropostaViewSet(ViewSet):
    permission_classes = (AllowAny, )

    # Solicita todas as propostas
    @action(detail=False, methods=['GET'], url_path="propostas")
    def get_propostas(self, request):
        try:
            propostas = Proposta.objects.all()
            serializer = PropostaSerializer(propostas, many=True)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                data={"detail": str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )

    # Solicita uma proposta
    @action(detail=False, methods=['GET'], url_path="propostas/detail")
    def get_proposta_detail(self, request):
        try:
            propostas = Proposta.objects.get(id=request.data.get("id", None))
            serializer = PropostaSerializer(propostas)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                data={"detail": str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )

    # Cria uma nova proposta
    @action(detail=False, methods=['POST'], url_path='propostas/nova')
    def post_nova_proposta(self, request):
        try:
            data = request.data
            data['cpf'] = formata_cpf(data.get('cpf', ''))
            proposta = PropostaSerializer(data=data)
            proposta.is_valid()
            proposta.save()
            return Response(
                data={"proposta": proposta.data},
                status=status.HTTP_201_CREATED
            )
        except Exception as error:
            return Response(
                data={"detail": str(error)},
                status=status.HTTP_400_BAD_REQUEST
            )
