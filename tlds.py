from bs4 import BeautifulSoup
import requests


def get_tlds():
    url = 'https://support.google.com/domains/answer/6010092'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tlds = []
    for td in soup.find_all('td'):
        text = td.text.strip()
        if text.startswith('.'):
            tlds.append(text)

    return tlds


def get_clever_tlds():
    tlds = get_tlds()
    clever_tlds = {}

    for tld in tlds:
        clever_tlds[tld] = []

    with open('/usr/share/dict/words', 'r') as words:
        for word in words:
            word = word.strip()

            for tld in tlds:
                naked_tld = tld.strip('.')

                # 2-letter TLDs are not interesting. Exclude them.
                if len(naked_tld) > 2 and word.endswith(naked_tld) and word != naked_tld:
                        clever_tlds[tld].append(word)

    return clever_tlds
