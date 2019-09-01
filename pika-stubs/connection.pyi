# Stubs for pika.connection (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

BACKPRESSURE_WARNING: str
PRODUCT: str
LOGGER: Any

class InternalCloseReasons:
    SOCKET_ERROR: int = ...
    BLOCKED_CONNECTION_TIMEOUT: int = ...

class Parameters:
    DEFAULT_USERNAME: str = ...
    DEFAULT_PASSWORD: str = ...
    DEFAULT_BACKPRESSURE_DETECTION: bool = ...
    DEFAULT_BLOCKED_CONNECTION_TIMEOUT: Any = ...
    DEFAULT_CHANNEL_MAX: Any = ...
    DEFAULT_CLIENT_PROPERTIES: Any = ...
    DEFAULT_CREDENTIALS: Any = ...
    DEFAULT_CONNECTION_ATTEMPTS: int = ...
    DEFAULT_FRAME_MAX: Any = ...
    DEFAULT_HEARTBEAT_TIMEOUT: Any = ...
    DEFAULT_HOST: str = ...
    DEFAULT_LOCALE: str = ...
    DEFAULT_PORT: int = ...
    DEFAULT_RETRY_DELAY: float = ...
    DEFAULT_SOCKET_TIMEOUT: float = ...
    DEFAULT_SSL: bool = ...
    DEFAULT_SSL_OPTIONS: Any = ...
    DEFAULT_SSL_PORT: int = ...
    DEFAULT_VIRTUAL_HOST: str = ...
    DEFAULT_TCP_OPTIONS: Any = ...
    DEFAULT_HEARTBEAT_INTERVAL: Any = ...
    backpressure_detection: Any = ...
    blocked_connection_timeout: Any = ...
    channel_max: Any = ...
    client_properties: Any = ...
    connection_attempts: Any = ...
    credentials: Any = ...
    frame_max: Any = ...
    heartbeat: Any = ...
    host: Any = ...
    locale: Any = ...
    port: Any = ...
    retry_delay: Any = ...
    socket_timeout: Any = ...
    ssl: Any = ...
    ssl_options: Any = ...
    virtual_host: Any = ...
    tcp_options: Any = ...
    def __init__(self) -> None: ...
    @property
    def backpressure_detection(self): ...
    @backpressure_detection.setter
    def backpressure_detection(self, value: Any) -> None: ...
    @property
    def blocked_connection_timeout(self): ...
    @blocked_connection_timeout.setter
    def blocked_connection_timeout(self, value: Any) -> None: ...
    @property
    def channel_max(self): ...
    @channel_max.setter
    def channel_max(self, value: Any) -> None: ...
    @property
    def client_properties(self): ...
    @client_properties.setter
    def client_properties(self, value: Any) -> None: ...
    @property
    def connection_attempts(self): ...
    @connection_attempts.setter
    def connection_attempts(self, value: Any) -> None: ...
    @property
    def credentials(self): ...
    @credentials.setter
    def credentials(self, value: Any) -> None: ...
    @property
    def frame_max(self): ...
    @frame_max.setter
    def frame_max(self, value: Any) -> None: ...
    @property
    def heartbeat(self): ...
    @heartbeat.setter
    def heartbeat(self, value: Any) -> None: ...
    @property
    def host(self): ...
    @host.setter
    def host(self, value: Any) -> None: ...
    @property
    def locale(self): ...
    @locale.setter
    def locale(self, value: Any) -> None: ...
    @property
    def port(self): ...
    @port.setter
    def port(self, value: Any) -> None: ...
    @property
    def retry_delay(self): ...
    @retry_delay.setter
    def retry_delay(self, value: Any) -> None: ...
    @property
    def socket_timeout(self): ...
    @socket_timeout.setter
    def socket_timeout(self, value: Any) -> None: ...
    @property
    def ssl(self): ...
    @ssl.setter
    def ssl(self, value: Any) -> None: ...
    @property
    def ssl_options(self): ...
    @ssl_options.setter
    def ssl_options(self, value: Any) -> None: ...
    @property
    def virtual_host(self): ...
    @virtual_host.setter
    def virtual_host(self, value: Any) -> None: ...
    @property
    def tcp_options(self): ...
    @tcp_options.setter
    def tcp_options(self, value: Any) -> None: ...

