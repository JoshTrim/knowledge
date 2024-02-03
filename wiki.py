# add wikipedia lookup for each node label
# docs: https://wikipedia.readthedocs.io/en/latest/
import wikipedia

def get_wikipedia_url(topic):
    # query = wikipedia.suggest(topic)
    # print(query)
    # if query:
    res = wikipedia.page(topic)
    return res.url
