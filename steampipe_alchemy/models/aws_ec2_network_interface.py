from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2NetworkInterface(Base):
    __tablename__ = 'aws_ec2_network_interface'
    network_interface_id = Column(name='network_interface_id', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    interface_type = Column(name='interface_type', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    availability_zone = Column(name='availability_zone', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    association_allocation_id = Column(name='association_allocation_id', type_=Text, nullable=True)
    association_carrier_ip = Column(name='association_carrier_ip', type_=psql.INET, nullable=True)
    association_customer_owned_ip = Column(name='association_customer_owned_ip', type_=psql.INET, nullable=True)
    association_id = Column(name='association_id', type_=Text, nullable=True)
    association_ip_owner_id = Column(name='association_ip_owner_id', type_=Text, nullable=True)
    association_public_dns_name = Column(name='association_public_dns_name', type_=Text, nullable=True)
    association_public_ip = Column(name='association_public_ip', type_=psql.INET, nullable=True)
    attached_instance_id = Column(name='attached_instance_id', type_=Text, nullable=True)
    attached_instance_owner_id = Column(name='attached_instance_owner_id', type_=Text, nullable=True)
    attachment_id = Column(name='attachment_id', type_=Text, nullable=True)
    attachment_status = Column(name='attachment_status', type_=Text, nullable=True)
    attachment_time = Column(name='attachment_time', type_=TIMESTAMP, nullable=True)
    delete_on_instance_termination = Column(name='delete_on_instance_termination', type_=Boolean, nullable=True)
    device_index = Column(name='device_index', type_=BigInteger, nullable=True)
    mac_address = Column(name='mac_address', type_=Text, nullable=True)
    outpost_arn = Column(name='outpost_arn', type_=Text, nullable=True)
    private_dns_name = Column(name='private_dns_name', type_=Text, nullable=True)
    private_ip_address = Column(name='private_ip_address', type_=psql.INET, nullable=True)
    requester_id = Column(name='requester_id', type_=Text, nullable=True)
    requester_managed = Column(name='requester_managed', type_=Boolean, nullable=True)
    source_dest_check = Column(name='source_dest_check', type_=Boolean, nullable=True)
    groups = Column(name='groups', type_=JSON, nullable=True)
    ipv6_addresses = Column(name='ipv6_addresses', type_=JSON, nullable=True)
    private_ip_addresses = Column(name='private_ip_addresses', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)