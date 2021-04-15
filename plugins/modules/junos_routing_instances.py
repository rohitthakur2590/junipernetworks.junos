#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for junos_routing_instances
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: junos_routing_instances
version_added: 1.3.1
short_description: Manage routing instances on Junos devices.
description: Manage routing instances on Junos network devices.
author: Rohit Thakur (@rohitthakur2590)
requirements:
  - ncclient (>=v0.6.4)
  - xmltodict (>=0.12.0)
notes:
  - This module requires the netconf system service be enabled on the device being managed.
  - This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
  - Tested against JunOS v18.4R1
options:
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the Junos device
        by executing the command B(show routing-instance).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result
    type: str
  config:
    description: The provided Routing instance configuration list.
    type: list
    elements: dict
    suboptions:
      name:
        description: Specify routing instance name.
        type: str
      connector_id_advertise:
        description: Advertise connector-id attribute.
        type: bool
      description:
        description: Specify text description of routing instance.
        type: str
      egress_protection:
        description: Egress instance protection dictionary.
        type: dict
        suboptions:
          context_identifier:
            description: Specify context identifier.
            type: str
          protector:
            description: Enable Edge Protector functionality for this VPN.
            type: bool
      instance_role:
        description: Primary role of L2Backhaul-vpn router.
        type: str
        choices: ['access', 'nni']
      type:
        description: Specify instance type.
        type: str
        choices:
          - evpn
          - evpn-vpws
          - forwarding
          - l2backhaul-vpn
          - l2vpn
          - layer2-control
          - mpls-forwarding
          - mpls-internet-multicast
          - no-forwarding
          - virtual-router
          - vpls
          - vrf
      interfaces:
        description: Interface name for this routing instance.
        type: list
        elements: dict
        suboptions:
          name:
            description: Specify name of the interface.
            type: str
          protect_interface:
            description: Specify name of the protected interface.
            type: str
      l2vpn_id:
        description: Layer-2 vpn-id for this instance.
        type: str
      no_irb_layer_2_copy:
        description: Disable transmission of layer-2 copy of packets of irb routing-interface.
        type: bool
      no_local_switching:
        description: Disable vlan id normalization for interfaces.
        type: bool
      no_vrf_advertise:
        description: Disable vlan id normalization for interfaces.
        type: bool
      no_vrf_propagate_ttl:
        description: Disable TTL propagation from IP to MPLS (on push) and MPLS to IP (on pop).
        type: bool
      protocols:
        description:  Routing protocol configuration list.
        type: list
        elements: str
      qualified_bum_pruning_mode:
        description: Enable BUM pruning for VPLS instance.
        type: bool
      routing_interface:
        description: Routing interface name for this routing-instance.
        type: list
        elements: str

  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - parsed
    - gathered
    - rendered
    default: merged
"""
EXAMPLES = """





















"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.routing_instances.routing_instances import Routing_instancesArgs
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.routing_instances.routing_instances import Routing_instances


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    module = AnsibleModule(
        argument_spec=Routing_instancesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )
    result = Routing_instances(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
