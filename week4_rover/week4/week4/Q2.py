#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from math import pi
import random

class RoverControl(Node):
    def __init__(self):
        super().__init__('Controller')
        self.publisher=self.create_publisher(Float64MultiArray,'/rover/control_input',10)
        self.timer = self.create_timer(2,self.timer_callback)
        self.i=1
        
    def timer_callback(self):
        msg=Float64MultiArray()
        msg1=Float64MultiArray()
        if self.i%5==1:
            msg.data=[0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0]
            self.publisher.publish(msg)
        elif self.i%5==2:
            msg.data=[-pi/2,-pi/2,-pi/2,-pi/2,0.0,0.0,0.0,0.0]
            self.publisher.publish(msg)
        elif self.i%5==3:
            msg.data=[0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0]
            self.publisher.publish(msg)
        elif self.i%5==4:
            j=random.randint(1,2)
            if j==1:         
                msg.data=[0.0,0.0,0.0,0.0,1.0,-1.0,1.0,-1.0]                    
                self.publisher.publish(msg)
            else:
                msg.data=[-pi/4,pi/4,pi/4,-pi/4,1.0,1.0,1.0,1.0]
                self.publisher.publish(msg)
        elif self.i%5==0:
            msg.data=[pi/4,pi/4,pi/4,pi/4,0.0,0.0,0.0,0.0]
            self.publisher.publish(msg)
            msg1.data=[0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0]
            self.publisher.publish(msg1)
        self.i+=1
            
def main(args=None):
    rclpy.init(args=args)
    rover_control = RoverControl()
    rclpy.spin(rover_control)

if __name__ == '__main__':
    main()
            
