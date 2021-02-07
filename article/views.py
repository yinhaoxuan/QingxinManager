from django.shortcuts import render
from django.http import HttpResponse
from QingxinManager.network import gen_response, preprocess
from article.models import Person, Department, Article


# Create your views here.

def index(request):
    return HttpResponse("Hello.")


def verify_admin(identity):
    return True


def add_person(request):
    status, res = preprocess(request, ["identity", "name", "id_number", "department"])
    if not status:
        return res
    identity = res["identity"]
    name = res["name"]
    id_number = res["id_number"]
    try:
        department = Department.objects.filter(name__exact=res["department"])[0]
    except Exception as e:
        return gen_response(409, "No such department.")
    if not verify_admin(identity):
        return gen_response(401, "Permission denied.")
    Person(name=name, id_number=id_number, department=department).save()
    return gen_response(201, "Add person successfully.")


def add_article(request):
    pass


def get_article(request):
    pass


def get_person(request):
    pass


def get_department(request):
    pass
