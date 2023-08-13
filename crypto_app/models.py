from django.db import models

class Parser(models.Model):  
    rank = models.IntegerField()
    name = models.TextField()
    symbol = models.TextField()
    market_cap = models.IntegerField(max_digits=14, decimal_places=2) 
    price = models.FloatField(max_digits=6, decimal_places=2) 
    circulating_supply = models.TextField() 
    volume_24h = models.FloatField(max_digits=14, decimal_places=2) 
    one_hour = models.FloatField(max_digits=4, decimal_places=2) 
    twenty_four_hours = models.FloatField(max_digits=4, decimal_places=2)
    seven_days = models.FloatField(max_digits=4, decimal_places=2) 
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.price = float(self.price)
        self.one_hour = float(self.one_hour)
        self.twenty_four_hours = float(self.twenty_four_hours)
        self.seven_days = float(self.seven_days)

    def __int__(self):
        return self.rank 






# For testing scraping functionality, you'd likely create separate tests using tools like
# 'unittest.mock' to simulate web requests and responses.

# Data Saving
# Field Validation