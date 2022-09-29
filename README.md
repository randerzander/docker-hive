Repo based on https://hshirodkar.medium.com/apache-hive-on-docker-4d7280ac6f8e

Start Hive & components
```
docker-compose up
```
Bash in and create table
```
docker exec -it hive-server /bin/bash
cd /employee
# create table
hive -f employee/employe_table.hql
# put data for table into hdfs
hadoop fs -put employee.csv hdfs://namenode:8020/user/hive/warehouse/testdb.db/employee
# test everything looks good
hive -e "select * from testdb.employee"
```

Start a container with the same network (`docker network ls` to list)
```
pip install -y pyhive[hive]
conda install -c conda-forge -y sasl

python dask_sql_test.py
```
Trace:
```
>>> c.create_table("employee", cursor, hive_table_name="testdb.employee")
INFO:pyhive.hive:USE default
INFO:pyhive.hive:DESCRIBE FORMATTED testdb.employee
thread '<unnamed>' panicked at 'not implemented: SqlTypeName::from_string() for str type: STRING', src/sql/types.rs:323:18
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/conda/envs/rapids/lib/python3.9/site-packages/dask_sql/context.py", line 238, in create_table
    dc = InputUtil.to_dc(
  File "/opt/conda/envs/rapids/lib/python3.9/site-packages/dask_sql/input_utils/convert.py", line 68, in to_dc
    table = filled_get_dask_dataframe(input_item)
  File "/opt/conda/envs/rapids/lib/python3.9/site-packages/dask_sql/input_utils/convert.py", line 57, in <lambda>
    filled_get_dask_dataframe = lambda *args: cls._get_dask_dataframe(
  File "/opt/conda/envs/rapids/lib/python3.9/site-packages/dask_sql/input_utils/convert.py", line 90, in _get_dask_dataframe
    return plugin.to_dc(
  File "/opt/conda/envs/rapids/lib/python3.9/site-packages/dask_sql/input_utils/hive.py", line 69, in to_dc
    column_information = {
  File "/opt/conda/envs/rapids/lib/python3.9/site-packages/dask_sql/input_utils/hive.py", line 70, in <dictcomp>
    col: sql_to_python_type(SqlTypeName.fromString(col_type.upper()))
pyo3_runtime.PanicException: not implemented: SqlTypeName::from_string() for str type: STRING
```
