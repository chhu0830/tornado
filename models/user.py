from models import Service
from models.base import Base

class User(Base):
  def __init__(self):
    super().__init__(table="users")
