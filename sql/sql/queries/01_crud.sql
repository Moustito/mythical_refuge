-- a. All unicorns, ordered by power, strongest first.
SELECT name, power_level 
FROM creatures 
WHERE species = 'Unicorn' 
ORDER BY power_level DESC;

-- b. Creatures whose name starts with S.
SELECT name 
FROM creatures 
WHERE name LIKE 'S%';

-- c. Insert the dragon Cinder and get its id back.
INSERT INTO creatures (name, species, origin, power_level, element) 
VALUES ('Cinder', 'Dragon', 'Ashlands', 60, 'fire') 
RETURNING id;

-- d. Ember resurrects: increment resurrection_count and return the new value.
UPDATE creatures 
SET resurrection_count = resurrection_count + 1 
WHERE name = 'Ember' 
RETURNING resurrection_count;

-- e. Health records of the last 30 days, as of DATE '2026-03-15'.
SELECT * 
FROM health_records 
WHERE examined_on >= DATE '2026-03-15' - INTERVAL '30 days' 
  AND examined_on <= DATE '2026-03-15';

-- f. Ongoing missions with their due date computed in SQL.
SELECT c.name, m.departure_date, m.duration_days, (m.departure_date + m.duration_days) AS due_date 
FROM missions m 
JOIN creatures c ON m.creature_id = c.id 
WHERE m.returned_on IS NULL;

-- g. Every creature with its element, or 'none' if it has no element.
SELECT name, COALESCE(element, 'none') AS element 
FROM creatures;

-- h. Delete Cinder, then attempt to delete Frostbite (should fail due to foreign key constraints).
DELETE FROM creatures WHERE name = 'Cinder';
DELETE FROM creatures WHERE name = 'Frostbite';