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
The module file for junos_acls
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_acls
short_description: ACLs resource module
description: This module provides declarative management of acls/filters on Juniper
  JUNOS devices
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
    description: A dictionary of acls options
    type: list
    elements: dict
    suboptions:
      afi:
        description:
        - Protocol family to use by the acl filter
        type: str
        required: true
        choices:
        - ipv4
        - ipv6
      acls:
        description:
        - List of Access Control Lists (ACLs).
        type: list
        elements: dict
        suboptions:
          name:
            description:
            - Name to use for the acl filter
            type: str
            required: true
          aces:
            description:
            - List of Access Control Entries (ACEs) for this Access Control List (ACL).
            type: list
            elements: dict
            suboptions:
              name:
                description:
                - Filter term name
                type: str
                required: true
              grant:
                description:
                - Action to take after matching condition (allow, discard/reject)
                type: str
                choices: [permit, deny]
              source:
                type: dict
                description:
                - Specifies the source for the filter
                suboptions:
                  address:
                    description:
                    - IP source address to use for the filter
                    type: raw
                  prefix_list:
                    description:
                    - IP source prefix list to use for the filter
                    type: list
                    elements: dict
                    suboptions:
                      name:
                        description: Name of the list
                        type: str
                  port_protocol:
                    description:
                    - Specify the source port or protocol.
                    type: dict
                    suboptions:
                      eq:
                        description:
                        - Match only packets on a given port number.
                        type: str
                      range:
                        description:
                        - Match only packets in the range of port numbers
                        type: dict
                        suboptions:
                          start:
                            description:
                            - Specify the start of the port range
                            type: int
                          end:
                            description:
                            - Specify the end of the port range
                            type: int
              destination:
                type: dict
                description:
                - Specifies the destination for the filter
                suboptions:
                  address:
                    description:
                    - Match IP destination address
                    type: raw
                  prefix_list:
                    description:
                    - Match IP destination prefixes in named list
                    type: list
                    elements: dict
                    suboptions:
                      name:
                        description: Name of the list
                        type: str
                  port_protocol:
                    description:
                    - Specify the destination port or protocol.
                    type: dict
                    suboptions:
                      eq:
                        description:
                        - Match only packets on a given port number.
                        type: str
                      range:
                        description:
                        - Match only packets in the range of port numbers
                        type: dict
                        suboptions:
                          start:
                            description:
                            - Specify the start of the port range
                            type: int
                          end:
                            description:
                            - Specify the end of the port range
                            type: int
              protocol:
                description:
                - Specify the protocol to match.
                - Refer to vendor documentation for valid values.
                type: str
              protocol_options:
                description: All possible suboptions for the protocol chosen.
                type: dict
                suboptions:
                  icmp:
                    description: ICMP protocol options.
                    type: dict
                    suboptions:
                      dod_host_prohibited:
                        description: Host prohibited
                        type: bool
                      dod_net_prohibited:
                        description: Net prohibited
                        type: bool
                      echo:
                        description: Echo (ping)
                        type: bool
                      echo_reply:
                        description: Echo reply
                        type: bool
                      host_redirect:
                        description: Host redirect
                        type: bool
                      host_tos_redirect:
                        description: Host redirect for TOS
                        type: bool
                      host_tos_unreachable:
                        description: Host unreachable for TOS
                        type: bool
                      host_unknown:
                        description: Host unknown
                        type: bool
                      host_unreachable:
                        description: Host unreachable
                        type: bool
                      net_redirect:
                        description: Network redirect
                        type: bool
                      net_tos_redirect:
                        description: Net redirect for TOS
                        type: bool
                      network_unknown:
                        description: Network unknown
                        type: bool
                      port_unreachable:
                        description: Port unreachable
                        type: bool
                      protocol_unreachable:
                        description: Protocol unreachable
                        type: bool
                      reassembly_timeout:
                        description: Reassembly timeout
                        type: bool
                      redirect:
                        description: All redirects
                        type: bool
                      router_advertisement:
                        description: Router discovery advertisements
                        type: bool
                      router_solicitation:
                        description: Router discovery solicitations
                        type: bool
                      source_route_failed:
                        description: Source route failed
                        type: bool
                      time_exceeded:
                        description: All time exceeded.
                        type: bool
                      ttl_exceeded:
                        description: TTL exceeded
                        type: bool
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
    default: merged
"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# admin# show firewall

- name: Merge JUNOS acl
  junipernetworks.junos.junos_acls:
    config:
    - afi: ipv4
      acls:
      - name: allow_ssh_acl
        aces:
        - name: ssh_rule
          source:
            port_protocol:
              eq: ssh
          protocol: tcp
      state: merged

# After state:
# -------------
# admin# show firewall
# family inet {
#     filter allow_ssh_acl {
#         term ssh_rule {
#             from {
#                 protocol tcp;
#                 source-port ssh;
#             }
#         }
#     }
# }

"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
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
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.acls.acls import (
    Acls,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    argument_spec = (convert_doc_to_ansible_module_kwargs(DOCUMENTATION))[
        "argument_spec"
    ]
    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True
    )

    result = Acls(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
