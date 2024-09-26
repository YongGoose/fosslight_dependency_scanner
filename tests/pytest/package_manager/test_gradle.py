#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
import os

UBUNTU_COMMANDS = [
    "fosslight_dependency -p tests/test_gradle/jib -o tests/result/gradle",
    "fosslight_dependency -p tests/test_gradle2 -o tests/result/gradle2"
]

DIST_PATH = os.path.join(os.path.abspath(os.sep), "dist", "cli.exe")
INPUT_PATH = os.path.join("tests", "test_gradle", "jib")
OUTPUT_PATH = os.path.join("tests", "result", "gradle")
INPUT_PATH2 = os.path.join("tests", "test_gradle2")
OUTPUT_PATH2 = os.path.join("tests", "result", "gradle2")

WINDOW_COMMANDS = [
    f"{DIST_PATH} -p {INPUT_PATH} -o {OUTPUT_PATH} -m gradle",
    f"{DIST_PATH} -p {INPUT_PATH2} -o {OUTPUT_PATH2} -m gradle",
]

def test_ubuntu(run_command):
    for command in UBUNTU_COMMANDS:
        return_code, stdout, stderr = run_command(command)
        assert return_code == 0, f"Command failed: {command}\nstdout: {stdout}\nstderr: {stderr}"


def test_windows(run_command):
    for command in WINDOW_COMMANDS:
        return_code, stdout, stderr = run_command(command)
        assert return_code == 0, f"Command failed: {command}\nstdout: {stdout}\nstderr: {stderr}"
