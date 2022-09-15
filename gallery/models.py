from django.db import models
from user.models import Artist


class Art(models.Model):

    class Meta:
        db_table = "arts"

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField("작품 제목", max_length=65)
    price = models.IntegerField("작품 가격")
    size = models.IntegerField("작품 호수")


class Exbihition(models.Model):

    class Meta:
        db_table = "exbihitions"

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField("전시 이름", max_length=65)
    start = models.DateField("전시 시작일")
    end = models.DateField("전시 종료일")
    arts = models.ManyToManyField(Art)