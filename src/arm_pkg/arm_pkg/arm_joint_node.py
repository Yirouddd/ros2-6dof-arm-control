import rclpy
from rclpy.node import Node

from arm_msg.msg import ArmJointAngles


class ArmJointNode(Node):
    def __init__(self):
        super().__init__('arm_joint_node')

        self.publisher_ = self.create_publisher(
            ArmJointAngles,
            'arm_joint_angles',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )

        self.get_logger().info('Arm Joint Node Started')

    def timer_callback(self):
        msg = ArmJointAngles()
        msg.angles = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

        self.publisher_.publish(msg)

        self.get_logger().info(f'Published: {msg.angles}')


def main(args=None):
    rclpy.init(args=args)
    
    node = ArmJointNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()