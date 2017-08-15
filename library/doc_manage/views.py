import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import user_passes_test

from graphene_django.views import GraphQLView
from library.schema import schema
# Create your views here.
def _issuperuser(user):
    return user.is_superuser
def _islibstaff(user):
    return user.groups.filter(name__in=['library_staff']).exists()

@user_passes_test(lambda x: _issuperuser(x) or _islibstaff(x))
def private_graphql(request):
    return GraphQLView.as_view(graphiql=True, schema=schema)(request)

def test_query(request):
    query = """
    {
        allUsers {
            edges {
                node {
                    username
                }
            }
        }

        allCategories {
            edges {
                node {
                    name
                }
            }
        }
        allBorrows {
            edges {
                node {
                    borrowTime
                    returnTime
                    borrower {
                        username
                    }
                }
            }
        }
    }
    """
    res = schema.execute(query, context_value=request)
    print('data: ', res.data)
    print('errs: ', res.errors)
    return JsonResponse(json.dumps(res.data), safe=False)
