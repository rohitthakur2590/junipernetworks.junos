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
The module file for junos_static_routes
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_static_routes
short_description: Static routes resource module
description: This module provides declarative management of static routes on Juniper
  JUNOS devices
version_added: 1.0.0
author: Daniel Mellado (@dmellado)
requirements:
- ncclient (>=v0.6.4)
- xmltodict (>=0.12)
notes:
- This module requires the netconf system service be enabled on the device being managed.
- This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- Tested against JunOS v18.4R1
options:
  config:
    description: A dictionary of static routes options
    type: list
    elements: dict
    suboptions:
      vrf:
        description:
        - Virtual Routing and Forwarding (VRF) name
        type: str
      address_families:
        description:
        - Address family to use for the static routes
        elements: dict
        type: list
        suboptions:
          afi:
            description:
            - afi to use for the static routes
            type: str
            required: true
            choices:
            - ipv4
            - ipv6
          routes:
            description:
            - Static route configuration
            elements: dict
            type: list
            suboptions:
              dest:
                description:
                - Static route destination including prefix
                type: str
              next_hop:
                elements: dict
                type: list
                description:
                - Next hop to destination
                suboptions:
                  forward_router_address:
                    description:
                    - List of next hops
                    type: str
              metric:
                description:
                - Metric value for the static route
                type: int
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show routing-options).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result
    type: str
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
"""

EXAMPLES = """
# Using deleted

# Before state
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
#     route 10.200.16.75/24 next-hop 10.200.16.2;
# }

- name: Delete provided configuration (default operation is merge)
  junipernetworks.junos.junos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 10.200.16.75/24
          next_hop:
          - forward_router_address: 10.200.16.2
    state: deleted

# After state:
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
# }

# Using merged

# Before state
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
# }

- name: Merge provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 10.200.16.75/24
          next_hop:
          - forward_router_address: 10.200.16.2
    state: merged

# After state:
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
#     route 10.200.16.75/24 next-hop 10.200.16.2;
# }

# Using overridden

# Before state
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.0.1;
# }

- name: Override provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 10.200.16.75/24
          next_hop:
          - forward_router_address: 10.200.16.2
    state: overridden

# After state:
# ------------
#
# admin# show routing-options
# static {
#     route 10.200.16.75/24 next-hop 10.200.16.2;
# }

# Using replaced

# Before state
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 172.16.1.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
# }

- name: Replace provided configuration with device configuration (default operation
    is merge)
  junipernetworks.junos.junos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 192.168.47.0/24
          next_hop:
          - forward_router_address: 10.200.16.2
    state: replaced

# After state:
# ------------
#
# admin# show routing-options
# static {
#     route 192.168.47.0/24 next-hop 10.200.16.2;
#     route 192.168.16.0/24 next-hop 172.16.1.2;
# }


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: str
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: str
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
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    convert_doc_to_ansible_module_kwargs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.static_routes.static_routes import (
    Static_routes,
)


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
    argument_spec = (convert_doc_to_ansible_module_kwargs(DOCUMENTATION))[
        "argument_spec"
    ]
    module = AnsibleModule(
        argument_spec=argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )
    result = Static_routes(module).execute_module()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
