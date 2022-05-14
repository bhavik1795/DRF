from functools import partial
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

#----> For class base view
from django.utils.decorators import method_decorator 
from django.views import View
import json





#'''                             Function Based View                '''

@csrf_exempt
def student_api(request):

    if request.method == 'GET':
        Json_data = request.body        # Get data from client that is in JSON format
        print("------------------JSON------", Json_data)
        stream = io.BytesIO(Json_data)  # Stream Json data
        print("------------------Strem------", stream)
        pythondata = JSONParser().parse(stream) # # Covert Json to Python Dict
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)        # **  Complex Data
            serializer = StudentSerializer(stu)     # **  Convert Complex Data to Python Dict
            #json_data = JSONRenderer().render(serializer.data)     # ** Covert to JSON form
            #return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(serializer.data)    # **  Covert to Json & Render to user
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)  # "many=True" because 'stu' object has list of data
        return JsonResponse(serializer.data, safe=False)    # If "safe=True" then it expect single dictionary object or give Error! 
        # Give Json response to client


    if request.method == "POST":
        json_data = request.body
        print("------------------JSON------", json_data)    # b'{"name": "bhavik", "roll": "324", "city": "Boisar"}'

        # stream = io.BytesIO(json_data)
        # print("------------------Strem------", stream)
        print("------jsonloads---------", json.loads(json_data))    # {'name': 'bhavik', 'roll': '324', 'city': 'Boisar'}
        a = json.loads(json_data)
        # pythondata = JSONParser().parse(json_data)
        serializer = StudentSerializer(data=a)           # Convert Dict to Complex Data & save the complex data
        print("------serializer-------", serializer)     # (data={'name': 'bhavik', 'roll': '324', 'city': 'Boisar'})
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : serializer.data}
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors)


    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)  # If "partial=True" then no need to write all fields.
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data has been Updated successfully !!'}
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors)


    if request.method == "DELETE":
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg' : 'Data has been Deleted successfully !!'}
        return JsonResponse(res, safe=False)



#'''         Class Based View        '''


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):

    def get(self,request, *args, **kwargs):
        Json_data = request.body
        stream = io.BytesIO(Json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)       
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)    # **  Convert to Json & Render to user
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)  # "many=True" because 'stu' object has list of data
        return JsonResponse(serializer.data, safe=False) # If "safe=True" then it expect single dictionary object or give Error!


    def post(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data has been loged successfully'}
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors)

        
    def put(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True) 
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data has been Updated successfully !!'}
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors)


    def delete(self,request, *args, **kwargs):
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg' : 'Data has been Deleted successfully !!'}
        return JsonResponse(res, safe=False)




