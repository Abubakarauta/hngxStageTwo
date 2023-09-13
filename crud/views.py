from rest_framework import generics
from .models import person
from .serializers import PersonSerializer

# Create your views here.

class PersonList(generics.ListCreateAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer

    def personCreate(self, serializer):
        name = self.request.data.get('name')
        user = person(name = name)
        user.save()

    def get_queryset(self):
        queryset =  super().get_queryset()
        name = self.request.query_params.get('name', None)
        
        if name:
                # Filter the queryset based on the provided name
            queryset= queryset.filter(name=name)
        return queryset
    

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = person.objects.all()
    serializer_class = PersonSerializer

    def personUpate(self, serializer):
        name = self.request.data.get('name')
        if name:
            serializer.instance.name = name
        serializer.save()



