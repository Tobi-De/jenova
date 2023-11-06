from __future__ import annotations

import inspect
from pathlib import Path

from jinja2 import Environment
from jinja2 import FileSystemLoader
from parse import parse
from requests import session as RequestsSession
from webob import Request
from whitenoise import WhiteNoise
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter

from .middleware import Middleware
from .response import Response


class API:
    def __init__(self, templates_dir: Path, static_dir: Path):
        self.routes = {}

        self.templates_env = Environment(
            loader=FileSystemLoader(templates_dir.resolve())
        )

        self.exception_handler = None

        self.whitenoise = WhiteNoise(self.wsgi_app, root=static_dir)

        self.middleware = Middleware(self)

    def __call__(self, environ: dict, start_response: callable) -> Response:
        path_info = environ["PATH_INFO"]
        if path_info.startswith("/static"):
            environ["PATH_INFO"] = path_info[len("/static") :]
            return self.whitenoise(environ, start_response)
        return self.middleware(environ, start_response)

    def wsgi_app(self, environ: dict, start_response: callable):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def add_middleware(self, middleware_cls: type):
        self.middleware.add(middleware_cls)

    def route(self, path: str, allowed_methods: list[str] | None = None):
        def wrapper(handler):
            self.add_route(path, handler, allowed_methods)
            return handler

        return wrapper

    def add_route(
        self, path: str, handler: callable, allowed_methods: list[str] | None = None
    ) -> None:
        assert path not in self.routes, "Such route already exists."

        if allowed_methods is None:
            allowed_methods = ["get", "post", "put", "patch", "delete", "options"]

        self.routes[path] = {"handler": handler, "allowed_methods": allowed_methods}

    def default_response(self, response: Response) -> None:
        response.status_code = 404
        response.text = "Not found."

    def handle_request(self, request: Request) -> Response:
        response = Response()
        handler_data, kwargs = self.find_handler(request_path=request.path)

        try:
            if handler_data is not None:
                handler = handler_data["handler"]
                allowed_methods = handler_data["allowed_methods"]
                if inspect.isclass(handler):
                    handler = getattr(handler(), request.method.lower(), None)
                    if handler is None:
                        raise AttributeError(f"Method {request.method} not allowed")
                elif request.method.lower() not in allowed_methods:
                    raise AttributeError("Method not allowed", request.method)
                handler(request, response, **kwargs)
            else:
                self.default_response(response)
        except Exception as e:
            if self.exception_handler is None:
                raise e
            else:
                self.exception_handler(request, response, e)
        return response

    def find_handler(self, request_path: str) -> tuple[dict | None, dict | None]:
        for path, handler_data in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler_data, parse_result.named
        return None, None

    def template(self, template_name: str, context: dict | None = None) -> str:
        context = context or {}

        return self.templates_env.get_template(template_name).render(context)

    def test_session(self, base_url="http://testserver"):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session

    def add_exception_handler(self, exception_handler: callable) -> None:
        self.exception_handler = exception_handler
