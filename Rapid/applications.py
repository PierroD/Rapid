from fastapi import FastAPI
from fastapi.routing import Mount
from starlette.types import ASGIApp

class Rapid(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    def mount_app(self, path: str, app: ASGIApp, include_sub_routes: bool | None = False, name: str | None = None):
        self.mount(path, app, name)
        if include_sub_routes:
            for object in self.routes:
                if isinstance(object, Mount):
                    if object.app is not None and object.app.router is not None:
                        self.include_router(object.app.router, prefix=object.path)
