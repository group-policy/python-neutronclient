# Copyright 2012 OpenStack Foundation.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

import logging
import string

from neutronclient.common import utils
from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListEndpoint(neutronV20.ListCommand):
    """List endpoints that belong to a given tenant."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.ListEndpoint')
    _formatters = {}
    list_columns = ['id', 'name', 'description', 'endpoint_group_id']
    pagination_support = True
    sorting_support = True


class ShowEndpoint(neutronV20.ShowCommand):
    """Show information of a given endpoint."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.ShowEndpoint')


class CreateEndpoint(neutronV20.CreateCommand):
    """Create a endpoint for a given tenant."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.CreateEndpoint')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--description',
            help=_('Description of the endpoint'))
        parser.add_argument(
            '--endpoint-group', metavar='EPG',
            default='',
            help=_('endpoint_group uuid'))
        parser.add_argument(
            '--port',
            default='',
            help=_('Neutron Port'))
        parser.add_argument(
            'name', metavar='NAME',
            help=_('Name of endpoint to create'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'description'])
        if parsed_args.endpoint_group:
            body[self.resource]['endpoint_group_id'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'endpoint_group',
                    parsed_args.endpoint_group)
        if parsed_args.port:
            body[self.resource]['port_id'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'port',
                    parsed_args.port)
        return body


class DeleteEndpoint(neutronV20.DeleteCommand):
    """Delete a given endpoint."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.DeleteEndpoint')


class UpdateEndpoint(neutronV20.UpdateCommand):
    """Update endpoint's information."""

    resource = 'endpoint'
    log = logging.getLogger(__name__ + '.UpdateEndpoint')


class ListEndpointGroup(neutronV20.ListCommand):
    """List endpoint_groups that belong to a given tenant."""

    resource = 'endpoint_group'
    log = logging.getLogger(__name__ + '.ListEndpointGroup')
    list_columns = ['id', 'name', 'description']
    pagination_support = True
    sorting_support = True


class ShowEndpointGroup(neutronV20.ShowCommand):
    """Show information of a given endpoint_group."""

    resource = 'endpoint_group'
    log = logging.getLogger(__name__ + '.ShowEndpointGroup')


class CreateEndpointGroup(neutronV20.CreateCommand):
    """Create a endpoint_group for a given tenant."""

    resource = 'endpoint_group'
    log = logging.getLogger(__name__ + '.CreateEndpointGroup')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--description',
            help=_('Description of the endpoint_group'))
        parser.add_argument(
            'name', metavar='NAME',
            help=_('Name of endpoint_group to create'))
        parser.add_argument(
            '--l2-policy', metavar='L2_POLICY',
            default='',
            help=_('L2 policy uuid'))
        parser.add_argument(
            '--provided-contracts', type=utils.str2dict,
            default={},
            help=_('Dictionary of provided contract uuids'))
        parser.add_argument(
            '--consumed-contracts', type=utils.str2dict,
            default={},
            help=_('Dictionary of consumed contract uuids'))
        parser.add_argument(
            '--subnets', type=string.split,
            help=_('Subnet to map the endpoint group'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }

        if parsed_args.l2_policy:
            body[self.resource]['l2_policy_id'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'l2_policy',
                    parsed_args.l2_policy)

        if parsed_args.provided_contracts:
            for key in parsed_args.provided_contracts.keys():
                id_key = neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'contract',
                    key)
                parsed_args.provided_contracts[id_key] = \
                    parsed_args.provided_contracts.pop(key)

        if parsed_args.consumed_contracts:
            for key in parsed_args.consumed_contracts.keys():
                id_key = neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'contract',
                    key)
                parsed_args.consumed_contracts[id_key] = \
                    parsed_args.consumed_contracts.pop(key)

        if parsed_args.subnets:
            for subnet in parsed_args.subnets:
                subnet_id = neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'subnet',
                    subnet)
                parsed_args.subnets.remove(subnet)
                parsed_args.subnets.append(subnet_id)

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'description',
                                'provided_contracts', 'subnets',
                                'consumed_contracts'])

        return body


class DeleteEndpointGroup(neutronV20.DeleteCommand):
    """Delete a given endpoint_group."""

    resource = 'endpoint_group'
    log = logging.getLogger(__name__ + '.DeleteEndpointGroup')


