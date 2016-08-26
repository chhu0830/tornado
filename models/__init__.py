class Service():
  pass

from models.base import Base
from models.user import User

Service.User = User()
