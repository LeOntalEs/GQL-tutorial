import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from library.schema import schema
# Create your views here.
def test_query(request):
    query = """
    {
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
    res = schema.execute(query)
    print('data: ', res.data)
    print('errs: ', res.errors)
    return JsonResponse(json.dumps(res.data), safe=False)
