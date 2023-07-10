from django.db import models
from django.db.models import TextChoices

from utils.base.base_model import AbstractBaseModel


class Task(AbstractBaseModel):
    name = models.CharField("نام", max_length=200)

    def __str__(self):
        return self.name


class TaskState(AbstractBaseModel):
    task = models.ForeignKey(Task, verbose_name="تسک", on_delete=models.CASCADE)

    class TaskStateChoices(TextChoices):
        IN_PROGRESS = "0", "در حال انجام"
        DONE = "1", "انجام شده"
        FINISHED = "2", "خاتمه یافته"

        @classmethod
        def get_value_by_label(cls, label):
            return next(filter(lambda member: member.label == label, cls)).value

    state = models.CharField("وضعیت", max_length=2, choices=TaskStateChoices.choices)
