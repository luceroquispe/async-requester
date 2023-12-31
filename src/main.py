from loguru import logger
from src.http_requests import Requests, RequestInfo

# list the requests
requests = [
    RequestInfo("GET", "get"),
    RequestInfo(method="POST", path="post", body={"test": "example"}),
    RequestInfo(method="GET", path="get", params="test"),
]

if __name__ == "__main__":
    req = Requests()
    responses = req.client_requests(requests)
    for response in responses:
        logger.info(response.json())
