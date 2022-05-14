from api.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100) #,validators=[starts_with_r])    # I can use validator function here!
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)


    def create(self, validate_data):
        return Student.objects.create(**validate_data)


    def update(self, instance, validated_data):                 # instance = old data(present in db)

        print("--------initially it was old name-----------------", instance.name)

        instance.name = validated_data.get('name', instance.name)       # if 'name = None' then it will keep old data (i.e. data present in "instance.name") as it is & save it.

        print("--------updated to new name-----------------", instance.name)

        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    '''#               FIELD LEVEL VALIDATION for *Single Field*        '''
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError("seat full")
    #     return value

    '''#               OBJECT LEVEL VALIDATION for *Multiple Fields*        '''
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')

    #     if nm.lower() == "rohit" and ct.lower() != "Ranchi":
    #         raise serializers.ValidationError("City must be Ranchi")
    #     return data

'''#                           VALIDATORS (Note: Write outside class)       '''
# def starts_with_r(value): #(Function name can be anything as per ur choise)
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Name should start with R")

''' ***Note: --->>   "VALIDATORS"(*"High Priority"*) --> (2nd) "FIELD LEVEL VALIDATION" ----> (3rd) "OBJECT LEVEL VALIDATION"    while checking: "is_valid()"   '''




'''----------------------------------------------Model Serializer--------------------------------------------------'''

# def starts_with_r(value): #(Function name can be anything as per ur choise)
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Name should start with R")


# class StudentSerializer(serializers.ModelSerializer):

    # name = serializers.CharField(read_only=True)    ---> validation For single field
    # name = serializers.CharField(validators=[starts_with_r])    ---> Validator 

    # class Meta:
    #     model = Student
    #     fields = ['id', 'name', 'roll', 'city']


    # read_only_fields = ['name', 'roll']       -----> validation For multiple fields
    # extra_kwargs = {'name':{'read_only':True}}    --> perform same task