// Copyright 2016-2021, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

const HasDefaultIdentifier = "nested:index:HasDefault"

type HasDefaultArgs struct {
	Value  string     `pulumi:"value"`
	Nested NestedArgs `pulumi:"nested"`
}

type HasDefault struct {
	pulumi.ResourceState

	Value pulumi.StringOutput `pulumi:"value"`
}

func NewHasDefault(ctx *pulumi.Context,
	name string, args *HasDefaultArgs, opts ...pulumi.ResourceOption) (*HasDefault, error) {
	if args == nil {
		args = &HasDefaultArgs{}
	}

	component := &HasDefault{}
	err := ctx.RegisterComponentResource(HasDefaultIdentifier, name, component, opts...)
	if err != nil {
		return nil, err
	}

	component.Value = pulumi.String(args.Value).ToStringOutput()

	if err := ctx.RegisterResourceOutputs(component, pulumi.Map{
		"value": component.Value,
	}); err != nil {
		return nil, err
	}

	return component, nil
}
