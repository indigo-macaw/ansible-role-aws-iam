#!/usr/bin/env python

from ansible.module_utils.ec2 import compare_policies


class FilterModule(object):
    def filters(self):
        return {
            "compare_policies": compare_policies,
        }
