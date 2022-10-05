import logging

import meilisearch

logger = logging.getLogger(__name__)

meili_client = meilisearch.client('http://localhost:7700')

def index_data(json):
    logger.info('Indexing data...')
    # Example
    # client.index('movies').add_documents(movies)


def search_query(query):
    logger.info('Searching data...')
    # Example
    # dclient.index('movies').search(query)
