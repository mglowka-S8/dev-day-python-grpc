import logging
from concurrent import futures

import grpc

from api import ConfigEntry, ConfigGetResponse
from api_pb2_grpc import ApiServiceServicer, add_ApiServiceServicer_to_server
from common.config import read_props


class ConfigServer(ApiServiceServicer):
    def get_config(self, request, context):
        props = read_props()
        flattened_props = {}
        self.get_props(props, '', flattened_props)
        config_list = []
        for prop in flattened_props:
            config_list.append(ConfigEntry(key=prop, value=flattened_props[prop]))

        return ConfigGetResponse(entry=config_list)

    def get_props(self, props, prefix, prop_dict):
        for item in props.items():
            if isinstance(item[1], dict):
                self.get_props(item[1], prefix + "." + item[0] if prefix != '' else item[0], prop_dict)
            else:
                prop_dict[prefix + "." + item[0]] = item[1]


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    add_ApiServiceServicer_to_server(ConfigServer(), server)
    server.add_insecure_port('[::]:5005')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    serve()
