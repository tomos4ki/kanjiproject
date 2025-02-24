from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.db import models

class Kanji(models.Model):
    character = models.CharField(max_length=100000)
    english_translation = models.CharField(max_length=100)
    onyomi = models.CharField(max_length=100)
    kunyomi = models.CharField(max_length=100)
    stroke_count = models.IntegerField()
    jlpt_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    example_sentence = models.TextField()

    def __str__(self):
        return self.character