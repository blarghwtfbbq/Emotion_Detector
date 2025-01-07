import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy', f"Expected joy but got {result['dominant_emotion']}")
        print(f"Test Joy: {result}")

    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger', f"Expected anger but got {result['dominant_emotion']}")
        print(f"Test Anger: {result}")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust', f"Expected disgust but got {result['dominant_emotion']}")
        print(f"Test Disgust: {result}")

    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness', f"Expected sadness but got {result['dominant_emotion']}")
        print(f"Test Sadness: {result}")

    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear', f"Expected fear but got {result['dominant_emotion']}")
        print(f"Test Fear: {result}")

if __name__ == '__main__':
    unittest.main()
