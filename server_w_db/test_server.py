from Server_class import Server
from globals_ import serverAHost, serverAPort, serverBHost, serverBPort
from globals_ import databaseAFilePath, databaseBFilePath

import time
import random

# methods
def switch_server(closeServer, runServer):
    # closeServer : Server to be closed
    # runServer : server to replace closed server

    # run new server
    runServer.start()
    
    # message clients that server will close and they need to switch
    # FIXME : Needs further testing ...
    closeServer.server_switch_msg(runServer)

    # close old server
    closeServer.pause()

    # pass

# globals
exitFlag = False

# init servers and clients
serverA = Server("A", serverAHost, serverAPort, databaseAFilePath)
serverB = Server("B", serverBHost, serverBPort, databaseBFilePath)

# serverA.run()

# # run system
while not exitFlag:
    # switch listening server every random minutes

    # NOTE : Server A starts first

    # time.sleep(random.randint(1,60))

    switch_server(serverA,serverB)

    # time.sleep(random.randint(1,60))
    time.sleep(4)

    switch_server(serverB,serverA)

    time.sleep(3)
