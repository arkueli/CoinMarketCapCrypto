# import time 
# #from django.core.management.base import BaseCommand
# from selenium import webdriver
# import os
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from decimal import Decimal
import xlsxwriter
from .models import Parser
from .serializers import ParserSerializer
from rest_framework import status
import re
from django.conf import settings
from .tasks import async_background_task
#from .tasks import background_task
from utils.scraping_utils import scrape_data

    
class RunScraperView(APIView):
    def get(self, request):
        async_background_task.delay()  
        return Response({'message': 'Scraping started'})
    

def generate_excel_file():
    records = Parser.objects.all() 
    serialized_records = ParserSerializer(records, many=True).data
    data_frame = pd.DataFrame(serialized_records)

    excel_file = settings.EXCEL_FILE_PATH

    writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
    data_frame.to_excel(writer, sheet_name='Sheet_1', index=False)
    print("Excel sheet generated successfully!")
    writer.close()    



class GenerateExcelView(APIView):
    def get(self, request): 
        generate_excel_file()
        return Response({'message': 'Excel file generated'})


class ListRecordsView(APIView):
    def get(self, request):
        records = Parser.objects.all()[:200] 
        serialized_records = ParserSerializer(records, many=True).data
        return Response(serialized_records)  
    
    def post(self, request):
        serializer = ParserSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save()       
            return Response("Data is correct") 
        else:           
            return Response("Data is invalid") 
        

class DeleteRecordsView(APIView):
    def get(self, request):
        Parser.objects.all().delete() 
        return Response({'message': 'All data deleted'}) 

    




