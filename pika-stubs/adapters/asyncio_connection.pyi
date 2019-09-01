# Stubs for pika.adapters.asyncio_connection (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pika.adapters import base_connection
from typing import Any, Optional

class IOLoopAdapter:
    loop: Any = ...
    handlers: Any = ...
    readers: Any = ...
    writers: Any = ...
    def __init__(self, loop: Any) -> None: ...
    def close(self) -> None: ...
    def add_timeout(self, deadline: Any, callback_method: Any): ...
    @staticmethod
    def remove_timeout(handle: Any): ...
    def add_callback_threadsafe(self, callback: Any) -> None: ...
    def add_handler(self, fd: Any, cb: Any, event_state: Any) -> None: ...
    def remove_handler(self, fd: Any) -> None: ...
    def update_handler(self, fd: Any, event_state: Any) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class AsyncioConnection(base_connection.BaseConnection):
    sleep_counter: int = ...
    loop: Any = ...
    ioloop: Any = ...
    def __init__(self, parameters: Optional[Any] = ..., on_open_callback: Optional[Any] = ..., on_open_error_callback: Optional[Any] = ..., on_close_callback: Optional[Any] = ..., stop_ioloop_on_close: bool = ..., custom_ioloop: Optional[Any] = ...) -> None: ...