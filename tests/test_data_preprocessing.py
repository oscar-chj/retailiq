import unittest
from src.data.data_preprocessing import clean_data
import pandas as pd

class TestDataPreprocessing(unittest.TestCase):
    def test_clean_data(self):
        df = pd.DataFrame({
            'feature': [1, 2, None, 4],
            'category': ['A', 'B', 'A', None]
        })
        cleaned_df = clean_data(df)
        self.assertFalse(cleaned_df.isnull().values.any())

if __name__ == '__main__':
    unittest.main()
