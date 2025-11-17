import re
import sys, pdb
from entities.user import User

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        # pysäytetään ohjelman suoritus tälle riville
        pdb.Pdb(stdout=sys.__stdout__).set_trace()

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        existing = self._user_repository.find_by_username(username)
        if existing:
            raise UserInputError("Username already exists")
        
        if len(username) <= 2:
            raise UserInputError("Username too short")

        if not re.fullmatch(r"[a-zA-Z]+", username):
            raise UserInputError("Username must contain only letters a-z")
        
        if re.fullmatch(r"[a-öA-Ö]+", password) or len(password) < 8:
            raise UserInputError("Password must be over 8 characters and contain something other than a letter")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
