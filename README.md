# First_Task_PubSub
This repo has 3 code files, the 'Pub.py', 'PubSub.py' and 'Sub.py'.
Pub performs the role of getting an input and encrypting it, pubsub has to recieve message from the pub file, decrypt it, and publish it to the sub node, which simply prints whatever data it gets from the pubsub node.
Steps to run these (in order).
1- Open a new terminal, and start the master node with the 'roscore' command.
2- In new terminal, run the pub node, by using the command 'rosrun task pub.py', since all my codes are stored under the 'task' package in src folder of catkin workspace.
3- Give input when this node runs, and hit enter.
4- Open a new terminal, and run the 'pubsub', by running the 'rosrun task pubsub.py' command.
5- Open a new terminal, and run the 'sub', by running the 'rosrun task sub.py' command.
Screenshots of outputs
![running_roscore](https://github.com/YJawale/First_Task_PubSub/assets/125810583/39f9cbff-e841-4bd0-9406-5907549e2926)
![running_pub](https://github.com/YJawale/First_Task_PubSub/assets/125810583/abd3dadd-ea4b-424e-b535-2cd389900193)
![running_pubsub](https://github.com/YJawale/First_Task_PubSub/assets/125810583/114bfde3-021b-485f-bf58-95dc02123a58)
![running_sub](https://github.com/YJawale/First_Task_PubSub/assets/125810583/da4ee7ba-df86-4687-b7b4-1300730831cd)
