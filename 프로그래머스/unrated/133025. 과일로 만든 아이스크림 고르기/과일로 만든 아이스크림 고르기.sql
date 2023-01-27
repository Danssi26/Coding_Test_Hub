-- 코드를 입력하세요
SELECT ice.FLAVOR 
FROM ICECREAM_INFO ice JOIN FIRST_HALF fir ON 
    ice.flavor = fir.flavor
WHERE TOTAL_ORDER > 3000 AND INGREDIENT_TYPE = 'fruit_based'
