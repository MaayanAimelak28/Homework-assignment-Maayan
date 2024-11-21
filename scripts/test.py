# Import the requests library to send HTTP requests
import requests

# This function test the web server by sending a GET request to the specified IP
def test_web_server(ip):
    url = f"http://{ip}"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Hello from" in response.text

# This function test the nginx load balancer by sending a GET request to the Nginx IP
def test_nginx():
    url = "http://192.168.56.24"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Hello from" in response.text

# Runs the tests
if __name__ == "__main__":
    print("Testing the web servers: ")
    test_web_server("192.168.56.19")
    test_web_server("192.168.56.20")
    print("Testing Nginx load balancer: ")
    test_nginx()
    print("All tests passed!")
