import rclpy
from rclpy.node import Node

from arm_msg.msg import ArmJointAngles
from arm_msg.srv import RecordControl

from arm_pkg.servo_controller import ServoController
from arm_pkg.trajectory_recorder import TrajectoryRecorder
from arm_pkg.trajectory_player import TrajectoryPlayer

class ArmJointNode(Node):
    def __init__(self):
        super().__init__('arm_joint_node')

        self.servo_controller = ServoController()
        self.recorder = TrajectoryRecorder()
        self.player = TrajectoryPlayer()

        self.publisher_ = self.create_publisher(
            ArmJointAngles,
            'arm_joint_angles',
            10
        )

        self.subscriber_ = self.create_subscription(
            ArmJointAngles,
            'cmd_arm_joint_angles',
            self.subscriber_callback,
            10
        )

        self.service = self.create_service(
            RecordControl,
            'record_control',
            self.service_callback
        )

        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )

        self.get_logger().info('Arm Joint Node Started')

    def subscriber_callback(self, msg):
        if len(msg.angles) != 6:
            self.get_logger().error('Received invalid joint angles length')
            return

        success = self.servo_controller.set_joint_angles(msg.angles)

        if success:
            self.get_logger().info(
                f'Received: {self.servo_controller.get_joint_angles()}'
            )

    def service_callback(self, request, response):
        action = request.action
        filename = request.filename

        if action == 'start_recording':
            self.recorder.start_recording()
            response.success = True
            response.message = 'Recording started'

        elif action == 'stop_recording':
            self.recorder.stop_recording()
            self.recorder.save_to_file(filename)
            response.success = True
            response.message = f'Recording stopped and saved to {filename}'

        elif action == 'start_playback':
            try:
                self.player.load_from_file(filename)
                self.player.start_playback()
                response.success = True
                response.message = f'Playback started from {filename}'
            except FileNotFoundError:
                response.success = False
                response.message = f'File not found: {filename}'
        
        else:
            response.success = False
            response.message = f'Unknown action: {action}'

        self.get_logger().info(response.message)
        return response

    def timer_callback(self):
        playback_point = self.player.get_next_point()

        if playback_point is not None:
            self.servo_controller.set_joint_angles(playback_point)

        msg = ArmJointAngles()
        current_angles = self.servo_controller.get_joint_angles()
        msg.angles = current_angles

        self.publisher_.publish(msg)

        self.recorder.record_point(current_angles)

        self.get_logger().info(f'Published: {msg.angles}')


def main(args=None):
    rclpy.init(args=args)
    
    node = ArmJointNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()