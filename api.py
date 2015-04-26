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


import falcon
import simplejson as js
from uuid import uuid4


def js_response(req, resp, resource):
    resp.body = js.dumps(resp.body, sort_keys=True, indent=4 * ' ')


def js_body(req, resp, resource, params):
    resp.body = {}


def js_post_validate(req, resp, resource, params):
    """Handles POST requests"""
    try:
        raw_json = req.stream.read()
    except Exception as ex:
        raise falcon.HTTPError(falcon.HTTP_400,
                               'Error',
                               ex.message)

    try:
        result_json = js.loads(raw_json, encoding='utf-8')
    except ValueError:
        raise falcon.HTTPError(falcon.HTTP_400,
                               'Malformed JSON',
                               'Could not decode the Gate body. The '
                               'JSON was incorrect.')


class Constants:
    """ for constants"""
    pass


class ReqResource(Constants):
    @falcon.before(js_body)
    @falcon.after(js_response)
    def on_get(self, req, resp, pipe_id):
        """Handles GET requests"""

        resp.status = falcon.HTTP_201
        resp.body['expire'] = 10

    @falcon.before(js_body)
    @falcon.after(js_response)
    def on_post(self, req, resp, secret):
        pass


class InfoResource(Constants):
    @falcon.before(js_body)
    @falcon.after(js_response)
    def on_get(self, req, resp, pipe_id):
        pass


# falcon.API instances are callable WSGI apps
app = falcon.API()

# things will handle all requests to the '/things' URL path
app.add_route('/api/pipe/{pipe_id}', ReqResource())