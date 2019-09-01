# Stubs for pika.spec (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from pika import amqp_object
from typing import Any, Optional

str = bytes
PROTOCOL_VERSION: Any
PORT: int
ACCESS_REFUSED: int
CHANNEL_ERROR: int
COMMAND_INVALID: int
CONNECTION_FORCED: int
CONTENT_TOO_LARGE: int
FRAME_BODY: int
FRAME_END: int
FRAME_END_SIZE: int
FRAME_ERROR: int
FRAME_HEADER: int
FRAME_HEADER_SIZE: int
FRAME_HEARTBEAT: int
FRAME_MAX_SIZE: int
FRAME_METHOD: int
FRAME_MIN_SIZE: int
INTERNAL_ERROR: int
INVALID_PATH: int
NOT_ALLOWED: int
NOT_FOUND: int
NOT_IMPLEMENTED: int
NO_CONSUMERS: int
NO_ROUTE: int
PERSISTENT_DELIVERY_MODE: int
PRECONDITION_FAILED: int
REPLY_SUCCESS: int
RESOURCE_ERROR: int
RESOURCE_LOCKED: int
SYNTAX_ERROR: int
TRANSIENT_DELIVERY_MODE: int
UNEXPECTED_FRAME: int

class Connection(amqp_object.Class):
    INDEX: int = ...
    NAME: str = ...
    class Start(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        version_major: Any = ...
        version_minor: Any = ...
        server_properties: Any = ...
        mechanisms: Any = ...
        locales: Any = ...
        def __init__(self, version_major: int = ..., version_minor: int = ..., server_properties: Optional[Any] = ..., mechanisms: str = ..., locales: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class StartOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        client_properties: Any = ...
        mechanism: Any = ...
        response: Any = ...
        locale: Any = ...
        def __init__(self, client_properties: Optional[Any] = ..., mechanism: str = ..., response: Optional[Any] = ..., locale: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Secure(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        challenge: Any = ...
        def __init__(self, challenge: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class SecureOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        response: Any = ...
        def __init__(self, response: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Tune(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        channel_max: Any = ...
        frame_max: Any = ...
        heartbeat: Any = ...
        def __init__(self, channel_max: int = ..., frame_max: int = ..., heartbeat: int = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class TuneOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        channel_max: Any = ...
        frame_max: Any = ...
        heartbeat: Any = ...
        def __init__(self, channel_max: int = ..., frame_max: int = ..., heartbeat: int = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Open(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        virtual_host: Any = ...
        capabilities: Any = ...
        insist: Any = ...
        def __init__(self, virtual_host: str = ..., capabilities: str = ..., insist: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class OpenOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        known_hosts: Any = ...
        def __init__(self, known_hosts: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Close(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        reply_code: Any = ...
        reply_text: Any = ...
        class_id: Any = ...
        method_id: Any = ...
        def __init__(self, reply_code: Optional[Any] = ..., reply_text: str = ..., class_id: Optional[Any] = ..., method_id: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class CloseOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Blocked(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        reason: Any = ...
        def __init__(self, reason: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Unblocked(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...

class Channel(amqp_object.Class):
    INDEX: int = ...
    NAME: str = ...
    class Open(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        out_of_band: Any = ...
        def __init__(self, out_of_band: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class OpenOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        channel_id: Any = ...
        def __init__(self, channel_id: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Flow(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        active: Any = ...
        def __init__(self, active: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class FlowOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        active: Any = ...
        def __init__(self, active: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Close(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        reply_code: Any = ...
        reply_text: Any = ...
        class_id: Any = ...
        method_id: Any = ...
        def __init__(self, reply_code: Optional[Any] = ..., reply_text: str = ..., class_id: Optional[Any] = ..., method_id: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class CloseOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...

class Access(amqp_object.Class):
    INDEX: int = ...
    NAME: str = ...
    class Request(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        realm: Any = ...
        exclusive: Any = ...
        passive: Any = ...
        active: Any = ...
        write: Any = ...
        read: Any = ...
        def __init__(self, realm: str = ..., exclusive: bool = ..., passive: bool = ..., active: bool = ..., write: bool = ..., read: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class RequestOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        def __init__(self, ticket: int = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...

class Exchange(amqp_object.Class):
    INDEX: int = ...
    NAME: str = ...
    class Declare(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        exchange: Any = ...
        type: Any = ...
        passive: Any = ...
        durable: Any = ...
        auto_delete: Any = ...
        internal: Any = ...
        nowait: Any = ...
        arguments: Any = ...
        def __init__(self, ticket: int = ..., exchange: Optional[Any] = ..., type: str = ..., passive: bool = ..., durable: bool = ..., auto_delete: bool = ..., internal: bool = ..., nowait: bool = ..., arguments: Any = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class DeclareOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Delete(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        exchange: Any = ...
        if_unused: Any = ...
        nowait: Any = ...
        def __init__(self, ticket: int = ..., exchange: Optional[Any] = ..., if_unused: bool = ..., nowait: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class DeleteOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Bind(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        destination: Any = ...
        source: Any = ...
        routing_key: Any = ...
        nowait: Any = ...
        arguments: Any = ...
        def __init__(self, ticket: int = ..., destination: Optional[Any] = ..., source: Optional[Any] = ..., routing_key: str = ..., nowait: bool = ..., arguments: Any = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class BindOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Unbind(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        destination: Any = ...
        source: Any = ...
        routing_key: Any = ...
        nowait: Any = ...
        arguments: Any = ...
        def __init__(self, ticket: int = ..., destination: Optional[Any] = ..., source: Optional[Any] = ..., routing_key: str = ..., nowait: bool = ..., arguments: Any = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class UnbindOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...

class Queue(amqp_object.Class):
    INDEX: int = ...
    NAME: str = ...
    class Declare(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        queue: Any = ...
        passive: Any = ...
        durable: Any = ...
        exclusive: Any = ...
        auto_delete: Any = ...
        nowait: Any = ...
        arguments: Any = ...
        def __init__(self, ticket: int = ..., queue: str = ..., passive: bool = ..., durable: bool = ..., exclusive: bool = ..., auto_delete: bool = ..., nowait: bool = ..., arguments: Any = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class DeclareOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        queue: Any = ...
        message_count: Any = ...
        consumer_count: Any = ...
        def __init__(self, queue: Optional[Any] = ..., message_count: Optional[Any] = ..., consumer_count: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Bind(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        queue: Any = ...
        exchange: Any = ...
        routing_key: Any = ...
        nowait: Any = ...
        arguments: Any = ...
        def __init__(self, ticket: int = ..., queue: str = ..., exchange: Optional[Any] = ..., routing_key: str = ..., nowait: bool = ..., arguments: Any = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class BindOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Purge(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        queue: Any = ...
        nowait: Any = ...
        def __init__(self, ticket: int = ..., queue: str = ..., nowait: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class PurgeOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        message_count: Any = ...
        def __init__(self, message_count: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Delete(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        queue: Any = ...
        if_unused: Any = ...
        if_empty: Any = ...
        nowait: Any = ...
        def __init__(self, ticket: int = ..., queue: str = ..., if_unused: bool = ..., if_empty: bool = ..., nowait: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class DeleteOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        message_count: Any = ...
        def __init__(self, message_count: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Unbind(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        queue: Any = ...
        exchange: Any = ...
        routing_key: Any = ...
        arguments: Any = ...
        def __init__(self, ticket: int = ..., queue: str = ..., exchange: Optional[Any] = ..., routing_key: str = ..., arguments: Any = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class UnbindOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...

class Basic(amqp_object.Class):
    INDEX: int = ...
    NAME: str = ...
    class Qos(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        prefetch_size: Any = ...
        prefetch_count: Any = ...
        global_: Any = ...
        def __init__(self, prefetch_size: int = ..., prefetch_count: int = ..., global_: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class QosOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Consume(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        queue: Any = ...
        consumer_tag: Any = ...
        no_local: Any = ...
        no_ack: Any = ...
        exclusive: Any = ...
        nowait: Any = ...
        arguments: Any = ...
        def __init__(self, ticket: int = ..., queue: str = ..., consumer_tag: str = ..., no_local: bool = ..., no_ack: bool = ..., exclusive: bool = ..., nowait: bool = ..., arguments: Any = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class ConsumeOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        consumer_tag: Any = ...
        def __init__(self, consumer_tag: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Cancel(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        consumer_tag: Any = ...
        nowait: Any = ...
        def __init__(self, consumer_tag: Optional[Any] = ..., nowait: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class CancelOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        consumer_tag: Any = ...
        def __init__(self, consumer_tag: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Publish(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        exchange: Any = ...
        routing_key: Any = ...
        mandatory: Any = ...
        immediate: Any = ...
        def __init__(self, ticket: int = ..., exchange: str = ..., routing_key: str = ..., mandatory: bool = ..., immediate: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Return(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        reply_code: Any = ...
        reply_text: Any = ...
        exchange: Any = ...
        routing_key: Any = ...
        def __init__(self, reply_code: Optional[Any] = ..., reply_text: str = ..., exchange: Optional[Any] = ..., routing_key: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Deliver(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        consumer_tag: Any = ...
        delivery_tag: Any = ...
        redelivered: Any = ...
        exchange: Any = ...
        routing_key: Any = ...
        def __init__(self, consumer_tag: Optional[Any] = ..., delivery_tag: Optional[Any] = ..., redelivered: bool = ..., exchange: Optional[Any] = ..., routing_key: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Get(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        ticket: Any = ...
        queue: Any = ...
        no_ack: Any = ...
        def __init__(self, ticket: int = ..., queue: str = ..., no_ack: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class GetOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        delivery_tag: Any = ...
        redelivered: Any = ...
        exchange: Any = ...
        routing_key: Any = ...
        message_count: Any = ...
        def __init__(self, delivery_tag: Optional[Any] = ..., redelivered: bool = ..., exchange: Optional[Any] = ..., routing_key: Optional[Any] = ..., message_count: Optional[Any] = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class GetEmpty(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        cluster_id: Any = ...
        def __init__(self, cluster_id: str = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Ack(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        delivery_tag: Any = ...
        multiple: Any = ...
        def __init__(self, delivery_tag: int = ..., multiple: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Reject(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        delivery_tag: Any = ...
        requeue: Any = ...
        def __init__(self, delivery_tag: Optional[Any] = ..., requeue: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class RecoverAsync(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        requeue: Any = ...
        def __init__(self, requeue: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Recover(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        requeue: Any = ...
        def __init__(self, requeue: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class RecoverOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Nack(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        delivery_tag: Any = ...
        multiple: Any = ...
        requeue: Any = ...
        def __init__(self, delivery_tag: int = ..., multiple: bool = ..., requeue: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...

class Tx(amqp_object.Class):
    INDEX: int = ...
    NAME: str = ...
    class Select(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class SelectOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Commit(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class CommitOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class Rollback(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class RollbackOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...

class Confirm(amqp_object.Class):
    INDEX: int = ...
    NAME: str = ...
    class Select(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        nowait: Any = ...
        def __init__(self, nowait: bool = ...) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...
    class SelectOk(amqp_object.Method):
        INDEX: int = ...
        NAME: str = ...
        def __init__(self) -> None: ...
        @property
        def synchronous(self): ...
        def decode(self, encoded: Any, offset: int = ...): ...
        def encode(self): ...

class BasicProperties(amqp_object.Properties):
    CLASS: Any = ...
    INDEX: int = ...
    NAME: str = ...
    FLAG_CONTENT_TYPE: Any = ...
    FLAG_CONTENT_ENCODING: Any = ...
    FLAG_HEADERS: Any = ...
    FLAG_DELIVERY_MODE: Any = ...
    FLAG_PRIORITY: Any = ...
    FLAG_CORRELATION_ID: Any = ...
    FLAG_REPLY_TO: Any = ...
    FLAG_EXPIRATION: Any = ...
    FLAG_MESSAGE_ID: Any = ...
    FLAG_TIMESTAMP: Any = ...
    FLAG_TYPE: Any = ...
    FLAG_USER_ID: Any = ...
    FLAG_APP_ID: Any = ...
    FLAG_CLUSTER_ID: Any = ...
    content_type: Any = ...
    content_encoding: Any = ...
    headers: Any = ...
    delivery_mode: Any = ...
    priority: Any = ...
    correlation_id: Any = ...
    reply_to: Any = ...
    expiration: Any = ...
    message_id: Any = ...
    timestamp: Any = ...
    type: Any = ...
    user_id: Any = ...
    app_id: Any = ...
    cluster_id: Any = ...
    def __init__(self, content_type: Optional[Any] = ..., content_encoding: Optional[Any] = ..., headers: Optional[Any] = ..., delivery_mode: Optional[Any] = ..., priority: Optional[Any] = ..., correlation_id: Optional[Any] = ..., reply_to: Optional[Any] = ..., expiration: Optional[Any] = ..., message_id: Optional[Any] = ..., timestamp: Optional[Any] = ..., type: Optional[Any] = ..., user_id: Optional[Any] = ..., app_id: Optional[Any] = ..., cluster_id: Optional[Any] = ...) -> None: ...
    def decode(self, encoded: Any, offset: int = ...): ...
    def encode(self): ...

methods: Any
props: Any

def has_content(methodNumber: Any): ...