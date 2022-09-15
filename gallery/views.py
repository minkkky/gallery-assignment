from django.shortcuts import redirect
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Art as ArtModel
from .models import Exbihition as ExbihitionModel
from user.models import Artist as ArtistModel
from .serializers import ArtSerializer, ExbihitionSerializer
from user.serializers import ArtistSerializer
from user.views import stateCheck


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "gallery/exbihitions.html"
    # template_name = "index.html"

    def get(self, request):
        user_id = request.user.id
        state = stateCheck(user_id)
        exbititions = ExbihitionModel.objects.all().order_by("-end")
        exbitition_serializer = ExbihitionSerializer(exbititions, many=True).data
        return Response({"state":state, "exbihition_list":exbitition_serializer}, status=status.HTTP_200_OK)


class ArtView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "gallery/arts.html"

    def get(self, request):
        user_id = request.user.id
        state = stateCheck(user_id)
        arts = ArtModel.objects.all().order_by("-pk")
        serialzer_data = ArtSerializer(arts, many=True).data
        return Response({"state":state, "art_list":serialzer_data}, status=status.HTTP_200_OK)


class ArtistListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "gallery/artists.html"

    def get(self, request):
        user_id = request.user.id
        state = stateCheck(user_id)
        artists = ArtistModel.objects.filter(is_artist=True).order_by("-pk")
        serialzer_data = ArtistSerializer(artists, many=True).data
        return Response({"state":state, "artist_list":serialzer_data}, status=status.HTTP_200_OK)


class ExbihitionView(APIView):

    def post(self, request):
        return Response(status=status.HTTP_200_OK)