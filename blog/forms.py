from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'n_pies', 'n_slices')
        # In this approach, each field is added explicitly.
        # Instead, there is a way to have all fields added automatically.  But it's insecure.
        # Or can add all fields automatically except ones that are specifically excluded.
