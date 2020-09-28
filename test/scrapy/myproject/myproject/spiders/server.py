from typing import List
from elasticsearch import Elasticsearch
from bottle import route, run, request, template

es = Elasticsearch(["localhost:9200"])
@route("/")
def index():
    query = request.query.q
    pages = search_pages(query) if query else []

    # return template("search", query=query, pages=pages)

def search_pages(query:str)->List[dict]:
    result = es.search(index="pages", body={
        "query": {
            "simple_query_string": {
                "query":query,
                "fields":["title^5", "content"],
                "default_operator":"and"
            }
        },
        "hightlight": {
            "fields": {
                "content": {
                    "frament_size":150,
                    "number_of_framents":1,
                    "no_match_size":150
                }
            }
        }
    })
    return result["hits"]["hits"]


if __name__ == "__main__":
    run(host='0.0.0.0', port=8000, debug=True, reloader=True)
