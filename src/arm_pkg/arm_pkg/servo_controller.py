class ServoController:
    def __init__(self):
        # simulated surrent servo state
        self.current_joint_angles = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        print('[ServoController] Initialized')

    def set_joint_angles(self, angles):
        if len(angles) != 6:
            print('[ServoController] Invalid joint angles length')
            return

        self.current_joint_angles = list(angles)
        print(f'[ServoController] Updated angles: {self.current_joint_angles}')
        return True

    def get_joint_angles(self):
        return self.current_joint_angles
