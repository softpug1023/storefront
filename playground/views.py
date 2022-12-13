
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q,F
from store.models import Product,OrderItem, Order, Collection
from tags.models import TaggedItem
from django.db import transaction
from django.db import connection


def say_hello(request): 

    with connection.cursor() as cursor:
        cursor.execute()




    return render(request, 'hello.html', {'name': 'Mosh'})
