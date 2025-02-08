from django import forms
from .models import Kanji

class KanjiForm(forms.ModelForm):
    class Meta:
        model = Kanji
        fields = ['character', 'english_translation', 'onyomi', 'kunyomi', 'stroke_count', 'jlpt_level', 'example_sentence']