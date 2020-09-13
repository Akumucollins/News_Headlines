import unittest
from app.models import Source

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('CNN','CNN News','View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN','https://www.nytimes.com/2020/09/11/us/fires-oregon-california-washington.html','Business News','BBC News','en')

    def test_instance(self):
        '''
        Test to check creation of new article Sources instance
        '''
        self.assertTrue(isinstance(self.new_source,Source))
