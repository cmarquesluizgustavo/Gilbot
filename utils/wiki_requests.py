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

def wiki_get(topic):
    key            = getPageKey(topic)
    bs             = getPageHtml(key)
    firstParagraph = getFirstParagraph(bs)

    return firstParagraph
