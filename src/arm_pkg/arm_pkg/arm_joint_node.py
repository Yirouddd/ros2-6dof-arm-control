import rclpy
from rclpy.node import Node

class ArmJointNode(Node):
    def __init__(self):
        super().__init__('arm_joint_node')
        self.get_logger().info('ArmJointNode has been started.')

def main(args=None):
    rclpy.init(args=args)
    node = ArmJointNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
