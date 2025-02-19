# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network public-ip prefix create",
)
class Create(AAZCommand):
    """Create a public IP prefix resource.

    :example: Create a public IP prefix resource. (autogenerated)
        az network public-ip prefix create --length 28 --location westus2 --name MyPublicIPPrefix --resource-group MyResourceGroup
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/publicipprefixes/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the public IP prefix.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.edge_zone = AAZStrArg(
            options=["--edge-zone"],
            help="The name of edge zone.",
        )
        _args_schema.location = AAZResourceLocationArg(
            help="Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.custom_ip_prefix = AAZObjectArg(
            options=["--custom-ip-prefix"],
            help="The customIpPrefix that this prefix is associated with.",
        )
        cls._build_args_sub_resource_create(_args_schema.custom_ip_prefix)
        _args_schema.length = AAZIntArg(
            options=["--length"],
            help="Length of the prefix (i.e. `XX.XX.XX.XX/<Length>`).",
        )
        _args_schema.version = AAZStrArg(
            options=["--version"],
            help="IP address type.  Allowed values: IPv4, IPv6.",
            default="IPv4",
            enum={"IPv4": "IPv4", "IPv6": "IPv6"},
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
        )
        _args_schema.zone = AAZListArg(
            options=["-z", "--zone"],
            help="Space-separated list of availability zones into which to provision the resource.  Allowed values: 1, 2, 3.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        zone = cls._args_schema.zone
        zone.Element = AAZStrArg()

        # define Arg Group "ExtendedLocation"

        _args_schema = cls._args_schema
        _args_schema.type = AAZStrArg(
            options=["--type"],
            arg_group="ExtendedLocation",
            help="The type of the extended location.",
            enum={"EdgeZone": "EdgeZone"},
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.sku = AAZObjectArg(
            options=["--sku"],
            arg_group="Parameters",
            help="The public IP prefix SKU.",
        )

        sku = cls._args_schema.sku
        sku.name = AAZStrArg(
            options=["name"],
            help="Name of a public IP prefix SKU.",
            default="Standard",
            enum={"Standard": "Standard"},
        )
        sku.tier = AAZStrArg(
            options=["tier"],
            help="Tier of a public IP prefix SKU.",
            enum={"Global": "Global", "Regional": "Regional"},
        )

        # define Arg Group "Properties"
        return cls._args_schema

    _args_sub_resource_create = None

    @classmethod
    def _build_args_sub_resource_create(cls, _schema):
        if cls._args_sub_resource_create is not None:
            _schema.id = cls._args_sub_resource_create.id
            return

        cls._args_sub_resource_create = AAZObjectArg()

        sub_resource_create = cls._args_sub_resource_create
        sub_resource_create.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
        )

        _schema.id = cls._args_sub_resource_create.id

    def _execute_operations(self):
        self.pre_operations()
        yield self.PublicIPPrefixesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class PublicIPPrefixesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "publicIpPrefixName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("extendedLocation", AAZObjectType)
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("sku", AAZObjectType, ".sku")
            _builder.set_prop("tags", AAZDictType, ".tags")
            _builder.set_prop("zones", AAZListType, ".zone")

            extended_location = _builder.get(".extendedLocation")
            if extended_location is not None:
                extended_location.set_prop("name", AAZStrType, ".edge_zone")
                extended_location.set_prop("type", AAZStrType, ".type")

            properties = _builder.get(".properties")
            if properties is not None:
                _build_schema_sub_resource_create(properties.set_prop("customIPPrefix", AAZObjectType, ".custom_ip_prefix"))
                properties.set_prop("prefixLength", AAZIntType, ".length")
                properties.set_prop("publicIPAddressVersion", AAZStrType, ".version")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".name")
                sku.set_prop("tier", AAZStrType, ".tier")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            zones = _builder.get(".zones")
            if zones is not None:
                zones.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
            )
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.sku = AAZObjectType()
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.zones = AAZListType()

            extended_location = cls._schema_on_200_201.extended_location
            extended_location.name = AAZStrType()
            extended_location.type = AAZStrType()

            properties = cls._schema_on_200_201.properties
            properties.custom_ip_prefix = AAZObjectType(
                serialized_name="customIPPrefix",
            )
            _build_schema_sub_resource_read(properties.custom_ip_prefix)
            properties.ip_prefix = AAZStrType(
                serialized_name="ipPrefix",
                flags={"read_only": True},
            )
            properties.ip_tags = AAZListType(
                serialized_name="ipTags",
            )
            properties.load_balancer_frontend_ip_configuration = AAZObjectType(
                serialized_name="loadBalancerFrontendIpConfiguration",
            )
            _build_schema_sub_resource_read(properties.load_balancer_frontend_ip_configuration)
            properties.nat_gateway = AAZObjectType(
                serialized_name="natGateway",
            )
            properties.prefix_length = AAZIntType(
                serialized_name="prefixLength",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_address_version = AAZStrType(
                serialized_name="publicIPAddressVersion",
            )
            properties.public_ip_addresses = AAZListType(
                serialized_name="publicIPAddresses",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )

            ip_tags = cls._schema_on_200_201.properties.ip_tags
            ip_tags.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.ip_tags.Element
            _element.ip_tag_type = AAZStrType(
                serialized_name="ipTagType",
            )
            _element.tag = AAZStrType()

            nat_gateway = cls._schema_on_200_201.properties.nat_gateway
            nat_gateway.etag = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.id = AAZStrType()
            nat_gateway.location = AAZStrType()
            nat_gateway.name = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            nat_gateway.sku = AAZObjectType()
            nat_gateway.tags = AAZDictType()
            nat_gateway.type = AAZStrType(
                flags={"read_only": True},
            )
            nat_gateway.zones = AAZListType()

            properties = cls._schema_on_200_201.properties.nat_gateway.properties
            properties.idle_timeout_in_minutes = AAZIntType(
                serialized_name="idleTimeoutInMinutes",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.public_ip_addresses = AAZListType(
                serialized_name="publicIpAddresses",
            )
            properties.public_ip_prefixes = AAZListType(
                serialized_name="publicIpPrefixes",
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )
            properties.subnets = AAZListType(
                flags={"read_only": True},
            )

            public_ip_addresses = cls._schema_on_200_201.properties.nat_gateway.properties.public_ip_addresses
            public_ip_addresses.Element = AAZObjectType()
            _build_schema_sub_resource_read(public_ip_addresses.Element)

            public_ip_prefixes = cls._schema_on_200_201.properties.nat_gateway.properties.public_ip_prefixes
            public_ip_prefixes.Element = AAZObjectType()
            _build_schema_sub_resource_read(public_ip_prefixes.Element)

            subnets = cls._schema_on_200_201.properties.nat_gateway.properties.subnets
            subnets.Element = AAZObjectType()
            _build_schema_sub_resource_read(subnets.Element)

            sku = cls._schema_on_200_201.properties.nat_gateway.sku
            sku.name = AAZStrType()

            tags = cls._schema_on_200_201.properties.nat_gateway.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200_201.properties.nat_gateway.zones
            zones.Element = AAZStrType()

            public_ip_addresses = cls._schema_on_200_201.properties.public_ip_addresses
            public_ip_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.public_ip_addresses.Element
            _element.id = AAZStrType()

            sku = cls._schema_on_200_201.sku
            sku.name = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            zones = cls._schema_on_200_201.zones
            zones.Element = AAZStrType()

            return cls._schema_on_200_201


def _build_schema_sub_resource_create(_builder):
    if _builder is None:
        return
    _builder.set_prop("id", AAZStrType, ".id")


_schema_sub_resource_read = None


def _build_schema_sub_resource_read(_schema):
    global _schema_sub_resource_read
    if _schema_sub_resource_read is not None:
        _schema.id = _schema_sub_resource_read.id
        return

    _schema_sub_resource_read = AAZObjectType()

    sub_resource_read = _schema_sub_resource_read
    sub_resource_read.id = AAZStrType()

    _schema.id = _schema_sub_resource_read.id


__all__ = ["Create"]
