# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from posts.models import Post
from datetime import datetime
from django.utils.timezone import utc
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'GET':
    
        list_post = Post.objects.all().order_by('-data_criacao')
        paginator = Paginator(list_post, 1)
        
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
            
        try:
            posts = paginator.page(page)
        except (EmptyPage, InvalidPage):
            posts = paginator.page(paginator.num_pages)        
            
        return render_to_response('posts/index.html', {"list_post": posts})  
         
    elif request.method == 'POST':

        list_post = Post.objects.get(corpo_icontains=request.POST['busca']).order_by('-data_criacao')
        paginator = Paginator(list_post, 1)
        
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
            
        try:
            posts = paginator.page(page)
        except (EmptyPage, InvalidPage):
            posts = paginator.page(paginator.num_pages)        
            
        return render_to_response('posts/index.html', {"list_post": posts})                       

