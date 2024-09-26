#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 LG Electronics Inc.
# SPDX-License-Identifier: Apache-2.0
import os.path

UBUNTU_COMMANDS = [
    "fosslight_dependency -p tests/test_nuget -o tests/result/nuget1",
    "fosslight_dependency -p tests/test_nuget2 -o tests/result/nuget2"
]

DIST_PATH = os.path.join(os.path.abspath(os.sep), "dist", "cli.exe")
INPUT_PATH = os.path.join("tests", "test_nuget")
OUTPUT_PATH = os.path.join("tests", "result", "nuget1")
INPUT_PATH2 = os.path.join("tests", "test_nuget2")
OUTPUT_PATH2 = os.path.join("tests", "result", "nuget2")

WINDOW_COMMANDS = [
    f"{DIST_PATH} -p {INPUT_PATH} -o {OUTPUT_PATH}",
    f"{DIST_PATH} -p {INPUT_PATH2} -o {OUTPUT_PATH2}"
]


def test_ubuntu(run_command):
    for command in UBUNTU_COMMANDS:
        return_code, stdout, stderr = run_command(command)
        assert return_code == 0, f"Command failed: {command}\nstdout: {stdout}\nstderr: {stderr}"


def test_windows(run_command):
    for command in WINDOW_COMMANDS:
        return_code, stdout, stderr = run_command(command)
        assert return_code == 0, f"Command failed: {command}\nstdout: {stdout}\nstderr: {stderr}"