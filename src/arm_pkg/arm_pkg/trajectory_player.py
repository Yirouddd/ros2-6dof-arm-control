import json

class TrajectoryPlayer:
    def __init__(self):
        self.trajectories = []
        self.current_index = 0
        self.is_playing = False

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.trajectories = json.load(f)
        
        self.current_index = 0

        print(f'[TrajectoryPlayer] Loaded {len(self.trajectories)} points from {filename}') 

    def start_playback(self):
        if len(self.trajectories) == 0:
            print('[TrajectoryPlayer] No trajectories to play')
            return
        
        self.is_playing = True
        self.current_index = 0

        print('[TrajectoryPlayer] Started playback')
        return True
    
    def stop_playback(self):
        self.is_playing = False
        print('[TrajectoryPlayer] Stopped playback')

    def get_next_point(self):
        if not self.is_playing:
            return None
        
        if self.current_index >= len(self.trajectories):
            self.is_playing = False
            print('[TrajectoryPlayer] Playback finished')
            return None

        point = self.trajectories[self.current_index]
        self.current_index += 1

        return point['joint_angles']

