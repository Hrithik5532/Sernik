
from django.utils.timezone import now
from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUserAdmin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField( blank=False)
# Create your models here.
#category
class IpModel(models.Model):
    ip = models.CharField(max_length=100)
    def __str__(self):
        return self.ip


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.cat_title
    def get_absolute_url(self):
        return reverse('add_post')
# Post class
class Post(models.Model):
    title = models.CharField(max_length=100)
    post_id = models.AutoField(primary_key=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    #discription=models.CharField(max_length=200,blank=False,null=True)
    writer_name=models.CharField(max_length=50)
    content = RichTextField()
    post_date= models.DateField()
    tags = TaggableManager(blank=True)
    like_post = models.ManyToManyField(IpModel, related_name="post_like", blank=True)
    post_now= models.BooleanField(default=False)
    def image_tag(self):

        return format_html('<img src="/media/{}" style="width:40px;height:40px;"'.format(self.thumbnail))

    def like_count(self):
        return self.like_post.count()
    class Meta:
        ordering = ['-post_date',]

    def get_absolute_url(self):
        return reverse("blog",  kwargs={'pk': self.post_id})
    @property
    def get_comments(self):
        return self.comment_content.all()


class Contact(models.Model):
       # new = models.AutoField(primary_key=True, default='')
    fname= models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10,null=False, blank=False)


    message= models.CharField(max_length=100, null=True)
    def __str__(self) :
        return self.fname

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True,default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
    post = models.ForeignKey(Post, related_name='comment_content', on_delete=models.CASCADE)
   # parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username + str(self.sno)
class ReplayComment(models.Model):
    rno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parrent = models.ForeignKey(BlogComment,on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
            return self.user.username + str(self.rno)

class SubcribeUsers(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
