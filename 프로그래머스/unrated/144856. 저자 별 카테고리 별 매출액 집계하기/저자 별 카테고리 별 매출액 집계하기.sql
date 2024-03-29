SELECT BOOK.AUTHOR_ID, AUTHOR.AUTHOR_NAME, BOOK.CATEGORY, SUM(BOOK.PRICE * BOOK_SALES.SALES)TOTAL_SALES
FROM BOOK JOIN AUTHOR ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID 
          JOIN BOOK_SALES ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE YEAR(BOOK_SALES.SALES_DATE) = 2022 AND MONTH(BOOK_SALES.SALES_DATE) = 1
GROUP BY 1,3
ORDER BY BOOK.AUTHOR_ID, CATEGORY DESC