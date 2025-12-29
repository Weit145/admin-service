from abc import ABC, abstractmethod
from proto import admin_pb2

class IAdminServiceImpl(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def DeletePost(self,request, context) -> admin_pb2.Empty:
        pass

    @abstractmethod
    async def DeleteUser(self,request, context) -> admin_pb2.Empty:
        pass

    @abstractmethod
    async def BanUser(self,request, context) -> admin_pb2.Empty:
        pass