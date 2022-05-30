from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Sum
from django.conf import settings


class Profile(models.Model):
  external_id = models.PositiveIntegerField(
    verbose_name = 'ID Пользователя',
    unique=True,
  )
  name = models.TextField(
    verbose_name='Имя пользователя',
  )

  def __str__(self):
    return f'#{self.external_id} {self.name}'
  
  class Meta:
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'

class Message(models.Model):
  profile = models.ForeignKey(
    to='ugc.Profile',
    verbose_name='Профиль',
    on_delete=models.PROTECT,
  )
  text=models.TextField(
    verbose_name='Текст',
  )
  created_at = models.DateTimeField(
    verbose_name='Время получения',
    auto_now_add=True,
  )
  def __str__(self):
    return f'Сообщеие {self.pk} от {self.profile}'
  class Meta:
    verbose_name = 'Сообщение'
    verbose_name_plural = 'Cooбщения'




class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def articles(self):
        return self.get_queryset().filter(content_type__model='page').order_by('-page__time_create')
 
    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)
 
    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)
 
    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

class LikeDislike(models.Model):
  LIKE = 1
  DISLIKE = -1
  VOTES = (
      (DISLIKE, 'Не нравится'),
      (LIKE, 'Нравится')
  )
  
  vote = models.SmallIntegerField(verbose_name = ("Голос"), choices=VOTES)
  user = models.ForeignKey(Profile, verbose_name= ("Пользователь"), on_delete=models.CASCADE)

  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey()

  objects = LikeDislikeManager()


class Page(models.Model):
  title = models.CharField(max_length=255)
  short_description = models.TextField(blank = True)
  content = models.TextField()
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='page_likes')
  thumbnail_image = models.ImageField(upload_to="images/posts/thumbnail", blank=True)
  cover_image = models.ImageField(upload_to="images/posts/cover", blank=True)
  time_create = models.DateTimeField(auto_now_add=True)
  time_update = models.DateTimeField(auto_now=True)
  is_published = models.BooleanField(default=True)
  votes = GenericRelation(LikeDislike, related_query_name='articles')

  # def get_absolute_url(self):
  #     return reverse("page:detail", kwargs={"page_id": self.pk})

  # def get_like_url(self):
  #     return reverse("page:like", kwargs={"page_id": self.pk})

  # def get_api_like_url(self):
  #     return reverse("page:like-api", kwargs={"page_id": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Page,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
  
def __str__ (self):
  return self.title