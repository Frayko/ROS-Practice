#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist, Pose
from turtlesim.msg import Pose as TurtlePose
from turtlesim.srv import Spawn
import math

class TurtlesRunner:
    def __init__(self):
        rospy.init_node('turtles_runner')

        rospy.wait_for_service('spawn')
        spawner = rospy.ServiceProxy('spawn', Spawn)
        spawner(0, 0, 0, 'turtle2')

        self.turtle1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        self.turtle2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=1)
        self.turtle1_sub = rospy.Subscriber('/turtle1/pose', TurtlePose, self.turtle1_callback)
        self.turtle2_sub = rospy.Subscriber('/turtle2/pose', TurtlePose, self.turtle2_callback)
        
        self.rate = rospy.Rate(10)
        self.turtle1_pose = None
        self.turtle2_pose = None

    def turtle1_callback(self, data):
        self.turtle1_pose = data

    def turtle2_callback(self, data):
        self.turtle2_pose = data

    def start(self):
        while not rospy.is_shutdown():
            if self.turtle1_pose and self.turtle2_pose:
                self.speed = rospy.get_param('~speed', 1.0)
                dx = self.turtle1_pose.x - self.turtle2_pose.x
                dy = self.turtle1_pose.y - self.turtle2_pose.y
                angle = math.atan2(dy, dx)
                distance = math.sqrt(dx ** 2 + dy ** 2)
                cmd = Twist()
                cmd.linear.x = self.speed * distance
                cmd.angular.z = 8.0 * (angle - self.turtle2_pose.theta)
                self.turtle2_pub.publish(cmd)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        turtles_runner = TurtlesRunner()
        turtles_runner.start()
    except rospy.ROSInterruptException:
        pass