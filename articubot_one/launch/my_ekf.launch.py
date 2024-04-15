from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_node',
            parameters=[
                {'use_imu': False},
                {'use_mag': False},
                {'use_gps': False},
                {'use_odom': True},
                {'broadcast_tf': True},
                {'odom_topic': '/odom'},  # Replace with your actual topic
                #{'odom_frame': 'your_encoder_frame'},  # Replace with your actual frame
                {'scan_topic': '/scan'},  # Replace with your actual topic
                #{'scan_frame': 'your_lidar_frame'},  # Replace with your actual frame
            ]
        )
    ])
