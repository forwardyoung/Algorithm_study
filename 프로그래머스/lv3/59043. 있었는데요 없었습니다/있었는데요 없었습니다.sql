-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME FROM ANIMAL_OUTS O, ANIMAL_INS I
WHERE O.ANIMAL_ID = I.ANIMAL_ID AND O.DATETIME < I.DATETIME 
ORDER BY I.DATETIME;