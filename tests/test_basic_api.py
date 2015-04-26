# Pipe -- API gateway
# Copyright (C) 2015  Jan Karásek
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import sys

sys.path.append('../Gate')

import pytest
import Gate.Api
import redis


class TestClass:
    def setup(self):
        self.redis = redis.StrictRedis()

        self.req_data = {
            "public_token": "fgagasd",
            "timestamp": 12354564641,
            "pipe": "basic-test"
        }

    def test_new_request_valid(self):
        req = Gate.Api.Request(self.redis)

        assert req.new(self.req_data)

    def test_new_request_invalid(self):
        req = Gate.Api.Request(self.redis)

        invalid_data = self.req_data
        invalid_data['pipe'] = 12345

        assert req.new(self.req_data) == False