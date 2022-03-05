import json
from bs4            import BeautifulSoup
from urllib.parse   import quote_plus
from urllib.request import urlopen

wikipediaSearchUrl = "https://pt.wikipedia.org/w/rest.php/v1/search/title?q={}&limit=1"
wikipediaPageUrl   = "https://pt.wikipedia.org/wiki/{}"

def filterKey(page):
    return page["key"]

# Recebe o termo a ser buscado e retorna a chave a ser acessada na wikipedia
def getPageKey(topic):
    topic     = quote_plus(topic)

    pageTxt   = urlopen(wikipediaSearchUrl.format(topic)).read().decode('utf-8')
    pages     = json.loads(pageTxt)["pages"]

    pagesList = list(map(filterKey, pages))

    if (len(pagesList) != 0):
        return pagesList[0]

    raise Exception('Not found topic "{}"'.format(topic))

# Recebe a chave e retorna o conteúdo existente na página solicitada
def getPageHtml(key):
    html = urlopen(wikipediaPageUrl.format(key))
    return BeautifulSoup(html, 'html.parser')

# Recebe o conteúdo da página e retorna apenas o primeiro parágrafo
def getFirstParagraph(bs):
    div = bs.find('div', id="mw-content-text").div
    return div.p.text

# Recebe uma string e retorna a mesma sem artigos
def removeArticles(topic):
    artigos = ['a', 'o', 'um', 'uma', 'uns', 'umas', 'as', 'os', 'numa', 'num']
    topicAsArray = topic.split(' ')
    topicAsArray = [word for word in topicAsArray if word not in artigos and word != '']
    topic = ' '.join(topicAsArray)
    return topic

def wiki_get(topic):
    print(topic)
    topic = removeArticles(topic)
    print(topic)
    try:
        key            = getPageKey(topic)
        bs             = getPageHtml(key)
        firstParagraph = getFirstParagraph(bs)

        return firstParagraph
    except:
        return 'Não achei nada sobre isso.'

    
