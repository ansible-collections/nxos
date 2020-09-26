# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

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
The arg spec for the nxos_ospfv3 module
"""


class Ospfv3Args(object):  # pylint: disable=R0903
    """The arg spec for the nxos_ospfv3 module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "type": "dict",
            "options": {
                "processes": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "address_family": {
                            "type": "dict",
                            "options": {
                                "afi": {"type": "str", "choices": ["ipv6"]},
                                "safi": {
                                    "type": "str",
                                    "choices": ["unicast"],
                                },
                                "areas": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "area_id": {
                                            "type": "str",
                                            "required": True,
                                        },
                                        "default_cost": {"type": "int"},
                                        "filter_list": {
                                            "type": "list",
                                            "elements": "dict",
                                            "options": {
                                                "route_map": {
                                                    "type": "str",
                                                    "required": True,
                                                },
                                                "direction": {
                                                    "type": "str",
                                                    "choices": ["in", "out"],
                                                    "required": True,
                                                },
                                            },
                                        },
                                        "ranges": {
                                            "type": "list",
                                            "elements": "dict",
                                            "options": {
                                                "prefix": {
                                                    "type": "str",
                                                    "required": True,
                                                },
                                                "cost": {"type": "int"},
                                                "not_advertise": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                    },
                                },
                                "default_information": {
                                    "type": "dict",
                                    "options": {
                                        "originate": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "always": {"type": "bool"},
                                                "route_map": {"type": "str"},
                                            },
                                        }
                                    },
                                },
                                "distance": {"type": "int"},
                                "maximum_paths": {"type": "int"},
                                "redistribute": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "protocol": {
                                            "type": "str",
                                            "choices": [
                                                "bgp",
                                                "direct",
                                                "eigrp",
                                                "isis",
                                                "lisp",
                                                "ospfv3",
                                                "rip",
                                                "static",
                                            ],
                                            "required": True,
                                        },
                                        "id": {"type": "str"},
                                        "route_map": {
                                            "type": "str",
                                            "required": True,
                                        },
                                    },
                                },
                                "summary_address": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "prefix": {
                                            "type": "str",
                                            "required": True,
                                        },
                                        "not_advertise": {"type": "bool"},
                                        "tag": {"type": "int"},
                                    },
                                },
                                "table_map": {
                                    "type": "dict",
                                    "options": {
                                        "name": {
                                            "type": "str",
                                            "required": True,
                                        },
                                        "filter": {"type": "bool"},
                                    },
                                },
                                "timers": {
                                    "type": "dict",
                                    "options": {
                                        "throttle": {
                                            "type": "dict",
                                            "options": {
                                                "spf": {
                                                    "type": "dict",
                                                    "options": {
                                                        "initial_spf_delay": {
                                                            "type": "int"
                                                        },
                                                        "min_hold_time": {
                                                            "type": "int"
                                                        },
                                                        "max_wait_time": {
                                                            "type": "int"
                                                        },
                                                    },
                                                }
                                            },
                                        }
                                    },
                                },
                            },
                        },
                        "areas": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "area_id": {"type": "str", "required": True},
                                "nssa": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "default_information_originate": {
                                            "type": "bool"
                                        },
                                        "no_redistribution": {"type": "bool"},
                                        "no_summary": {"type": "bool"},
                                        "route_map": {"type": "str"},
                                        "translate": {
                                            "type": "dict",
                                            "options": {
                                                "type7": {
                                                    "type": "dict",
                                                    "options": {
                                                        "always": {
                                                            "type": "bool"
                                                        },
                                                        "never": {
                                                            "type": "bool"
                                                        },
                                                        "supress_fa": {
                                                            "type": "bool"
                                                        },
                                                    },
                                                }
                                            },
                                        },
                                    },
                                },
                                "stub": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "no_summary": {"type": "bool"},
                                    },
                                },
                            },
                        },
                        "auto_cost": {
                            "type": "dict",
                            "options": {
                                "reference_bandwidth": {
                                    "type": "int",
                                    "required": True,
                                },
                                "unit": {
                                    "type": "str",
                                    "required": True,
                                    "choices": ["Gbps", "Mbps"],
                                },
                            },
                        },
                        "flush_routes": {"type": "bool"},
                        "graceful_restart": {
                            "type": "dict",
                            "options": {
                                "set": {"type": "bool"},
                                "grace_period": {"type": "int"},
                                "helper_disable": {"type": "bool"},
                                "planned_only": {"type": "bool"},
                            },
                        },
                        "isolate": {"type": "bool"},
                        "log_adjacency_changes": {
                            "type": "dict",
                            "options": {
                                "log": {"type": "bool"},
                                "detail": {"type": "bool"},
                            },
                        },
                        "max_lsa": {
                            "type": "dict",
                            "options": {
                                "max_non_self_generated_lsa": {
                                    "type": "int",
                                    "required": True,
                                },
                                "threshold": {"type": "int"},
                                "ignore_count": {"type": "int"},
                                "ignore_time": {"type": "int"},
                                "reset_time": {"type": "int"},
                                "warning_only": {"type": "bool"},
                            },
                        },
                        "max_metric": {
                            "type": "dict",
                            "options": {
                                "router_lsa": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "external_lsa": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "max_metric_value": {
                                                    "type": "int"
                                                },
                                            },
                                        },
                                        "stub_prefix_lsa": {"type": "bool"},
                                        "on_startup": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "wait_period": {"type": "int"},
                                                "wait_for_bgp_asn": {
                                                    "type": "int"
                                                },
                                            },
                                        },
                                        "inter_area_prefix_lsa": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "max_metric_value": {
                                                    "type": "int"
                                                },
                                            },
                                        },
                                    },
                                }
                            },
                        },
                        "name_lookup": {"type": "bool"},
                        "passive_interface": {
                            "type": "dict",
                            "options": {"default": {"type": "bool"}},
                        },
                        "process_id": {"type": "str", "required": True},
                        "router_id": {"type": "str"},
                        "shutdown": {"type": "bool"},
                        "timers": {
                            "type": "dict",
                            "options": {
                                "lsa_arrival": {"type": "int"},
                                "lsa_group_pacing": {"type": "int"},
                                "throttle": {
                                    "type": "dict",
                                    "options": {
                                        "lsa": {
                                            "type": "dict",
                                            "options": {
                                                "start_interval": {
                                                    "type": "int"
                                                },
                                                "hold_interval": {
                                                    "type": "int"
                                                },
                                                "max_interval": {
                                                    "type": "int"
                                                },
                                            },
                                        }
                                    },
                                },
                            },
                        },
                        "vrfs": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "areas": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "area_id": {
                                            "type": "str",
                                            "required": True,
                                        },
                                        "nssa": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "default_information_originate": {
                                                    "type": "bool"
                                                },
                                                "no_redistribution": {
                                                    "type": "bool"
                                                },
                                                "no_summary": {"type": "bool"},
                                                "translate": {
                                                    "type": "dict",
                                                    "options": {
                                                        "type7": {
                                                            "type": "dict",
                                                            "options": {
                                                                "always": {
                                                                    "type": "bool"
                                                                },
                                                                "never": {
                                                                    "type": "bool"
                                                                },
                                                                "supress_fa": {
                                                                    "type": "bool"
                                                                },
                                                            },
                                                        }
                                                    },
                                                },
                                            },
                                        },
                                        "stub": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "no_summary": {"type": "bool"},
                                            },
                                        },
                                    },
                                },
                                "auto_cost": {
                                    "type": "dict",
                                    "options": {
                                        "reference_bandwidth": {
                                            "type": "int",
                                            "required": True,
                                        },
                                        "unit": {
                                            "type": "str",
                                            "required": True,
                                            "choices": ["Gbps", "Mbps"],
                                        },
                                    },
                                },
                                "graceful_restart": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "grace_period": {"type": "int"},
                                        "helper_disable": {"type": "bool"},
                                        "planned_only": {"type": "bool"},
                                    },
                                },
                                "log_adjacency_changes": {
                                    "type": "dict",
                                    "options": {
                                        "log": {"type": "bool"},
                                        "detail": {"type": "bool"},
                                    },
                                },
                                "max_lsa": {
                                    "type": "dict",
                                    "options": {
                                        "max_non_self_generated_lsa": {
                                            "type": "int",
                                            "required": True,
                                        },
                                        "threshold": {"type": "int"},
                                        "ignore_count": {"type": "int"},
                                        "ignore_time": {"type": "int"},
                                        "reset_time": {"type": "int"},
                                        "warning_only": {"type": "bool"},
                                    },
                                },
                                "max_metric": {
                                    "type": "dict",
                                    "options": {
                                        "router_lsa": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "external_lsa": {
                                                    "type": "dict",
                                                    "options": {
                                                        "set": {
                                                            "type": "bool"
                                                        },
                                                        "max_metric_value": {
                                                            "type": "int"
                                                        },
                                                    },
                                                },
                                                "stub_prefix_lsa": {
                                                    "type": "bool"
                                                },
                                                "on_startup": {
                                                    "type": "dict",
                                                    "options": {
                                                        "set": {
                                                            "type": "bool"
                                                        },
                                                        "wait_period": {
                                                            "type": "int"
                                                        },
                                                        "wait_for_bgp_asn": {
                                                            "type": "int"
                                                        },
                                                    },
                                                },
                                                "inter_area_prefix_lsa": {
                                                    "type": "dict",
                                                    "options": {
                                                        "set": {
                                                            "type": "bool"
                                                        },
                                                        "max_metric_value": {
                                                            "type": "int"
                                                        },
                                                    },
                                                },
                                            },
                                        }
                                    },
                                },
                                "name_lookup": {"type": "bool"},
                                "passive_interface": {
                                    "type": "dict",
                                    "options": {"default": {"type": "bool"}},
                                },
                                "router_id": {"type": "str"},
                                "shutdown": {"type": "bool"},
                                "timers": {
                                    "type": "dict",
                                    "options": {
                                        "lsa_arrival": {"type": "int"},
                                        "lsa_group_pacing": {"type": "int"},
                                        "throttle": {
                                            "type": "dict",
                                            "options": {
                                                "lsa": {
                                                    "type": "dict",
                                                    "options": {
                                                        "start_interval": {
                                                            "type": "int"
                                                        },
                                                        "hold_interval": {
                                                            "type": "int"
                                                        },
                                                        "max_interval": {
                                                            "type": "int"
                                                        },
                                                    },
                                                }
                                            },
                                        },
                                    },
                                },
                                "vrf": {"type": "str", "required": True},
                            },
                        },
                    },
                }
            },
        },
        "state": {
            "type": "str",
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "parsed",
                "rendered",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
