import json
from datetime import datetime

class TrajectoryRecorder:
    def __init__(self):
        self.is_recording = False
        self.trajectories = []

    def start_recording(self):
        self.is_recording = True
        self.trajectories = []  # Clear previous trajectories
        print('[TrajectoryRecorder] Started recording')

    def stop_recording(self):
        self.is_recording = False
        print('[TrajectoryRecorder] Stopped recording')

    def record_point(self, joint_angles):
        if not self.is_recording:
            return

        point = {
            'timestamp': datetime.now().isoformat(),
            'joint_angles': [float(angle) for angle in joint_angles]
        }
        self.trajectories.append(point)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.trajectories, f, indent=4)

            print(f'[TrajectoryRecorder] Saved {len(self.trajectories)} points to {filename}')