from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from doc_manage.models import Document, Borrow, Category


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name']
        interfaces = (relay.Node, )


class DocumentNode(DjangoObjectType):
    class Meta:
        model = Document
        # Allow for some more advanced filtering here
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

class BorrowNode(DjangoObjectType):
    class Meta:
        model = Borrow
        # Allow for some more advanced filtering here
        filter_fields = {
            'borrower__username': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(AbstractType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    documents = relay.Node.Field(DocumentNode)
    all_documents = DjangoFilterConnectionField(DocumentNode)

    borrow = relay.Node.Field(BorrowNode)
    all_borrow = DjangoFilterConnectionField(BorrowNode)
