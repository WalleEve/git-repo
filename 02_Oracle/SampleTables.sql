-- Employees Table
CREATE TEMP TABLE FUNCTION Employees() AS (
  SELECT * FROM UNNEST([
    STRUCT('hpatel' AS user_id, 'Hitesh Patel' AS user_name, 101 AS team_id, DATE('2022-01-15') AS hire_date, 120000 AS salary),
    STRUCT('rsharma' AS user_id, 'Riya Sharma' AS user_name, 101 AS team_id, DATE('2021-06-01') AS hire_date, 150000 AS salary),
    STRUCT('pchen' AS user_id, 'Priya Chen' AS user_name, 102 AS team_id, DATE('2023-02-28') AS hire_date, 100000 AS salary),
    STRUCT('mkim' AS user_id, 'Min Kim' AS user_name, 102 AS team_id, DATE('2022-08-10') AS hire_date, 180000 AS salary),
    STRUCT('vrao' AS user_id, 'Vikram Rao' AS user_name, 103 AS team_id, DATE('2020-11-05') AS hire_date, 250000 AS salary),
    STRUCT('ajackson' AS user_id, 'Aisha Jackson' AS user_name, 101 AS team_id, DATE('2023-07-15') AS hire_date, 110000 AS salary),
    STRUCT('slee' AS user_id, 'Sam Lee' AS user_name, 104 AS team_id, DATE('2021-02-01') AS hire_date, 300000 AS salary),
    STRUCT('cwalsh' AS user_id, 'Conor Walsh' AS user_name, 102 AS team_id, DATE('2022-05-20') AS hire_date, 160000 AS salary)
  ])
);

-- Teams Table
CREATE TEMP TABLE FUNCTION Teams() AS (
  SELECT * FROM UNNEST([
    STRUCT(101 AS team_id, 'Cloud Crusaders' AS team_name, 'rsharma' AS lead_user_id),
    STRUCT(102 AS team_id, 'AI Innovators' AS team_name, 'mkim' AS lead_user_id),
    STRUCT(103 AS team_id, 'Infra Wizards' AS team_name, 'vrao' AS lead_user_id),
    STRUCT(104 AS team_id, 'Data Dynamos' AS team_name, 'slee' AS lead_user_id)
  ])
);

-- Projects Table
CREATE TEMP TABLE FUNCTION Projects() AS (
  SELECT * FROM UNNEST([
    STRUCT(1 AS project_id, 'Alpha Launch' AS project_name, 101 AS team_id, 'COMPLETED' AS status, DATE('2023-01-10') AS start_date, DATE('2023-06-30') AS end_date),
    STRUCT(2 AS project_id, 'Beta Test' AS project_name, 101 AS team_id, 'IN_PROGRESS' AS status, DATE('2023-07-01') AS start_date, NULL AS end_date),
    STRUCT(3 AS project_id, 'Model Training' AS project_name, 102 AS team_id, 'IN_PROGRESS' AS status, DATE('2023-03-15') AS start_date, NULL AS end_date),
    STRUCT(4 AS project_id, 'New Infra' AS project_name, 103 AS team_id, 'COMPLETED' AS status, DATE('2022-05-01') AS start_date, DATE('2023-05-01') AS end_date),
    STRUCT(5 AS project_id, 'Data Pipeline' AS project_name, 104 AS team_id, 'PLANNING' AS status, NULL AS start_date, NULL AS end_date),
    STRUCT(6 AS project_id, 'UI Refresh' AS project_name, 101 AS team_id, 'CANCELLED' AS status, DATE('2023-02-01') AS start_date, DATE('2023-03-01') AS end_date),
    STRUCT(7 AS project_id, 'Algo Optimization' AS project_name, 102 AS team_id, 'COMPLETED' AS status, DATE('2022-09-01') AS start_date, DATE('2023-02-28') AS end_date)
  ])
);

