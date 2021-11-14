#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
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
The arg spec for the junos_snmp_server module
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type


class Snmp_serverArgs(object):  # pylint: disable=R0903
    """The arg spec for the junos_snmp_server module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'options': {'arp': {'options': {'host_name_resolution': {'type': 'bool'},
                                            'set': {'type': 'bool'}},
                                'type': 'dict'},
                        'client_lists': {'elements': 'dict',
                                         'options': {'addresses': {'elements': 'dict',
                                                                   'options': {'address': {'type': 'str'},
                                                                               'restrict': {'type': 'bool'}},
                                                                   'type': 'list'},
                                                     'name': {'type': 'str'}},
                                         'type': 'list'},
                        'communities': {'elements': 'dict',
                                        'options': {'authorization': {'choices': ['read-only',
                                                                                  'read-write'],
                                                                      'type': 'str'},
                                                    'client_list_name': {'type': 'str'},
                                                    'clients': {'elements': 'dict',
                                                                'options': {'address': {'type': 'str'},
                                                                            'restrict': {'type': 'bool'}},
                                                                'type': 'list'},
                                                    'logical_system': {'elements': 'str',
                                                                       'type': 'list'},
                                                    'name': {'type': 'str'},
                                                    'routing_instance_access': {'options': {'access_lists': {'elements': 'str',
                                                                                                             'type': 'list'},
                                                                                            'set': {'type': 'bool'}},
                                                                                'type': 'dict'},
                                                    'routing_instances': {'elements': 'dict',
                                                                          'options': {'client_list_name': {'type': 'str'},
                                                                                      'clients': {'elements': 'dict',
                                                                                                  'options': {'address': {'type': 'str'},
                                                                                                              'restrict': {'type': 'bool'}},
                                                                                                  'type': 'list'},
                                                                                      'name': {'type': 'str'}},
                                                                          'type': 'list'},
                                                    'view': {'type': 'str'}},
                                        'type': 'list'},
                        'contact': {'type': 'str'},
                        'customization': {'options': {'ether_stats_ifd_only': {'type': 'bool'}},
                                          'type': 'dict'},
                        'description': {'type': 'str'},
                        'engine_id': {'options': {'local': {'type': 'str'},
                                                  'use_default_ip_address': {'type': 'bool'},
                                                  'use_mac_address': {'type': 'bool'}},
                                      'type': 'dict'},
                        'filter_duplicates': {'type': 'bool'},
                        'filter_interfaces': {'options': {'all_internal_interfaces': {'type': 'bool'},
                                                          'interfaces': {'elements': 'str',
                                                                         'type': 'list'},
                                                          'set': {'type': 'bool'}},
                                              'type': 'dict'},
                        'health_monitor': {'options': {'falling_threshold': {'type': 'int'},
                                                       'idp': {'type': 'bool'},
                                                       'interval': {'type': 'int'},
                                                       'rising_threshold': {'type': 'int'},
                                                       'set': {'type': 'bool'}},
                                           'type': 'dict'},
                        'if_count_with_filter_interfaces': {'type': 'bool'},
                        'interfaces': {'elements': 'str', 'type': 'list'},
                        'location': {'type': 'str'},
                        'logical_system_trap_filter': {'type': 'bool'},
                        'name': {'type': 'str'},
                        'nonvolatile': {'options': {'commit_delay': {'type': 'int'}},
                                        'type': 'dict'},
                        'proxies': {'elements': 'dict',
                                    'options': {'device_name': {'type': 'str'},
                                                'logical_system': {'elements': 'str',
                                                                   'type': 'list'},
                                                'name': {'type': 'str'},
                                                'routing_instances': {'elements': 'dict',
                                                                      'options': {'client_list_name': {'type': 'str'},
                                                                                  'clients': {'elements': 'dict',
                                                                                              'options': {'address': {'type': 'str'},
                                                                                                          'restrict': {'type': 'bool'}},
                                                                                              'type': 'list'},
                                                                                  'routing-instance': {'type': 'str'}},
                                                                      'type': 'list'},
                                                'version_v1': {'options': {'no_default_comm_to_v3_config': {'type': 'bool'},
                                                                           'snmp_community': {'type': 'str'}},
                                                               'type': 'dict'},
                                                'version_v2c': {'options': {'no_default_comm_to_v3_config': {'type': 'bool'},
                                                                            'snmp_community': {'type': 'str'}},
                                                                'type': 'dict'},
                                                'version_v3': {'options': {'context': {'type': 'bool'},
                                                                           'security_name': {'type': 'str'}},
                                                               'type': 'dict'}},
                                    'type': 'list'},
                        'rmon': {'options': {'alarms': {'elements': 'int',
                                                        'type': 'list'},
                                             'events': {'elements': 'int',
                                                        'type': 'list'},
                                             'set': {'type': 'bool'}},
                                 'type': 'dict'},
                        'routing_instance_access': {'options': {'access_lists': {'elements': 'str',
                                                                                 'type': 'list'},
                                                                'set': {'type': 'bool'}},
                                                    'type': 'dict'},
                        'snmp_v3': {'options': {'notify': {'elements': 'dict',
                                                           'options': {'name': {'type': 'str'},
                                                                       'tag': {'elements': 'str',
                                                                               'type': 'list'},
                                                                       'type': {'type': 'str'}},
                                                           'type': 'list'},
                                                'notify_filter': {'elements': 'dict',
                                                                  'options': {'name': {'type': 'str'},
                                                                              'oids': {'options': {'exclude': {'type': 'bool'},
                                                                                                   'include': {'type': 'bool'},
                                                                                                   'oid': {'type': 'str'}},
                                                                                       'type': 'dict'}},
                                                                  'type': 'list'},
                                                'snmp_community': {'elements': 'dict',
                                                                   'options': {'community_index': {'type': 'str'},
                                                                               'community_name': {'elements': 'str',
                                                                                                  'type': 'list'},
                                                                               'context': {'type': 'str'},
                                                                               'security_name': {'type': 'str'},
                                                                               'tag': {'type': 'str'}},
                                                                   'type': 'list'},
                                                'target_addresses': {'elements': 'dict',
                                                                     'options': {'address': {'type': 'str'},
                                                                                 'address_mask': {'type': 'str'},
                                                                                 'logical_system': {'type': 'str'},
                                                                                 'name': {'type': 'str'},
                                                                                 'port': {'type': 'int'},
                                                                                 'retry_count': {'type': 'int'},
                                                                                 'routing_instance': {'type': 'str'},
                                                                                 'tag_list': {'type': 'str'},
                                                                                 'target_parameters': {'type': 'str'},
                                                                                 'timeout': {'type': 'int'}},
                                                                     'type': 'list'},
                                                'target_parameters': {'elements': 'dict',
                                                                      'options': {'name': {'type': 'str'},
                                                                                  'notify_filter': {'type': 'str'},
                                                                                  'parameters': {'options': {'message_processing_model': {'choices': ['v1',
                                                                                                                                                      'v2c',
                                                                                                                                                      'v3'],
                                                                                                                                          'type': 'str'},
                                                                                                             'security_level': {'choices': ['authentication',
                                                                                                                                            'none',
                                                                                                                                            'privacy'],
                                                                                                                                'type': 'str'},
                                                                                                             'security_model': {'choices': ['usm',
                                                                                                                                            'v1',
                                                                                                                                            'v2c'],
                                                                                                                                'type': 'str'},
                                                                                                             'security_name': {'type': 'str'}},
                                                                                                 'type': 'dict'}},
                                                                      'type': 'list'},
                                                'usm': {'options': {'local_engine': {'options': {'users': {'elements': 'dict',
                                                                                                           'options': {'authentication_md5': {'options': {'key': {'type': 'str'},
                                                                                                                                                          'password': {'type': 'str'}},
                                                                                                                                              'type': 'dict'},
                                                                                                                       'authentication_none': {'type': 'bool'},
                                                                                                                       'authentication_sha': {'options': {'key': {'type': 'str'},
                                                                                                                                                          'password': {'type': 'str'}},
                                                                                                                                              'type': 'dict'},
                                                                                                                       'name': {'type': 'str'},
                                                                                                                       'privacy_3des': {'options': {'key': {'type': 'str'},
                                                                                                                                                    'password': {'type': 'str'}},
                                                                                                                                        'type': 'dict'},
                                                                                                                       'privacy_aes128': {'options': {'key': {'type': 'str'},
                                                                                                                                                      'password': {'type': 'str'}},
                                                                                                                                          'type': 'dict'},
                                                                                                                       'privacy_des': {'options': {'key': {'type': 'str'},
                                                                                                                                                   'password': {'type': 'str'}},
                                                                                                                                       'type': 'dict'},
                                                                                                                       'privacy_none': {'type': 'bool'}},
                                                                                                           'type': 'list'}},
                                                                                     'type': 'dict'},
                                                                    'remote_engine': {'elements': 'dict',
                                                                                      'options': {'id': {'type': 'str'},
                                                                                                  'users': {'elements': 'dict',
                                                                                                            'options': {'authentication_md5': {'options': {'key': {'type': 'str'},
                                                                                                                                                           'password': {'type': 'str'}},
                                                                                                                                               'type': 'dict'},
                                                                                                                        'authentication_none': {'type': 'bool'},
                                                                                                                        'authentication_sha': {'options': {'key': {'type': 'str'},
                                                                                                                                                           'password': {'type': 'str'}},
                                                                                                                                               'type': 'dict'},
                                                                                                                        'name': {'type': 'str'},
                                                                                                                        'privacy_3des': {'options': {'key': {'type': 'str'},
                                                                                                                                                     'password': {'type': 'str'}},
                                                                                                                                         'type': 'dict'},
                                                                                                                        'privacy_aes128': {'options': {'key': {'type': 'str'},
                                                                                                                                                       'password': {'type': 'str'}},
                                                                                                                                           'type': 'dict'},
                                                                                                                        'privacy_des': {'options': {'key': {'type': 'str'},
                                                                                                                                                    'password': {'type': 'str'}},
                                                                                                                                        'type': 'dict'},
                                                                                                                        'privacy_none': {'type': 'bool'}},
                                                                                                            'type': 'list'}},
                                                                                      'type': 'list'}},
                                                        'type': 'dict'}},
                                    'type': 'dict'},
                        'subagent': {'options': {'tcp': {'options': {'routing_instances_default': {'type': 'bool'},
                                                                     'set': {'type': 'bool'}},
                                                         'type': 'dict'}},
                                     'type': 'dict'},
                        'traceoptions': {'options': {'file': {'options': {'files': {'type': 'int'},
                                                                          'match': {'type': 'str'},
                                                                          'no_world_readable': {'type': 'bool'},
                                                                          'size': {'type': 'int'},
                                                                          'world_readable': {'type': 'bool'}},
                                                              'type': 'dict'},
                                                     'flag': {'options': {'all': {'type': 'bool'},
                                                                          'general': {'type': 'bool'},
                                                                          'interface_stats': {'type': 'bool'},
                                                                          'nonvolatile_sets': {'type': 'bool'},
                                                                          'pdu': {'type': 'bool'},
                                                                          'protocol_timeouts': {'type': 'bool'},
                                                                          'routing_socket': {'type': 'bool'},
                                                                          'subagent': {'type': 'bool'},
                                                                          'timer': {'type': 'bool'},
                                                                          'varbind_error': {'type': 'bool'}},
                                                              'type': 'dict'},
                                                     'memory_trace': {'options': {'set': {'type': 'bool'},
                                                                                  'size': {'type': 'bool'}},
                                                                      'type': 'dict'},
                                                     'no_remote_trace': {'type': 'bool'}},
                                         'type': 'dict'},
                        'trap_groups': {'elements': 'dict',
                                        'options': {'categories': {'options': {'authentication': {'type': 'bool'},
                                                                               'chassis': {'type': 'bool'},
                                                                               'chassis_cluster': {'type': 'bool'},
                                                                               'configuration': {'type': 'bool'},
                                                                               'dot3oam_events': {'type': 'bool'},
                                                                               'link': {'type': 'bool'},
                                                                               'otn_alarms': {'options': {'oc_lof': {'type': 'bool'},
                                                                                                          'oc_lom': {'type': 'bool'},
                                                                                                          'oc_los': {'type': 'bool'},
                                                                                                          'odu_ais': {'type': 'bool'},
                                                                                                          'odu_bbe_threshold': {'type': 'bool'},
                                                                                                          'odu_bdi': {'type': 'bool'},
                                                                                                          'odu_bdodu_es_threshold': {'type': 'bool'},
                                                                                                          'odu_lck': {'type': 'bool'},
                                                                                                          'odu_oci': {'type': 'bool'},
                                                                                                          'odu_rx_aps_change': {'type': 'bool'},
                                                                                                          'odu_sd': {'type': 'bool'},
                                                                                                          'odu_ses_threshold': {'type': 'bool'},
                                                                                                          'odu_sf': {'type': 'bool'},
                                                                                                          'odu_ttim': {'type': 'bool'},
                                                                                                          'odu_uas_threshold': {'type': 'bool'},
                                                                                                          'opu_ptm': {'type': 'bool'},
                                                                                                          'otu_ais': {'type': 'bool'},
                                                                                                          'otu_bbe_threshold': {'type': 'bool'},
                                                                                                          'otu_bdi': {'type': 'bool'},
                                                                                                          'otu_es_threshold': {'type': 'bool'},
                                                                                                          'otu_fec_deg': {'type': 'bool'},
                                                                                                          'otu_fec_exe': {'type': 'bool'},
                                                                                                          'otu_iae': {'type': 'bool'},
                                                                                                          'otu_sd': {'type': 'bool'},
                                                                                                          'otu_ses_threshold': {'type': 'bool'},
                                                                                                          'otu_sf': {'type': 'bool'},
                                                                                                          'otu_ttim': {'type': 'bool'},
                                                                                                          'otu_uas_threshold': {'type': 'bool'},
                                                                                                          'set': {'type': 'bool'},
                                                                                                          'wavelength_lock': {'type': 'bool'}},
                                                                                              'type': 'dict'},
                                                                               'remote_operations': {'type': 'bool'},
                                                                               'rmon_alarm': {'type': 'bool'},
                                                                               'routing': {'type': 'bool'},
                                                                               'services': {'type': 'bool'},
                                                                               'startup': {'type': 'bool'},
                                                                               'vrrp_events': {'type': 'bool'}},
                                                                   'type': 'dict'},
                                                    'destination_port': {'type': 'int'},
                                                    'logical_system': {'elements': 'str',
                                                                       'type': 'list'},
                                                    'name': {'type': 'str'},
                                                    'routing_instances': {'elements': 'dict',
                                                                          'options': {'client_list_name': {'type': 'str'},
                                                                                      'clients': {'elements': 'dict',
                                                                                                  'options': {'address': {'type': 'str'},
                                                                                                              'restrict': {'type': 'bool'}},
                                                                                                  'type': 'list'},
                                                                                      'routing-instance': {'type': 'str'}},
                                                                          'type': 'list'},
                                                    'set': {'type': 'bool'},
                                                    'targets': {'elements': 'str',
                                                                'type': 'list'},
                                                    'version': {'choices': ['all',
                                                                            'v1',
                                                                            'v2'],
                                                                'type': 'str'}},
                                        'type': 'list'},
                        'trap_options': {'options': {'agent_address': {'options': {'outgoing_interface': {'type': 'bool'}},
                                                                       'type': 'dict'},
                                                     'context_oid': {'type': 'bool'},
                                                     'enterprise_oid': {'type': 'bool'},
                                                     'logical_system': {'elements': 'str',
                                                                        'type': 'list'},
                                                     'routing_instances': {'elements': 'dict',
                                                                           'options': {'client_list_name': {'type': 'str'},
                                                                                       'clients': {'elements': 'dict',
                                                                                                   'options': {'address': {'type': 'str'},
                                                                                                               'restrict': {'type': 'bool'}},
                                                                                                   'type': 'list'},
                                                                                       'routing-instance': {'type': 'str'}},
                                                                           'type': 'list'},
                                                     'set': {'type': 'bool'},
                                                     'source_address': {'options': {'address': {'type': 'str'},
                                                                                    'lowest_loopback': {'type': 'bool'}},
                                                                        'type': 'dict'}},
                                         'type': 'dict'},
                        'views': {'elements': 'dict',
                                  'options': {'name': {'type': 'str'},
                                              'oids': {'elements': 'dict',
                                                       'options': {'exclude': {'type': 'bool'},
                                                                   'include': {'type': 'bool'},
                                                                   'name': {'type': 'str'}},
                                                       'type': 'list'}},
                                  'type': 'list'}},
            'type': 'dict'},
 'running_config': {'type': 'str'},
 'state': {'choices': ['merged',
                       'replaced',
                       'deleted',
                       'overridden',
                       'parsed',
                       'gathered',
                       'rendered'],
           'default': 'merged',
           'type': 'str'}}  # pylint: disable=C0301
