import asyncio
import os

from bot import log

log.setup()

# On Windows, the selector event loop is required for aiodns.
if os.name == "nt":
    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy(),  # type: ignore[attr-defined]
    )

# If not on Windows we can use uvloop to speedup Hikari.
if os.name != "nt":
    import uvloop

    uvloop.install()
