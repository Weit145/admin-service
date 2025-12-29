from proto import admin_pb2

from app.gateway.services.iadmin_service import IAdminServiceImpl
from app.kafka.repositories.kafka_repositories import KafkaRepository

class AdminServiceImpl(IAdminServiceImpl):
    def __init__(self):
        self.kf = KafkaRepository()
        return
    
    async def DeletePost(self, request, context) -> admin_pb2.Empty:
        await self.kf.send_message(topic="admin_delete_post", message={"id": request.post_id})
        return admin_pb2.Empty
    
    async def DeleteUser(self, request, context) -> admin_pb2.Empty:
        await self.kf.send_message(topic="admin_delete_user", message={"id": request.user_id})
        return admin_pb2.Empty
    
    async def BanUser(self, request, context) -> admin_pb2.Empty:
        await self.kf.send_message(topic="admin_ban_user", message={"id": request.user_id})
        return admin_pb2.Empty