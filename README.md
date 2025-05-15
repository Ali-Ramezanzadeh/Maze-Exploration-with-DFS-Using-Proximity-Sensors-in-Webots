# Maze Exploration with DFS Using Proximity Sensors in Webots

This project implements a Depth-First Search (DFS) algorithm for autonomous maze traversal using a simulated e-Puck robot in Webots. The robot detects and navigates through walls using only proximity sensors, without relying on GPS or Lidar. It explores the maze, records movement directions, and generates a schematic map of the environment.

## Project Overview

- Simulator: Webots 2023b  
- Robot: e-Puck  
- Sensors Used:  
  - Proximity Sensors (Front, Back, Left, Right)  
  - No GPS  
  - No Lidar  
- Control Strategy:  
  DFS-based navigation using internal direction tracking
- Goal:  
  Explore all reachable areas of the maze, detect walls per cell, and print a schematic representation of the discovered map

## Algorithm Highlights

- DFS Traversal:  
  The robot explores in a fixed direction priority (Left → Forward → Right → Back), recursively visiting unvisited paths
- Wall Detection:  
  Wall presence is inferred from calibrated proximity sensor readings
- Orientation Management:  
  Internal counters and angle tracking are used to simulate orientation without positional sensors
- Mapping:  
  A 4x4 matrix stores encoded wall information as four-digit values representing [Front, Back, Right, Left]

## Features

- Custom real-time wall calibration using differential proximity sensor readings
- Delay-based movement control without using time.sleep()
- Movement direction counters for reconstructing traveled paths
- Schematic ASCII map output at the end of traversal

## How to Run

1. Install Webots 2023b
2. Open your world file and add the e-Puck robot
3. Attach the `my_controller.py` script to the robot
4. Run the simulation and monitor the robot’s exploration behavior
5. View the printed schematic map in the Webots console

## File Structure

├── my_controller.py # Main control script for DFS maze traversal
├── README.md # Documentation


## Why DFS?

Depth-First Search is a simple and effective approach for fully exploring mazes or tree structures. It uses minimal memory and is well-suited to sensor-limited robots that do not rely on external localization systems.

## Learning Outcomes

- Implementing DFS in a robotics simulation environment
- Navigating using only local sensor input
- Designing algorithms under hardware constraints (no GPS, no Lidar)
- Handling robot orientation, movement, and mapping in discrete space

