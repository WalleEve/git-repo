-- functions
CREATE OR REPLACE FUNCTION totalsal (f_empno NUMBER)
RETURN NUMBER
IS
v_sal NUMBER(10);
v_comm NUMBER(10);
v_total NUMBER(10);
BEGIN
SELECT sal,comm INTO v_sal,v_comm FROM emp WHERE empno=f_empno;
v_total :=NVL(v_sal,0)+NVL(v_comm,0);
RETURN v_total;
END;

