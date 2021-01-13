from typing import Dict, Callable, Iterable


class API:
    def __call__(self, environ: Dict, start_response: Callable) -> Iterable:
        response_body = b"Hello, world"
        status = "200 0K"
        start_response(status, headers=[])
        return iter([response_body])
