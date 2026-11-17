# V. 0.23

## **Improvements**

### Robot Integration

- Removed the dedicated TCP server for the Laser: all Laser commands and communications are now routed through the Robot TCP client.

## **Fixed Issues**

### Test Air Blow and Test Flip Wizard

- Fixed the Wizard for the **Flip** and **Blow** tests: added the motor status check with automatic enabling, subsequent verification and error handling in case the motor fails to enable.
