from django.db import models
from app.helper import get_ndays_later


class TodoList(models.Model):
    title = models.CharField("할 일", max_length=30)
    content = models.TextField("설명")
    importance = models.CharField(
        "중요도",
        max_length=1,
        choices=tuple((str(n), n) for n in range(1, 7+1)),
        default='4',
    )
    created_date = models.DateField("생성 날짜", auto_now_add=True)
    expired_date = models.DateField("기한", default=get_ndays_later)
    is_solved = models.BooleanField("완료 여부", default=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.title[:10] + ': '+ self.content[:10]

    @property
    def is_expired(self):
        return self.expired_date < date.today()

    class Meta:
        ordering = ['created_date']
