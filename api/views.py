from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import StudentModel
from .serializers import StudentSerializer


# class StudentApi(ListModelMixin,GenericAPIView):
#     queryset=StudentModel.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

# class StudentRetrieve(RetrieveModelMixin,GenericAPIView):
#     queryset=StudentModel.objects.all()
#     serializer_class=StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)   
# class StudentCreate(CreateModelMixin,GenericAPIView):
#     queryset=StudentModel.objects.all() 
#     serializer_class=StudentSerializer
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args,**kwargs) 
    
# class StudentUpdate(UpdateModelMixin,GenericAPIView):
#     queryset=StudentModel.objects.all()
#     serializer_class=StudentSerializer
#     def put(self, request ,*args ,**kwargs):
#         return self.update(request, *args , **kwargs)

# class StudentDestroyed(DestroyModelMixin,GenericAPIView):
#     queryset=StudentModel.objects.all() 
#     serializer_class=StudentSerializer
#     def delete(self,request, *args ,**kwargs):
#         return self.destroy(request , *args ,**kwargs)       

#*******************************************************************************************************************************     

class LCStudent(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    def get(self,request, *args , **kwargs):
        return self.list(request ,*args ,**kwargs)
    def post(self, request , *args, **kwargs):
        return self.create(request, *args ,**kwargs)

class RUDStudent(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset=StudentModel.objects.all() 
    serializer_class=StudentSerializer
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self, request , *args, **kwargs):
        return self.update(request,*args , **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    
