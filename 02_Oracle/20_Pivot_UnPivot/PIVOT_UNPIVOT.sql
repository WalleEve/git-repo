--# UNPIVOT (columns to row)
with table1
as
(
select 'Audit Fee' hour3, '10% Liq. Damages' hour0, '20% Liq Damages' hour1, 'Intest' hour2
from dual
)
select *
  from table1 t1
unpivot (value for hour in (hour0 as '0',hour1 as '1',hour2 as '2', hour3 as '3'));
/


--# Rows to column 
--# Using DECODE
CREATE TABLE doc_tab (
  loan_number VARCHAR2(20),
  document_type VARCHAR2(20),
  document_id VARCHAR2(20)
);
/
INSERT INTO doc_tab VALUES('992452533663', 'Voters ID', 'XPD0355636');
INSERT INTO doc_tab VALUES('992452533663', 'Pan card', 'CHXPS5522D');
INSERT INTO doc_tab VALUES('992452533663', 'Drivers licence', 'DL-0420110141769');

COMMIT;

SELECT
    loan_number,
    MAX(DECODE(document_type, 'Voters ID', document_id)) AS voters_id,
    MAX(DECODE(document_type, 'Pan card', document_id)) AS pan_card,
    MAX(DECODE(document_type, 'Drivers licence', document_id)) AS drivers_licence
  FROM
    doc_tab
GROUP BY loan_number
ORDER BY loan_number;

--# USING PIVOT 
SELECT *
  FROM doc_tab
PIVOT (
  MAX(document_id) FOR document_type IN ('Voters ID','Pan card','Drivers licence')
);