class UpdateEndpointGroup(neutronV20.UpdateCommand):
    """Update endpoint_group's information."""

    resource = 'endpoint_group'
    log = logging.getLogger(__name__ + '.UpdateEndpointGroup')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--description',
            help=_('Description of the endpoint_group'))
        parser.add_argument(
            '--l2-policy', metavar='L2_POLICY',
            help=_('L2 policy uuid'))
        parser.add_argument(
            '--provided-contracts', type=utils.str2dict,
            help=_('Dictionary of provided contract uuids'))
        parser.add_argument(
            '--consumed-contracts', type=utils.str2dict,
            help=_('Dictionary of consumed contract uuids'))
        parser.add_argument(
            '--subnets', type=string.split,
            help=_('Subnet to map the endpoint group'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }
        if parsed_args.l2_policy:
            body[self.resource]['l2_policy_id'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'l2_policy',
                    parsed_args.l2_policy)

        if parsed_args.provided_contracts:
            for key in parsed_args.provided_contracts.keys():
                id_key = neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'contract',
                    key)
                parsed_args.provided_contracts[id_key] = \
                    parsed_args.provided_contracts.pop(key)

        if parsed_args.consumed_contracts:
            for key in parsed_args.consumed_contracts.keys():
                id_key = neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'contract',
                    key)
                parsed_args.consumed_contracts[id_key] = \
                    parsed_args.consumed_contracts.pop(key)

        if parsed_args.subnets:
            for subnet in parsed_args.subnets:
                subnet_id = neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'subnet',
                    subnet)
                parsed_args.subnets.remove(subnet)
                parsed_args.subnets.append(subnet_id)

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'description',
                                'provided_contracts', 'subnets',
                                'consumed_contracts'])

        return body


class ListL2Policy(neutronV20.ListCommand):
    """List L2 Policies that belong to a given tenant."""

    resource = 'l2_policy'
    log = logging.getLogger(__name__ + '.ListL2Policy')
    _formatters = {}
    list_columns = ['id', 'name', 'description', 'l3_policy_id']
    pagination_support = True
    sorting_support = True


class ShowL2Policy(neutronV20.ShowCommand):
    """Show information of a given l2_policy."""

    resource = 'l2_policy'
    log = logging.getLogger(__name__ + '.ShowL2Policy')


class CreateL2Policy(neutronV20.CreateCommand):
    """Create a bridge_domain for a given tenant."""

    resource = 'l2_policy'
    log = logging.getLogger(__name__ + '.CreateL2Policy')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--description',
            help=_('Description of the l2_policy'))
        parser.add_argument(
            '--network',
            help=_('Network to map the l2_policy'))
        parser.add_argument(
            '--l3-policy',
            default='',
            help=_('l3_policy uuid'))
        parser.add_argument(
            'name', metavar='NAME',
            help=_('Name of l2_policy to create'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'description'])
        if parsed_args.l3_policy:
            body[self.resource]['l3_policy_id'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'l3_policy',
                    parsed_args.l3_policy)
        if parsed_args.network:
            body[self.resource]['network_id'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'network',
                    parsed_args.network)
        return body


class DeleteL2Policy(neutronV20.DeleteCommand):
    """Delete a given l2_policy."""

    resource = 'l2_policy'
    log = logging.getLogger(__name__ + '.DeleteL2Policy')


class UpdateL2Policy(neutronV20.UpdateCommand):
    """Update l2_policy's information."""

    resource = 'l2_policy'
    log = logging.getLogger(__name__ + '.UpdateL2Policy')


class ListL3Policy(neutronV20.ListCommand):
    """List l3_policies that belong to a given tenant."""

    resource = 'l3_policy'
    log = logging.getLogger(__name__ + '.ListL3Policy')
    _formatters = {}
    list_columns = ['id', 'name', 'description', 'ip_pool',
                    'subnet_prefix_length']
    pagination_support = True
    sorting_support = True


class ShowL3Policy(neutronV20.ShowCommand):
    """Show information of a given l3_policy."""

    resource = 'l3_policy'
    log = logging.getLogger(__name__ + '.ShowL3Policy')


class CreateL3Policy(neutronV20.CreateCommand):
    """Create a l3_policy for a given tenant."""

    resource = 'l3_policy'
    log = logging.getLogger(__name__ + '.CreateL3Policy')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--description',
            help=_('Description of the l3_policy'))
        parser.add_argument(
            '--ip-version',
            type=int,
            default=4, choices=[4, 6],
            help=_('IP version, default is 4'))
        parser.add_argument(
            '--ip-pool',
            help=_('CIDR of IP pool to create, default is 10.0.0.0/8'))
        parser.add_argument(
            '--subnet-prefix-length',
            type=int,
            default=24,
            help=_('Subnet prefix length, default is 24'))
        parser.add_argument(
            'name', metavar='NAME',
            help=_('Name of l3_policy to create'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'description',
                                'ip_version', 'ip_pool',
                                'subnet_prefix_length'])

        return body


class DeleteL3Policy(neutronV20.DeleteCommand):
    """Delete a given l3_policy."""

    resource = 'l3_policy'
    log = logging.getLogger(__name__ + '.DeleteL3Policy')


class UpdateL3Policy(neutronV20.UpdateCommand):
    """Update l3_policy's information."""

    resource = 'l3_policy'
    log = logging.getLogger(__name__ + '.UpdateL3Policy')
