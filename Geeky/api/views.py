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

