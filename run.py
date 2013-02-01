#!/usr/bin/env python
# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

from subprocess import call
from sys import argv
import os
import subprocess
import workerpool
import multiprocessing

class SimulationJob (workerpool.Job):
    "Job to simulate things"
    def __init__ (self, cmdline):
        self.cmdline = cmdline
    def run (self):
        print (" ".join (self.cmdline))
        subprocess.call (self.cmdline)

pool = workerpool.WorkerPool(size = multiprocessing.cpu_count())

class Runner:
    # def congestion_zoom (self):
    #     cmdline = ["./build/congestion-zoom-ndn"]
    #     job = SimulationJob (cmdline)
    #     pool.put (job)

    #     cmdline = ["./build/congestion-zoom-tcp"]
    #     job = SimulationJob (cmdline)
    #     pool.put (job)

    # def congestion_pop (self):
    #     runs = range(1,101)
    #     for run in runs:
    #         cmdline = ["./build/congestion-pop-ndn",
    #                    "--run=%d" % run
    #                    ]
    #         job = SimulationJob (cmdline)
    #         pool.put (job)

    #         cmdline = ["./build/congestion-pop-tcp",
    #                    "--run=%d" % run
    #                    ]
    #         job = SimulationJob (cmdline)
    #         pool.put (job)

try:
    runner = Runner ()
    # runner.congestion_zoom()
    runner.congestion_pop()

finally:
    pool.shutdown ()
    pool.wait ()

print "\n\n >>> FINISHED <<< \n\n"