-- Assignments Table
CREATE TEMP TABLE FUNCTION Assignments() AS (
  SELECT * FROM UNNEST([
    STRUCT(1 AS assignment_id, 1 AS project_id, 'hpatel' AS user_id, 'SWE' AS role),
    STRUCT(2 AS assignment_id, 1 AS project_id, 'rsharma' AS user_id, 'TL' AS role),
    STRUCT(3 AS assignment_id, 2 AS project_id, 'hpatel' AS user_id, 'SWE' AS role),
    STRUCT(4 AS assignment_id, 2 AS project_id, 'ajackson' AS user_id, 'SWE' AS role),
    STRUCT(5 AS assignment_id, 2 AS project_id, 'rsharma' AS user_id, 'TL' AS role),
    STRUCT(6 AS assignment_id, 3 AS project_id, 'pchen' AS user_id, 'SWE' AS role),
    STRUCT(7 AS assignment_id, 3 AS project_id, 'mkim' AS user_id, 'TL' AS role),
    STRUCT(8 AS assignment_id, 3 AS project_id, 'cwalsh' AS user_id, 'SWE' AS role),
    STRUCT(9 AS assignment_id, 4 AS project_id, 'vrao' AS user_id, 'TL' AS role),
    STRUCT(10 AS assignment_id, 7 AS project_id, 'mkim' AS user_id, 'TL' AS role),
    STRUCT(11 AS assignment_id, 7 AS project_id, 'cwalsh' AS user_id, 'SWE' AS role)
  ])
);



-- Scenario: We need a list of all 'IN_PROGRESS' projects, including the project name, status, and the name of the team working on it.
-- Scenario: Find the average salary of employees within each team. Also, include the team name and the name of the team lead.
-- Scenario: For each employee, determine their salary rank within their own team (highest salary is rank 1). Also, calculate the difference between each employee's salary and the average salary of their team.
-- Scenario: Identify teams where the lead's salary is less than the average salary of the other members of their team.




