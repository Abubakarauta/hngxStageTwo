from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

# Create your views here.

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        queryset =self.filter_queryset( self.get_queryset())
        serializer = self.get_serializer(queryset, many = True)

        response_data = []

        for person_data in  serializer.data:
            person_item = {                
            "id": person_data["id"],
            "name": person_data["name"],
            "status":"Success",
            "message":"Person retrieved successfully.",
            "created_at": person_data["created_at"],
            "updated_at": person_data["updated_at"],
            }
            response_data.append(person_item)

        return Response(response_data, status = status.HTTP_200_OK)
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "id": serializer.data["id"],
                "name":serializer.data["name"],
                "status":"Success",
                "message":"Person created successfully.",
                "created_at": serializer.data["created_at"],
                "updated_at": serializer.data["updated_at"],

            }
            return Response(response_data, status= status.HTTP_201_CREATED)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)     



class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_data = {
            "id": serializer.data["id"],
            "name": serializer.data["name"],
            "status": "Success",
            "message": "Person updated successfully.",
            "created_at": serializer.data["created_at"],
            "updated_at": serializer.data["updated_at"],
        }        
        return Response(response_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                "id": serializer.data["id"],
                "name": serializer.data["name"],
                "status": "Success",
                "message": "Person updated successfully.",
                "created_at": serializer.data["created_at"],
                "updated_at": serializer.data["updated_at"]
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response_data = {
            "id": instance.id,
            "name": instance.name,
            "status": "Success",
            "message": "Person deleted successfully.",
            "created_at": instance.created_at,
            "updated_at": instance.updated_at
        }
        return Response(response_data, status= status.HTTP_204_NO_CONTENT)

