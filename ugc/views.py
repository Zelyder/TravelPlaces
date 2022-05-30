from django.shortcuts import render
from .forms import MyFeedbackForm
from .bot import sendMessage, start
from .models import Page, LikeDislike, Comment
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
import json
from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
  posts = Page.objects.all()
  return render(request, 'ugc/index.html', {'base_url':'https://travelplaces.andrieikoroshc1.repl.co/', 'posts': posts, 'title': 'Главная'})
  
def about(request):
  return render(request, 'ugc/about.html', {'title': 'О нас'})

def page(request, page_id):
  post = Page.objects.get(pk=page_id)
  return render(request, 'ugc/page.html', {'base_url':'https://travelplaces.andrieikoroshc1.repl.co/', 'post': post})

def events(request):
  return render(request, 'ugc/events.html', {'title': 'События'})

def login(request):
  return render(request, 'ugc/login.html', {'title': 'Регистрация'})

def directions_city(request):
  return render(request, 'ugc/directions_city.html')

def feedback(request):
  form = MyFeedbackForm()
  if request.method == "POST":
    form = MyFeedbackForm(request.POST)
    if form.is_valid():
      text = form.cleaned_data['text']
      start()

  else:
    pass
  return render(request, 'ugc/feedback.html', {'form': form, 'title': 'Обратная связь'})

@csrf_exempt
def comment(request,article_id):
 if request.method == 'POST':
  comments = request.POST['comment']
  if len(comments) < 5:
   result = U'Comments need to be greater than 5'
   return HttpResponse(json.dumps({'result': result}))
  else:
   result = 'successfully'
   Comment.objects.create(content= comments, article_id=article_id)
   return HttpResponse(json.dumps({'result': result}))

class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        page_id = self.kwargs.get("page_id")
        print(page_id)
        obj = get_object_or_404(Page, pk=page_id)
        
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, page_id=None, format=None):
        obj = get_object_or_404(Page, pk=page_id)
        
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)



class VotesView(View):
    model = None    # Модель данных - Статьи или Комментарии
    vote_type = None # Тип комментария Like/Dislike
 
    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id, user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True
 
        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )

