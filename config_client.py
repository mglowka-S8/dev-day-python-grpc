from flask import Flask
from flask_grpc import ChannelWrapper, StubWrapper

from api import ConfigGetRequest
from api_pb2_grpc import ApiServiceStub

app = Flask(__name__)
channel_wrapper = ChannelWrapper(
    target="localhost:5005",
    secure=False,
)
channel_wrapper.init_app(app)

api_stub = StubWrapper(ApiServiceStub, channel_wrapper)


@app.route("/")
def hello_world():
    response = api_stub.get_config(request=ConfigGetRequest())
    return response.entry
