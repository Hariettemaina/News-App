class Source:
    '''
    Class that defines Source objects
    '''
    def __init__(self,id,name,description):
        '''
        __init__ method to define the properties of a Source object
        Args:
            id : The unique identifier for the news source. 
            name : The display-friendly name of the news source.
            description : A brief description of the news source and what area they specialize in.
        '''
        self.id = id
        self.name = name
        self.description = description

class Article:
    '''
    Class that defines Article objects
    '''
    def __init__(self,source,title,urlToImage,description,urlToArticle,publishedAt):
        '''
        __init__ method to define the properties of an Article object
        Args:
            source : The identifier of the source requested.
            title : The headline or title of the article.
            urlToImage : The URL to a relevant image for the article.
            description : A description or preface for the article.
            urlToArticle : The direct URL to the content page of the article.
            publishedAt : The date for the article, in UTC (+0).
        '''
        self.source = source
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.urlToArticle = urlToArticle
        self.publishedAt = publishedAt

    @classmethod
    def publish_date_format(cls,publishedAt):
        '''
        Function that changes the format of the date from UTC to display-friendly format
        Args:
            publishedAt : The date for the article, in UTC (+0).
        '''
        date_to_display = publishedAt[:10]

        return date_to_display