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

'''         Class Based View        '''

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
            return JsonResponse(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)


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




'''                             Function Based View                '''
#                            Serialization / Get Data
'''@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        Json_data = request.body
        stream = io.BytesIO(Json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)


#               Deserialization / Post Data

    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data has been loged successfully'}
            return JsonResponse(res, safe=False)

        return JsonResponse(serializer.errors)


#                    Update Data

    if request.method == "PUT":
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
        

#                    Delete Data

    if request.method == "DELETE":
        jason_data = request.body
        stream = io.BytesIO(jason_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg' : 'Data has been Deleted successfully !!'}
        return JsonResponse(res, safe=False)
'''
