#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import math
import random

class RoverControl(Node):
    def __init__(self):
        super().__init__('Controller')
        self.publisher=self.create_publisher(Float64MultiArray,'/rover/control_input',10)
        self.timer = self.create_timer(2,self.timer_callback)
        self.i=1
        
        def timer_callback(self):
            if self.i==1:
                self.publisher.publish([0,0,0,0,1,1,1,1])
            elif self.i==2:
                self.publisher.publish([-pi/2,-pi/2,-pi/2,-pi/2,0,0,0,0])
            elif self.i==3:
                self.publisher.publish([0,0,0,0,1,1,1,1])
            elif self.i==4:
                j=random.randint(1,2)
                if j==1:
                    self.publisher.publish([0,0,0,0,1,-1,1,-1])
                else:
                    self.publisher.publish([-pi/4,pi/4,pi/4,-pi/4,1,1,1,1])
            elif self.i==5:
                self.publisher.publish([pi/4,pi/4,pi/4,pi/4,0,0,0,0])
                self.publisher.publish([0,0,0,0,1,1,1,1])
            self.i+=1
            
            
        
