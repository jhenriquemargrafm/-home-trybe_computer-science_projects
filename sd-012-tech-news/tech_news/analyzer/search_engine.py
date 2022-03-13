from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    # https://stackoverflow.com/questions/26699885/how-can-i-use-a-regex-variable-in-a-query-for-mongodb
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    title = search_news({"title": {"$regex": title, "$options": "i"}})

    news = []
    for news_information in title:
        current_news = (news_information["title"], news_information["url"])
        news.append(current_news)
    return news


# Requisito 7
def search_by_date(date):
    formatted_news = []
    try:
        # https://www.programiz.com/python-programming/datetime/strptime
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')
    news = search_news({'timestamp': {'$regex': date}})
    for news_information in news:
        current_news = (news_information['title'], news_information['url'])
        formatted_news.append(current_news)
    return formatted_news


# Requisito 8
def search_by_source(source):
    formatted_news = []
    # https://docs.mongodb.com/manual/reference/operator/query/regex/
    news = search_news({'sources': {'$regex': source, '$options': 'i'}})
    for news_information in news:
        current_news = (news_information['title'], news_information['url'])
        formatted_news.append(current_news)
    return formatted_news


# Requisito 9
def search_by_category(category):
    formatted_news = []
    news = search_news({'categories': {'$regex': category, '$options': 'i'}})
    for news_information in news:
        current_news = (news_information['title'], news_information['url'])
        formatted_news.append(current_news)
    return formatted_news
