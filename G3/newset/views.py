from .models import NewsetStudent
from .serializers import NewsetStudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

# from .custompermissions import MyPermission
# from .customauth import MyAuth

from rest_framework_simplejwt.authentication import JWTAuthentication

# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
# from .throttling import JackRateThrottle

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.pagination import PageNumberPagination
from .pegination import MyPageNumberPagination



class StudentModelViewset(viewsets.ModelViewSet):
    queryset = NewsetStudent.objects.all()
    serializer_class = NewsetStudentSerializer



    #               -------For JWT------
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

#               ------For Throttling------
    # authentication_classes = [SessionAuthentication]    
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # throttle_classes = [JackRateThrottle, AnonRateThrottle]  # custome throttling

#             -------Scoped Rate Throttling----->> used to throttle specific method for eg. list, retrieve, create, etc. You can add below code in each method inividually and throttle.
    # throttle_classes = [ScopedRateThrottle]  
    # throttle_scope = 'viewstu'    # "throttle_scope" can be different or same for each method.


#               ------For Backend Filtering------

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name','city']

    # filterset_fields = {
    #     'city': ["in", "exact"],
    # } 


#               ------For Search Filtering------

    # filter_backends = [SearchFilter]    # '^' Starts-with search // # '=' Exact matches // #'$' Regex search
    # search_fields  = ['name','city']    
        

#               ------For Backend Filtering------
    # filter_backends = [OrderingFilter]
    # ordering_fields   = ['name', 'roll']


#               ------For Pagination------
    # pagination_class = PageNumberPagination
    pagination_class = MyPageNumberPagination   #(Custom Pagination)





'''-----------------------------------------------------***Viewset ***-----------------------------------------------------------------------'''
# class StudentViewSet(viewsets.ViewSet):

#     def list(self, request):

#         print("****************************List**************************")
#         print("---------------Basename:----------------------", self.basename)
#         print("---------------Action:----------------------", self.action)
#         print("---------------Detail:----------------------", self.detail)
#         print("---------------Suffix:----------------------", self.suffix)
#         print("---------------Name:----------------------", self.name)
#         print("---------------Description:----------------------", self.description)

#         stu = NewsetStudent.objects.all()
#         serializer  = NewsetStudentSerializer(stu, many=True)
#         return Response(serializer.data)


#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = NewsetStudent.objects.get(id=id)
#             srializer = NewsetStudentSerializer(stu)
#             return Response(srializer.data)


#     def create(self, request):
#         serializer = NewsetStudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data has been created successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def update(self, request, pk):
#         id=pk
#         stu = NewsetStudent.objects.get(id=id)
#         serializer = NewsetStudentSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data has been updated successfully'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def partial_update(self, request, pk):
#         id=pk
#         stu = NewsetStudent.objects.get(id=id)
#         serializer = NewsetStudentSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg' : 'Data has been updated successfully'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def destroy(self, request, pk):
#         id=pk
#         stu = NewsetStudent.objects.get(id=id)
#         stu.delete()
#         return Response({"msg":"Data has been deleted successfully!"})





'''-----------------------------------------------------*** Read Only Model Viewset ***-----------------------------------------------------------------------#                     '''
# class StudentRomViewset(viewsets.ReadOnlyModelViewSet):
#     queryset = NewsetStudent.objects.all()
#     serializer_class = NewsetStudentSerializer