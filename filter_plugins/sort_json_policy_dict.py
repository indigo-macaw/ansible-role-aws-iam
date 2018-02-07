#!/usr/bin/env python

from ansible.module_utils.ec2 import sort_json_policy_dict


class FilterModule(object):
    def filters(self):
        return {
            "sort_json_policy_dict": sort_json_policy_dict,
        }
