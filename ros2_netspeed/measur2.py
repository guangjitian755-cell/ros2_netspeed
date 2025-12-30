#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import psutil
import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import speedtest

class Upload(Node):
    def __init__(self):
        super().__init__('upload')

        self.pub = self.create_publisher(Float64, 'upload_speed', 10)

        # Speedtest は1回だけ作る（403対策）
        self.st = speedtest.Speedtest()

        # 測定間隔は60秒（API制限対策）
        self.timer = self.create_timer(60.0, self.measure_speed)

    def measure_speed(self):
        try:
            upload = self.st.upload() / 1_000_000  # Mbps
            msg = Float64()
            msg.data = float(upload)
            self.pub.publish(msg)
        except Exception as e:
            self.get_logger().warn(f"Speedtest error: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = Upload()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

