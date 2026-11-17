# V. 0.24

## **New Features**

### Control Cameras

- Added management of **3 independent control cameras**, associated with FLB1, FLB2 and FLB3 respectively.
- Implemented the `start_control_` robot command with support for custom parameters, forwarded to the VisionPro scripts.
- Added management of customizable VisionPro scripts, with text output and `CogRecord` images including the graphical results.
- Implemented dedicated Main Tasks for the control cameras, with error handling, logging and sending of the results to the robot.
- Enabled the execution of checks even without a connected robot, to perform local tests from the HMI.
- Added shared HMI pages for camera configuration, VisionPro configuration and runtime display of the three control cameras.

## **Improvements**

### Clearances (Histograms)

- Updated the region management for all 8 models, 8 Histograms and 3 cameras, preserving the position, size and geometry of the saved ROIs.

## **Fixed Issues**

### Recipes

- Fixed the reset of the Histogram ROIs when changing recipe.
