import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from projeto.produto.models import Produto


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:

    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                origem=choice((True, False)),
                safra=Utils.gen_digits(8),
                preco=random() * randint(10, 50),
                estoque=randint(10, 200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    'Arabica',
    'Robusta'
)


ProdutoClass.criar_produtos(produtos)


