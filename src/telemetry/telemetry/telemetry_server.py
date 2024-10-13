import rclpy
from rclpy.node import Node
import asyncio
from websockets import serve
from websockets.exceptions import ConnectionClosed
from std_msgs.msg import Float64
from threading import Thread
import json
import time

class TelemetryServer(Node):
    def __init__(self):
        super().__init__('telemetry_server')
        
        self.__data = 0
        
        self.create_subscription(Float64, 'telemetry', self.__update_data, 10)
        
        Thread(target=lambda : asyncio.run(self.__start_websocket())).start()
        
    async def __update_data(self, msg: Float64):
        self.__data = msg.data
        
    async def __start_websocket(self):
        async with serve(self.__handle_connection, 'localhost', 8001):
            await asyncio.get_running_loop().create_future()
        
    async def __handle_connection(self, websocket):
        data = { 'data': self.__data, 'timestamp': time.time() * 1000 }
        try:
            await websocket.send(json.dumps(data))
        except ConnectionClosed:
            pass
        
def main():
    rclpy.init()
    
    node = TelemetryServer()
    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()