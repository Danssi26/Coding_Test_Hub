SELECT DATE_FORMAT(sale.SALES_DATE, '%Y') YEAR,
       DATE_FORMAT(sale.SALES_DATE, '%m') MONTH,
       COUNT(DISTINCT sale.USER_ID) PUCHASED_USERS, -- 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수
       ROUND(COUNT(DISTINCT sale.USER_ID)  / (SELECT COUNT(USER_ID)
                                     FROM USER_INFO
                                     WHERE YEAR(JOINED) = '2021'), 1) PUCHASED_RATIO -- 상품 구매한 회원의 비율
             
FROM USER_INFO user JOIN ONLINE_SALE sale 
     ON user.USER_ID = sale.USER_ID
WHERE YEAR(JOINED) = '2021'
GROUP BY YEAR, MONTH