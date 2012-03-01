#! /usr/bin/env python2

import sys
import subprocess
import time
import psutil
import matplotlib
probe_interval = 0.2

if len(sys.argv)< 2:
    sys.stderr.write ("usage: " + sys.argv[0] + " <command to profile>")
    sys.exit(2)

import matplotlib.pyplot as plt
proc = subprocess.Popen(sys.argv[1:])
p = psutil.Process(proc.pid)
i = 0
x = []
stats_rss = []
stats_vms = []
stats_usr = []
stats_sys = []
stats_io_r = []
stats_io_w = []
stats_io_r_b = []
stats_io_w_b = []
while proc.poll() is None:
    m = p.get_memory_info()
    c = p.get_cpu_times()
    io = p.get_io_counters()
    x.append(i)
    stats_rss.append(m[0])
    stats_vms.append(m[1])
    stats_usr.append(c[0])
    stats_sys.append(c[1])
    stats_io_r.append(io[0])
    stats_io_w.append(io[1])
    stats_io_r_b.append(io[2])
    stats_io_w_b.append(io[3])
    time.sleep(probe_interval)
    i += probe_interval

plt.figure()
plt.plot(x, stats_rss, label="Rss")
plt.plot(x, stats_vms, label="Vms")
plt.xlabel("Execution time (seconds)")
plt.ylabel("Memory Profile")
plt.legend(loc="upper left")
plt.savefig("profile_memory.png")

plt.figure()
plt.plot(x, stats_usr, label="Usr")
plt.plot(x, stats_sys, label="Sys")
plt.xlabel("Execution time (seconds)")
plt.ylabel("CPU Profile")
plt.legend(loc="upper left")
plt.savefig("profile_cpu.png")

plt.figure()
plt.plot(x, stats_io_r, label="IO Reads")
plt.plot(x, stats_io_w, label="IO Writes")
plt.plot(x, stats_io_r_b, label="IO Reads Bytes")
plt.plot(x, stats_io_w_b, label="IO Writes Bytes")
plt.xlabel("Execution time (seconds)")
plt.ylabel("IO Profile")
plt.legend(loc="upper left")
plt.savefig("profile_io.png")

sys.exit (proc.returncode)
