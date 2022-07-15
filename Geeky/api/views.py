import io
from django.shortcuts import render

from api.serializers import StudentSerializer

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse


#                       # GET Method #

# Model Object - Single student data (For One Instance)

def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)     #    *** Convert Complex Data to python dictionary

                                        #json_data = JSONRenderer().render(serializer.data)     #   *** Covert to JSON form
                                        #return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data)    


# Qury set - All student data

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
                                                    # json_data = JSONRenderer().render(serializer.data)
                                                    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)





                         # POST Method #

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(requst):
    if requst.method == "POST":
        json_data = requst.body         # Get data from client is in JSON form
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)    # Convert Json to Python Dict
        serializer = StudentSerializer(data=python_data)    # Convert Dict to Complex Data

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data has been loged successfully'}
                                                                # json_data = JSONRenderer().render(res)
                                                                # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)

        return JsonResponse(serializer.errors)

#   Superset :
# https://sairamkrish.medium.com/apache-superset-custom-authentication-and-integrate-with-other-micro-services-8217956273c1
# https://medium.com/geekculture/custom-security-manager-for-apache-superset-c91f413a8be7
# https://stackoverflow.com/questions/59247723/connecting-apache-superset-with-postgresql
# https://programmer.group/tutorial-how-to-integrate-superset-in-your-own-application.html
# https://flask-appbuilder.readthedocs.io/en/latest/security.html#role-based
# https://medium.com/dlt-labs-publication/exploring-apache-superset-18c7b5344daf

# Superset Issues :
# How to secure Superset '/login/' endpoint: https://stackoverflow.com/questions/70082354/how-to-secure-superset-login-endpoint
# https://stackoverflow.com/questions/65619149/reuse-the-credentials-of-one-system-to-log-in-to-another
# https://stackoverflow.com/questions/67189776/how-to-embed-use-graph-generated-by-apache-superset-directly-in-other-web-applic

# Token Authentication:
# https://stackoverflow.com/questions/44004837/flask-route-requesting-authorization-header-when-not-annotated-with-jwt-required
# https://stackoverflow.com/questions/13825278/python-request-with-authentication-access-token
# https://stackoverflow.com/questions/45868120/python-post-request-with-bearer-token
# https://stackoverflow.com/questions/55783580/sending-post-request-to-paypal-to-get-access-token-in-django

# Django :
# https://stackoverflow.com/questions/10065676/django-hide-button-in-template-if-user-is-not-super-user
# https://medium.com/python-pandemonium/json-web-token-based-authentication-in-django-b6dcfa42a332
# https://code.visualstudio.com/docs/python/tutorial-django
# https://stackoverflow.com/questions/35903832/how-to-redirect-to-external-url-in-django
# https://stackoverflow.com/questions/62162634/django-and-post-request-to-an-external-api-in-different-views

# Learning :
# https://medium.com/codex/top-tips-to-get-better-at-programming-d5e4c28d93e1
# https://medium.com/wwcode-python/5-data-engineering-project-ideas-276f29c8885f
# https://medium.com/@nutanbhogendrasharma/consume-rest-api-in-django-web-application-130c0daa6f70
# https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
# https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/

