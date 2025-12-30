#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import psutil
import time

class Download(Node):
    def __init__(self):
        super().__init__('download')

        self.pub = self.create_publisher(Float64, 'download_speed', 10)

        self.last_bytes = psutil.net_io_counters()
        self.last_time = time.time()

        self.timer = self.create_timer(1.0, self.measure_speed)

    def measure_speed(self):
        now_bytes = psutil.net_io_counters()
        now_time = time.time()

        dt = now_time - self.last_time
        if dt == 0:
            return

        download_bps = (now_bytes.bytes_recv - self.last_bytes.bytes_recv) / dt
        download_mbps = (download_bps * 8) / 1_000_000

        msg = Float64()
        msg.data = float(download_mbps)
        self.pub.publish(msg)

        self.last_bytes = now_bytes
        self.last_time = now_time