WITH
  Customers AS (
    SELECT * FROM UNNEST([
      STRUCT(1 AS customer_id, 'TechCorp' AS customer_name, 10 AS region_id, 100 AS vertical_id, DATE('2020-01-01') AS creation_date),
      STRUCT(2 AS customer_id, 'RetailInc' AS customer_name, 10 AS region_id, 101 AS vertical_id, DATE('2021-03-15') AS creation_date),
      STRUCT(3 AS customer_id, 'FinServ' AS customer_name, 11 AS region_id, 102 AS vertical_id, DATE('2019-05-10') AS creation_date)
    ])
  ),
  Regions AS (
    SELECT * FROM UNNEST([
      STRUCT(10 AS region_id, 'North America' AS region_name, 'US' AS country_code),
      STRUCT(11 AS region_id, 'EMEA' AS region_name, 'DE' AS country_code)
    ])
  ),
  Countries AS (
    SELECT * FROM UNNEST([
      STRUCT('US' AS country_code, 'United States' AS country_name, 'Americas' AS continent),
      STRUCT('DE' AS country_code, 'Germany' AS country_name, 'Europe' AS continent)
    ])
  ),
  Verticals AS (
    SELECT * FROM UNNEST([
      STRUCT(100 AS vertical_id, 'Technology' AS vertical_name),
      STRUCT(101 AS vertical_id, 'Retail' AS vertical_name),
      STRUCT(102 AS vertical_id, 'Finance' AS vertical_name)
    ])
  ),
  Campaigns AS (
    SELECT * FROM UNNEST([
      STRUCT(1 AS campaign_id, 1 AS customer_id, 'TechCorp Q1 Campaign' AS campaign_name, 'ACTIVE' AS status, DATE('2024-01-01') AS start_date, DATE('2024-03-31') AS end_date, 50000 AS budget),
      STRUCT(2 AS campaign_id, 1 AS customer_id, 'TechCorp Product Launch' AS campaign_name, 'ACTIVE' AS status, DATE('2024-02-15') AS start_date, NULL AS end_date, 100000 AS budget),
      STRUCT(3 AS campaign_id, 2 AS customer_id, 'RetailInc Spring Sale' AS campaign_name, 'PAUSED' AS status, DATE('2024-03-01') AS start_date, NULL AS end_date, 75000 AS budget)
    ])
  ),
  AdGroups AS (
    SELECT * FROM UNNEST([
      STRUCT(101 AS ad_group_id, 1 AS campaign_id, 'Generic Keywords' AS name, 'ENABLED' AS status),
      STRUCT(102 AS ad_group_id, 1 AS campaign_id, 'Brand Keywords' AS name, 'ENABLED' AS status),
      STRUCT(201 AS ad_group_id, 2 AS campaign_id, 'New Product Features' AS name, 'ENABLED' AS status),
      STRUCT(202 AS ad_group_id, 2 AS campaign_id, 'Competitor Terms' AS name, 'PAUSED' AS status)
    ])
  ),
  Ads AS (
    SELECT * FROM UNNEST([
      STRUCT(1001 AS ad_id, 101 AS ad_group_id, 'TEXT' AS type, 'ENABLED' AS status),
      STRUCT(1002 AS ad_id, 101 AS ad_group_id, 'TEXT' AS type, 'ENABLED' AS status),
      STRUCT(1003 AS ad_id, 102 AS ad_group_id, 'TEXT' AS type, 'ENABLED' AS status),
      STRUCT(2001 AS ad_id, 201 AS ad_group_id, 'VIDEO' AS type, 'ENABLED' AS status)
    ])
  ),
  AdPerformance AS (
    SELECT * FROM UNNEST([
      STRUCT(1 AS performance_id, DATE('2024-05-15') AS date, 1001 AS ad_id, 1000 AS impressions, 50 AS clicks, 25.0 AS cost_usd),
      STRUCT(2 AS performance_id, DATE('2024-05-16') AS date, 1001 AS ad_id, 1200 AS impressions, 60 AS clicks, 30.0 AS cost_usd),
      STRUCT(3 AS performance_id, DATE('2024-04-15') AS date, 1001 AS ad_id, 900 AS impressions, 40 AS clicks, 20.0 AS cost_usd), -- Outside 30 days
      STRUCT(4 AS performance_id, DATE('2024-05-20') AS date, 1003 AS ad_id, 500 AS impressions, 10 AS clicks, 15.0 AS cost_usd),
      STRUCT(5 AS performance_id, DATE('2024-05-18') AS date, 2001 AS ad_id, 2000 AS impressions, 100 AS clicks, 80.0 AS cost_usd)
    ])
  ),
  Employees AS (
    SELECT * FROM UNNEST([
      STRUCT(10001 AS employee_id, 'managerone' AS ldap, 'Maya Jaideep' AS full_name),
      STRUCT(10002 AS employee_id, 'managertwo' AS ldap, 'Ben Carter' AS full_name)
    ])
  ),
  CustomerAssignments AS (
    SELECT * FROM UNNEST([
      STRUCT(1 AS customer_id, 10001 AS employee_id, 'AM' AS assignment_type), -- AM = Account Manager
      STRUCT(1 AS customer_id, 10002 AS employee_id, 'SPECIALIST' AS assignment_type),
      STRUCT(2 AS customer_id, 10002 AS employee_id, 'AM' AS assignment_type)
    ])
  ),
  GeoTargets AS ( -- Bonus 11th table
     SELECT * FROM UNNEST([
      STRUCT(1 AS geo_target_id, 1 AS campaign_id, 'US' AS country_code),
      STRUCT(2 AS geo_target_id, 2 AS campaign_id, 'US' AS country_code),
      STRUCT(3 AS geo_target_id, 2 AS campaign_id, 'CA' AS country_code) -- Not in Countries table, will not join
    ])
  )

