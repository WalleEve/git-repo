pg_stat_activity Table: Overview
The pg_stat_activity system view in PostgreSQL provides real-time information about the active database connections and the queries being executed. It is a crucial tool for monitoring and diagnosing issues such as long-running queries, idle sessions, or connection overloads.

Key Columns in pg_stat_activity
Here are the most important columns in the pg_stat_activity view:

Column Name	Description
datid	OID of the database the session is connected to.
datname	Name of the database the session is connected to.
pid	Process ID (PID) of the backend process.
usename	Name of the user connected to the session.
application_name	Name of the application connected (set by the client).
client_addr	IP address of the client connected to the session (or NULL for local connections).
client_port	Port number of the client connected to the session.
backend_start	Timestamp when the backend process was started.
xact_start	Timestamp of the start of the current transaction, if any.
query_start	Timestamp of when the current query started executing.
state_change	Timestamp of the last state change (e.g., from active to idle).
state	Current state of the connection: active, idle, idle in transaction, waiting, disabled.
query	The most recent query executed by the session.
backend_type	Type of backend process (e.g., client backend, autovacuum worker, etc.).
Common States in the state Column
active: The session is currently executing a query.
idle: The session is waiting for the next query from the client.
idle in transaction: The session is in an open transaction but not executing any query.
waiting: The session is waiting for a resource (e.g., a lock).
disabled: The session is disabled due to connection limits or other reasons.
Practical Use Cases of pg_stat_activity
1. List All Active Queries
To identify queries currently being executed:


SELECT pid, usename, query, state, query_start
FROM pg_stat_activity
WHERE state = 'active';
2. Find Long-Running Queries
To identify queries that have been running for a long time:


SELECT pid, usename, query, NOW() - query_start AS duration
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY duration DESC;
3. Terminate a Session
To terminate a session (e.g., for a stuck or problematic query):


SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE pid = <process_id>;
4. Monitor Idle Sessions
To find idle sessions consuming resources:


SELECT pid, usename, application_name, state, backend_start
FROM pg_stat_activity
WHERE state = 'idle';
5. Track Application Usage
To see which applications are connected and their activity:


SELECT application_name, COUNT(*) AS connections
FROM pg_stat_activity
GROUP BY application_name;
Permissions Required
By default, regular users can only see their own queries in pg_stat_activity. To allow them to see all queries:

Grant them the pg_monitor role:

GRANT pg_monitor TO username;
Alternatively, superusers have unrestricted access.
Benefits of pg_stat_activity
Real-Time Monitoring: Helps in identifying performance bottlenecks or query-related issues.
Connection Management: Monitors how many sessions are connected and their state.
Resource Optimization: Tracks sessions and queries that may need termination or optimization.
Security Auditing: Identifies potentially malicious or unauthorized queries.
The pg_stat_activity table is an invaluable tool for database administrators, enabling effective monitoring and proactive management of PostgreSQL connections and workloads.