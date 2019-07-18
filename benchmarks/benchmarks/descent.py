# Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import greedy


class SteepestGradientDescentCython(object):

    def time_single_flip_1_read(self):
        num_samples = 1
        linear_biases = [2, 2]
        coupler_starts, coupler_ends, coupler_weights = [0], [1], [-1]
        initial_states = np.tile([1, 1], (num_samples, 1), dtype=np.int8)

        samples, energies = greedy.descent.steepest_gradient_descent(
            num_samples, linear_biases, coupler_starts, coupler_ends,
            coupler_weights, initial_states)

    def time_single_flip_1k_reads(self):
        num_samples = 1000
        linear_biases = [2, 2]
        coupler_starts, coupler_ends, coupler_weights = [0], [1], [-1]
        initial_states = np.tile([1, 1], (num_samples, 1), dtype=np.int8)

        samples, energies = greedy.descent.steepest_gradient_descent(
            num_samples, linear_biases, coupler_starts, coupler_ends,
            coupler_weights, initial_states)

    def time_single_flip_1M_reads(self):
        num_samples = 1000000
        linear_biases = [2, 2]
        coupler_starts, coupler_ends, coupler_weights = [0], [1], [-1]
        initial_states = np.tile([1, 1], (num_samples, 1), dtype=np.int8)

        samples, energies = greedy.descent.steepest_gradient_descent(
            num_samples, linear_biases, coupler_starts, coupler_ends,
            coupler_weights, initial_states)
