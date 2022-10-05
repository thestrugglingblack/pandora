import logging
import pymongo

logger = logging.getLogger(__name__)

mongo_client = pymongo.MongoClient('mongodb://localhost:27017')

curr_dbs = mongo_client.list_database_names()

'''
Verifying Mongo DB and Collection.
'''
if 'pandora_db' in curr_dbs:
    logger.info('Database name "pandora_db" was found...')
    pandora_db = mongo_client['pandora_db']
    curr_col = pandora_db.list_collection_names()
    if 'pandora' in curr_col:
        logger.info('Found "pandora" collection...')
        pass
    else:
        logger.info('Creating "pandora" collection...')
        pandora_col = pandora_db['pandora']
    pass
else:
    logger.info('Creating "pandora_db" database...')
    mongo_client['pandora_db']






