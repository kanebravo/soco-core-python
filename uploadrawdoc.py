from soco_core.soco_client import SOCOClient
from soco_parser.doc_api import DocAPI


if __name__ == '__main__':
    QUERY_API_KEY = '8228868a-4b50-4b4b-8a1c-8a010122cf8b'
    ADMIN_API_KEY = '965c966a-07db-4f3b-8f26-56293b21c3c9'

    q_client = SOCOClient(QUERY_API_KEY)
    a_client = SOCOClient(ADMIN_API_KEY)
    d_client = DocAPI(ADMIN_API_KEY)

    print("## Add some data to the index")   
    # url = "https://convmind-images.s3.us-east-2.amazonaws.com/pdfview/Fresh_Start_Program_Summary.pdf"
    # parsed_data = client.parse(file_url=url) #parse a url 
    data = d_client.parse_local_file("resources/1906.09308.pdf","en") 
    frames = DocConvert.document_to_frames(data, "en")
    a_client.replace_index(frames)

    print("## Wait for indexing is done ... ")
    a_client.wait_for_ready(check_frequency=2, verbose=False)

    print("## Make a query")
    responses = q_client.query("how many images", 10)
    SOCOClient.pprint(responses)