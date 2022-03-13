import requests
from time import sleep
from parsel import Selector
from .database import create_news


# Requisito 1
def fetch(url: str):
    sleep(1)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None
    except requests.Timeout:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content: str):
    page_selector = Selector(text=html_content)
    links = page_selector.css(
      'h3 a.tec--card__title__link::attr(href)').getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content: str):
    html = Selector(text=html_content)
    url = html.css(
      'a.z--mx-auto::attr(href)').get()

    if url:
        return url
    else:
        return None


# Requisito 4
def scrape_noticia(html_content: str):
    page = Selector(html_content)
    url = page.css("head link[rel=canonical]::attr(href)").get()
    title = page.css("h1.tec--article__header__title::text").get()
    timestamp = page.css("time#js-article-date::attr(datetime)").get()

    author__info__link = page.css(".tec--author__info__link::text").get()
    author_timestamp = page.css("div.tec--timestamp__item a::text").get()
    author_info = page.css("div.tec--author__info p.z--font-bold::text").get()

    if author__info__link:
        author = author__info__link
    elif author_timestamp:
        author = author_timestamp
    else:
        author = author_info

    shares_count = page.css(".tec--toolbar__item::text").get()
    comments_count = page.css("#js-comments-btn::attr(data-count)").get()
    summary = "".join(page.css(
        ".tec--article__body > p:first-child *::text").getall())
    sources = [item.strip() for item in page.css(
        "div.z--mb-16 div a::text").getall()]
    category = [item.strip() for item in page.css(
        "#js-categories a::text").getall()]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": author.strip() if author else None,
        "shares_count": int(
            shares_count.split()[0]) if shares_count else 0,
        "comments_count": int(comments_count) if comments_count else 0,
        "summary": summary,
        "sources": sources,
        "categories": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = fetch("https://www.tecmundo.com.br/novidades")
    # Adiciona links encontrados
    links = scrape_novidades(url)
    while len(links) < amount:
        next_page = scrape_next_page_link(url)
        page = fetch(next_page)
        # Adiciona mais links até chegar no amount
        links.extend(scrape_novidades(page))
    # Começa sem noticias
    whole_content = []
    # Adiciona os objetos no array de noticias
    for link in links[:amount]:
        page = fetch(link)
        news = scrape_noticia(page)
        whole_content.append(news)

    create_news(whole_content)
    return whole_content
