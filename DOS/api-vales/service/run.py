import sys
import grpc
from concurrent import futures

import vales_pb2
import vales_pb2_grpc

from dal import users

class Vales(vales_pb2_grpc.ValesServicer):

    def AlterUser(self, request, context):
        print(request)

        ret_code, ret_message = users.alter_user(
            request.userId,
            request.username,
            request.passwd,
            request.roleId,
            request.disabled,
            request.firstName,
            request.lastName
        )

        return vales_pb2.AlterUserResponse(
            returnCode=ret_code,
            returnMessage=ret_message
        )


def _engage():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vales_pb2_grpc.add_ValesServicer_to_server(Vales(), server)
    server.add_insecure_port('[::]:10080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':

    try:
        _engage()
    except KeyboardInterrupt:
        print('Exiting')
    except:
        if True:
            print('Whoops! Problem in server:', file=sys.stderr)
            # traceback.print_exc(file=sys.stderr)
        sys.exit(1)

    # assuming everything went right, exit gracefully
    sys.exit(0)
