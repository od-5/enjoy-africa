from django.forms import ModelForm, HiddenInput
from .models import ThemeComment

__author__ = 'alexy'


class ThemeCommentForm(ModelForm):
    class Meta:
        model = ThemeComment
        # fields = ('user', 'travel_review', 'text')
        widgets = {
            'user': HiddenInput(),
            'theme': HiddenInput(),
        }