class ConnectionParameters(Parameters):
    class _DEFAULT: ...
    backpressure_detection: Any = ...
    blocked_connection_timeout: Any = ...
    channel_max: Any = ...
    client_properties: Any = ...
    connection_attempts: Any = ...
    credentials: Any = ...
    frame_max: Any = ...
    heartbeat: Any = ...
    host: Any = ...
    locale: Any = ...
    retry_delay: Any = ...
    socket_timeout: Any = ...
    ssl: Any = ...
    ssl_options: Any = ...
    port: Any = ...
    virtual_host: Any = ...
    tcp_options: Any = ...
    def __init__(self, host: Any = ..., port: Any = ..., virtual_host: Any = ..., credentials: Any = ..., channel_max: Any = ..., frame_max: Any = ..., heartbeat: Any = ..., ssl: Any = ..., ssl_options: Any = ..., connection_attempts: Any = ..., retry_delay: Any = ..., socket_timeout: Any = ..., locale: Any = ..., backpressure_detection: Any = ..., blocked_connection_timeout: Any = ..., client_properties: Any = ..., tcp_options: Any = ..., **kwargs: Any) -> None: ...

class URLParameters(Parameters):
    ssl: bool = ...
    host: Any = ...
    port: Any = ...
    credentials: Any = ...
    virtual_host: Any = ...
    def __init__(self, url: Any) -> None: ...

class SSLOptions:
    keyfile: Any = ...
    key_password: Any = ...
    certfile: Any = ...
    server_side: Any = ...
    verify_mode: Any = ...
    ssl_version: Any = ...
    cafile: Any = ...
    capath: Any = ...
    cadata: Any = ...
    do_handshake_on_connect: Any = ...
    suppress_ragged_eofs: Any = ...
    ciphers: Any = ...
    server_hostname: Any = ...
    def __init__(self, keyfile: Optional[Any] = ..., key_password: Optional[Any] = ..., certfile: Optional[Any] = ..., server_side: bool = ..., verify_mode: Any = ..., ssl_version: Any = ..., cafile: Optional[Any] = ..., capath: Optional[Any] = ..., cadata: Optional[Any] = ..., do_handshake_on_connect: bool = ..., suppress_ragged_eofs: bool = ..., ciphers: Optional[Any] = ..., server_hostname: Optional[Any] = ...) -> None: ...

class Connection:
    ON_CONNECTION_BACKPRESSURE: str = ...
    ON_CONNECTION_BLOCKED: str = ...
    ON_CONNECTION_CLOSED: str = ...
    ON_CONNECTION_ERROR: str = ...
    ON_CONNECTION_OPEN: str = ...
    ON_CONNECTION_UNBLOCKED: str = ...
    CONNECTION_CLOSED: int = ...
    CONNECTION_INIT: int = ...
    CONNECTION_PROTOCOL: int = ...
    CONNECTION_START: int = ...
    CONNECTION_TUNE: int = ...
    CONNECTION_OPEN: int = ...
    CONNECTION_CLOSING: int = ...
    connection_state: Any = ...
    heartbeat: Any = ...
    params: Any = ...
    callbacks: Any = ...
    server_capabilities: Any = ...
    server_properties: Any = ...
    known_hosts: Any = ...
    closing: Any = ...
    remaining_connection_attempts: Any = ...
    def __init__(self, parameters: Optional[Any] = ..., on_open_callback: Optional[Any] = ..., on_open_error_callback: Optional[Any] = ..., on_close_callback: Optional[Any] = ...) -> None: ...
    def add_backpressure_callback(self, callback_method: Any) -> None: ...
    def add_on_close_callback(self, callback_method: Any) -> None: ...
    def add_on_connection_blocked_callback(self, callback_method: Any) -> None: ...
    def add_on_connection_unblocked_callback(self, callback_method: Any) -> None: ...
    def add_on_open_callback(self, callback_method: Any) -> None: ...
    def add_on_open_error_callback(self, callback_method: Any, remove_default: bool = ...) -> None: ...
    def add_timeout(self, deadline: Any, callback_method: Any) -> None: ...
    def channel(self, on_open_callback: Any, channel_number: Optional[Any] = ...): ...
    def close(self, reply_code: int = ..., reply_text: str = ...) -> None: ...
    def connect(self) -> None: ...
    def remove_timeout(self, timeout_id: Any) -> None: ...
    def set_backpressure_multiplier(self, value: int = ...) -> None: ...
    @property
    def is_closed(self): ...
    @property
    def is_closing(self): ...
    @property
    def is_open(self): ...
    @property
    def basic_nack(self): ...
    @property
    def consumer_cancel_notify(self): ...
    @property
    def exchange_exchange_bindings(self): ...
    @property
    def publisher_confirms(self): ...