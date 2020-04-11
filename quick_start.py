from soco_core.soco_client import SOCOClient
from soco_core.examples import load_example_doc_data

if __name__ == '__main__':
    ADMIN_API_KEY = '965c966a-07db-4f3b-8f26-56293b21c3c9'
    a_client = SOCOClient(ADMIN_API_KEY)

    # add data
    print("Add some data to the index")
    docs = load_example_doc_data(['mr-sun.json', 'technology.json'])
    a_client.delete_data()
    a_client.add_data(docs)
    print("Read {} documents".format(len(a_client.read_data())))

    print("Publish the index")
    a_client.abort(sync=False)
    a_client.publish()

    print("Make a query")
    QUERY_API_KEY = '8228868a-4b50-4b4b-8a1c-8a010122cf8b'
    q_client = SOCOClient(QUERY_API_KEY)
    responses = q_client.query({"query": "what is the distance from earth to sun?", "n_best": 10})
    SOCOClient.pprint(responses)
