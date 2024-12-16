use prueba;

SELECT * FROM  users___users
-- sentencia para query 1
SELECT 
    u.id AS user_id, 
    u.name, 
    u.email, 
    SUM(p.views) AS total_views
FROM 
    users___users u
JOIN 
    profiles___hoja_1 p
ON 
    u.id = p.user_id
GROUP BY 
    u.id, u.name, u.email
ORDER BY 
    total_views DESC
LIMIT 3;

-- sentencia para query 2

SELECT 
    u.id, 
    u.video,
    p.onboarding_goal,
    u.updated_at,
    u.created_at,
    r.name
FROM 
    users___users u
JOIN 
    profiles___hoja_1 p ON u.id = p.user_id
JOIN
	resumes___resumes r ON u.id = r.user_id
WHERE
	(p.onboarding_goal = 'be_discovered-[hire]' OR p.onboarding_goal = 'be_discovered-[collaborate]')
	AND r.type = 'pitch_video'
	AND u.video <> 'NULL'
	AND r.video <> ''
	AND r.created_at >= NOW() - INTERVAL 7 MONTH
GROUP BY
	u.id, u.video, p.onboarding_goal, u.updated_at, u.created_at, r.name;
    
-- sentecia para query 3

SELECT * FROM `challenges___challenges` WHERE status = 'published'
AND created_at >= curdate() - INTERVAL 3 month
ORDER BY created_at DESC



    

