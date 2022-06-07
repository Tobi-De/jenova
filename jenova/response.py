from __future__ import annotations

import json
from dataclasses import dataclass

import webob


@dataclass(kw_only=True, slots=True)
class Response:
    json: dict | None = None
    html: str | None = None
    text: str | None = None
    content_type: str | None = None
    body: bytes = b""
    status_code: int = 200

    def __call__(self, environ: dict, start_response: callable) -> webob.Response:
        self.set_body_and_content_type()
        response = webob.Response(
            body=self.body, content_type=self.content_type, status=self.status_code
        )
        return response(environ, start_response)

    def set_body_and_content_type(self):
        if self.json is not None:
            self.body = json.dumps(self.json).encode("UTF-8")
            self.content_type = "application/json"

        if self.html is not None:
            self.body = self.html.encode()
            self.content_type = "text/html"

        if self.text is not None:
            self.body = self.text
            self.content_type = "text/plain"
