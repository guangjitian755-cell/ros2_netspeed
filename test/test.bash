#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Hikaru Yoshida
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch ros2_netspeed netspeed.launch.py > /tmp/netspeed.log

grep -E '[0-9]+\.[0-9]+\s+[0-9]+\.[0-9]+' /tmp/netspeed.log
