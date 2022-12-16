--1) users who has friend_id -NULL (users who haven't made any friends):
SELECT 
    id as users_with_no_friends 
FROM user 
WHERE id NOT IN 
    (SELECT 
        DISTINCT user_id 
    FROM friend);

--2) users who haven't posted any notes yet
SELECT 
    id AS users_with_no_notes
FROM user
WHERE id NOT IN 
    (SELECT 
        DISTINCT user_id
    FROM note);

--3) user who have not commented in any of the notes
SELECT 
    id 
FROM user 
WHERE id NOT IN 
    (SELECT    
        DISTINCT commenter_id
    FROM comment);  

--4) user who are most inactive (union of 1 & 2 & 3)
SELECT 
    id,
    COUNT(id)
FROM    
    (SELECT 
        id 
    FROM user
    WHERE id NOT IN
        (SELECT 
            DISTINCT user_id    
        FROM friend)      
    UNION ALL
    SELECT
        id
    FROM user
    WHERE id NOT IN
        (SELECT 
            DISTINCT user_id
        FROM note)
    UNION ALL
    SELECT 
        id 
    FROM user 
    WHERE id NOT IN 
        (SELECT    
            DISTINCT commenter_id
        FROM comment))
GROUP BY id;        
             
--5) no. of friends for each of the users
SELECT 
    id,
    COUNT(DISTINCT friend.friend_id)
FROM user
LEFT JOIN friend ON
    user.id = friend.user_id
GROUP BY id;            

--6) compare the count of notes published - friends vs public
SELECT visible_to, COUNT(visible_to) from note GROUP BY visible_to;

--7) no.of comments per notes for all users 
SELECT 
    user.id,
    note.id as note_id,
    COUNT(comment.commenter_id)
FROM user
INNER JOIN note ON
    user.id = note.user_id
LEFT JOIN comment ON
    note.id = comment.note_id
GROUP BY user.id
ORDER BY COUNT(comment.commenter_id);

--8) no. of notes per user
SELECT 
    user.id as user_id,
    COUNT(note.id) as total_notes
FROM user
LEFT JOIN note ON
    user.id = note.user_id
GROUP BY user.id; 

--9)no.of events per note
SELECT 
    note.id,
    COUNT(event.id)
FROM note
LEFT JOIN event ON
    note.id = event.note_id
GROUP BY note.id;

--10) Total no. of connections btwn users 
SELECT COUNT(*)/2 FROM friend;
