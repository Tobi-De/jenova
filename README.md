# JENOVA

[![pypi](https://badge.fury.io/py/jenova.svg)](https://pypi.org/project/jenova/)
[![Docs: Sphinx](https://img.shields.io/badge/sphinx-docs-blue.svg)](https://tobi-de.github.io/jenova)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Tobi-De/jenova/blob/main/LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


> [!Note]
> Learning experience, nothing serious

The goal of this project is to understand the ins and outs of how a web framework works on a deeper level. I'm also using this project as a playground to build common components found in the web framework ecosystem, such as forms, ORM, etc. After building the core of the framework, I will attempt to implement, mostly from scratch, the parts that interest me the most. After completing my own implementation, I plan to replace it with open-source packages that I like or want to try.

## Features

In brackets are the potential open source packages to use once my own implementation is complete.

- [ ] The core of the framework, built around the WSGI standard
- [ ] Implement the ASGI standard, mixing and matching sync and async views should be possible
- [ ] A Dependency injection system based on type hints ([di](https://github.com/adriangb/di/))
- [ ] Orm and query builder ([pydantic](https://github.com/samuelcolvin/pydantic/) + [asyncpg](https://github.com/samuelcolvin/pydantic/) / [SQLModel](https://github.com/tiangolo/sqlmodel) / [orm](https://github.com/encode/orm))
- [ ] Postgres Database driver
- [ ] A django-like form framework ([pydantic](https://github.com/samuelcolvin/pydantic/) / [typesystem](https://github.com/encode/typesystem) / [deform](https://github.com/Pylons/deform))
- [ ] First class Integration with [edgedb](https://github.com/edgedb/edgedb)
- [ ] Authentication with support for oauth2 (???) -  https://datatracker.ietf.org/doc/html/rfc6749#section-4.1 - https://oauth.net/2/
- [ ] Messages / notifications system (???)
- [ ] Open Api generation  (???)
- [ ] Server sent events (???)
- [ ] Admin interface (???)
- [ ] Media storage engine (???)
- [ ] Email Management (???)
- [ ] Websockets (???)
- [ ] Templating language, with htmx support
- [ ] Django-like Management commands ([typer](https://github.com/tiangolo/typer) + [rich](https://github.com/Textualize/rich))
- [ ] Settings management ([pydantic](https://github.com/samuelcolvin/pydantic/) / [hydra](https://github.com/facebookresearch/hydra))
- [ ] A web server (something wih goroutines ???)

## Misc

- [Why You Should Learn To Program The Hard Way](https://www.youtube.com/watch?v=Qf56xUKbx24)
- [Building a python interpreter and compiler](https://mathspp.com/blog/tag:bpci)
- [Build your own http server](https://app.codecrafters.io/courses/http-server/overview)
- https://defn.io/2018/02/25/web-app-from-scratch-01/
- https://joaoventura.net/blog/2017/python-webserver/
