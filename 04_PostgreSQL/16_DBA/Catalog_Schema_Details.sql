In PostgreSQL, catalog tables (also called system catalogs) store metadata about the database objects such as tables, 
columns, data types, indexes, users, and other entities. These tables are part of the system schema, typically pg_catalog, 
and are automatically managed by PostgreSQL.

Key Catalog Tables in PostgreSQL
1. pg_database
Purpose: Stores information about databases in the cluster.
Key Columns:
datname: Name of the database.
datdba: Owner of the database.
encoding: Character encoding of the database.
datistemplate: Indicates if the database is a template.
Example Usage:

SELECT datname, datdba, encoding FROM pg_database;
2. pg_namespace
Purpose: Stores schemas within the database.
Key Columns:
nspname: Name of the schema.
nspowner: Owner of the schema.
Example Usage:

SELECT nspname, nspowner FROM pg_namespace;
3. pg_class
Purpose: Stores information about tables, indexes, and other relation-like objects.
Key Columns:
relname: Name of the relation (table, index, etc.).
relkind: Type of relation (r = table, i = index, etc.).
relnamespace: Schema ID of the relation.
Example Usage:

SELECT relname, relkind FROM pg_class WHERE relkind = 'r'; -- Lists all tables
4. pg_attribute
Purpose: Stores information about columns in tables.
Key Columns:
attname: Column name.
atttypid: Data type of the column.
attnum: Column position.
Example Usage:

SELECT attname, atttypid, attnum FROM pg_attribute WHERE attrelid = 'table_name'::regclass;
5. pg_type
Purpose: Stores data type definitions.
Key Columns:
typname: Name of the data type.
typtype: Type kind (b = base type, c = composite type, etc.).
Example Usage:

SELECT typname, typtype FROM pg_type;
6. pg_roles
Purpose: Stores information about roles and users.
Key Columns:
rolname: Role name.
rolsuper: Indicates if the role is a superuser.
rolvaliduntil: Password expiry timestamp.
Example Usage:

SELECT rolname, rolsuper FROM pg_roles;
7. pg_proc
Purpose: Stores information about functions and procedures.
Key Columns:
proname: Name of the function.
prorettype: Return type ID.
pronargs: Number of arguments.
Example Usage:

SELECT proname, pronargs FROM pg_proc;
8. pg_index
Purpose: Stores information about indexes.
Key Columns:
indexrelid: Index relation ID.
indrelid: Table relation ID.
indisunique: Indicates if the index is unique.
Example Usage:

SELECT indexrelid, indrelid, indisunique FROM pg_index;
9. pg_settings
Purpose: Stores runtime configuration settings.
Key Columns:
name: Configuration parameter name.
setting: Current value of the parameter.
Example Usage:

SELECT name, setting FROM pg_settings WHERE name = 'max_connections';
10. pg_stat_activity
Purpose: Provides information about currently running queries and sessions.
Key Columns:
datname: Database name.
usename: User name.
query: Current query being executed.
Example Usage:

SELECT datname, usename, query FROM pg_stat_activity;

Use of Catalog Tables
Metadata Queries: Catalog tables provide essential details about database objects for introspection, debugging, and management tasks.

Example: Listing all tables in a schema.


SELECT relname FROM pg_class c JOIN pg_namespace n ON c.relnamespace = n.oid
WHERE n.nspname = 'public' AND c.relkind = 'r';
Auditing and Monitoring: System views like pg_stat_activity or pg_locks help monitor database performance and identify long-running queries or lock contention.

Dynamic SQL and Automation: Catalog tables enable dynamic SQL generation based on metadata. Example: Generate SQL to drop all tables in a schema.


SELECT 'DROP TABLE ' || quote_ident(n.nspname) || '.' || quote_ident(c.relname) || ';'
FROM pg_class c JOIN pg_namespace n ON c.relnamespace = n.oid
WHERE n.nspname = 'public' AND c.relkind = 'r';
Dependency Tracking: Catalog tables track dependencies between objects. For example, pg_depend shows relationships between tables, indexes, and constraints.

Custom Scripts and Tools: Many database management tools and scripts use catalog tables to provide a user-friendly interface for database administration.