from django.test import TestCase
from article.models import Person, Department, Article
import json


# Create your tests here.

class ArticleTest(TestCase):
    def setUp(self):
        self.plb = Department(name='评论部')
        self.plb.save()
        self.ztb = Department(name='专题部')
        self.ztb.save()

    def post_response(self, url, data):
        res = self.client.post('/api/' + url, data=data, content_type='application/json')
        return res.status_code, json.loads(res.content)['data']

    def get_response(self, url, data):
        res = self.client.get('/api/' + url, data=data, content_type='application/json')
        return res.status_code, json.loads(res.content)['data']

    def test_all(self):
        # Add user.
        code, content = self.post_response('add_person', {
            'identity': 'admin',
            'name': '尹昊萱',
            'id_number': '2018011276',
            'department': self.plb.id,
        })
        self.assertEqual(code, 200)
        self.assertEqual(content, 'Add person successfully.')
        self.yhx = Person.objects.get(name='尹昊萱')
        code, content = self.post_response('add_person', {
            'identity': 'admin',
            'name': '陈洪淼',
            'id_number': '2018012933',
            'department': self.plb.id,
        })
        self.assertEqual(code, 200)
        self.assertEqual(content, 'Add person successfully.')
        self.chm = Person.objects.get(name='陈洪淼')
        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(self.plb.members.count(), 2)

        # Add article.
        code, content = self.post_response('add_article', {
            'identity': 'admin',
            'title': '文章1',
            'content': '内容1',
            'authors': [self.yhx.id, self.chm.id],
            'editor': self.yhx.id,
            'department': self.plb.id,
        })
        self.assertEqual(code, 200)
        self.assertEqual(content, 'Add article successfully.')
        self.atc1 = Article.objects.get(title='文章1')
        code, content = self.post_response('add_article', {
            'identity': 'admin',
            'title': '文章2',
            'content': '内容2',
            'authors': [self.chm.id],
            'editor': self.yhx.id,
            'department': self.plb.id,
        })
        self.assertEqual(code, 200)
        self.assertEqual(content, 'Add article successfully.')
        self.atc2 = Article.objects.get(title='文章2')
        self.assertEqual(self.yhx.wrote.count(), 1)
        self.assertEqual(self.yhx.edited.count(), 2)
        self.assertEqual(self.chm.wrote.count(), 2)
        self.assertEqual(self.chm.edited.count(), 0)
        self.assertEqual(self.plb.articles.count(), 2)

        # Get department.
        code, content = self.get_response('get_department', {
            'id': self.plb.id,
        })
        self.assertEqual(code, 200)
        self.assertEqual(content['name'], '评论部')
        self.assertEqual(len(content['articles']), 2)
        self.assertEqual(content['articles'][0]['id'], self.atc1.id)
        self.assertEqual(content['articles'][1]['id'], self.atc2.id)
        self.assertEqual(len(content['members']), 2)
        self.assertEqual(content['members'][0]['id'], self.yhx.id)
        self.assertEqual(content['members'][1]['id'], self.chm.id)

        # Get person.
        code, content = self.get_response('get_person', {
            'id': self.yhx.id,
        })
        self.assertEqual(code, 200)
        self.assertEqual(content['name'], '尹昊萱')
        self.assertEqual(content['id_number'], '2018011276')
        self.assertEqual(len(content['wrote']), 1)
        self.assertEqual(content['wrote'][0]['id'], self.atc1.id)
        self.assertEqual(len(content['edited']), 2)
        self.assertEqual(content['edited'][0]['id'], self.atc1.id)
        self.assertEqual(content['edited'][1]['id'], self.atc2.id)

        # Get article.
        code, content = self.get_response('get_article', {
            'id': self.atc1.id,
        })
        self.assertEqual(code, 200)
        self.assertEqual(content['title'], '文章1')
        self.assertEqual(content['content'], '内容1')
        self.assertEqual(len(content['authors']), 2)
        self.assertEqual(content['authors'][0]['id'], self.yhx.id)
        self.assertEqual(content['authors'][1]['id'], self.chm.id)
        self.assertEqual(content['editor']['id'], self.yhx.id)

        # Get person list.
        code, content = self.get_response('person_list', {})
        self.assertEqual(code, 200)
        self.assertEqual(len(content), 2)
        self.assertEqual(content[0]['id'], self.yhx.id)
        self.assertEqual(content[1]['id'], self.chm.id)

        # Get department list.
        code, content = self.get_response('department_list', {})
        self.assertEqual(code, 200)
        self.assertEqual(len(content), 2)
        self.assertEqual(content[0]['id'], self.plb.id)
        self.assertEqual(content[1]['id'], self.ztb.id)

        # Get article list.
        code, content = self.get_response('article_list', {})
        self.assertEqual(code, 200)
        self.assertEqual(len(content), 2)
        self.assertEqual(content[0]['id'], self.atc1.id)
        self.assertEqual(content[1]['id'], self.atc2.id)
