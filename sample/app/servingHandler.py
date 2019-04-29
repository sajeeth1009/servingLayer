# -*- coding: utf-8 -*-

import grpc
from google.protobuf import text_format
from tensorflow_serving.apis import model_service_pb2_grpc, predict_pb2, prediction_service_pb2, model_management_pb2, prediction_service_pb2_grpc
from tensorflow_serving.config import model_server_config_pb2
import Constants as const
import time
import tensorflow as tf


def makeRequest():
    channel = grpc.insecure_channel(const.host + ":" + const.port)
    stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
    request = predict_pb2.PredictRequest()
    request.model_spec.name = '1556447744'
    request.model_spec.signature_name = 'serving_default'

    # read image into numpy array
    img = {
       "length": [6],
       "tokens": [["F","O","Q","I","O","e"]]
     }

    # convert to tensor proto and make request
    # shape is in NHWC (num_samples x im x width x channels) format
    request.inputs['tokens'].CopyFrom(
        tf.contrib.util.make_tensor_proto(img["tokens"]))
    request.inputs['length'].CopyFrom(
        tf.contrib.util.make_tensor_proto(img["length"]))
    tt = time.time()
    resp = stub.Predict(request, 30.0)
    rt = time.time()
    return str({"timeTaken": rt - tt})


def getConfigurations():
    channel = grpc.insecure_channel(const.host + ":" + const.port)
    stub = model_service_pb2_grpc.ModelServiceStub(channel)
    model_server_config = model_server_config_pb2.ModelServerConfig()
    return model_server_config

def updateConfigurations():
    channel = grpc.insecure_channel(const.host+":"+const.port)
    stub = model_service_pb2_grpc.ModelServiceStub(channel)
    request = model_management_pb2.ReloadConfigRequest()
    model_server_config = model_server_config_pb2.ModelServerConfig()

    # Create a config to add to the list of served models
    configurations = open("models.conf", "r").read()
    config_list = model_server_config_pb2.ModelConfigList()
    model_server_config = text_format.Parse(text=configurations, message=model_server_config)

    request.config.CopyFrom(model_server_config)

    print(request.IsInitialized())
    print(request.ListFields())

    response = stub.HandleReloadConfigRequest(request, 10)
    if response.status.error_code == 0:
        return {"status": 200, "message": "Reload sucessfully"}
    else:
        return {"status": response.status.error_code, "message": response.status.error_message}