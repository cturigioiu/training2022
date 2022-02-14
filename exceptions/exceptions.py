class UnknownApiVersionException(Exception):
    def __init__(self):
        super().__init__("Unexpected API version received. Expected version 1 or 2")


class UserNotCreatedException(Exception):
    def __init__(self):
        super().__init__("User was no successfully created")


class PostNotCreatedException(Exception):
    def __init__(self):
        super().__init__("Post was no successfully created")


class CommentNotCreatedException(Exception):
    def __init__(self):
        super().__init__("Commnet was no successfully created")


class TodoNotCreatedException(Exception):
    def __init__(self):
        super().__init__("Todo was no successfully created")


class ModificationFailedException(Exception):
    def __init__(self):
        super().__init__("Expected modification is not seen")
