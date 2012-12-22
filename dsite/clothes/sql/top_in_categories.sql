SELECT R.*, S.name FROM (
  SELECT * FROM clothes_article ORDER BY cost DESC
) R, clothes_articletype S
WHERE R.article_type_id = S.id
GROUP BY article_type_id
ORDER BY cost DESC;