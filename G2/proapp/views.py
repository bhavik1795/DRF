from django.shortcuts import render
from rest_framework.decorators import api_view # permission_classes, authentication_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated




'''----------------------Function Based APIView---------------------------                  '''

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def student_api(request, pk=None):

    print("Request.Data---------------------------", request.data)

    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)



    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data has been created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data) 

        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data has been Updated successfully !!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True) 

        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data has been Updated successfully !!'}) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg' : 'Data has been Deleted successfully !!'})



'''----------------------Class Based APIView---------------------------            '''

# class StudentAPI(APIView):
#     def get(self, request, pk=None, format=None):   # Convert Json to Python & give Py.dict
        
#         print("Request.Data---------------------------", request.data)      #  Python Dict   
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)        # Find id and give corresponding data 
#             serializer = StudentSerializer(stu)     # Convert Complex data to Python Dict
#             return Response(serializer.data)        # Convert Python to Json and render Json response to user

#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)


#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)   # Convert Python to Complex
#         if serializer.is_valid():                           # Validate & save in db
#             serializer.save()
#             return Response({'msg' : 'Data has been created successfully'}, status=status.HTTP_201_CREATED) # render Json response to user
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, pk, format=None):

#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data has been Updated successfully !!'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def patch(self, request, pk, format=None):

#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu, data=request.data, partial=True) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data has been Updated successfully !!'}) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk, format=None):

#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg' : 'Data has been Deleted successfully !!'})