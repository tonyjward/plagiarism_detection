import unittest

from src.scraping import get_article_text, get_driver

# Before running these tests make sure you have a firefox selenium driver container running
# sudo docker run -d --rm --name standalone-firefox -p 4444:4444 -p 5900:5900 --shm-size 2g selenium/standalone-firefox-debug:3.141.59

class Test_get_articles(unittest.TestCase):
    
    def setUp(self):
        'Instantiate a selenium web driver so we can start web scraping'
        self.driver = get_driver()
        self.links = ['https://statcore.co.uk/']

    def test_get_articles(self):
        result = get_article_text(self.links, self.driver, pause_time = 4)
        self.assertTrue(result['links_worked'][0] == 'https://statcore.co.uk/')
        self.assertTrue('We provide innovative ways to help you use your data more effectively' in result['articles'][0])
        self.assertTrue(len(result['links_failed']) == 0)

    def tearDown(self):
        'Close selenium web driver once we are finished testing'
        self.driver.close()

if __name__ == '__main__':
    unittest.main()



# class Test_1_solution(unittest.TestCase):
#     def setUp(self):
#         self.predictions = np.array([1, 2, 3])
#         self.actuals = np.array([0.9, 2.2, 2.7])

#     def test_Rmse(self):
#         rmse = Rmse(self.predictions, self.actuals)
#         self.assertIsNone(np.testing.assert_allclose(rmse, 0.374165739))

#     def test_Mae(self):
#         mae = Mae(self.predictions, self.actuals)
#         self.assertIsNone(np.testing.assert_allclose(mae, 0.2))