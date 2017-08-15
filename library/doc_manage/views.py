import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from graphene_django.views import GraphQLView
from library.schema import schema
from auth.util import *
# Create your views here.

@user_passes_test(lambda x: issuperuser(x) or islibstaff(x))
def private_graphql(request):
    return GraphQLView.as_view(graphiql=True, schema=schema)(request)

@login_required
def test_query(request):
    query = """
    {
      allBorrows {
        edges {
          node {
            borrower {
              username
            }
            doc {
              title
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
