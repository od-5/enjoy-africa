from django.forms import ModelForm, HiddenInput
from .models import GroupsComment

__author__ = 'alexy'


class GroupsCommentForm(ModelForm):
    class Meta:
        model = GroupsComment
        # fields = ('user', 'travel_review', 'text')
        widgets = {
            'user': HiddenInput(),
            'groups': HiddenInput(),
        }
