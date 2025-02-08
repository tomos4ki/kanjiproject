from django.db import models

# Create your models here.
from django.db import models

class Kanji(models.Model):
    character = models.CharField(max_length=1)
    english_translation = models.CharField(max_length=100)
    onyomi = models.CharField(max_length=100)
    kunyomi = models.CharField(max_length=100)
    stroke_count = models.IntegerField()
    jlpt_level = models.IntegerField()
    example_sentence = models.TextField()

    def __str__(self):
        return self.character