# ROS2 6DOF Arm Control System

A modular ROS2-based 6DOF robotic arm project designed for learning and experimentation with:

- ROS2 distributed communication
- robotic arm control
- custom ROS2 interfaces
- motion recording and playback
- computer vision
- AI / LLM integration
- robotics software engineering workflows

This project is built progressively from low-level ROS2 communication to higher-level autonomous robotic control.

---

# Features
## Current Features
- Custom ROS2 messages and services
- ROS2 publisher/subscriber architecture
- Joint angle state publishing
- Commanded joint angle subscription
- Modular ROS2 workspace structure
- GitHub-integrated robotics workflow

## Planned Features
- Real servo motor control
- Serial communication drivers
- Trajectory recording/playback
- OpenCV integration
- Object detection and tracking
- LLM / Agentic AI integration
- LangGraph robotic workflows
- Voice-command robotic control
- Motion planning and interpolation
- MoveIt2 integration

# Workspace Structure
```python
dev_workspace/
├── src/
│   ├── arm_msg/        # Custom ROS2 interfaces
│   ├── arm_pkg/        # Arm control nodes
│   ├── vision_pkg/     # Vision and OpenCV nodes
│   ├── AI_pkg/         # AI / LLM integration
│   └── turtle_pkg/     # ROS2 practice package
│
├── build/
├── install/
└── log/
```

# ROS2 Architecture

The project follows a distributed ROS2 node architecture.
```python
User / AI Agent
        ↓
ROS2 Topics / Services
        ↓
Arm Control Node
        ↓
Servo Controller
        ↓
Robotic Arm Hardware
```
