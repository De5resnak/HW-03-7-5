from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['author', 'type', 'category', 'title', 'text']

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("text")
        name = cleaned_data.get("title")

        if name == description:
            raise ValidationError(
                "Содержание не должно быть идентично названию."
            )

        return cleaned_data