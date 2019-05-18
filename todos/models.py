from datetime import date
from django.db import models
from helpers.helper import get_ndays_later

IMPORTANCE_SIZE = 7
IMPORTANCE_DEFAULT = 4


class TodoList(models.Model):
    title = models.CharField("할 일", max_length=30)
    content = models.TextField("설명")
    importance = models.CharField(
        "중요도",
        max_length=1,
        choices=tuple((str(n+1), n+1) for n in range(IMPORTANCE_SIZE)),
        default=str(IMPORTANCE_DEFAULT),
    )
    created_date = models.DateField("생성 날짜", auto_now_add=True)
    expired_date = models.DateField("기한", default=get_ndays_later)
    is_solved = models.BooleanField("완료 여부", default=False)


    class Meta:
        ordering = ['created_date']

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.title[:10] + ': '+ self.content[:10]

    @property
    def is_expired(self):
        return self.expired_date < date.today()

