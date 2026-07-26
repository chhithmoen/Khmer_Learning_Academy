from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    thumbnail = models.ImageField(
        upload_to="courses/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )

    title = models.CharField(max_length=200)

    content = models.TextField(
        blank=True
    )

    video_url = models.URLField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title