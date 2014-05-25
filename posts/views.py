# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
# from django.template import RequestContext
from posts.models import Post
from datetime import datetime
from django.utils.timezone import utc

def index(request):
  return render_to_response('posts/index.html',{
    'list_post': Post.objects.all().order_by('-data_criacao')
  })

