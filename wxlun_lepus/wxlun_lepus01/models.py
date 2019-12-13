# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminMenu(models.Model):
    menu_id = models.SmallIntegerField(primary_key=True)
    menu_title = models.CharField(max_length=30)
    menu_content = models.CharField(max_length=30)
    menu_level = models.IntegerField()
    parent_id = models.IntegerField()
    menu_url = models.CharField(max_length=255, blank=True, null=True)
    menu_icon = models.CharField(max_length=50, blank=True, null=True)
    system = models.IntegerField()
    status = models.IntegerField()
    display_order = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'admin_menu'


class AdminUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    realname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    login_count = models.IntegerField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=100, blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user'


class DbServersMysql(models.Model):
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True, null=True)
    monitor = models.IntegerField(blank=True, null=True)
    send_mail = models.IntegerField(blank=True, null=True)
    send_mail_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_sms_to_list = models.CharField(max_length=255, blank=True, null=True)
    send_slowquery_to_list = models.CharField(max_length=255, blank=True, null=True)
    alarm_threads_connected = models.IntegerField(blank=True, null=True)
    alarm_threads_running = models.IntegerField(blank=True, null=True)
    alarm_threads_waits = models.IntegerField(blank=True, null=True)
    alarm_repl_status = models.IntegerField(blank=True, null=True)
    alarm_repl_delay = models.IntegerField(blank=True, null=True)
    threshold_warning_threads_connected = models.IntegerField(blank=True, null=True)
    threshold_warning_threads_running = models.IntegerField(blank=True, null=True)
    threshold_warning_threads_waits = models.IntegerField(blank=True, null=True)
    threshold_warning_repl_delay = models.IntegerField(blank=True, null=True)
    threshold_critical_threads_connected = models.IntegerField(blank=True, null=True)
    threshold_critical_threads_running = models.IntegerField(blank=True, null=True)
    threshold_critical_threads_waits = models.IntegerField(blank=True, null=True)
    threshold_critical_repl_delay = models.IntegerField(blank=True, null=True)
    slow_query = models.IntegerField()
    binlog_auto_purge = models.IntegerField()
    binlog_store_days = models.SmallIntegerField()
    bigtable_monitor = models.IntegerField()
    bigtable_size = models.IntegerField()
    is_delete = models.IntegerField()
    display_order = models.SmallIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_servers_mysql'


class MysqlBigtable(models.Model):
    server_id = models.SmallIntegerField(blank=True, null=True)
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    db_name = models.CharField(max_length=50, blank=True, null=True)
    table_name = models.CharField(max_length=100, blank=True, null=True)
    table_size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    table_comment = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_bigtable'


