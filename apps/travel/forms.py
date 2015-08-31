from django.forms import ModelForm, HiddenInput
from .models import TravelReviewComment

__author__ = 'alexy'


class TravelReviewCommentForm(ModelForm):
    class Meta:
        model = TravelReviewComment
        # fields = ('user', 'travel_review', 'text')
        widgets = {
            'user': HiddenInput(),
            'travel_review': HiddenInput(),
        }
