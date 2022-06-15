from typing import Union, Optional

class User:
    pass

# 3.8
def get_user_id(user_id: Union[str, int]) -> Optional[User]:
    return User()

# 3.10
def get_user_id(user_id: str | int) -> User | None:
    return User()
