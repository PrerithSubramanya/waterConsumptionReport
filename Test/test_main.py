import unittest
import main
import json
import os


class MyTestCase(unittest.TestCase):

    def test_convertLocal(self):
        self.assertEqual(main.convertLocal('2021-12-17T13:00:01.000Z'), '2021-12-18 00:00:01+11:00')
        self.assertEqual(main.convertLocal('2021-12-18T05:02:01.000Z'), '2021-12-18 16:02:01+11:00')
        self.assertEqual(main.convertLocal('2021-12-18T16:04:24.327+11:00'), None)

    def test_dateExtractUTC(self):
        self.assertEqual(main.dateExtractUTC('2021-12-18T05:02:01.000Z'), '2021-12-18')
        self.assertEqual(main.dateExtractUTC('2021-12-17T13:00:01.000Z'), '2021-12-17')
        self.assertEqual(main.dateExtractUTC('2021-12-18T16:04:24.327+11:00'), None)

    def test_dateExtractLocal(self):
        self.assertEqual(main.dateExtractLocal('2021-12-18 00:00:01+11:00'), '2021-12-18')
        self.assertEqual(main.dateExtractLocal('2021-12-18 16:02:01+11:00'), '2021-12-18')
        self.assertEqual(main.dateExtractLocal('2021-12-17T13:00:01'), None)

    def test_analytics(self):
        output = {'2021-12-30': 13.0}
        with open('Test/data/sample.json') as sample_readings:
            sample_readings = json.load(sample_readings)
            self.assertDictEqual(main.analytics(sample_readings), output)

    def test_litersTokLiters(self):
        self.assertEqual(main.literTokLiter(500), 0.5)
        self.assertEqual(main.literTokLiter(1000), 1)


    def test_writeToCsv(self):
        filePath = 'Test/Output/out.csv'
        with open('Test/data/sample.json') as sample_readings:
            sample_readings = json.load(sample_readings)
        self.assertTrue(main.writeToCsv(sample_readings, filePath))
        self.assertTrue(os.path.getsize(filePath)>0)



if __name__ == '__main__':
    unittest.main()
