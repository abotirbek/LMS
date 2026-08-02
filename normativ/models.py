from django.conf import settings
from django.db import models

from accounts.models import StudentProfile, TimeStampedModel
from courses.models import Lesson


class NormativQuestion(TimeStampedModel):
    # null=True, blank=True ni ish bitganidan keyin o'chirib kerak
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='normativ_question', null=True, blank=True)
    text = models.TextField()
    max_score = models.PositiveSmallIntegerField(default=10)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']
        # COnstrains ni to'g'irlash kerak
        # constraints = [
        #     models.UniqueConstraint(fields=['normativ_question', 'order'], name='unique_question_order'),
        # ]

    def __str__(self):
        return f'{self.lesson} — savol {self.order}'


class NormativAnswer(TimeStampedModel):
    question = models.ForeignKey(NormativQuestion, on_delete=models.CASCADE, related_name='answers')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='normativ_answers')
    answer_text = models.TextField()
    score = models.PositiveSmallIntegerField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    checked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='checked_answers',
    )
    checked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'student'], name='unique_answer'),
        ]

    def __str__(self):
        return f'{self.student} — {self.question}'

    @property
    def is_checked(self):
        return self.score is not None
