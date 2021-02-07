from django.test import TestCase
from article.models import Person, Department, Article
import json
# Create your tests here.

class ArticleTest(TestCase):
    def setUp(self):
        Department.objects.create(name="评论部")
        Department.objects.create(name="专题部")

    def get_response(self, url, data):
        res = self.client.post('/api/' + url, data=data, content_type='application/json')
        return res.status_code, json.loads(res.content)['data']

    def test_add_user(self):
        code, content = self.get_response('add_person', {
            'identity': 'admin',
            'name': '尹昊萱',
            'id_number': '2018011276',
            'department': '评论部',
        })
        self.assertEqual(code, 201)
        self.assertEqual(content, 'Add person successfully.')
        response = self.get_response('add_person', {
            'identity': 'admin',
            'name': '陈洪淼',
            'id_number': '2018012933',
            'department': '评论部',
        })
        self.assertEqual(code, 201)
        self.assertEqual(content, 'Add person successfully.')
        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(Department.objects.filter(name='评论部')[0].member.count(), 2)