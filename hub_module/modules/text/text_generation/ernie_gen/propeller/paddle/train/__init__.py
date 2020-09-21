#   Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Propeller training"""

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import sys
import logging
from time import time

log = logging.getLogger(__name__)

from ernie_gen.propeller.paddle.train.monitored_executor import *
from ernie_gen.propeller.paddle.train.trainer import *
from ernie_gen.propeller.paddle.train.hooks import *
from ernie_gen.propeller.train.model import Model
from ernie_gen.propeller.paddle.train import exporter
from ernie_gen.propeller.paddle.train import distribution
from ernie_gen.propeller.paddle.train import metrics