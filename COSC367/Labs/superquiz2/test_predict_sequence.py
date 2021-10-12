import unittest
from predict_sequence import SequencePredicter

class TestPredictSequence(unittest.TestCase):
    def test_predict_rest(self):
        sequence = [0, 1, 2, 3, 4, 5, 6, 7]
        predicter = SequencePredicter(sequence)
        self.assertEqual(predicter.predicted_sequence, [8, 9, 10, 11, 12])
        self.assertEqual(sequence, [0, 1, 2, 3, 4, 5, 6, 7])
        sequence = [0, 2, 4, 6, 8, 10, 12, 14]
        predicter = SequencePredicter(sequence)
        self.assertEqual(predicter.predicted_sequence, [16, 18, 20, 22, 24])
        self.assertEqual(sequence, [0, 2, 4, 6, 8, 10, 12, 14])
        sequence = [31, 29, 27, 25, 23, 21]
        predicter = SequencePredicter(sequence)
        self.assertEqual(predicter.predicted_sequence, [19, 17, 15, 13, 11])
        self.assertEqual(sequence, [31, 29, 27, 25, 23, 21])
        sequence = [0, 1, 4, 9, 16, 25, 36, 49]
        predicter = SequencePredicter(sequence)
        self.assertEqual(predicter.predicted_sequence, [64, 81, 100, 121, 144])
        self.assertEqual(sequence, [0, 1, 4, 9, 16, 25, 36, 49])
        sequence = [3, 2, 3, 6, 11, 18, 27, 38]
        predicter = SequencePredicter(sequence)
        self.assertEqual(predicter.predicted_sequence, [51, 66, 83, 102, 123])
        self.assertEqual(sequence, [3, 2, 3, 6, 11, 18, 27, 38])
        sequence = [0, -1, 1, 0, 1, -1, 2, -1]
        predicter = SequencePredicter(sequence)
        self.assertEqual(predicter.predicted_sequence, [5, -4, 29, -13, 854])
        self.assertEqual(sequence, [0, -1, 1, 0, 1, -1, 2, -1])

    def test_fibbonacci(self):
        sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
        predicter = SequencePredicter(sequence)
        self.assertEqual(predicter.predicted_sequence, [21, 34, 55, 89, 144])
        self.assertEqual(sequence, [0, 1, 1, 2, 3, 5, 8, 13])

if __name__ == "__main__":
    unittest.main()
