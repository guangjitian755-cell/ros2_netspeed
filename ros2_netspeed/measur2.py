#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import speedtest

class Upload(Node):
    def __init__(self):
        super().__init__('upload')
        self.pub = self.create_publisher(Float64, 'upload_speed', 10)
        self.timer = self.create_timer(1.0, self.measure_speed)

    def measure_speed(self):
        st = speedtest.Speedtest()
        upload = st.upload() / 1_000_000

        msg = Float64()
        msg.data = float(upload)

        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Upload()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
