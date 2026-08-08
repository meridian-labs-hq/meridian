import time
from collections.abc import Callable


def with_retry(fn: Callable, attempts: int = 3, backoff_s: float = 0.5):
    last: Exception | None = None
    for i in range(attempts):
        try:
            return fn()
        except ConnectionError as exc:  # transient only
            last = exc
            time.sleep(backoff_s * (2 ** i))
    raise last  # type: ignore[misc]
