import grpc
from loguru import logger
from peewee import DoesNotExist
from passlib.hash import pbkdf2_sha256

from user_srv.model.models import User
from user_srv.proto import user_pb2, user_pb2_grpc


@logger.catch
class UserServicer(user_pb2_grpc.UserServicer):

    def convert_user_to_rsp(self, user):
        user_info_rsp = user_pb2.UserInfoResponse

        user_info_rsp.id = user.id
        user_info_rsp.password = user.password
        user_info_rsp.mobile = user.mobile
        user_info_rsp.role = user.role

        if user.nick_name:
            user_info_rsp.nick_name = user.nick_name
        if user.gender:
            user_info_rsp.gender = user.gender

        return user_info_rsp

    def GetUserList(self, request: user_pb2.PageInfo, context):
        rsp = user_pb2.UserInfoResponse

        users = User.select()
        rsp.total = users.count()

        start = 0
        page = 1
        per_page_nums = 10
        if request.pSize:
            per_page_nums = request.pSize
        if request.pn:
            start = per_page_nums * (page + 1)

        for user in users:
            rsp.data.append(self.convert_user_to_rsp(user))
        return rsp

    @logger.catch
    def GetUserById(self, request: user_pb2.PageInfo, context):
        try:
            user = User.get(User.id == request.id)
            return self.convert_user_to_rsp(user)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def GetUserByMobile(self, request: user_pb2.PageInfo, context):
        try:
            user = User.get(User.mobile == request.mobile)
            return self.convert_user_to_rsp(user)
        except DoesNotExist as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("用户不存在")
            return user_pb2.UserInfoResponse()

    @logger.catch
    def CreateUser(self, request: user_pb2.PageInfo, context):
        try:
            User.get(User.mobile == request.mobile)
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details("用户已存在")
            return user_pb2.UserInfoResponse()
        except Exception as e:
            pass
        user = User()
        user.nick_name = request.nickname
        user.mobile = request.mobile
        user.password = pbkdf2_sha256.hash(request.password)
        user.save()

        return self.convert_user_to_rsp(user)

    @logger.catch
    def CheckPassWord(self, request: user_pb2.PasswordCheckInfo, context):
        user_pb2.CheckResponse(success=pbkdf2_sha256.verify(request.password, request.encryptedPassword))
