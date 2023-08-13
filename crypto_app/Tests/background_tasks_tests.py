#  Test to see if background task is being triggered and executed properly using 'unittest'

import unittest
from unittest.mock import patch
from crypto_app.tasks import async_background_task

class TestAsyncBackgroundTask(unittest.TestCase):

    @patch('crypto_app.tasks.scrape_data')  
    @patch('crypto_app.tasks.Parser.objects.create')  
    def test_async_background_task_execution(self, mock_create, mock_scrape_data):
        
        mock_scrape_data.return_value = [{'Rank': 1, 'Name': 'Bitcoin', 'Symbol': 'BTC'}]              
        async_background_task()
        mock_scrape_data.assert_called_once()

        mock_create.assert_called_once_with(Rank=1, Name='Bitcoin', Symbol='BTC')

if __name__ == '__main__':
    unittest.main()
