from urllib import request


def call_url(url):
    """
    A function to build our payload, our payload will be comma
    seperated numbers. For this test it will be list(range(10000001))
    """

    # first of we need to build the payload of
    # data to be shipped to API
    payload = str(list(range(10000001)))[1:-1].replace(" ", "")

    # encode the payload for transport to api
    params = "numbers={}".format(payload).encode('utf-8')

    # send a request to the API endpoint
    req = request.Request(url, data=params)
    response = request.urlopen(req)

    # read and return response from API endpoint
    return response.read(response.length).decode('utf-8')


# will call the API and log our output to display to user
response = call_url(url='http://localhost:5000/total')
print(response)
