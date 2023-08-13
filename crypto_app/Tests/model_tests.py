from django.test import TestCase
from crypto_app.models import Parser
from django.core.exceptions import ValidationError


class ParserModelTest(TestCase):
    def test_data_saving(self):
        parser = Parser.objects.create(
            rank=1,
            name="Bitcoin",
            symbol="BTC",
            market_cap=1000000000,
            price=50000.0,
            circulating_supply="1000000",
            volume_24h=10000000.0,
            one_hour=1.5,
            twenty_four_hours=3.0,
            seven_days=10.0
        )

        saved_parser = Parser.objects.get(pk=parser.pk)

        # Verify that the fields match the values  provided
        self.assertEqual(saved_parser.rank, 1)
        self.assertEqual(saved_parser.name, "Bitcoin")
        self.assertEqual(saved_parser.symbol, "BTC")
        self.assertEqual(saved_parser.market_cap, 1000000000)
        self.assertEqual(saved_parser.price, 50000.0)
        self.assertEqual(saved_parser.circulating_supply, "1000000")
        self.assertEqual(saved_parser.volume_24h, 10000000.0)
        self.assertEqual(saved_parser.one_hour, 1.5)
        self.assertEqual(saved_parser.twenty_four_hours, 3.0)
        self.assertEqual(saved_parser.seven_days, 10.0)








class ParserModelValidationTest(TestCase):
    def test_valid_data(self):
        parser = Parser(
            rank=1,
            name="Bitcoin",
            symbol="BTC",
            market_cap=1000000000,
            price=50000.0,
            circulating_supply="1000000",
            volume_24h=10000000.0,
            one_hour=1.5,
            twenty_four_hours=3.0,
            seven_days=10.0
        )
        parser.full_clean()  # This should not raise any ValidationError

    def test_invalid_data(self):
        parser = Parser(
            rank=None, 
            name="",
            symbol="BT",
            market_cap=10.00,
            price=50000.0,
            circulating_supply="1000000",
            volume_24h=100.0,
            one_hour=1000.5,
            twenty_four_hours=35.0,
            seven_days=1000000.0
        )
        with self.assertRaises(ValidationError):
            parser.full_clean()  # This should raise a ValidationError
