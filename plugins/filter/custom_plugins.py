# Copyright (c) 2014 John Dewey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


class FilterModule(object):
    """ Custom filters are loaded by FilterModule objects """

    def filters(self):
        """ 
        FilterModule objects return a dict mapping filter names to
        filter functions.
        """
        return {
            'endpoint_servers': self.endpoint_servers,
        }

    def endpoint_servers(self, value, **kwargs):
        groups = kwargs.get('groups')
        port = kwargs.get('port')
        interface = kwargs.get('interface', 'ansible_eth1')
        family = kwargs.get('family', 'ipv4')
        servers_list = []
        for group in groups:
            host = value[group][interface][family]['address']
            host_with_port = "{host}:{port}".format(**locals())
            servers_list.append(host_with_port)
        return ','.join(servers_list)
