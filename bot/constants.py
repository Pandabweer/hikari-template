from pydantic_settings import BaseSettings


class EnvConfig(
    BaseSettings,  #  type: ignore[misc]
    env_file=(".env.server", ".env"),
    env_file_encoding="utf-8",
    env_nested_delimiter="__",
    extra="ignore",
):  # type: ignore[call-arg]

    """Our default configuration for models that should load from .env files."""


class _Miscellaneous(EnvConfig):
    debug: bool = True
    file_logs: bool = True


Miscellaneous = _Miscellaneous()


FILE_LOGS = Miscellaneous.file_logs
DEBUG_MODE = Miscellaneous.debug


class _Bot(EnvConfig, env_prefix="bot_"):  # type: ignore[call-arg]
    token: str = ""


Bot = _Bot()
