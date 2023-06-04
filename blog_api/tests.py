from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from django.contrib.auth.models import User



class PostTests(APITestCase):
    

    def test_view_post(self):
        """
        Ensure we can view all objects
        
        """
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_post(self):
        """
        Ensure we can create a Post object or view object
        """
        self.test_category = Category.objects.create(name="MyTestCategory")
        self.testuser1 = User.objects.create_superuser(username="ModelTest", password="ModelTest123")
        self.client.login(username=self.testuser1.username, password="ModelTest123")


        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse("blog_api:listcreate")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        root = reverse(("blog_api:detailcreate"), kwargs={"pk": 1})
        response = self.client.get(root, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_udpate(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='JavaScript')
        self.testuser_1 = User.objects.create_user(username="admin", password="admin123")
        self.testuser_2 = User.objects.create_user(username="admin2", password="admin2123")
        client.login(username=self.testuser_1.username, password="admin123")
        test_post = Post.objects.create(category_id=1, author_id=1, title="Test Post", slug="Test-slug", excerpt="Test Excerpt", content="Test Content", status="published")
        url = reverse(("blog_api:detailcreate"), kwargs={"pk": 1})
        response = client.put(url, {
            "title": "New",
            "author": 2,
            "excerpt": "New",
            "content": "New",
            "status": "published",

        }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

