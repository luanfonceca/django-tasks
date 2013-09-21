from django.db import models
from django.utils.translation import ugettext as _


class Task(models.Model):
    name = models.CharField(
        max_length=80,
        null=False,
        verbose_name=_("Name")
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name=_("Status")
    )

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def change_state(self):
        """
        >>> task = Task.objects.create(name="Test Task name")
        >>> task.change_state()
        >>> assert(task.is_done, True)
        >>> task.delete()
        """
        self.is_done = not self.is_done
        self.save()
