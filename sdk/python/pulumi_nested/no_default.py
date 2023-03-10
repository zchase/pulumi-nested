# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['NoDefaultArgs', 'NoDefault']

@pulumi.input_type
class NoDefaultArgs:
    def __init__(__self__, *,
                 nested: Optional[pulumi.Input['NestedNoDefaultArgs']] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NoDefault resource.
        """
        if nested is not None:
            pulumi.set(__self__, "nested", nested)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def nested(self) -> Optional[pulumi.Input['NestedNoDefaultArgs']]:
        return pulumi.get(self, "nested")

    @nested.setter
    def nested(self, value: Optional[pulumi.Input['NestedNoDefaultArgs']]):
        pulumi.set(self, "nested", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class NoDefault(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 nested: Optional[pulumi.Input[pulumi.InputType['NestedNoDefaultArgs']]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a NoDefault resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[NoDefaultArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a NoDefault resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param NoDefaultArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NoDefaultArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 nested: Optional[pulumi.Input[pulumi.InputType['NestedNoDefaultArgs']]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NoDefaultArgs.__new__(NoDefaultArgs)

            __props__.__dict__["nested"] = nested
            __props__.__dict__["value"] = value
        super(NoDefault, __self__).__init__(
            'nested:index:NoDefault',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        return pulumi.get(self, "value")

