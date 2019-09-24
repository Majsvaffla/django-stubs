from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
from functools import wraps as wraps  # noqa: F401

from django.db.models.base import Model

def curry(_curried_func: Any, *args: Any, **kwargs: Any): ...

class cached_property:
    func: Callable = ...
    __doc__: Any = ...
    name: str = ...
    def __init__(self, func: Callable, name: Optional[str] = ...) -> None: ...
    def __get__(self, instance: Any, cls: Type[Any] = ...) -> Any: ...

class Promise: ...

def lazy(func: Union[Callable, Type[str]], *resultclasses: Any) -> Callable: ...
def lazystr(text: Any): ...
def keep_lazy(*resultclasses: Any) -> Callable: ...
def keep_lazy_text(func: Callable) -> Callable: ...

empty: Any

def new_method_proxy(func: Any): ...

class LazyObject:
    def __init__(self) -> None: ...
    __getattr__: Any = ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __reduce__(self) -> Tuple[Callable, Tuple[Model]]: ...
    def __copy__(self): ...
    def __deepcopy__(self, memo: Any): ...
    __bytes__: Any = ...
    __bool__: Any = ...
    __dir__: Any = ...
    __class__: Any = ...
    __ne__: Any = ...
    __hash__: Any = ...
    __getitem__: Any = ...
    __setitem__: Any = ...
    __delitem__: Any = ...
    __iter__: Any = ...
    __len__: Any = ...
    __contains__: Any = ...

def unpickle_lazyobject(wrapped: Model) -> Model: ...

class SimpleLazyObject(LazyObject):
    def __init__(self, func: Callable) -> None: ...
    def __copy__(self) -> List[int]: ...
    def __deepcopy__(self, memo: Dict[Any, Any]) -> List[int]: ...

def partition(predicate: Callable, values: List[Model]) -> Tuple[List[Model], List[Model]]: ...
