from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.core.paginator import Paginator

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Artist as ArtistModel
from gallery.models import Art  as  ArtModel
from gallery.models import Exbihition as ExbihitionModel
from .serializers import UserSerializer, ArtistSerializer, ArtistPostSerializer
from gallery.serializers import ArtSerializer, ExbihitionSerializer
        

class SignUpView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/signup.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        pw1 = request.POST.get("password", "")
        pw2 = request.POST.get("password2", "")
        if pw1 == pw2:
            user_serializer = UserSerializer(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return redirect("artist:signin")
            print(user_serializer.errors)
            return Response({"error":"이미 존재하는 계정입니다."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error":"비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/signin.html"

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect("gallery:index")
        else:
            return Response(status=status.HTTP_200_OK)

    def post(self, request):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        me = authenticate(request, username=username, password=password)
        if me:
            login(request, me)
            return redirect("gallery:index")
        else:
            return Response({"error":"ID 혹은 비밀번호를 확인해주세요."}, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ArtistView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/regist/application.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        form_data = request.POST.copy()

        year = form_data.get("year")
        month = form_data.get("month")
        day = form_data.get("day")
        phone1 = form_data.get("phone1")
        phone2 = form_data.get("phone2")
        phone3 = form_data.get("phone3")

        birth = f"{year}-{month}-{day}"
        phone = f"{phone1}-{phone2}-{phone3}"
        user =  request.user.id

        form_data["birth"] = birth
        form_data["phone"] = phone
        form_data["user"] = user
        form_data["is_artist"] = None

        artist_serializer = ArtistPostSerializer(data=form_data)
        print(form_data)

        if artist_serializer.is_valid():
            artist_serializer.save()
            return redirect("gallery:index")

        return Response(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DashboardView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/dashboard.html"

    def get(self, request):
        user =  request.user.id
        user_data = ArtistModel.objects.get(user=user)
        art_data = ArtModel.objects.filter(artist=user)
        ex_data = ExbihitionModel.objects.filter(artist=user)
        user_serializer = ArtistSerializer(user_data)
        art_serializer = ArtSerializer(art_data, many=True)
        ex_serializer = ExbihitionSerializer(ex_data, many=True)

        data = {
            "artist": user_serializer.data,
            "art": art_serializer.data,
            "exbihition": ex_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)


class ArtPostView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/regist/art.html"

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        user =  request.user.id
        form_data = request.POST.copy()
        form_data["artist"] = user
        art_serializer = ArtSerializer(data=form_data)

        if art_serializer.is_valid():
            art_serializer.save()
            return redirect("artist:info")

        return Response(art_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExbihionPostView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user/regist/exbihition.html"

    def get(self, request):
        user =  request.user.id
        arts = ArtModel.objects.filter(artist=user)
        art_serialzer = ArtSerializer(arts, many=True)
        return Response({"arts":art_serialzer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        form_data = request.POST.copy()
        user =  request.user.id
        form_data["artist"] = user
        ex_serializer = ExbihitionSerializer(data=form_data)

        if ex_serializer.is_valid():
            ex_serializer.save()
            return redirect("artist:info")
        return Response(ex_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def stateCheck(user_id):
    artist_data = ArtistModel.objects.filter(user=user_id)
    if not artist_data:
        state = "미신청"
    else:
        artist_data = ArtistModel.objects.get(user=user_id)
        if artist_data.is_artist:
            state = "승인"
        elif artist_data.is_artist == None:
            state = "미처리"
        else:
            state = "반려"
        return state