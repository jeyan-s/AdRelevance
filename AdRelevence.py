from KeywordExtractor import KeywordExtractor
from Aggregator import Aggregator
from HistoryCache import HistoryCache
import Scraper

class AdRelevence:
    def __init__(self, HistoryURLs, KeywordsPerSite = 3, CacheSize = 10):
        try: KeywordsPerSite = int(KeywordsPerSite)
        except: KeywordsPerSite = 3 
        try: CacheSize = int(CacheSize)
        except: CacheSize = 10
        self.HistoryURLs = HistoryURLs
        self.KeywordExtractor = KeywordExtractor(KeywordsPerSite)
        self.HistoryCache = HistoryCache(CacheSize)

    def GetReleventAd(self):
        for URL in self.HistoryURLs:
            Content = Scraper.Scrape(URL)
            SemanticKeywords = []
            for x in Content:
                SemanticKeywords += Aggregator(x).GetSemanticKeywords()
            RequiredKeywords = self.KeywordExtractor.GetRequiredKeywords(SemanticKeywords)
            self.HistoryCache.AddHistory(RequiredKeywords)

        return self.HistoryCache.MostFrequentHistory()