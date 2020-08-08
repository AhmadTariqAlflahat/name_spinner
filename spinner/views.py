from django.shortcuts import render
from .instagram_scraping import post_info, comments_fetching
from django.conf import settings
import urllib.request
from django.http import HttpResponse
import os
from celery.result import AsyncResult
import simplejson as json
import json


def index(request):
    context = {}
    if request.GET.get('q'):
        short_code = request.GET['q']
        comments = comments_fetching(request, short_code)
        post = post_info(short_code)
        commented_user, comments_list = [], {}
        for comment in comments:
            commented_user.append(comment['node']['owner']['username'])
            comments_list.update({comment['node']['owner']['username']: comment['node']['text']})

        file_name = post['username'] + '.jpg'
        urllib.request.urlretrieve(
            post['profile_pic_url'],
            os.path.join(settings.STATICFILES_DIRS[0], 'download', file_name)
        )
        context.update({
            'username': set(commented_user),
            'comments': comments_list,
            'count': len(commented_user),
            'total_count': len(set(commented_user)),
            'duplication': len(commented_user) - len(set(commented_user)),
            'post_info': post,
        })
    else:
        context.update({'not_search': True})
    return render(request, 'spinner/index.html', context)
