from yowsup.stacks import  YowStackBuilder
from layer import EchoLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.auth import AuthError


CREDENTIALS = ("4915903191887", "EHUY9FwgpcQjPsC3PJbyU5vageo=") # replace with your phone and password

if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\
        .pushDefaultLayers(1)\
        .push(EchoLayer)\
        .build()

    stack.setCredentials(CREDENTIALS)

    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
    try:
        stack.loop()
    except AuthError as e:
        print("Authentication Error: %s" % e.message)
