from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    start_telemetry_source_node = Node(
        package='telemetry',
        executable='telemetry_source'
    )
    
    start_telemetry_server_node = Node(
        package='telemetry',
        executable='telemetry_server'
    )
    
    ld = LaunchDescription()
    
    ld.add_action(start_telemetry_source_node)
    ld.add_action(start_telemetry_server_node)
    
    return ld