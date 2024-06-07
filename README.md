# ROBOTICS-PROJECT-SEM05 🤖🚀

## Introduction
This project, serves as our  Robotics semester project for the 5th semester of BS Artificial Intelligence at Bahria University. The project focuses on creating a wall-following robot controller using the Webots simulation environment. The robot will navigate along a wall while avoiding obstacles.

## Table of Contents
- [Introduction](#introduction)
- [Program](#program)
- [University](#university)
- [Instructor](#instructor)
- [Implementation Details](#implementation-details)
  - [Robot Configuration](#robot-configuration)
  - [Controller Logic](#controller-logic)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Group Members](#group-members)

## Program
📘 This project is part of the BS Artificial Intelligence program at Bahria University.

## University
🏫 Bahria University

## Instructor
🎓 Professor Adil Khan

## Implementation Details

### Robot Configuration
🤖 - The robot consists of two wheels: a left wheel and a right wheel.
- Eight proximity sensors (ps0 to ps7) detect obstacles around the robot.

### Controller Logic
1. **Initialization:**
   - Set the time step for simulation.
   - Define the maximum speed for the robot.

2. **Motor Configuration:**
   - Enable the left and right motors.
   - Set the initial motor positions and velocities.

3. **Sensor Setup:**
   - Enable the proximity sensors.
   - Read sensor values during each simulation step.

4. **Main Loop:**
   - While the simulation is running:
     - Read sensor data from all eight proximity sensors.
     - Determine if there's a wall on the left, a corner on the left, or an obstacle in front.
     - Adjust the left and right motor speeds accordingly:
       - If there's a front wall, turn right in place.
       - If there's a left wall, drive forward.
       - If there's a left corner, steer right to avoid collision.

5. **Actuator Commands:**
   - Set the left and right motor velocities based on the calculated speeds.

6. **Exit Cleanup:**
   - Perform any necessary cleanup before exiting the simulation.

## Getting Started
🚀 To get started with this project, follow these steps:
1. Clone this repository to your local machine.
2. Open the Webots environment.
3. Load the robot model and the corresponding file.
4. Run the simulation and observe the robot's behavior.

## Contributing
🙌 Contributions are welcome! If you'd like to improve this project, please:
- Fork the repository.
- Create a new branch (`git checkout -b feature/improvement`).
- Make your changes.
- Commit your changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/improvement`).
- Create a new Pull Request.

## Other Group Members
👥
- Babar Ali
- Zain ul Abadeen
