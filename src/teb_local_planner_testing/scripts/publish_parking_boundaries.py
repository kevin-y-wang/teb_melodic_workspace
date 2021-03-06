#!/usr/bin/env python

# Author: christoph.roesmann@tu-dortmund.de

import rospy, math
from costmap_converter.msg import ObstacleArrayMsg, ObstacleMsg
from geometry_msgs.msg import PolygonStamped, Point32


def publish_obstacle_msg():
  pub = rospy.Publisher('/move_base/TebLocalPlannerROS/obstacles', ObstacleArrayMsg, queue_size=1)
  rospy.init_node("obstacle_msg")


  obstacle_msg = ObstacleArrayMsg() 
  obstacle_msg.header.stamp = rospy.Time.now()
  obstacle_msg.header.frame_id = "odom" # CHANGE HERE: odom/map

  # Add line obstacle
  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[0].id = 1
  line_start = Point32()
  line_start.x = -2.0
  line_start.y = 0.0
  line_end = Point32()
  line_end.x = -0.5
  line_end.y = 0.0
  obstacle_msg.obstacles[0].polygon.points = [line_start, line_end]
  
  # Add line obstacle
  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[1].id = 2
  line_start = Point32()
  line_start.x = -0.5
  line_start.y = 0.0
  line_end = Point32()
  line_end.x = -0.5
  line_end.y = -0.5
  obstacle_msg.obstacles[1].polygon.points = [line_start, line_end]

  # Add line obstacle
  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[2].id = 2
  line_start = Point32()
  line_start.x = -0.5
  line_start.y = -0.5
  line_end = Point32()
  line_end.x = 0.5
  line_end.y = -0.5
  obstacle_msg.obstacles[2].polygon.points = [line_start, line_end]

  # Add line obstacle
  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[3].id = 3
  line_start = Point32()
  line_start.x = 0.5
  line_start.y = -0.5
  line_end = Point32()
  line_end.x = 0.5
  line_end.y = 0.0
  obstacle_msg.obstacles[3].polygon.points = [line_start, line_end]

  # Add line obstacle
  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[4].id = 3
  line_start = Point32()
  line_start.x = 0.5
  line_start.y = 0.0
  line_end = Point32()
  line_end.x = 2.0
  line_end.y = 0.0
  obstacle_msg.obstacles[4].polygon.points = [line_start, line_end]

  r = rospy.Rate(10) # 10hz
  t = 0.0
  while not rospy.is_shutdown():
    
    pub.publish(obstacle_msg)
    
    r.sleep()



if __name__ == '__main__': 
  try:
    publish_obstacle_msg()
  except rospy.ROSInterruptException:
    pass

