# Python - connecting to Cassandra

## Scripts

Run the python scripts ordered by number to have a set of interactions with the DB from Python.

## CQL Console

Some CQL commands to check the result of the Python scripts:

```cql
use todos;
DESCRIBE TABLE todoitems;
```

```cql
select * from todoitems;
```

**Cleanup**

**Caution: You will lose all the data** if you run the following command in the CQL Console

```cql
DROP TABLE IF EXISTS todos.todoitems;
```
