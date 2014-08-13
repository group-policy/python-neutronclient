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

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListServiceChainInstance(neutronV20.ListCommand):
    """List service chain instances that belong to a given tenant."""

    resource = 'servicechain_instance'
    log = logging.getLogger(__name__ + '.ListServiceChainInstance')
    _formatters = {}
    list_columns = ['id', 'name', 'description', 'servicechain_spec', 'port']
    pagination_support = True
    sorting_support = True


class ShowServiceChainInstance(neutronV20.ShowCommand):
    """Show information of a given service chain instance."""

    resource = 'servicechain_instance'
    log = logging.getLogger(__name__ + '.ShowServiceChainInstance')


class CreateServiceChainInstance(neutronV20.CreateCommand):
    """Create a service chain instance."""

    resource = 'servicechain_instance'
    log = logging.getLogger(__name__ + '.CreateServiceChainInstance')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name',
            help=_('Name for the Service Chain Instance.'))
        parser.add_argument(
            '--description',
            help=_('Description of the Service Chain Instance.'))
        parser.add_argument(
            '--service-chain-spec', dest='servicechain_spec',
            help=_('Service Chain Spec ID or the Service Chain Spec name'))
        parser.add_argument(
            '--port', dest='port_id',
            help=_('Neutron Port to be attached to the Service Instance.'))
        parser.add_argument(
            '--config-params', dest='config_params',
            help=_('Service Configuration Parameters for the Service Chain '
                   'Node.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }
        if parsed_args.servicechain_spec:
            body[self.resource]['servicechain_spec'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'servicechain_spec',
                    parsed_args.servicechain_spec)
        if parsed_args.port_id:
            body[self.resource]['port_id'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'port',
                    parsed_args.port_id)

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'description',
                                'servicechain_spec', 'port_id',
                                'config_params'])
        return body


class UpdateServiceChainInstance(neutronV20.UpdateCommand):
    """Update a given service chain instance."""

    resource = 'servicechain_instance'
    log = logging.getLogger(__name__ + '.UpdateServiceChainInstance')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--service-chain-spec', dest='servicechain_spec',
            help=_('Service Chain Spec ID or the Service Chain Spec name'))
        parser.add_argument(
            '--port', dest='port_id',
            help=_('Neutron Port to be attached to the Service Instance.'))
        parser.add_argument(
            '--config-params', dest='config_params',
            help=_('Service Configuration Parameters for the Service Chain '
                   'Node.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }
        if parsed_args.servicechain_spec:
            body[self.resource]['servicechain_spec'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'servicechain_spec',
                    parsed_args.servicechain_spec)
        if parsed_args.port_id:
            body[self.resource]['port_id'] = \
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(), 'port',
                    parsed_args.port_id)

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'description',
                                'servicechain_spec', 'port_id',
                                'config_params'])
        return body


class DeleteServiceChainInstance(neutronV20.DeleteCommand):
    """Delete a given service chain instance."""

    resource = 'servicechain_instance'
    log = logging.getLogger(__name__ + '.DeleteServiceChainInstance')


class ListServiceChainNode(neutronV20.ListCommand):
    """List service chain nodes that belong to a given tenant."""

    resource = 'servicechain_node'
    log = logging.getLogger(__name__ + '.ListServiceChainNode')
    _formatters = {}
    list_columns = ['id', 'name', 'description', 'service_type']
    pagination_support = True
    sorting_support = True


class ShowServiceChainNode(neutronV20.ShowCommand):
    """Show information of a given service chain node."""

    resource = 'servicechain_node'
    log = logging.getLogger(__name__ + '.ShowServiceChainNode')


class CreateServiceChainNode(neutronV20.CreateCommand):
    """Create a service chain node."""

    resource = 'servicechain_node'
    log = logging.getLogger(__name__ + '.CreateServiceChainNode')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name',
            help=_('Name for the Service Chain Node.'))
        parser.add_argument(
            '--description',
            help=_('Description of the Service Chain Node.'))
        parser.add_argument(
            '--servicetype', dest='service_type',
            help=_('Service type ID or the Service Type name'))
        parser.add_argument(
            '--config',
            help=_('Service Configuration for the Service Chain Node.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'service_type', 'config',
                                'tenant_id', 'description'])
        return body


class UpdateServiceChainNode(neutronV20.UpdateCommand):
    """Update a given service chain node."""

    resource = 'servicechain_node'
    log = logging.getLogger(__name__ + '.UpdateServiceChainNode')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--servicetype', dest='service_type',
            help=_('Service type ID or the Service Type name'))
        parser.add_argument(
            '--config',
            help=_('Service Configuration for the Service Chain Node.'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }
        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'service_type', 'config',
                                'tenant_id', 'description'])
        return body


class DeleteServiceChainNode(neutronV20.DeleteCommand):
    """Delete a given service chain node."""

    resource = 'servicechain_node'
    log = logging.getLogger(__name__ + '.DeleteServiceChainNode')


class ListServiceChainSpec(neutronV20.ListCommand):
    """List service chain specs that belong to a given tenant."""

    resource = 'servicechain_spec'
    log = logging.getLogger(__name__ + '.ListServiceChainSpec')
    _formatters = {}
    list_columns = ['id', 'name', 'description', 'nodes']
    pagination_support = True
    sorting_support = True


class ShowServiceChainSpec(neutronV20.ShowCommand):
    """Show information of a given service chain spec."""

    resource = 'servicechain_spec'
    log = logging.getLogger(__name__ + '.ShowServiceChainSpec')


class CreateServiceChainSpec(neutronV20.CreateCommand):
    """Create a service chain spec."""

    resource = 'servicechain_spec'
    log = logging.getLogger(__name__ + '.CreateServiceChainSpec')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name',
            help=_('Name for the Service Chain Spec.'))
        parser.add_argument(
            '--description',
            help=_('Description of the Service Chain Specification.'))
        parser.add_argument(
            '--nodes', metavar='NODES', type=string.split,
            help=_('Service Chain Node ID or name of the Service Chain Node'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }

        if parsed_args.nodes:
            body[self.resource]['nodes'] = [
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(),
                    'servicechain_node',
                    elem) for elem in parsed_args.nodes]

        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['name', 'tenant_id', 'description'])
        return body


class UpdateServiceChainSpec(neutronV20.UpdateCommand):
    """Update a given service chain spec."""

    resource = 'servicechain_spec'
    log = logging.getLogger(__name__ + '.UpdateServiceChainSpec')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--nodes', type=string.split,
            help=_('List of Service Chain Node IDs or names of the Service '
                   'Chain Nodes'))

    def args2body(self, parsed_args):
        body = {self.resource: {}, }
        if parsed_args.nodes:
            body[self.resource]['nodes'] = [
                neutronV20.find_resourceid_by_name_or_id(
                    self.get_client(),
                    'servicechain_node',
                    elem) for elem in parsed_args.nodes]
        return body


class DeleteServiceChainSpec(neutronV20.DeleteCommand):
    """Delete a given service chain spec."""

    resource = 'servicechain_spec'
    log = logging.getLogger(__name__ + '.DeleteServiceChainSpec')