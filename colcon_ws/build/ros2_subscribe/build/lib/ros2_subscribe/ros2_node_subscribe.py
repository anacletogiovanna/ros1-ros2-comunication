import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Subscriber(Node):
    def __init__(self):
        super().__init__('ros2_subscribe')
        self.subscription = self.create_subscription(
            Twist,
            'ros2_topic_subscribe',
            self.listener_callback,
            1)
        self.subscription
    def listener_callback(self, msg):
        msg_values  = ["linear: \n " + str(msg.linear.x) + "\n", str(msg.linear.y) + "\n", str(msg.linear.z) + "\n", "angular: \n " + str(msg.angular.x) + "\n", str(msg.angular.y) + "\n", str(msg.angular.z) + "\n"]
        self.get_logger().info("".join(msg_values))


def main(args=None):
    rclpy.init(args=args)
    
    subscriber = Subscriber()
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
