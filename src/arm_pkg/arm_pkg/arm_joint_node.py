import rclpy
from rclpy.node import Node

from arm_msg.msg import ArmJointAngles


class ArmJointNode(Node):
    def __init__(self):
        super().__init__('arm_joint_node')

        # Current arms state
        self.current_joint_angles = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        # Publisher
        self.publisher_ = self.create_publisher(
            ArmJointAngles,
            'arm_joint_angles',
            10
        )

        # Subscriber
        self.subscriber_ = self.create_subscription(
            ArmJointAngles,
            'cmd_arm_joint_angles',
            self.subscriber_callback,
            10
        )

        # Timer
        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )

        self.get_logger().info('Arm Joint Node Started')

    def subscriber_callback(self, msg):

        if len(msg.angles) != 6:
            self.get_logger().error('Received invalid joint angles length')
            return

        self.current_joint_angles = list(msg.angles)
        self.get_logger().info(f'Received: {self.current_joint_angles}')

    def timer_callback(self):
        msg = ArmJointAngles()
        msg.angles = self.current_joint_angles

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