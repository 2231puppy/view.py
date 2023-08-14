from rich.console import RenderableType

__all__ = (
    "ViewWarning",
    "NotLoadedWarning",
    "ViewError",
    "MissingLibraryError",
    "EnvironmentError",
    "InvalidBodyError",
    "MistakeError",
)


class ViewWarning(UserWarning):
    ...


class NotLoadedWarning(ViewWarning):
    ...


class ConfigWarning(ViewWarning):
    ...


class ViewError(Exception):
    def __init__(
        self,
        *args: object,
        hint: RenderableType | None = None,
    ) -> None:
        self.hint = hint
        super().__init__(*args)


class MissingLibraryError(ViewError):
    ...


class EnvironmentError(ViewError):
    ...


class InvalidBodyError(ViewError):
    ...


class MistakeError(ViewError):
    ...