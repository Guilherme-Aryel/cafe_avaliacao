from models.dataclasses.user import User


class SoleAdminDeletionError(Exception):
    """Raised when attempting to delete the only remaining user with the 'admin' role."""

    def __init__(self, actor: User, target: User) -> None:
        self.actor: User = actor
        self.target: User = target
        super().__init__("Sole admin can't be deleted.")


class UserNotDefinedError(Exception):
    """Raised when a expected user is not found"""

    def __init__(self) -> None:
        super().__init__("User not defined or found.")