from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.renderers import TemplateHTMLRenderer

from gallery.models import Art as ArtModel
from gallery.models import Exbihition as ExbihitionModel
from user.models import Artist as ArtistModel
from user.serializers import ArtistSerializer
from gallery.serializers import ArtSerializer, ExbihitionSerializer
from user.views import stateCheck


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "tool/dashboard.html"

    def get(self, request):
        user_id = request.user.id
        state = stateCheck(user_id)
        return Response({"state":state}, status=status.HTTP_200_OK)


class StatisticsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "tool/statistics.html"

    def get(self, request):
        user_id = request.user.id
        state = stateCheck(user_id)
        return Response({"state":state}, status=status.HTTP_200_OK)


class RegistrationView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "tool/registration.html"

    def get(self, request):
        user_id = request.user.id
        state = stateCheck(user_id)
        return Response({"state":state}, status=status.HTTP_200_OK)