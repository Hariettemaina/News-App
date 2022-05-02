import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Article class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_article = Article("Scott Morrison and Anthony Albanese are disaster prepping for tomorrow's likely election campaign interest rate hike - ABC News")
    
    def test_instacnce(self):
        '''
        Test case to check if self.new article is an intance of Article
        '''
        self.assertTrue( isinstance( self.new_article, Article ) )
        
    def test_init(self):
        '''
        Test case to check if the Article class is initialised
        '''
        self.assertEqual( self.new_article.source, 'ABC News (AU)')
        self.assertEqual( self.new_article.title, "Scott Morrison and Anthony Albanese are disaster prepping for tomorrow's likely election campaign interest rate hike - ABC News")
        self.assertEqual( self.new_article.urlToImage, "https://live-production.wcms.abc-cdn.net.au/33f0ed4265c51b2d24d6c3b9a2e594a9?impolicy=wcms_crop_resize&cropH=450&cropW=800&xPos=0&yPos=75&width=862&height=485")
        self.assertEqual( self.new_article.description, "Such is the pressure for governments to hold a hose in the housing conflagration, it matters not that they're squirting kerosene, writes Annabel Crabb.")
        self.assertEqual( self.new_article.urlToArticle, 'https://www.abc.net.au/news/2022-05-02/election-2022-morrison-albanese-rba-interest-rate-rise/101031740')
        self.assertEqual( self.new_article.publishedAt, "2022-05-02T07:55:08Z")

    def test_publish_date_format(self):
        '''
        Test case to check if UTC date format is converted to a display-friendly format
        '''
        display_friendly_format = self.new_article.publish_date_format(self.new_article.publishedAt)
        self.assertEqual( display_friendly_format, '2022-05-02')
        

        
        