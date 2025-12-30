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

        self.last_bytes = psutil.net_io_counters()
        self.last_time = time.time()

        self.timer = self.create_timer(1.0, self.measure_speed)

    def measure_speed(self):
        now_bytes = psutil.net_io_counters()
        now_time = time.time()

        dt = now_time - self.last_time
        if dt == 0:
            return

        upload_bps = (now_bytes.bytes_sent - self.last_bytes.bytes_sent) / dt
        upload_mbps = (upload_bps * 8) / 1_000_000

        msg = Float64()
        msg.data = float(upload_mbps)
        self.pub.publish(msg)

        self.last_bytes = now_bytes
        self.last_time = now_time
def main(args=None):
    rclpy.init(args=args)
    node = Upload()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
