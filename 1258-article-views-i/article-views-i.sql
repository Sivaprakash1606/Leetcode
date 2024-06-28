SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id =viewer_id
ORDER BY author_id ASC;

-- SELECT DISTINCT v.author_id AS id
-- FROM Views AS v
-- WHERE v.author_id = v.viewer_id
-- ORDER BY v.author_id ASC;
