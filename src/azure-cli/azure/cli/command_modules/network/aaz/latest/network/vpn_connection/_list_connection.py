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
    "network vpn-connection list-connection",
)
class ListConnection(AAZCommand):
    """List all the connections in a virtual network gateway.
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualnetworkgateways/{}/connections", "2022-01-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vnet_gateway = AAZStrArg(
            options=["--vnet-gateway"],
            help="Name of the VNet gateway.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualNetworkGatewaysListConnections(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class VirtualNetworkGatewaysListConnections(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/connections",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualNetworkGatewayName", self.ctx.args.vnet_gateway,
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
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType()
            _element.location = AAZStrType()
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.authorization_key = AAZStrType(
                serialized_name="authorizationKey",
            )
            properties.connection_mode = AAZStrType(
                serialized_name="connectionMode",
            )
            properties.connection_protocol = AAZStrType(
                serialized_name="connectionProtocol",
            )
            properties.connection_status = AAZStrType(
                serialized_name="connectionStatus",
            )
            properties.connection_type = AAZStrType(
                serialized_name="connectionType",
                flags={"required": True},
            )
            properties.egress_bytes_transferred = AAZIntType(
                serialized_name="egressBytesTransferred",
                flags={"read_only": True},
            )
            properties.enable_bgp = AAZBoolType(
                serialized_name="enableBgp",
            )
            properties.express_route_gateway_bypass = AAZBoolType(
                serialized_name="expressRouteGatewayBypass",
            )
            properties.gateway_custom_bgp_ip_addresses = AAZListType(
                serialized_name="gatewayCustomBgpIpAddresses",
            )
            properties.ingress_bytes_transferred = AAZIntType(
                serialized_name="ingressBytesTransferred",
                flags={"read_only": True},
            )
            properties.ipsec_policies = AAZListType(
                serialized_name="ipsecPolicies",
            )
            properties.local_network_gateway2 = AAZObjectType(
                serialized_name="localNetworkGateway2",
            )
            _ListConnectionHelper._build_schema_virtual_network_connection_gateway_reference_read(properties.local_network_gateway2)
            properties.peer = AAZObjectType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.resource_guid = AAZStrType(
                serialized_name="resourceGuid",
                flags={"read_only": True},
            )
            properties.routing_weight = AAZIntType(
                serialized_name="routingWeight",
            )
            properties.shared_key = AAZStrType(
                serialized_name="sharedKey",
            )
            properties.traffic_selector_policies = AAZListType(
                serialized_name="trafficSelectorPolicies",
            )
            properties.tunnel_connection_status = AAZListType(
                serialized_name="tunnelConnectionStatus",
                flags={"read_only": True},
            )
            properties.use_policy_based_traffic_selectors = AAZBoolType(
                serialized_name="usePolicyBasedTrafficSelectors",
            )
            properties.virtual_network_gateway1 = AAZObjectType(
                serialized_name="virtualNetworkGateway1",
                flags={"required": True},
            )
            _ListConnectionHelper._build_schema_virtual_network_connection_gateway_reference_read(properties.virtual_network_gateway1)
            properties.virtual_network_gateway2 = AAZObjectType(
                serialized_name="virtualNetworkGateway2",
            )
            _ListConnectionHelper._build_schema_virtual_network_connection_gateway_reference_read(properties.virtual_network_gateway2)

            gateway_custom_bgp_ip_addresses = cls._schema_on_200.value.Element.properties.gateway_custom_bgp_ip_addresses
            gateway_custom_bgp_ip_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.gateway_custom_bgp_ip_addresses.Element
            _element.custom_bgp_ip_address = AAZStrType(
                serialized_name="customBgpIpAddress",
                flags={"required": True},
            )
            _element.ip_configuration_id = AAZStrType(
                serialized_name="ipConfigurationId",
                flags={"required": True},
            )

            ipsec_policies = cls._schema_on_200.value.Element.properties.ipsec_policies
            ipsec_policies.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.ipsec_policies.Element
            _element.dh_group = AAZStrType(
                serialized_name="dhGroup",
                flags={"required": True},
            )
            _element.ike_encryption = AAZStrType(
                serialized_name="ikeEncryption",
                flags={"required": True},
            )
            _element.ike_integrity = AAZStrType(
                serialized_name="ikeIntegrity",
                flags={"required": True},
            )
            _element.ipsec_encryption = AAZStrType(
                serialized_name="ipsecEncryption",
                flags={"required": True},
            )
            _element.ipsec_integrity = AAZStrType(
                serialized_name="ipsecIntegrity",
                flags={"required": True},
            )
            _element.pfs_group = AAZStrType(
                serialized_name="pfsGroup",
                flags={"required": True},
            )
            _element.sa_data_size_kilobytes = AAZIntType(
                serialized_name="saDataSizeKilobytes",
                flags={"required": True},
            )
            _element.sa_life_time_seconds = AAZIntType(
                serialized_name="saLifeTimeSeconds",
                flags={"required": True},
            )

            peer = cls._schema_on_200.value.Element.properties.peer
            peer.id = AAZStrType()

            traffic_selector_policies = cls._schema_on_200.value.Element.properties.traffic_selector_policies
            traffic_selector_policies.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.traffic_selector_policies.Element
            _element.local_address_ranges = AAZListType(
                serialized_name="localAddressRanges",
                flags={"required": True},
            )
            _element.remote_address_ranges = AAZListType(
                serialized_name="remoteAddressRanges",
                flags={"required": True},
            )

            local_address_ranges = cls._schema_on_200.value.Element.properties.traffic_selector_policies.Element.local_address_ranges
            local_address_ranges.Element = AAZStrType()

            remote_address_ranges = cls._schema_on_200.value.Element.properties.traffic_selector_policies.Element.remote_address_ranges
            remote_address_ranges.Element = AAZStrType()

            tunnel_connection_status = cls._schema_on_200.value.Element.properties.tunnel_connection_status
            tunnel_connection_status.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.tunnel_connection_status.Element
            _element.connection_status = AAZStrType(
                serialized_name="connectionStatus",
            )
            _element.egress_bytes_transferred = AAZIntType(
                serialized_name="egressBytesTransferred",
                flags={"read_only": True},
            )
            _element.ingress_bytes_transferred = AAZIntType(
                serialized_name="ingressBytesTransferred",
                flags={"read_only": True},
            )
            _element.last_connection_established_utc_time = AAZStrType(
                serialized_name="lastConnectionEstablishedUtcTime",
                flags={"read_only": True},
            )
            _element.tunnel = AAZStrType(
                flags={"read_only": True},
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListConnectionHelper:
    """Helper class for ListConnection"""

    _schema_virtual_network_connection_gateway_reference_read = None

    @classmethod
    def _build_schema_virtual_network_connection_gateway_reference_read(cls, _schema):
        if cls._schema_virtual_network_connection_gateway_reference_read is not None:
            _schema.id = cls._schema_virtual_network_connection_gateway_reference_read.id
            return

        cls._schema_virtual_network_connection_gateway_reference_read = _schema_virtual_network_connection_gateway_reference_read = AAZObjectType()

        virtual_network_connection_gateway_reference_read = _schema_virtual_network_connection_gateway_reference_read
        virtual_network_connection_gateway_reference_read.id = AAZStrType(
            flags={"required": True},
        )

        _schema.id = cls._schema_virtual_network_connection_gateway_reference_read.id


__all__ = ["ListConnection"]
