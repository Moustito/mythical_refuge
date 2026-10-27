-- Occupancy. For every enclosure, including empty ones: name, capacity, number of occupants and free slots.
SELECT 
    e.name AS enclosure_name,
    e.capacity,
    COUNT(c.id) AS occupants,
    e.capacity - COUNT(c.id) AS free_slots
FROM enclosures e
LEFT JOIN creatures c ON c.enclosure_id = e.id
GROUP BY e.id, e.name, e.capacity;

-- Full enclosures. The same query, keeping only full enclosures (HAVING).
SELECT 
    e.name AS enclosure_name
FROM enclosures e
LEFT JOIN creatures c ON c.enclosure_id = e.id
GROUP BY e.id, e.name, e.capacity
HAVING e.capacity - COUNT(c.id) = 0;

-- Species. For each species: number of creatures and average power rounded to one decimal.
SELECT 
    c.species,
    COUNT(*) AS creature_count,
    ROUND(AVG(power_level)::numeric, 1) AS average_power
FROM creatures c
GROUP BY species

-- Workload. Number of missions per handler, including handlers with none.
SELECT 
    e.full_name,
    COUNT(m.handler_id) AS nbr_missions
FROM employees e
LEFT JOIN missions m ON m.handler_id = e.id
WHERE e.role = 'handler'
GROUP BY e.full_name

-- Workload 2.0. Then keep only handlers with at least 3 missions.
SELECT 
    e.full_name AS handler_name,
    COUNT(m.id) AS mission_count
FROM employees e
LEFT JOIN missions m ON m.handler_id = e.id
GROUP BY e.id, e.full_name
<<<<<<< HEAD
HAVING COUNT(m.id) >= 3;

-- Earnings. Reward earned per creature on completed missions (base reward × danger multiplier), highest first.
SELECT 
    c.name AS creature_name,
    (m.base_reward * d.danger_multiplier)::INTEGER AS earned_reward
FROM missions m
JOIN creatures c ON c.id = m.creature_id
JOIN destinations d ON d.id = m.destination_id
WHERE m.returned_on IS NOT NULL
ORDER BY earned_reward DESC;
=======
HAVING COUNT(m.id) >= 3;
>>>>>>> 73584b32e5547621d9d3f2683e4e61b91899df83
