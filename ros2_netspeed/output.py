#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class Output(Node):
    def __init__(self):
        super().__init__('output')
        self.sub_download = self.create_subscription(
            Float64,
            'download_speed',
            self.download_callback,
            10
        )
        self.sub_upload = self.create_subscription(
            Float64,
            'upload_speed',
            self.upload_callback,
            10
        )

    def download_callback(self, msg):
        self.get_logger().info(f"{msg.data}")

    def upload_callback(self, msg):
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node = Output()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
