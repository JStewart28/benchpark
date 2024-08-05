# Copyright 2023 Lawrence Livermore National Security, LLC and other
# Benchpark Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import sys

from ramble.appkit import *
from ramble.app.builtin.beatnik import Beatnik as BeatnikBase


class Beatnik(BeatnikBase):

    tags = ['chemistry','material-science','molecular-dynamics',
            'fft','particles','nbody','spatial-discretization',
            'large-scale','multi-node','single-node','sub-node',
            'mpi','network-collectives','network-point-to-point',
            'c++','python','kokkos','cuda','rocm','openmp','vectorization']
