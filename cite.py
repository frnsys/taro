import requests
import lxml.html

BASE_URL = 'https://scholar.google.com/scholar'

def get_citation(title):
    """Given a paper title, attempts to get citation
    strings for that paper from Google Scholar."""
    # Search for the paper by title
    resp = requests.get(BASE_URL, params={'q': title})
    html = lxml.html.fromstring(resp.content)
    result_els = html.cssselect('.gs_r')
    if not result_els:
        return None

    # Only consider the first match
    result_el = result_els[0]

    # result_title = result_el.cssselect('.gs_rt a')[0].text

    # Request the citations
    result_id = result_el.attrib['data-cid']
    resp = requests.get(BASE_URL, params={
        'q': 'info:{}:scholar.google.com/'.format(result_id),
        'output': 'cite'
    })
    html = lxml.html.fromstring(resp.content)
    citations = {}
    for format_el, citation_el in zip(html.cssselect('th'), html.cssselect('td .gs_citr')):
        format = format_el.text
        citation = citation_el.text_content()
        citations[format] = citation
    return citations
