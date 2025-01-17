from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRedshiftSnapshot(Base):
    __tablename__ = 'aws_redshift_snapshot'
    snapshot_identifier = Column('snapshot_identifier', Text, nullable=True)
    cluster_identifier = Column('cluster_identifier', Text, nullable=True)
    snapshot_type = Column('snapshot_type', Text, nullable=True)
    actual_incremental_backup_size_in_mega_bytes = Column('actual_incremental_backup_size_in_mega_bytes', psql.DOUBLE_PRECISION, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    backup_progress_in_mega_bytes = Column('backup_progress_in_mega-bytes', psql.DOUBLE_PRECISION, nullable=True)
    cluster_create_time = Column('cluster_create_time', TIMESTAMP, nullable=True)
    cluster_version = Column('cluster_version', Text, nullable=True)
    current_backup_rate_in_mega_bytes_per_second = Column('current_backup_rate_in_mega_bytes_per_second', psql.DOUBLE_PRECISION, nullable=True)
    db_name = Column('db_name', Text, nullable=True)
    elapsed_time_in_seconds = Column('elapsed_time_in_seconds', Text, nullable=True)
    encrypted = Column('encrypted', Boolean, nullable=True)
    encrypted_with_hsm = Column('encrypted_with_hsm', Boolean, nullable=True)
    engine_full_version = Column('engine_full_version', Text, nullable=True)
    enhanced_vpc_routing = Column('enhanced_vpc_routing', Boolean, nullable=True)
    estimated_seconds_to_completion = Column('estimated_seconds_to_completion', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    maintenance_track_name = Column('maintenance_track_name', Text, nullable=True)
    manual_snapshot_remaining_days = Column('manual_snapshot_remaining_days', BigInteger, nullable=True)
    manual_snapshot_retention_period = Column('manual_snapshot_retention_period', BigInteger, nullable=True)
    master_username = Column('master_username', Text, nullable=True)
    node_type = Column('node_type', Text, nullable=True)
    number_of_nodes = Column('number_of_nodes', BigInteger, nullable=True)
    owner_account = Column('owner_account', Text, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    snapshot_create_time = Column('snapshot_create_time', Text, nullable=True)
    snapshot_retention_start_time = Column('snapshot_retention_start_time', TIMESTAMP, nullable=True)
    source_region = Column('source_region', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    total_backup_size_in_mega_bytes = Column('total_backup_size_in_mega_bytes', psql.DOUBLE_PRECISION, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    accounts_with_restore_access = Column('accounts_with_restore_access', JSON, nullable=True)
    restorable_node_types = Column('restorable_node_types', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)