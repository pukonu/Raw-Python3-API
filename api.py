import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


class SimpleRequestHandler(BaseHTTPRequestHandler):
    def content_factory(self, content, status=200, header="text/html"):
        """
        A function to build a response to a request caller
        """
        self.send_response(200)
        self.send_header("Content-Length", len(content))
        self.send_header("Content-Type", header)
        self.end_headers()
        self.wfile.write(bytes(str("%s%s" % (content, "\n")).encode('utf-8')))

    def sum_value(self, request_data):
        """
        A function to sum all the values extracted from the request object
        """
        request_data = parse_qs(request_data.decode('utf-8'))

        # we'll try to extract the number variable from the post data
        # but return a NaN if we can't find it
        try:
            arr = list(map(int, request_data['numbers'][0].split(",")))
            total = sum(arr)
        except KeyError:
            total = "NaN"

        return total

    def do_GET(self):
        """
        when a get request is made just return this string so
        the user knows who to query this API
        """

        content = """You have reached the home page, why not try running
        a post call with comma seperated numbers to this endpoint<b>/total</b>
        """
        self.content_factory(content, status=200)

    def do_POST(self):
        """
        A function to sum data input will be the only value to be returned
        """

        # lets receive the request data from the caller
        request_data = \
            self.rfile\
                .read(int(self.headers['Content-Length']))

        # will only return the sum if the endpoint is /total
        current_path = self.path[1:]
        if current_path.startswith("total"):
            result = {
                "total": self.sum_value(request_data)
            }
            # we'll encode data as json for transport
            content = json.dumps(result)
        else:
            content = "You've probably posted to a wrong endpoint'"

        # lets return a json response
        self.content_factory(content, status=200, header="application/json")

    def log_message(self, format, *args):
        return


def run(
        server_class=HTTPServer,
        handler_class=SimpleRequestHandler,
        should_shutdown=False):
    """
    A simple simple API to sum all input sent in the structure
    below
    POST DATA >>> numbers=1,2,3,.....,n
    """

    # start server and listen on port 5000 forever
    server_address = ('0.0.0.0', 5000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
