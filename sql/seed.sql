INSERT INTO enclosures (name, capacity) VALUES
    ('Ember Caves', 3), ('Crystal Glade', 4), ('Sky Nest', 2), ('Frozen Hall', 2);

INSERT INTO creatures (name, species, origin, power_level, element, resurrection_count, in_refuge, enclosure_id) VALUES
    ('Frostbite', 'Dragon',   'Nordic Realms',   95, 'ice',  0, FALSE, 1),
    ('Ignis',     'Dragon',   'Volcanic Depths', 88, 'fire', 0, TRUE,  1),
    ('Ember',     'Phoenix',  'Ashlands',        72, NULL,   2, FALSE, 3),
    ('Stardust',  'Unicorn',  'Silver Woods',    45, NULL,   0, TRUE,  2),
    ('Moonbeam',  'Unicorn',  'Crystal Lake',    67, NULL,   0, TRUE,  2),
    ('Talon',     'Griffin',  'Eagle Peaks',     80, NULL,   0, TRUE,  3),
    ('Sylph',     'Phoenix',  'Cloud Isles',     58, NULL,   0, TRUE,  NULL),
    ('Gorgo',     'Basilisk', 'Serpent Marsh',   91, NULL,   0, TRUE,  1),
    ('Willow',    'Unicorn',  'Moon Meadows',    42, NULL,   0, FALSE, 2);

INSERT INTO employees (full_name, email, role, certification_level, supervisor_id, hired_on) VALUES
    ('Aldric Stone',  'aldric@refuge.example', 'handler',      5,    NULL, '2019-04-01'),
    ('Brynn Ashford', 'brynn@refuge.example',  'handler',      3,    1,    '2022-09-15'),
    ('Cael Morrow',   'cael@refuge.example',   'handler',      2,    1,    '2025-11-03'),
    ('Dara Quill',    'dara@refuge.example',   'veterinarian', NULL, NULL, '2018-02-12'),
    ('Elio Fenn',     'elio@refuge.example',   'veterinarian', NULL, 4,    '2023-06-20'),
    ('Faye Lumen',    'faye@refuge.example',   'handler',      4,    1,    '2021-01-10');

INSERT INTO destinations (name, danger_multiplier) VALUES
    ('Northern Pass', 1.0), ('Frozen Peaks', 2.0), ('Shadow Forest', 3.0), ('Sunlit Valley', 1.0);

INSERT INTO missions (creature_id, handler_id, destination_id, departure_date, duration_days, base_reward, returned_on, notes) VALUES
    (1, 1, 2, '2026-01-05', 14, 500.00, '2026-01-19', ''),
    (3, 6, 1, '2026-01-10',  7, 200.00, '2026-01-17', ''),
    (5, 6, 1, '2026-01-20',  3, 120.00, '2026-01-23', ''),
    (2, 1, 3, '2026-02-01', 14, 600.00, '2026-02-17', 'Delayed by a storm'),
    (6, 6, 2, '2026-02-10', 10, 300.00, '2026-02-20', ''),
    (4, 2, 1, '2026-02-15',  3,  80.00, '2026-02-18', ''),
    (1, 1, 3, '2026-03-01', 14, 700.00, NULL, ''),
    (3, 6, 2, '2026-03-02',  7, 250.00, NULL, ''),
    (9, 2, 1, '2026-03-12',  3,  60.00, NULL, '');

INSERT INTO health_records (creature_id, vet_id, examined_on, status, diagnosis, treatment) VALUES
    (1, 4, '2026-01-02', 'healthy',           'Routine check',            ''),
    (2, 5, '2026-01-25', 'healthy',           'Routine check',            ''),
    (3, 4, '2026-01-08', 'healthy',           'Routine check',            ''),
    (4, 5, '2026-02-20', 'under_observation', 'Limping after mission',    'Rest'),
    (4, 5, '2026-03-05', 'healthy',           'Fully recovered',          ''),
    (8, 4, '2026-02-28', 'quarantine',        'Unstable petrifying gaze', 'Isolation'),
    (5, 5, '2026-03-10', 'in_treatment',      'Horn fracture',            'Splint and rest'),
    (6, 4, '2026-02-22', 'healthy',           'Routine check',            ''),
    (9, 5, '2026-03-10', 'healthy',           'Routine check',            '');