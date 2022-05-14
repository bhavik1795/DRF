from .models import ConcreteStudent
from .serializers import ConcreteStudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView,RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer

class StudentCreate(CreateAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ConcreteStudent.objects.all()
    serializer_class = ConcreteStudentSerializer
