import inspect
import os
from typing import Dict, Callable

from jinja2 import Environment, FileSystemLoader
from parse import parse
from requests import session as RequestsSession
from webob import Request, Response
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter


class API:
    def __init__(self, templates_dir="templates"):
        self.routes = {}

        self.templates_env = Environment(
            loader=FileSystemLoader(os.path.abspath(templates_dir))
        )

    def __call__(self, environ: Dict, start_response: Callable) -> Response:
        request = Request(environ=environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def route(self, path: str):
        def wrapper(handler):
            self.add_route(path, handler)
            return handler

        return wrapper

    def add_route(self, path, handler):
        assert path not in self.routes, "Such route already exists."
        self.routes[path] = handler

    def default_response(self, response: Response):
        response.status_code = 404
        response.text = "Not found."

    def handle_request(self, request: Request) -> Response:
        response = Response()
        handler, kwargs = self.find_handler(request_path=request.path)
        if handler is not None:
            if inspect.isclass(handler):
                handler = getattr(handler(), request.method.lower(), None)
                if handler is None:
                    raise AttributeError(f"Method {request.method} not allowed")
                handler(request, response, **kwargs)
            else:
                handler(request, response, **kwargs)
        else:
            self.default_response(response)
        return response

    def find_handler(self, request_path: str):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None

    def template(self, template_name, context=None):
        context = context or {}

        return self.templates_env.get_template(template_name).render(context)

    def test_session(self, base_url="http://testserver"):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session

