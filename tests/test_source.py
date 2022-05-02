import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Source class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.news_source = Source('abc-news-au','ABC News (AU)', 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.')

    def test_instance(self):
        '''
        Test case to check if self.news_source is an instance of Source
        '''
        self.assertTrue( isinstance( self.news_source, Source ) )

    def test_init(self):
        '''
        Test case to check if the Source class is initialised
        '''
        self.assertEqual( self.news_source.id, 'abc-news-au')
        self.assertEqual( self.news_source.name, 'ABC News (AU)')
        self.assertEqual( self.news_source.description, 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.')
