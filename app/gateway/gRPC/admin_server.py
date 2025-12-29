from proto import admin_pb2_grpc

from app.gateway.services.admin_service import AdminServiceImpl

class AdminServicer(admin_pb2_grpc.AdminServicer):
    async def DeletePost(self, request, context):
        return await AdminServiceImpl().DeletePost(request, context)
    
    async def DeleteUser(self, request, context):
        return await AdminServiceImpl().DeleteUser(request, context)
    
    async def BanUser(self, request, context):
        return await AdminServiceImpl().BanUser(request, context)