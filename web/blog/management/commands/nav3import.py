'''
mkdir -p old
mv media old/media_`date '+%FT%T'`
mv db old/db_`date '+%FT%T'`
mkdir -p media db
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py initadmin
# Add a blog index page
# python3 manage.py runserver
python3 manage.py nav3import ~/Desktop/baby-blog/
mv static/ old/static_`date '+%FT%T'`
mkdir static
python3 manage.py collectstatic --noinput
'''

from django.conf import settings
import subprocess
from django.core.management.base import BaseCommand
import datetime
import html

from blog.models import BlogIndexPage, BlogPage, BlogPageComment, Page
from home.models import HomePage

from io import BytesIO
import requests
from django.core.files.images import ImageFile
from wagtail.images import get_image_model
Image = get_image_model()

import os


from wagtail.core import blocks


# from wagtail.wagtailcore.models import Collection
# root_coll = Collection.get_first_root_node()
# root_coll.add_child(name='testcoll')

import json

from django.db import transaction

from pyquery import PyQuery as pq

def html_to_blocks(html, filename_to_value):
    body = []
    d = pq(html)
    for p in d('p'):
        if pq(p)('img'):
            body.append({'type': 'image', 'value': filename_to_value[pq(p)('img').attr('src').split('/')[-1]]})
        else:
            body.append({'type': 'paragraph', 'value': pq(p).html()})
    return body




class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('baby_blog', type=str)


    def handle(self, *args, **options):
        home = HomePage.objects.all()[0]
        baby_blog = options['baby_blog']
        with transaction.atomic():
            index = BlogIndexPage(title="Eddie's Blog", seo_title="Blog", intro="")
            home.add_child(instance=index)

            cmd = [
                'nav3-list',
                'datePublished'
            ] + [
                os.path.join('public', 'blog', path) for path in os.listdir(os.path.join(baby_blog, 'public', 'blog')) if os.path.isdir(os.path.join(baby_blog, 'public', 'blog', path))
            ]
            # print(baby_blog, cmd)
            p = subprocess.Popen(cmd, cwd=baby_blog, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (stdout, stderr) = p.communicate() 
            if p.wait() != 0:
                print(stderr)
                raise Exception('nav3-list failed')
            # print(stdout)
            data = json.loads(stdout)
            for post in data:
                title = post['data']['title']
                article = post['data']['article']
                date_published = datetime.datetime.fromisoformat(post['data']['datePublished'].split('+')[0])
                intro = html.unescape(post['data']['description'])
                comments = json.loads(post['data']['comments'])
                slug = post['page'].split('/')[1]
                print(slug, title, date_published, len(comments))

                filename_to_value = {}
                for filename in os.listdir(os.path.join(baby_blog,  'public', 'blog', slug, '_', 'img')):
                    if filename.lower().endswith('.jpg'):
                        full_path = os.path.join(baby_blog, 'public', 'blog',  slug, '_', 'img', filename)
                        image_field = ImageFile(open(full_path, 'rb'), name=filename)
                        image = Image(title=filename, file=image_field)
                        image.save()
                        print(filename, image.pk, image_field.size)
                        filename_to_value[filename] = image.pk

                body = html_to_blocks(article, filename_to_value)
                print(body)
                blog_page= BlogPage(
                    title=title,
                    slug=slug,
                    intro=intro,
                    date=date_published,
                    body=json.dumps(body),
                )
                index.add_child(instance=blog_page)
                for c in comments:
                    print(c)
                    comment = BlogPageComment.objects.create(
                        page=blog_page,
                        date=datetime.datetime.utcfromtimestamp(int(c['id'].split('-')[0])/1000), #datetime.datetime.now(),  # XXX
                        author=c['name'],
                        comment=c['comment']
                    )
                # later when a cms user updates the page manually 
                # there will be no first revision to compare against unless
                # you add a page revision also programmatically.
                
                blog_page.save_revision().publish() 
            index.save_revision().publish() 
            photos = HomePage(title='Photos')
            home.add_child(instance=photos)
            for filename in os.listdir(os.path.join(baby_blog,  'public', 'photos', '_', 'img')):
                if filename.lower().endswith('.jpg'):
                    full_path = os.path.join(baby_blog, 'public', 'photos', '_', 'img', filename)
                    image_field = ImageFile(open(full_path, 'rb'), name=filename)
                    image = Image(title=filename, file=image_field)
                    image.save()
                    print(filename, image.pk, image_field.size)
                    filename_to_value[filename] = image.pk
            home.save_revision().publish() 
            photos.save_revision().publish() 
