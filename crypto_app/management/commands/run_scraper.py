from django.core.management.base import BaseCommand
from crypto_app.views import generate_excel_file, background_task

class Command(BaseCommand):
    help = 'Generate the Excel file with updated crypto data'  
    def handle(self, *args, **options): 
        background_task()  
        generate_excel_file()





# from django.core.management.base import BaseCommand
# from crypto_app.tasks import background_task
# import os


# class Command(BaseCommand):
#     help = 'Generate the Excel file with updated crypto data'

#     def handle(self, *args, **options):
#         # Run the tasks
#         background_task.delay()

#         # Restart the Celery worker
#         os.system("pkill -f 'celery worker'")

#         self.stdout.write(self.style.SUCCESS('Tasks completed and Celery worker restarted'))

