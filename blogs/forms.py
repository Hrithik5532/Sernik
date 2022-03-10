
from django import forms
from .models import Post, BlogComment,ReplayComment,SubcribeUsers
from ckeditor.fields import RichTextField
from taggit.forms import TagWidget

class DateInput(forms.DateInput):
    input_type = 'date'
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['post_id','thumbnail','writer_name','category','title','content','post_date','tags']

        widgets={
        'post_id': forms.TextInput(attrs={'class':'form-control','style':'border-style: outset;'}),
        'writer_name': forms.TextInput(attrs={'class':'form-control','style':'border-style: outset;'}),
        'title': forms.TextInput(attrs={'class':'form-control','style':'border-style: outset;'}),
        #'discription':forms.Textarea(attrs={'class':'form-control','style':'border-style: outset;'}),
        'content': RichTextField(),
        'tags': TagWidget(attrs={'class':'form-control','style':'border-style: outset;'}),
        'category': forms.Select(attrs={'class':'form-control','style':'border-style: outset;'}),
        'post_date':DateInput()

    }



class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubcribeUsers
        fields=['email']