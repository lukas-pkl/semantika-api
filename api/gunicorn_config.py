#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:49:43 2020

@author: lukas
"""

pidfile = "application.pid"
worker_tmp_dir = "/dev/shm"
worker_class = "gthread"
workers = 10
worker_connections = 100
timeout = 300
keepalive = 2
threads = 2
proc_name = "application"
bind = "0.0.0.0:8080"
backlog = 2048
accesslog = "-"
errorlog = "-"
user = "ubuntu"
group = "ubuntu"

