from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .models import Comment

# Create your views here.
def update_comment(request):
    refer = request.META.get('HTTP_REFERER', reverse('home'))

    if not request.user.is_authenticated:
        return render(request, "error.html", 
                     {'message':"用户未登录", 'redirect_to':refer})
    text = request.POST.get("text", "").strip()
    if text == "":
        return render(request, "error.html", 
                     {'message':"评论不能为空", 'redirect_to':refer})
    try:
        content_type = request.POST.get('content_type', "")
        object_id = int(request.POST.get('object_id', ""))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_object = model_class.objects.get(pk=object_id)
    except Exception:
        return render(request, "error.html", 
                     {'message':"评论对象不存在", 'redirect_to':refer})

    comment = Comment()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_object
    comment.save()
    return redirect(refer)