# JENOVA

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Tobi-De/jenova/blob/master/LICENSE)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The goal of this project is to understand the ins and outs of how a web framework works on a deeper level.
I'm also using this project as a playground to try to build common components found in the web framework ecosystem 
like forms, orm, etc. After building the core of the framework, I will try to implement from scratch (mostly) 
the part that interests me the most. After building my own implementation, I plan to swap it with open source packages
that I liked or wanted to try.

## Todos

In brackets are the potential open source packages to use once my own implementation is complete.

- [ ] The core of the framework, built around the WSGI standard
- [ ] Implement the ASGI standard, mixing and matching sync and async views should be possible
- [ ] A Dependency injection system based on type hints ([di](https://github.com/adriangb/di/))
- [ ] Orm and query builder ([pydantic](https://github.com/samuelcolvin/pydantic/) + [asyncpg](https://github.com/samuelcolvin/pydantic/) / [SQLModel](https://github.com/tiangolo/sqlmodel) / [orm](https://github.com/encode/orm))
- [ ] A django-like form framework ([pydantic](https://github.com/samuelcolvin/pydantic/) / [typesystem](https://github.com/encode/typesystem) / [deform](https://github.com/Pylons/deform))
- [ ] First class Integration with [edgedb](https://github.com/edgedb/edgedb)
- [ ] Authentication with support for oauth2 (???)
- [ ] Messages / notifications system (???)
- [ ] Open Api generation  (???)
- [ ] Server sent events (???) 
- [ ] Admin interface (???)
- [ ] Media storage engine (???)
- [ ] Email Management (???)
- [ ] Websockets (???)
- [ ] Django-like Management commands ([typer](https://github.com/tiangolo/typer))
