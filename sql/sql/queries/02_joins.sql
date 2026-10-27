-- 1. Mission log. For each mission: departure date, creature name, species, handler name and destination, ordered by departure date.
SELECT 
    departure_date, 
    creatures.name AS creature_name, 
    species, 
    full_name AS handler_name, 
    destinations.name AS destination
FROM missions
JOIN creatures ON creatures.id = missions.creature_id
JOIN employees ON employees.id = missions.handler_id
JOIN destinations ON destinations.id = missions.destination_id
ORDER BY departure_date;

-- 2. Ongoing missions. Creature, destination, due date and an overdue boolean as of 2026-03-15.
SELECT 
    c.name AS creature,
    d.name AS destination,
    (m.departure_date + m.duration_days) AS due_date,
    (m.departure_date + m.duration_days) < '2026-03-15'::date AS is_overdue
FROM missions m
JOIN creatures c ON c.id = m.creature_id
JOIN destinations d ON d.id = m.destination_id
WHERE m.returned_on IS NULL
ORDER BY due_date;

-- Housing. Every creature with the name of its enclosure, or unassigned when it has none.
SELECT 
    c.name, 
    COALESCE(e.name, 'unassigned') AS enclosure_name
FROM creatures c
LEFT JOIN enclosures e ON e.id = c.enclosure_id

-- Anti-joins (LEFT JOIN + IS NULL):
-- creatures that were never sent on a mission;
SELECT c.name AS unassigned_creature
FROM creatures c
LEFT JOIN missions m ON m.creature_id = c.id
WHERE m.id IS NULL;

-- destinations that were never visited;
SELECT d.name AS never_visited
FROM destinations d
LEFT JOIN missions m ON m.destination_id = d.id
WHERE m.id IS NULL;

-- handlers who never escorted anyone.
SELECT e.full_name AS never_escorted
FROM employees e
LEFT JOIN missions m ON m.handler_id = e.id
WHERE e.role = 'handler' AND m.id IS NULL;

-- Self-join. Every employee with the name of their supervisor, or - when they have none.
SELECT 
    e.full_name AS employee,
    COALESCE(s.full_name, '-') AS supervisor
FROM employees e
LEFT JOIN employees s ON s.id = e.supervisor_id;

-- The NULL trap. List all creatures together with their missions departed since 2026-02-01, keeping the creatures that have none.
-- First write the naive version, with the date filter in WHERE.
-- Explain why it loses rows.
-- Then fix it.
SELECT 
    c.name,
    m.departure_date
FROM creatures c
LEFT JOIN missions m ON m.creature_id = c.id AND m.departure_date > '2026-02-01'

-- Health alerts. Creatures that have at least one record with status quarantine or in_treatment, with the status and the examination date.
SELECT 
    c.name,
    hr.status,
    hr.examined_on
FROM creatures c
JOIN health_records hr ON hr.creature_id = c.id
WHERE hr.status = 'quarantine' or hr.status = 'in_treatment'