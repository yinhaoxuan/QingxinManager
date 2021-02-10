from django.shortcuts import render
from django.http import HttpResponse
from QingxinManager.network import gen_response, process_post, process_get
from article.models import Person, Department, Article


# Create your views here.

def index(request):
    return HttpResponse('Hello.')


def verify_admin(identity):
    return True


def verify_user(identity):
    return True


def person_short_info(person):
    return {'id': person.id, 'name': person.name}


def article_short_info(article):
    return {'id': article.id, 'name': article.title}


def department_short_info(department):
    return {'id': department.id, 'name': department.name}


def add_person(request):
    status, res = process_post(request, ['identity', 'name', 'id_number', 'department'])
    if not status:
        return res
    identity = res['identity']
    name = res['name']
    id_number = res['id_number']
    try:
        department = Department.objects.get(pk=res['department'])
    except Exception as e:
        return gen_response(409, f'No such department: {e}')
    if not verify_admin(identity):
        return gen_response(401, 'Permission denied.')
    Person(name=name, id_number=id_number, department=department).save()
    return gen_response(200, 'Add person successfully.')


def add_article(request):
    status, res = process_post(request, ['identity', 'title', 'content', 'authors', 'editor', 'department'])
    if not status:
        return res
    identity = res['identity']
    title = res['title']
    content = res['content']
    try:
        authors = [Person.objects.get(pk=author) for author in res['authors']]
        editor = Person.objects.get(pk=res['editor'])
    except Exception as e:
        return gen_response(409, f'No such person: {e}')
    try:
        department = Department.objects.get(pk=res['department'])
    except Exception as e:
        return gen_response(409, f'No such department: {e}')
    if not verify_user(identity):
        return gen_response(401, 'Permission denied.')
    article = Article(title=title, content=content, editor=editor, department=department)
    article.save()
    for author in authors:
        article.authors.add(author)
    return gen_response(200, 'Add article successfully.')


def get_article(request):
    status, res = process_get(request, ['id'])
    if not status:
        return res
    article_id = res['id']
    try:
        article = Article.objects.get(id=article_id)
        return gen_response(200, {
            'title': article.title,
            'content': article.content,
            'authors': [person_short_info(author) for author in article.authors.all()],
            'editor': person_short_info(article.editor),
        })
    except Exception as e:
        return gen_response(409, f'Article not found: {e}')


def get_person(request):
    status, res = process_get(request, ['id'])
    if not status:
        return res
    person_id = res['id']
    try:
        person = Person.objects.get(id=person_id)
        return gen_response(200, {
            'name': person.name,
            'id_number': person.id_number,
            'department': department_short_info(person.department),
            'wrote': [article_short_info(article) for article in person.wrote.all()],
            'edited': [article_short_info(article) for article in person.edited.all()],
        })
    except Exception as e:
        return gen_response(409, f'Person not found: {e}')


def get_department(request):
    status, res = process_get(request, ['id'])
    if not status:
        return res
    department_id = res['id']
    try:
        department = Department.objects.get(id=department_id)
        return gen_response(200, {
            'name': department.name,
            'members': [person_short_info(member) for member in department.members.all()],
            'articles': [article_short_info(article) for article in department.articles.all()],
        })
    except Exception as e:
        return gen_response(409, f'Department not found: {e}')


def person_list(request):
    return gen_response(200, [person_short_info(person) for person in Person.objects.all()])


def article_list(request):
    return gen_response(200, [article_short_info(article) for article in Article.objects.all()])


def department_list(request):
    return gen_response(200, [department_short_info(department) for department in Department.objects.all()])
