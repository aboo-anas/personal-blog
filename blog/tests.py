from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


class Test_Create_Post(TestCase):
    

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='JavaScript')
        test_user = User.objects.create_user(username='Muhammad2', password='Mu08ha09?')
        test_post = Post.objects.create(category_id=1, title='Post Title', excerpt = 'Post Excerpt', content='Post Content', author_id=1, status="published")


    def test_blog_content(self):
        post = Post.objects.get(post_id=1)
        cat =  Category.objects.get(category_id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'Muhammad2')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(excerpt, 'Post Excerpt')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Post Title')
        self.assertEqual(str(cat), 'JavaScript')

