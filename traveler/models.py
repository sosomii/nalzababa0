from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_no = models.IntegerField() #태그 고유번호
    tagname = models.CharField(max_length=20) #태그명

    def __str__(self):
        return self.tagname

class Travel(models.Model):
    no = models.IntegerField(unique=True)#엑셀 파일과 매칭 번호
    local = models.CharField(max_length=20) #지역
    place = models.CharField(max_length=40) #장소명
    place_type = models.IntegerField() #타입
    address = models.TextField() #주소
    comment = models.TextField() #설명
    tags = models.ManyToManyField(Tag) #태그(복수 허용)

    def __str__(self):
        return self.place
