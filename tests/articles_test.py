import unittest
from models import Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('MIKE ISAAC and TAYLOR LORENZ','Sumter mirrors SC, nation in COVID-19\'s disproportionate impact on African-Americans','2020-09-12T01:20:00Z','https://edition.cnn.com/','https://www.nytimes.com/article/wildfires-photos-california-oregon-washington-state.html','News and buzz')

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Articles))
        
if __name__ == '__main__':
    unittest.main()        