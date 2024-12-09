import unittest
import numpy as np
from chart import p, MIN_SELLER_PERCENTAGE, ADDITIONAL_PERCENTAGE, PRICE_INFLECTION, create_plots

class TestProfitModel(unittest.TestCase):
    def test_minimum_percentage(self):
        """Test that very high values approach but don't go below MIN_SELLER_PERCENTAGE"""
        high_value = 1000000.0
        self.assertGreaterEqual(p(high_value), MIN_SELLER_PERCENTAGE)
        self.assertLess(p(high_value), MIN_SELLER_PERCENTAGE + 0.01)

    def test_maximum_percentage(self):
        """Test that very low values approach MAX_SELLER_PERCENTAGE"""
        low_value = 1.0
        max_percentage = MIN_SELLER_PERCENTAGE + ADDITIONAL_PERCENTAGE
        self.assertLess(p(low_value), max_percentage)
        self.assertGreater(p(low_value), max_percentage - 0.01)

    def test_inflection_point(self):
        """Test that the percentage at inflection point is reasonable"""
        percentage_at_inflection = p(PRICE_INFLECTION)
        max_percentage = MIN_SELLER_PERCENTAGE + ADDITIONAL_PERCENTAGE
        # Should be roughly halfway between min and max
        self.assertGreater(percentage_at_inflection, MIN_SELLER_PERCENTAGE)
        self.assertLess(percentage_at_inflection, max_percentage)

    def test_monotonic_decrease(self):
        """Test that the percentage strictly decreases as value increases"""
        x_values = np.linspace(10, 10000, 100)
        percentages = [p(x) for x in x_values]
        for i in range(len(percentages)-1):
            self.assertGreaterEqual(percentages[i], percentages[i+1])

    def test_plots_creation(self):
        """Test that plots can be created without displaying them"""
        fig1, fig2 = create_plots(show_plots=False)
        self.assertIsNotNone(fig1)
        self.assertIsNotNone(fig2)
        # Verify basic plot properties
        self.assertEqual(fig1.get_size_inches().tolist(), [12, 6])
        self.assertEqual(fig2.get_size_inches().tolist(), [12, 6])

if __name__ == '__main__':
    unittest.main()
