from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth.models import User
from doc_manage.models import Document, Borrow, Category
from auth.util import *

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name']
        interfaces = (relay.Node, )


class DocumentNode(DjangoObjectType):
    class Meta:
        model = Document
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

class BorrowNode(DjangoObjectType):
    class Meta:
        model = Borrow
        filter_fields = {
            'borrower__username': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(AbstractType):
    # users = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    # category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    # documents = relay.Node.Field(DocumentNode)
    all_documents = DjangoFilterConnectionField(DocumentNode)

    # borrows = relay.Node.Field(BorrowNode)
    all_borrows = DjangoFilterConnectionField(BorrowNode)

    def resolve_all_users(self, args, context, info):
        print()
        print(context.user, context.user.is_superuser)
        print()
        if context.user.is_superuser:
            return User.objects.all()
        else:
            raise Exception('Unauthorized')

    def resolve_all_borrows(self, args, context, info):
        user = context.user
        if issuperuser(user) or islibstaff(user):
            return Borrow.objects.all()
        elif isstudent(user):
            return Borrow.objects.filter(borrower=user)
        else:
            raise Exception('Unauthorized')
