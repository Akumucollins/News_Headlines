
import unittest
from app.models import Category

class CategoryTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Category class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_category = Category('MIKE ISAAC and TAYLOR LORENZ','Sumter mirrors SC, nation in COVID-19\'s disproportionate impact on African-Americans','2020-09-12T01:20:00Z','https://edition.cnn.com/','https://www.nytimes.com/article/wildfires-photos-california-oregon-washington-state.html','News and buzz')

    def test_instance(self):
        '''
        Test to check creation of new Category instance,(is True)
        '''
        self.assertTrue(isinstance(self.new_category,Category))
        