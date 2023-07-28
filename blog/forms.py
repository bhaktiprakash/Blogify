from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import category,blog
class blogForm(ModelForm):
    class Meta:
        model = blog
        fields = ['category','title','description','image']
        widgets = {
            'description': SummernoteWidget(),
        }
