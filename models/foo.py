from .rbac import RBACBase

class OutputFoo(RBACBase):
    _path = __name__
    f1: int = None
    f2: str = None

    def print_foo_module(cls):
        print(f"module: {cls.__module__} with class {cls.__name__}")
