from django.test import TestCase
from ..models import Articles

class ArticlesModelTest(TestCase):

    def test_string_representation(self):   
        articleTitle = Articles(title="My test of the title")
        self.assertEqual(str(articleTitle), articleTitle.title)

