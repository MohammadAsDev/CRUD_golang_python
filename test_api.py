import requests
from tqdm.auto import tqdm

"""
    This is a simple code to test the performance
"""


HOST = "http://127.0.0.1"   # running tests on localhost
PYTHON_PORT = 8000          # django by default use 8000    
GOLANG_PORT = 5000          # i like to 5000 for golang apps

"""
    CRUD API actions
"""
actions = {
    "CREATE" : {    # Create a new product
        "path" : "products/",     
        "method" : "POST"
    },
    "UPDATE" : {    # Update a product
        "path" : "products/{}/",
        "method" : "PUT",
    },   
    "DELETE" : {    # Delete a product
        "path" : "products/{}/",
        "method" : "DELETE"
    },
    "READ" : {      # Get a product
        "path" : "products/{}/",
        "method" : "GET"
    },
    "LIST" : {      # List all products
        "path" : "products/",
        "method" : "GET"
    }
}


"""
    This is a simple http client, to deal with API
"""
class HttpClient:
    def __init__(self, host : str , port : int) -> None:
        self._host = host
        self._port = port
        self._url = host+":"+str(port)+"/"

    def create_product(self, product_data : dict) -> float:
        create_path = self._url + actions["CREATE"]["path"]
        response = requests.post(
            url=create_path , 
            json=  product_data
        )
        return response.elapsed.total_seconds()
    
    def get_product(self, id : int):
        product_path = self._url + actions["READ"]["path"].format(id)
        repsonse = requests.get(product_path)
        return repsonse.elapsed.total_seconds()

    def update_product(self , id : int, product_data : dict):
        update_path = self._url + actions["UPDATE"]["path"].format(id)
        response = requests.put(
            url=update_path , 
            json= product_data
        )
        return response.elapsed.total_seconds()
    
    def delete_product(self, id : int):
        delete_path = self._url + actions["DELETE"]["path"].format(id)
        response = requests.delete(delete_path)
        return response.elapsed.total_seconds()

    def list_products(self) -> list:
        list_path = self._url + actions["LIST"]["path"]
        response = requests.get(list_path)
        return response.elapsed.total_seconds()

def generate_products(n_product) -> list:
    products = []
    print("Generating {} products:".format(n_product))
    for i in tqdm(range(n_product)):
        products.append({
            "product_name" : "product_{}".format(i),
            "product_description" : "product description {}".format(i)
        })

    return products

"""
    TODO Refactor testing functions bellow
"""
def create_test(products : list, python_client : HttpClient, golang_client : HttpClient) -> tuple:
    golang_create_time = 0.0
    python_create_time = 0.0

    for product in tqdm(products):
        golang_time = golang_client.create_product(product)
        python_time = python_client.create_product(product)

        python_create_time += python_time
        golang_create_time += golang_time

    return (python_create_time , golang_create_time)

def update_test(products : list, python_client : HttpClient, golang_client : HttpClient) -> tuple:
    golang_update_time = 0.0
    python_update_time = 0.0

    pbar = tqdm(total=len(products))
    for id , product in enumerate(products):
        golang_time = golang_client.update_product(id + 1, product)
        python_time = python_client.update_product(id + 1, product)

        python_update_time += python_time
        golang_update_time += golang_time

        pbar.update(1)
    pbar.close()

    return (python_update_time , golang_update_time)

def delete_test(n_products : int, python_client : HttpClient, golang_client : HttpClient) -> tuple:
    golang_delete_time = 0.0
    python_delete_time = 0.0

    for product_id in tqdm(range(n_products)):
        golang_time = golang_client.delete_product(product_id + 1)
        python_time = python_client.delete_product(product_id + 1)

        python_delete_time += python_time
        golang_delete_time += golang_time

    return (python_delete_time , golang_delete_time)

def read_test(n_products : int, python_client : HttpClient, golang_client : HttpClient) -> tuple:
    golang_read_time = 0.0
    python_read_time = 0.0

    for product_id in tqdm(range(n_products)):
        golang_time = golang_client.get_product(product_id + 1)
        python_time = python_client.get_product(product_id + 1)

        python_read_time += python_time
        golang_read_time += golang_time

    return (python_read_time , golang_read_time)

def list_test(python_client : HttpClient, golang_client : HttpClient) -> tuple:
    golang_list_time = golang_client.list_products()
    python_list_time = python_client.list_products()
    return python_list_time, golang_list_time


"""
    The main operation
"""
def main():
    n_products = 1000   # number of products that i will deal with.
    products = generate_products(n_products)
    
    golang_client = HttpClient(host=HOST , port=GOLANG_PORT)
    python_clinet = HttpClient(host=HOST , port=PYTHON_PORT)

    print("Testing 'Create products' operation: ")
    python_avg_create, golang_avg_create = create_test(products=products , python_client=python_clinet , golang_client=golang_client)
    print("Python time: {}\tGolang time: {}".format(python_avg_create, golang_avg_create))

    print("Testing 'Read a product' operation: ")
    python_avg_create, golang_avg_create = read_test(n_products=n_products , python_client=python_clinet, golang_client=golang_client)
    print("Python time: {}\tGolang time: {}".format(python_avg_create, golang_avg_create))

    print("Testing 'Update products' operation: ")
    python_avg_create, golang_avg_create = update_test(products=products, python_client=python_clinet, golang_client=golang_client)
    print("Python time: {}\tGolang time: {}".format(python_avg_create, golang_avg_create))
    
    print("Testing 'List products' operation: ")
    python_avg_create, golang_avg_create = list_test(python_client=python_clinet, golang_client=golang_client)
    print("Python time: {}\tGolang time: {}".format(python_avg_create, golang_avg_create))

    print("Testing 'Delete products' operation: ")
    python_avg_create, golang_avg_create = delete_test(n_products= n_products, python_client=python_clinet, golang_client=golang_client)
    print("Python avg time: {}\tGolang avg time: {}".format(python_avg_create, golang_avg_create))
    

if __name__ == "__main__":
    main()