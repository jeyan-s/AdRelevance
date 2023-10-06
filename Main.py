from AdRelevence import AdRelevence

if __name__ == "__main__":
    HistoryURLs = ["https://www.parentcircle.com/moral-stories-for-kids-in-english-for-competition/article", "https://www.geeksforgeeks.org/python-programming-language/", "https://www.geeksforgeeks.org/types-software-testing/", "https://www.geeksforgeeks.org/python-programming-language/", "https://www.geeksforgeeks.org/python-programming-language/", "https://www.parentcircle.com/moral-stories-for-kids-in-english-for-competition/article"]
    # HistoryURLs = ["dfgh"]
    AdRelevence = AdRelevence(HistoryURLs, 5, 100)
    RecommendedAdTags = AdRelevence.GetReleventAd()
    print(*RecommendedAdTags, sep = "\n")