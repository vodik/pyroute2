from pyroute2.netlink import nla


class vlan(nla):
    nla_map = (('IFLA_VLAN_UNSPEC', 'none'),
               ('IFLA_VLAN_ID', 'uint16'),
               ('IFLA_VLAN_FLAGS', 'vlan_flags'),
               ('IFLA_VLAN_EGRESS_QOS', 'qos'),
               ('IFLA_VLAN_INGRESS_QOS', 'qos'),
               ('IFLA_VLAN_PROTOCOL', 'be16'))

    class vlan_flags(nla):
        fields = (('flags', 'I'),
                  ('mask', 'I'))

    class qos(nla):
        nla_map = (('IFLA_VLAN_QOS_UNSPEC', 'none'),
                   ('IFLA_VLAN_QOS_MAPPING', 'qos_mapping'))

        class qos_mapping(nla):
            fields = (('from', 'I'),
                      ('to', 'I'))
