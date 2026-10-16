from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from leadApp.models import Lead
from leadApp.serializers import LeadSerializer
from rest_framework import authentication,permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter   #searchfilter-oru condition base cheythit namk search cheythitulla items list cheyam,OrderingFilter -ethelum oru col basil items sort cheyth edkn vendyt(asc,desc)

# Create your views here.

class LeadCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[        #source,status basil search cheyth edkan. 3 clasum leadlistviewlk apply cheyunnu filter_backends enna keywordil
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields=['status','source']
    serach_fields=['name','email','status','source']   #[] ullil model clsinte colmns
    ordering_fields=['name','added_date']

class LeadRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    
    


