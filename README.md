# open4.0

### Overview

Open4.0 is an open-source framework (in progress) for intelligent IoT applications. 

### Milestone 1: Vision on the Edge

The edge app executable is written in Golang. Using the dynamic web UI, users can easily setup a camera connection over the network or CSI serial (e.g. Raspberry Pi cam) and build an analysis pipeline. Object detection models will use the ONNX standard to simplify the process of swapping models for performance trade-offs.

When running any model or analysis function, all availble insights are pooled into an 'insight pool'. The user can setup triggers to start actions based on the state of any one of the insights. For example, if the insight pool contains number of detected people in the image, the user can trigger an event when the number of people equals 0, then a different event when people detections exceed 10. 

Event triggers include posting a message to an open socket, publishing to a cloud service (MQTT or HTTP), or saving image and video to the file system.

![image](https://github.com/user-attachments/assets/14ecb017-a792-400a-a1dc-e7c8062434ca)


### Milestone 2: Cloud Connected

All the insights and configruation on the edge will be available in a cloud deployment. The full stack simply uses a Go binary, a Redis instance, and a Dockerized build of whatever custom analysis needs to happen (Python, C++). Using cloud repositories, it will be possible for the user to update software versions for edge devices, view live data, and publish custom trained ML models to the edge device.


![image](https://github.com/user-attachments/assets/95e65903-2ad3-4a42-b328-17aa0de669f0)
