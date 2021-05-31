#pacotes
import requests
import re
from bs4 import BeautifulSoup
#ficheiros

url_base = 'http://vocabularies.unesco.org/browser/thesaurus/en/search?clang=en&q='
url_base_fim = '&vocabs='
bs_page = None
resultados = 0

def get_page(termo):
    """
    Faz pedido ao requests para enviar um request HTTPS para depois dar ao BEAUTIFUL SOUP para recolher os elementos
    :param termo:
    :return:
    """
    termo = re.sub(r"\s+", "+", termo)
    r = requests.get(url_base+termo+url_base_fim)
    bs_page = BeautifulSoup(r.content, 'html.parser')
    resultados = get_result_number(bs_page)
    lista_definicoes = get_definitions(bs_page)
    return lista_definicoes
def get_result_number(webpage):
    """
    encontrar o elemento onde a página indica o numero de resultados
    :param webpage: conteudo da webpage devolvido pelo BS
    :return:
    """
    resultados = webpage.find('div', class_='search-count')
    resultados = resultados.get_text()
    num_resul = filter(str.isdigit, resultados)
    resultados = "".join(num_resul)
    return int(resultados, base=10)

def get_definitions(webpage):

    lista_definicoes = []
    a = None
    for el in webpage.find_all('div', class_='search-result'):
        a = el.get_text()
        lista_definicoes.append(a)

    return lista_definicoes

