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
        self.latest_download = msg.data
        self.print_if_ready()

    def upload_callback(self, msg):
        self.latest_upload = msg.data
        self.print_if_ready()

    def print_if_ready(self):
        if self.latest_download is not None and self.latest_upload is not None:
            print(f"{self.latest_download:15.3f}  {self.latest_upload:15.3f}")
            self.latest_download = None
            self.latest_upload = None


def main():
    rclpy.init()
    node = Output()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
