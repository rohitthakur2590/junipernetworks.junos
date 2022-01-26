#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
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
The module file for junos_acl_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_acl_interfaces
short_description: ACL interfaces resource module
description:
- This module manages adding and removing Access Control Lists (ACLs) from interfaces
  on devices running Juniper JUNOS.
version_added: 1.0.0
author: Daniel Mellado (@dmellado)
requirements:
- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)
notes:
- This module requires the netconf system service be enabled on the device being managed.
- This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- Tested against JunOS v18.4R1
options:
  config:
    description: A dictionary of ACL options for interfaces.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name/Identifier for the interface.
        type: str
      access_groups:
        type: list
        elements: dict
        description:
        - Specifies ACLs attached to the interface.
        suboptions:
          afi:
            description:
            - Specifies the AFI for the ACL(s) to be configured on this interface.
            type: str
            choices: [ipv4, ipv6]
          acls:
            type: list
            description:
            - Specifies the ACLs for the provided AFI.
            elements: dict
            suboptions:
              name:
                description:
                - Specifies the name of the IPv4/IPv4 ACL for the interface.
                type: str
              direction:
                description:
                - Specifies the direction of packets that the ACL will be applied
                  on.
                type: str
                choices: [in, out]
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show interfaces).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result
    type: str
  state:
    description:
    - The state the configuration should be left in.
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

# Before state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input inbound_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

- name: Delete JUNOS L3 interface filter
  junipernetworks.junos.junos_acl_interfaces:
    config:
    - name: ge-1/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: inbound_acl
          direction: in
        - name: outbound_acl
          direction: out
      state: deleted

# After state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }


# Using merged

# Before state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface without filter";
#     unit 0 {
#         family inet {
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

- name: Merge JUNOS L3 interface filter
  junipernetworks.junos.junos_acl_interfaces:
    config:
    - name: ge-1/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: inbound_acl
          direction: in
        - name: outbound_acl
          direction: out
      state: merged

# After state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input inbound_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }


# Using overridden

# Before state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface without filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input foo_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

- name: Override JUNOS L3 interface filter
  junipernetworks.junos.junos_acl_interfaces:
    config:
    - name: ge-1/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: inbound_acl
          direction: in
        - name: outbound_acl
          direction: out
      state: overridden

# After state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input inbound_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }


# Using replaced

# Before state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface without filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input foo_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }

- name: Replace JUNOS L3 interface filter
  junipernetworks.junos.junos_acl_interfaces:
    config:
    - name: ge-1/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: inbound_acl
          direction: in
      state: replaced

# After state:
# -------------
#
# admin# show interfaces
# ge-1/0/0 {
#     description "L3 interface with filter";
#     unit 0 {
#         family inet {
#             filter {
#                 input inbound_acl;
#                 output outbound_acl;
#             }
#             address 100.64.0.1/10;
#             address 100.64.0.2/10;
#         }
#         family inet6;
#     }


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
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
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.acl_interfaces.acl_interfaces import (
    Acl_interfaces,
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
    result = Acl_interfaces(module).execute_module()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
