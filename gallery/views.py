from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Art as ArtModel
from .models import Exbihition as ExbihitionModel
from user.models import UserInfo as UserInfoModel


class ArtListView(ListView):
    model = ArtModel
    ordering = '-pk'
    template_name = 'gallery/arts.html'


class ExbihitionListView(ListView):
    model = ExbihitionModel
    ordering = 'end'
    template_name = 'gallery/exbihitions.html'


class ArtistListView(ListView):
    model = UserInfoModel
    queryset = UserInfoModel.objects.filter(is_artist=True)
    ordering = '-pk'
    template_name = 'gallery/artists.html'


class SearchResultsView(View):
    def get(self, request):
        option = self.request.GET.get("s") # 검색 조건
        query = self.request.GET.get("q") # 검색어

        if option == '1':
            results = ArtModel.objects.filter(
                title__icontains=query
            )

        elif option == '2':
            results = UserInfoModel.objects.filter(
                name__icontains=query
            )

        elif option == '3':
            results = ExbihitionModel.objects.filter(
                title__icontains=query
            )

        return render(results, 'gallery/search-result.html')


class ArtCreateView(CreateView):
    model = ArtModel
    fields = ['title', 'price', 'size']
