#!/usr/bin/env python3

import argparse
import psutil
import matplotlib

# Like top command to get cpu percentage every second
psutil.cpu_percent(interval=1, percpu=True)

# Memory usage percentage
mem = psutil.virtual_memory()
mem.percent
