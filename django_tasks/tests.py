from django.test import TestCase

from .models import Task


class TaskTest(TestCase):
    def test_assert_name(self):
        task = Task.objects.create(name="Test Task name")
        self.assertEqual(task.name, "Test Task name")
        self.assertEqual(task.is_done, False)

    def test_assert_edition(self):
        task = Task.objects.create(name="Test Task name")
        task.name = "New test task name"
        task.save()
        self.assertEqual(task.name, "New test task name")

    def test_assert_change_status(self):
        task = Task.objects.create(name="Test Task name")
        task.change_state()
        self.assertEqual(task.is_done, True)

    def test_assert_deletion(self):
        task = Task.objects.create(name="Test Task name")
        self.assertQuerysetEqual(
            qs=Task.objects.all(),
            values=['<Task: Task object>']
        )
        task.delete()
        self.assertQuerysetEqual(
            qs=Task.objects.all(),
            values=[]
        )
