#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import psutil
import time

class Upload(Node):
    def __init__(self):
        super().__init__('upload')

        self.pub = self.create_publisher(Float64, 'upload_speed', 10)

        # 初期値
        self.prev = psutil.net_io_counters()
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        now = psutil.net_io_counters()

        # bytes_sent の差分 → Mbps
        diff = now.bytes_sent - self.prev.bytes_sent
        mbps = diff * 8 / 1e6

        msg = Float64()
        msg.data = float(mbps)

        self.pub.publish(msg)
        self.prev = now
def main(args=None):
    rclpy.init(args=args)
    node = Upload()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

