from SentimentAnalysis.sentiment_analysis import sentiment_analysis_func
import unittest


class TestEmotionDetection(unittest.TestCase):
    def test_sentiment_analysis_func(self):
        result = sentiment_analysis_func("I am glad this happened")
        self.assertEqual(result[2], [(['glad'], 0.5, 1.0, None)])


if __name__ == "__main__":
    unittest.main()
