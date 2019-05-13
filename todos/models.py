from datetime import date
from django.db import models


LONG_FUTURE = date(3000, 12, 31)

class TodoList(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    importance = models.CharField(
        max_length=1,
        choices=tuple((str(n), n) for n in range(1, 7+1))
    )
    created_date = models.DateField(auto_now_add=True)
    expired_date = models.DateField(default=LONG_FUTURE)
    is_solved = models.BooleanField(default=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.title[:10] + ': '+ self.content[:10]

    @property
    def is_expired(self):
        return self.expired_date < date.today()