class MysqlBigtableHistory(models.Model):
    server_id = models.SmallIntegerField(blank=True, null=True)
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    db_name = models.CharField(max_length=50, blank=True, null=True)
    table_name = models.CharField(max_length=100, blank=True, null=True)
    table_size = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    table_comment = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    ymd = models.IntegerField(db_column='Ymd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysql_bigtable_history'


class MysqlInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    host = models.CharField(max_length=30)
    post = models.CharField(max_length=30)
    is_delete = models.IntegerField()
    instance_name = models.CharField(max_length=30, blank=True, null=True)
    dblist = models.CharField(max_length=5000, blank=True, null=True)
    dbcount = models.BigIntegerField(blank=True, null=True)
    tablecount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_info'


class MysqlReplication(models.Model):
    server_id = models.SmallIntegerField(blank=True, null=True)
    tags = models.CharField(max_length=50)
    host = models.CharField(max_length=30, blank=True, null=True)
    port = models.CharField(max_length=20, blank=True, null=True)
    is_master = models.IntegerField(blank=True, null=True)
    is_slave = models.PositiveIntegerField(blank=True, null=True)
    read_only = models.CharField(max_length=10, blank=True, null=True)
    gtid_mode = models.CharField(max_length=10, blank=True, null=True)
    master_server = models.CharField(max_length=30, blank=True, null=True)
    master_port = models.CharField(max_length=20, blank=True, null=True)
    slave_io_run = models.CharField(max_length=20, blank=True, null=True)
    slave_sql_run = models.CharField(max_length=20, blank=True, null=True)
    delay = models.CharField(max_length=20, blank=True, null=True)
    current_binlog_file = models.CharField(max_length=30, blank=True, null=True)
    current_binlog_pos = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_file = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_pos = models.CharField(max_length=30, blank=True, null=True)
    master_binlog_space = models.BigIntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_replication'


class MysqlSlowQueryReview(models.Model):
    checksum = models.BigIntegerField(primary_key=True)
    fingerprint = models.TextField()
    sample = models.TextField()
    first_seen = models.DateTimeField(blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)
    reviewed_by = models.CharField(max_length=20, blank=True, null=True)
    reviewed_on = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mysql_slow_query_review'


class MysqlSlowQueryReviewHistory(models.Model):
    serverid_max = models.SmallIntegerField()
    db_max = models.CharField(max_length=100, blank=True, null=True)
    user_max = models.CharField(max_length=100, blank=True, null=True)
    checksum = models.BigIntegerField(primary_key=True)
    sample = models.TextField()
    ts_min = models.DateTimeField()
    ts_max = models.DateTimeField()
    ts_cnt = models.FloatField(blank=True, null=True)
    query_time_sum = models.FloatField(db_column='Query_time_sum', blank=True, null=True)  # Field name made lowercase.
    query_time_min = models.FloatField(db_column='Query_time_min', blank=True, null=True)  # Field name made lowercase.
    query_time_max = models.FloatField(db_column='Query_time_max', blank=True, null=True)  # Field name made lowercase.
    query_time_pct_95 = models.FloatField(db_column='Query_time_pct_95', blank=True, null=True)  # Field name made lowercase.
    query_time_stddev = models.FloatField(db_column='Query_time_stddev', blank=True, null=True)  # Field name made lowercase.
    query_time_median = models.FloatField(db_column='Query_time_median', blank=True, null=True)  # Field name made lowercase.
    lock_time_sum = models.FloatField(db_column='Lock_time_sum', blank=True, null=True)  # Field name made lowercase.
    lock_time_min = models.FloatField(db_column='Lock_time_min', blank=True, null=True)  # Field name made lowercase.
    lock_time_max = models.FloatField(db_column='Lock_time_max', blank=True, null=True)  # Field name made lowercase.
    lock_time_pct_95 = models.FloatField(db_column='Lock_time_pct_95', blank=True, null=True)  # Field name made lowercase.
    lock_time_stddev = models.FloatField(db_column='Lock_time_stddev', blank=True, null=True)  # Field name made lowercase.
    lock_time_median = models.FloatField(db_column='Lock_time_median', blank=True, null=True)  # Field name made lowercase.
    rows_sent_sum = models.FloatField(db_column='Rows_sent_sum', blank=True, null=True)  # Field name made lowercase.
    rows_sent_min = models.FloatField(db_column='Rows_sent_min', blank=True, null=True)  # Field name made lowercase.
    rows_sent_max = models.FloatField(db_column='Rows_sent_max', blank=True, null=True)  # Field name made lowercase.
    rows_sent_pct_95 = models.FloatField(db_column='Rows_sent_pct_95', blank=True, null=True)  # Field name made lowercase.
    rows_sent_stddev = models.FloatField(db_column='Rows_sent_stddev', blank=True, null=True)  # Field name made lowercase.
    rows_sent_median = models.FloatField(db_column='Rows_sent_median', blank=True, null=True)  # Field name made lowercase.
    rows_examined_sum = models.FloatField(db_column='Rows_examined_sum', blank=True, null=True)  # Field name made lowercase.
    rows_examined_min = models.FloatField(db_column='Rows_examined_min', blank=True, null=True)  # Field name made lowercase.
    rows_examined_max = models.FloatField(db_column='Rows_examined_max', blank=True, null=True)  # Field name made lowercase.
    rows_examined_pct_95 = models.FloatField(db_column='Rows_examined_pct_95', blank=True, null=True)  # Field name made lowercase.
    rows_examined_stddev = models.FloatField(db_column='Rows_examined_stddev', blank=True, null=True)  # Field name made lowercase.
    rows_examined_median = models.FloatField(db_column='Rows_examined_median', blank=True, null=True)  # Field name made lowercase.
    rows_affected_sum = models.FloatField(db_column='Rows_affected_sum', blank=True, null=True)  # Field name made lowercase.
    rows_affected_min = models.FloatField(db_column='Rows_affected_min', blank=True, null=True)  # Field name made lowercase.
    rows_affected_max = models.FloatField(db_column='Rows_affected_max', blank=True, null=True)  # Field name made lowercase.
    rows_affected_pct_95 = models.FloatField(db_column='Rows_affected_pct_95', blank=True, null=True)  # Field name made lowercase.
    rows_affected_stddev = models.FloatField(db_column='Rows_affected_stddev', blank=True, null=True)  # Field name made lowercase.
    rows_affected_median = models.FloatField(db_column='Rows_affected_median', blank=True, null=True)  # Field name made lowercase.
    rows_read_sum = models.FloatField(db_column='Rows_read_sum', blank=True, null=True)  # Field name made lowercase.
    rows_read_min = models.FloatField(db_column='Rows_read_min', blank=True, null=True)  # Field name made lowercase.
    rows_read_max = models.FloatField(db_column='Rows_read_max', blank=True, null=True)  # Field name made lowercase.
    rows_read_pct_95 = models.FloatField(db_column='Rows_read_pct_95', blank=True, null=True)  # Field name made lowercase.
    rows_read_stddev = models.FloatField(db_column='Rows_read_stddev', blank=True, null=True)  # Field name made lowercase.
    rows_read_median = models.FloatField(db_column='Rows_read_median', blank=True, null=True)  # Field name made lowercase.
    merge_passes_sum = models.FloatField(db_column='Merge_passes_sum', blank=True, null=True)  # Field name made lowercase.
    merge_passes_min = models.FloatField(db_column='Merge_passes_min', blank=True, null=True)  # Field name made lowercase.
    merge_passes_max = models.FloatField(db_column='Merge_passes_max', blank=True, null=True)  # Field name made lowercase.
    merge_passes_pct_95 = models.FloatField(db_column='Merge_passes_pct_95', blank=True, null=True)  # Field name made lowercase.
    merge_passes_stddev = models.FloatField(db_column='Merge_passes_stddev', blank=True, null=True)  # Field name made lowercase.
    merge_passes_median = models.FloatField(db_column='Merge_passes_median', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_min = models.FloatField(db_column='InnoDB_IO_r_ops_min', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_max = models.FloatField(db_column='InnoDB_IO_r_ops_max', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_pct_95 = models.FloatField(db_column='InnoDB_IO_r_ops_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_stddev = models.FloatField(db_column='InnoDB_IO_r_ops_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_ops_median = models.FloatField(db_column='InnoDB_IO_r_ops_median', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_min = models.FloatField(db_column='InnoDB_IO_r_bytes_min', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_max = models.FloatField(db_column='InnoDB_IO_r_bytes_max', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_pct_95 = models.FloatField(db_column='InnoDB_IO_r_bytes_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_stddev = models.FloatField(db_column='InnoDB_IO_r_bytes_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_bytes_median = models.FloatField(db_column='InnoDB_IO_r_bytes_median', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_min = models.FloatField(db_column='InnoDB_IO_r_wait_min', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_max = models.FloatField(db_column='InnoDB_IO_r_wait_max', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_pct_95 = models.FloatField(db_column='InnoDB_IO_r_wait_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_stddev = models.FloatField(db_column='InnoDB_IO_r_wait_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_io_r_wait_median = models.FloatField(db_column='InnoDB_IO_r_wait_median', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_min = models.FloatField(db_column='InnoDB_rec_lock_wait_min', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_max = models.FloatField(db_column='InnoDB_rec_lock_wait_max', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_pct_95 = models.FloatField(db_column='InnoDB_rec_lock_wait_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_stddev = models.FloatField(db_column='InnoDB_rec_lock_wait_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_rec_lock_wait_median = models.FloatField(db_column='InnoDB_rec_lock_wait_median', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_min = models.FloatField(db_column='InnoDB_queue_wait_min', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_max = models.FloatField(db_column='InnoDB_queue_wait_max', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_pct_95 = models.FloatField(db_column='InnoDB_queue_wait_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_stddev = models.FloatField(db_column='InnoDB_queue_wait_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_queue_wait_median = models.FloatField(db_column='InnoDB_queue_wait_median', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_min = models.FloatField(db_column='InnoDB_pages_distinct_min', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_max = models.FloatField(db_column='InnoDB_pages_distinct_max', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_pct_95 = models.FloatField(db_column='InnoDB_pages_distinct_pct_95', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_stddev = models.FloatField(db_column='InnoDB_pages_distinct_stddev', blank=True, null=True)  # Field name made lowercase.
    innodb_pages_distinct_median = models.FloatField(db_column='InnoDB_pages_distinct_median', blank=True, null=True)  # Field name made lowercase.
    qc_hit_cnt = models.FloatField(db_column='QC_Hit_cnt', blank=True, null=True)  # Field name made lowercase.
    qc_hit_sum = models.FloatField(db_column='QC_Hit_sum', blank=True, null=True)  # Field name made lowercase.
    full_scan_cnt = models.FloatField(db_column='Full_scan_cnt', blank=True, null=True)  # Field name made lowercase.
    full_scan_sum = models.FloatField(db_column='Full_scan_sum', blank=True, null=True)  # Field name made lowercase.
    full_join_cnt = models.FloatField(db_column='Full_join_cnt', blank=True, null=True)  # Field name made lowercase.
    full_join_sum = models.FloatField(db_column='Full_join_sum', blank=True, null=True)  # Field name made lowercase.
    tmp_table_cnt = models.FloatField(db_column='Tmp_table_cnt', blank=True, null=True)  # Field name made lowercase.
    tmp_table_sum = models.FloatField(db_column='Tmp_table_sum', blank=True, null=True)  # Field name made lowercase.
    tmp_table_on_disk_cnt = models.FloatField(db_column='Tmp_table_on_disk_cnt', blank=True, null=True)  # Field name made lowercase.
    tmp_table_on_disk_sum = models.FloatField(db_column='Tmp_table_on_disk_sum', blank=True, null=True)  # Field name made lowercase.
    filesort_cnt = models.FloatField(db_column='Filesort_cnt', blank=True, null=True)  # Field name made lowercase.
    filesort_sum = models.FloatField(db_column='Filesort_sum', blank=True, null=True)  # Field name made lowercase.
    filesort_on_disk_cnt = models.FloatField(db_column='Filesort_on_disk_cnt', blank=True, null=True)  # Field name made lowercase.
    filesort_on_disk_sum = models.FloatField(db_column='Filesort_on_disk_sum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mysql_slow_query_review_history'
        unique_together = (('checksum', 'ts_min', 'ts_max'),)


class MysqlSlowQuerySendmailLog(models.Model):
    server_id = models.SmallIntegerField()
    sendmail_status = models.IntegerField()
    sendmail_info = models.CharField(max_length=50, blank=True, null=True)
    sendmail_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mysql_slow_query_sendmail_log'


class MysqlStatus(models.Model):
    server_id = models.SmallIntegerField()
    host = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    connect = models.SmallIntegerField()
    role = models.CharField(max_length=30)
    uptime = models.IntegerField()
    version = models.CharField(max_length=50)
    max_connections = models.SmallIntegerField()
    max_connect_errors = models.SmallIntegerField()
    open_files_limit = models.IntegerField()
    open_files = models.SmallIntegerField()
    table_open_cache = models.SmallIntegerField()
    open_tables = models.SmallIntegerField()
    max_tmp_tables = models.SmallIntegerField()
    max_heap_table_size = models.IntegerField()
    max_allowed_packet = models.IntegerField()
    threads_connected = models.IntegerField()
    threads_running = models.IntegerField()
    threads_waits = models.IntegerField()
    threads_created = models.IntegerField()
    threads_cached = models.IntegerField()
    connections = models.IntegerField()
    aborted_clients = models.IntegerField()
    aborted_connects = models.IntegerField()
    connections_persecond = models.SmallIntegerField()
    bytes_received_persecond = models.IntegerField()
    bytes_sent_persecond = models.IntegerField()
    com_select_persecond = models.SmallIntegerField()
    com_insert_persecond = models.SmallIntegerField()
    com_update_persecond = models.SmallIntegerField()
    com_delete_persecond = models.SmallIntegerField()
    com_commit_persecond = models.SmallIntegerField()
    com_rollback_persecond = models.SmallIntegerField()
    questions_persecond = models.IntegerField()
    queries_persecond = models.IntegerField()
    transaction_persecond = models.SmallIntegerField()
    created_tmp_tables_persecond = models.SmallIntegerField()
    created_tmp_disk_tables_persecond = models.SmallIntegerField()
    created_tmp_files_persecond = models.SmallIntegerField()
    table_locks_immediate_persecond = models.IntegerField()
    table_locks_waited_persecond = models.SmallIntegerField()
    key_buffer_size = models.BigIntegerField()
    sort_buffer_size = models.IntegerField()
    join_buffer_size = models.IntegerField()
    key_blocks_not_flushed = models.IntegerField()
    key_blocks_unused = models.IntegerField()
    key_blocks_used = models.IntegerField()
    key_read_requests_persecond = models.IntegerField()
    key_reads_persecond = models.IntegerField()
    key_write_requests_persecond = models.IntegerField()
    key_writes_persecond = models.IntegerField()
    innodb_version = models.CharField(max_length=30)
    innodb_buffer_pool_instances = models.SmallIntegerField()
    innodb_buffer_pool_size = models.BigIntegerField()
    innodb_doublewrite = models.CharField(max_length=10)
    innodb_file_per_table = models.CharField(max_length=10)
    innodb_flush_log_at_trx_commit = models.IntegerField()
    innodb_flush_method = models.CharField(max_length=30)
    innodb_force_recovery = models.IntegerField()
    innodb_io_capacity = models.IntegerField()
    innodb_read_io_threads = models.IntegerField()
    innodb_write_io_threads = models.IntegerField()
    innodb_buffer_pool_pages_total = models.IntegerField()
    innodb_buffer_pool_pages_data = models.IntegerField()
    innodb_buffer_pool_pages_dirty = models.IntegerField()
    innodb_buffer_pool_pages_flushed = models.BigIntegerField()
    innodb_buffer_pool_pages_free = models.IntegerField()
    innodb_buffer_pool_pages_misc = models.IntegerField()
    innodb_page_size = models.IntegerField()
    innodb_pages_created = models.BigIntegerField()
    innodb_pages_read = models.BigIntegerField()
    innodb_pages_written = models.BigIntegerField()
    innodb_row_lock_current_waits = models.CharField(max_length=100)
    innodb_buffer_pool_pages_flushed_persecond = models.IntegerField()
    innodb_buffer_pool_read_requests_persecond = models.IntegerField()
    innodb_buffer_pool_reads_persecond = models.IntegerField()
    innodb_buffer_pool_write_requests_persecond = models.IntegerField()
    innodb_rows_read_persecond = models.IntegerField()
    innodb_rows_inserted_persecond = models.IntegerField()
    innodb_rows_updated_persecond = models.IntegerField()
    innodb_rows_deleted_persecond = models.IntegerField()
    query_cache_hitrate = models.CharField(max_length=10)
    thread_cache_hitrate = models.CharField(max_length=10)
    key_buffer_read_rate = models.CharField(max_length=10)
    key_buffer_write_rate = models.CharField(max_length=10)
    key_blocks_used_rate = models.CharField(max_length=10)
    created_tmp_disk_tables_rate = models.CharField(max_length=10)
    connections_usage_rate = models.CharField(max_length=10)
    open_files_usage_rate = models.CharField(max_length=10)
    open_tables_usage_rate = models.CharField(max_length=10)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mysql_status'


class MysqlVariables(models.Model):
    id = models.BigAutoField(primary_key=True)
    vname = models.CharField(max_length=30)
    vvalue = models.CharField(max_length=30)
    host = models.CharField(max_length=30)
    post = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mysql_variables'
