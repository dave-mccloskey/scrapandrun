SELECT R.*, S.name
FROM clothes_article R, clothes_articletype S
WHERE R.article_type_id = S.id
ORDER BY cost DESC
LIMIT 10;