from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, default=0)
    def update_rating(self):
        postRat = self.post_set.aggregate(postRating = Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')
        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')
        self.ratingAuthor = pRat * 3 + cRat
        self.save()



class Category(models.Model):
    name = models.CharField(max_length= 255, unique=True)

    def __str__(self):
        return self.name.title()

class Post(models.Model):
    ARTICLE = 'AT'
    NEWS = 'NS'
    TYPE_OF_POST = [
        (ARTICLE, 'статья'),
        (NEWS, 'новость'),
    ]
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE_OF_POST, default=ARTICLE)
    article_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255, default='title')
    text = models.TextField(default='text')
    rating = models.IntegerField(default=0)
    def like(self):
        self.rating+=1
        self.save()
    def dislike(self):
        self.rating-=1
        self.save()
    def preview(self):
        if str(self.text).len() > 123:
            prev = str(self.text)[0:123]+'...'
            return prev
        else:
            prev = str(self.text)
        return prev

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, default='None')
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=False, default=0)
    def like(self):
        self.rating+=1
        self.save()
    def dislike(self):
        self.rating-=1
        self.save()

class Subscriptions(models.Model):
    user = models.ForeignKey(
        to = User,
        on_delete = models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to = 'Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )