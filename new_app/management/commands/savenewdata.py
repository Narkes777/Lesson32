from django.core.management.base import BaseCommand
from new_app.models import Author, Post, Category
from django.db.models import Q


class Command(BaseCommand):

    def handle(self, *args, **options):

        author_1 = Author.objects.create(name='Author_1', bio="Bio of author 1", email='author1@email.com')
        author_2 = Author(name="Author_2", bio="bio of author 2")
        author_2.email = 'author2@email.com'
        author_2.save()
        author_3 = Author.objects.create(name='Author_3', bio="Bio of author 3", email='author3@mail.com')

        category_1 = Category.objects.create(name='Category_1', description='Desc 1')
        category_2 = Category.objects.create(name='Category_2', description='Desc 2')
        category_3 = Category.objects.create(name='Category_3', description='Desc 3')

        post_1 = Post.objects.create(title='post_title_1', content='content of post 1',
                                     views=11, author_id=author_1)
        post_1.categories.add(category_1, category_2)
        post_2 = Post.objects.create(title='post_title_2', content='content of post 2',
                                     views=6, author_id=author_2)
        post_2.categories.add(category_3, category_2)
        post_3 = Post(title='post_title_3', content='content of post 3', views=1,
                      status='d', author_id=author_3)
        post_3.save()
        post_3.categories.add(category_1)

# python manage.py savenewdata
# python manage.py migrate <название приложения> zero