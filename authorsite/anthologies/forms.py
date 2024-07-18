from django import forms
from .models import Collection, Cover, Story

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('title', 'authors')

class CoverForm(forms.ModelForm):
    class Meta:
        model = Cover
        exclude = ('collection',)
        fields = ('image',)

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        exclude = ('collection',)
        fields = ('title', 'track')