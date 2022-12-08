from app.application.interfaces.user_repository import AbstractRepository
from app.domain.entity import User


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def create_user(self, user_name: str):
        _user = User(name=user_name)
        # check if user already exists, raise Exception
        if self.repository.find_one(model=_user):
            raise ValueError("User already exists.")
        user = self.repository.create(_user)

        return user
