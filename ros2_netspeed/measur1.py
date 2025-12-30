#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import speedtest

class Download(Node):
    def __init__(self):
        super().__init__('download')

        self.pub = self.create_publisher(Float64, 'download_speed', 10)

        self.st = speedtest.Speedtest()
        self.timer = self.create_timer(60.0, self.measure_speed)

    def measure_speed(self):
        try:
            download = self.st.download() / 1_000_000  # Mbps
            msg = Float64()
            msg.data = float(download)
            self.pub.publish(msg)
        except Exception as e:
            self.get_logger().warn(f"Speedtest error: {e}")
def main(args=None):
    rclpy.init(args=args)
    node = Download()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

