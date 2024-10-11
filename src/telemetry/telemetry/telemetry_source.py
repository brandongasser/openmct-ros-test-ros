import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from math import sqrt

class TelemetrySource(Node):
    def __init__(self):
        super().__init__('telemetry_source')
        
        self.__data = 0
        
        self.__publisher = self.create_publisher(Float64, 'telemetry', 10)
        
        self.create_timer(0.2, self.__publish_data)
        
    def __publish_data(self):
        msg = Float64()
        msg.data = sqrt(self.__data)
        
        self.__data += 1
        
        self.__publisher.publish(msg)
        
def main():
    rclpy.init()
    
    node = TelemetrySource()
    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()