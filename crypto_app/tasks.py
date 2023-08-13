from __future__ import absolute_import, unicode_literals
from .models import Parser
import multiprocessing
from celery import shared_task
from utils.scraping_utils import scrape_data


@shared_task
def async_background_task():   
    data = scrape_data()  
    for item in data[:200]:   
        parser = Parser.objects.create(**item) 
        parser.save() 
    
    print("Scraping complete")
    
scraping_process = multiprocessing.Process(target=async_background_task) 
#pass
































