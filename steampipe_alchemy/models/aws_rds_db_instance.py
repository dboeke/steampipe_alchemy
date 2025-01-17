from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRdsDbInstance(Base):
    __tablename__ = 'aws_rds_db_instance'
    db_instance_identifier = Column('db_instance_identifier', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    db_cluster_identifier = Column('db_cluster_identifier', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    _class = Column('class', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)
    allocated_storage = Column('allocated_storage', BigInteger, nullable=True)
    auto_minor_version_upgrade = Column('auto_minor_version_upgrade', Boolean, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    backup_retention_period = Column('backup_retention_period', BigInteger, nullable=True)
    ca_certificate_identifier = Column('ca_certificate_identifier', Text, nullable=True)
    character_set_name = Column('character_set_name', Text, nullable=True)
    copy_tags_to_snapshot = Column('copy_tags_to_snapshot', Boolean, nullable=True)
    customer_owned_ip_enabled = Column('customer_owned_ip_enabled', Boolean, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    db_name = Column('db_name', Text, nullable=True)
    db_subnet_group_arn = Column('db_subnet_group_arn', Text, nullable=True)
    db_subnet_group_description = Column('db_subnet_group_description', Text, nullable=True)
    db_subnet_group_name = Column('db_subnet_group_name', Text, nullable=True)
    db_subnet_group_status = Column('db_subnet_group_status', Text, nullable=True)
    deletion_protection = Column('deletion_protection', Boolean, nullable=True)
    endpoint_address = Column('endpoint_address', Text, nullable=True)
    endpoint_hosted_zone_id = Column('endpoint_hosted_zone_id', Text, nullable=True)
    endpoint_port = Column('endpoint_port', BigInteger, nullable=True)
    engine = Column('engine', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    enhanced_monitoring_resource_arn = Column('enhanced_monitoring_resource_arn', Text, nullable=True)
    iam_database_authentication_enabled = Column('iam_database_authentication_enabled', Boolean, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    iops = Column('iops', BigInteger, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    latest_restorable_time = Column('latest_restorable_time', TIMESTAMP, nullable=True)
    license_model = Column('license_model', Text, nullable=True)
    master_user_name = Column('master_user_name', Text, nullable=True)
    max_allocated_storage = Column('max_allocated_storage', BigInteger, nullable=True)
    monitoring_interval = Column('monitoring_interval', BigInteger, nullable=True)
    monitoring_role_arn = Column('monitoring_role_arn', Text, nullable=True)
    multi_az = Column('multi_az', Boolean, nullable=True)
    nchar_character_set_name = Column('nchar_character_set_name', Text, nullable=True)
    performance_insights_enabled = Column('performance_insights_enabled', Boolean, nullable=True)
    performance_insights_kms_key_id = Column('performance_insights_kms_key_id', Text, nullable=True)
    performance_insights_retention_period = Column('performance_insights_retention_period', BigInteger, nullable=True)
    preferred_backup_window = Column('preferred_backup_window', Text, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    promotion_tier = Column('promotion_tier', BigInteger, nullable=True)
    publicly_accessible = Column('publicly_accessible', Boolean, nullable=True)
    read_replica_source_db_instance_identifier = Column('read_replica_source_db_instance_identifier', Text, nullable=True)
    replica_mode = Column('replica_mode', Text, nullable=True)
    secondary_availability_zone = Column('secondary_availability_zone', Text, nullable=True)
    storage_encrypted = Column('storage_encrypted', Boolean, nullable=True)
    storage_type = Column('storage_type', Text, nullable=True)
    tde_credential_arn = Column('tde_credential_arn', Text, nullable=True)
    timezone = Column('timezone', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    associated_roles = Column('associated_roles', JSON, nullable=True)
    db_parameter_groups = Column('db_parameter_groups', JSON, nullable=True)
    db_security_groups = Column('db_security_groups', JSON, nullable=True)
    domain_memberships = Column('domain_memberships', JSON, nullable=True)
    enabled_cloudwatch_logs_exports = Column('enabled_cloudwatch_logs_exports', JSON, nullable=True)
    option_group_memberships = Column('option_group_memberships', JSON, nullable=True)
    processor_features = Column('processor_features', JSON, nullable=True)
    read_replica_db_cluster_identifiers = Column('read_replica_db_cluster_identifiers', JSON, nullable=True)
    read_replica_db_instance_identifiers = Column('read_replica_db_instance_identifiers', JSON, nullable=True)
    status_infos = Column('status_infos', JSON, nullable=True)
    subnets = Column('subnets', JSON, nullable=True)
    vpc_security_groups = Column('vpc_security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)