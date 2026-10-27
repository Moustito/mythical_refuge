# 🐉 Mythical Creature Refuge — Running Exercise

> Guided integration project for the OOP and SQL modules (Python + PostgreSQL).
> The refuge is a **learning playground**: it exists to practise every topic of the course in a realistic, connected context.
> Your **final project** will be built on **your own domain**. Use the refuge as a reference you can look back at, not as a template to copy.

---

## Table of contents

1. [How to use this document](#how-to-use-this-document)
2. [Roadmap](#roadmap)
3. [Final project hierarchy](#final-project-hierarchy)
4. [The refuge at a glance (domain reference)](#the-refuge-at-a-glance-domain-reference)
5. [Chapter 1 — Classes, objects & encapsulation](#chapter-1--classes-objects--encapsulation)
6. [Chapter 2 — Inheritance & polymorphism](#chapter-2--inheritance--polymorphism)
7. [Chapter 3 — Relational databases](#chapter-3--relational-databases)
8. [Chapter 4 — SQL: JOINs & aggregates](#chapter-4--sql-joins--aggregates)
9. [Chapter 5 — Composition, special methods, interfaces & database connection](#chapter-5--composition-special-methods-interfaces--database-connection)
10. [Chapter 6 — SOLID principles & clean code](#chapter-6--solid-principles--clean-code)
11. [Chapter 7 — Testing & project structure](#chapter-7--testing--project-structure)
12. [Pack A — Advanced SQL (after the final project)](#pack-a--advanced-sql-after-the-final-project)
13. [Bonus exercises](#bonus-exercises)
14. [Appendix A — Fast-track brief (experienced developers)](#appendix-a--fast-track-brief-experienced-developers)
15. [Appendix B — Mirror milestones for your own project](#appendix-b--mirror-milestones-for-your-own-project)

---

## How to use this document

### Structure of an exercise

Every exercise follows the same layout:

| Block         | Content                                                                                                                                    |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **Context**   | Why the refuge needs this feature.                                                                                                         |
| **Tasks**     | What to build. Names, signatures and messages are imposed so that everyone gets the same outputs.                                          |
| **Verify**    | A snippet to run and its expected output. Your output must match.                                                                          |
| **Questions** | Short design questions. Answer them in `docs/design_notes.md`, one section per exercise. These answers are your **interview preparation**. |
| **Files**     | The files created or modified, matching the final hierarchy.                                                                               |

Some exercises also contain a **🧩 Pattern spotlight** (a design pattern discovered in context) or a **🧮 Algorithm corner** (an algorithm applied to the domain, with its complexity).

### Conventions

- **Python 3.11+**, **PostgreSQL 14+** (16 recommended), `psycopg2-binary`, `python-dotenv`, `mypy`, `ruff`, `black`.
- **Flat layout until 7.1.** During chapters 1 to 6, the package `refuge/` sits at the project root and every folder contains an `__init__.py`. You run scripts from the project root with `python -m playground.ex_2_1`. In 7.1 you migrate to the `src/` layout.
- **Playground.** Every *Verify* snippet goes into `playground/ex_<chapter>_<number>.py` (with an empty `playground/__init__.py`). In 7.2 these snippets become unit tests.
- **Reference date.** Whenever an expected output depends on "today", **today is 2026-03-15**. In SQL, write `DATE '2026-03-15'` instead of `CURRENT_DATE`. In Python, inject the date (you will see why in chapter 7).
- **Type hints** on every public function and method from chapter 2 onward, and a one-line **docstring** minimum on every public class and method.
- **No `isinstance` to branch on a type.** Polymorphism does that job. `isinstance` remains acceptable inside `__eq__` and to validate primitive values (`int`, `str`...).
- **Git.** Commit at the end of every exercise with a clear message (`ex 2.3: LSP & duck typing`).

---

## Roadmap


| Chapter                                                     | Exercises          | Design patterns                                      | Algorithms             |
|-------------------------------------------------------------|--------------------|------------------------------------------------------|------------------------|
| 1. Classes, objects & encapsulation                         | 1.1 – 1.3          | —                                                    | —                      |
| 2. Inheritance & polymorphism                               | 2.1 – 2.4          | Template Method (preview)                            | —                      |
| 3. Relational databases                                     | 3.1 – 3.2          | —                                                    | —                      |
| 4. SQL: JOINs & aggregates                                  | 4.1 – 4.2          | —                                                    | —                      |
| 5. Composition, special methods, interfaces & DB connection | 5.1 – 5.7          | Repository, Factory, Adapter, Singleton (discussion) | Interval overlap       |
| 6. SOLID & clean code                                       | 6.1 – 6.5          | Observer, Strategy                                   | Bin-packing heuristics |
| 7. Testing & project structure                              | 7.1 – 7.4          | Facade, Decorator                                    | —                      |
| *After the final project*                                   | Pack A (A.1 – A.5) | —                                                    | —                      |
| *Any time*                                                  | Bonus B.1 – B.5    | Command                                              | Sweep line, knapsack   |

---

## Final project hierarchy

This is the expected state of the repository **at the end of chapter 7**. The exercise that creates or modifies each file is noted on the right.

```
mythical_refuge/
├── README.md                                  # 7.1  install, run, test, structure
├── pyproject.toml                             # 7.1  metadata, dependencies, tools
├── .env.example                               # 5.3  template of the DB settings (committed)
├── .env                                       # 5.3  real settings (NEVER committed)
├── .gitignore                                 # 5.3
│
├── sql/
│   ├── schema.sql                             # 3.1  tables & constraints (re-runnable)
│   ├── seed.sql                               # 3.2  reference dataset
│   ├── migrations/
│   │   └── 001_kraken_and_volcanic_rift.sql   # 6.5  extension test
│   └── queries/
│       ├── 01_crud.sql                        # 3.2
│       ├── 02_joins.sql                       # 4.1
│       ├── 03_aggregates.sql                  # 4.2
│       └── 04_advanced.sql                    # Pack A (optional)
│
├── docs/
│   ├── er_diagram.puml                        # 3.1  ER diagram (PlantUML or any tool)
│   ├── design_notes.md                        # all chapters: answers to the Questions
│   └── architecture.md                        # 7.1  layers, patterns, SOLID summary
│
├── src/
│   └── refuge/
│       ├── __init__.py
│       ├── __main__.py                        # 7.1  `python -m refuge`
│       ├── cli.py                             # 7.1  argparse entry point (presentation layer)
│       ├── bootstrap.py                       # 7.1  composition root: the only place that wires concrete classes
│       ├── config.py                          # 5.3  reads .env
│       ├── exceptions.py                      # 1.3 → 2.1 → 5.1 → 5.4 → 5.5 → 6.3
│       │
│       ├── models/                            # pure domain objects, no I/O
│       │   ├── __init__.py
│       │   ├── creature.py                    # 1.1 – 1.3, 2.1, 2.2, 5.4
│       │   ├── species.py                     # 2.1, 2.2, 5.4, 6.5
│       │   ├── mixins.py                      # 2.2
│       │   ├── employee.py                    # 2.4, 5.2, 5.4
│       │   ├── enclosure.py                   # 5.1
│       │   ├── mission.py                     # 5.2
│       │   └── health_record.py               # 5.2
│       │
│       ├── algorithms/
│       │   ├── __init__.py
│       │   └── intervals.py                   # 5.7  overlap detection
│       │
│       ├── db/
│       │   ├── __init__.py
│       │   └── connection.py                  # 5.3  DatabaseConnection (context manager + transaction)
│       │
│       ├── repositories/                      # data access layer: all SQL lives here
│       │   ├── __init__.py
│       │   ├── protocols.py                   # 5.4, 5.6, 5.7, 6.4
│       │   ├── factories.py                   # 5.4, 6.5
│       │   ├── in_memory.py                   # 5.4, 5.6
│       │   └── postgres.py                    # 5.4, 5.6
│       │
│       ├── notifiers/
│       │   ├── __init__.py
│       │   ├── protocol.py                    # 5.5
│       │   ├── console.py                     # 5.5
│       │   ├── file.py                        # 5.5
│       │   ├── silent.py                      # 5.5
│       │   └── raven.py                       # 5.5  third-party client + adapter
│       │
│       ├── services/                          # business layer
│       │   ├── __init__.py
│       │   ├── mission_service.py             # 5.7, 6.2, 7.1
│       │   ├── events.py                      # 6.2  EventBus + events
│       │   ├── listeners.py                   # 6.2
│       │   ├── placement.py                   # 6.3
│       │   ├── reports.py                     # 6.4, 6.5
│       │   └── refuge_app.py                  # 7.1  Facade
│       │
│       └── utils/
│           ├── __init__.py
│           ├── logging_config.py              # 7.1
│           └── decorators.py                  # 7.1
│
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_creature.py                   # 7.2
│   │   ├── test_species.py                    # 7.2
│   │   ├── test_employee.py                   # 7.2
│   │   ├── test_enclosure.py                  # 7.2
│   │   ├── test_mission.py                    # 7.2
│   │   ├── test_health_record.py              # 7.2
│   │   ├── test_intervals.py                  # 7.2
│   │   ├── test_placement.py                  # 7.2
│   │   ├── test_mission_service.py            # 7.3
│   │   ├── test_listeners.py                  # 7.3
│   │   └── test_connection.py                 # 7.3  (mocked psycopg2)
│   └── integration/
│       ├── test_postgres_repositories.py      # 7.4
│       └── test_mission_flow.py               # 7.4
│
├── playground/                                # verification scripts of chapters 1–6 (can be removed after 7.2)
│   └── legacy_refuge_manager.py               # 6.1  provided legacy code
│
└── bonus/                                     # optional exercises, outside the core path
```

---

## The refuge at a glance (domain reference)

Keep this page open: every exercise relies on these rules.

### Species

| Species  | Class created in | Mission duration | Flies (2.2) | Specific rule                                         |
|----------|------------------|------------------|-------------|-------------------------------------------------------|
| Dragon   | 2.1              | 14 days          | yes         | Has an `element` (`"fire"`, `"ice"`...)               |
| Phoenix  | 2.1              | 7 days           | yes         | Has a `resurrection_count` and a `resurrect()` method |
| Unicorn  | 2.1              | 3 days           | no          | Refuses missions when `power_level < 40`              |
| Griffin  | 2.1              | 10 days          | yes         | —                                                     |
| Basilisk | 2.1              | 5 days           | no          | —                                                     |
| Kraken   | 6.5              | 21 days          | no          | Added later to test extensibility                     |

### Business rules

| Topic                | Rule                                                                                                                                                                                      |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Power                | `power_level` is an `int` between 0 and 100.                                                                                                                                              |
| Origin               | Set at registration, never modified.                                                                                                                                                      |
| Escort               | Every mission has a handler. A handler with `certification_level` *L* (1–5) can escort a creature if `L × 20 ≥ power_level`. Veterinarians never escort.                                  |
| Health               | Statuses: `healthy`, `under_observation` (missions allowed), `in_treatment`, `quarantine` (missions blocked). Only the **latest** record counts. A creature without any record may leave. |
| Enclosures           | An enclosure has a capacity. Incompatible species cannot share an enclosure: Dragon–Unicorn, Basilisk–Phoenix, Basilisk–Unicorn.                                                          |
| Missions             | Due date = departure date + duration. Reward = base reward × danger multiplier of the destination. A creature cannot depart twice on the same day.                                        |
| Handler availability | A handler cannot escort two missions whose periods `[departure, due date)` overlap.                                                                                                       |

### Main characters (reference dataset, chapter 3)

| Creatures                                                                                                                                                                                                        | Staff                                                                                                                      | Destinations (danger ×)                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Frostbite (Dragon, ice, 95), Ignis (Dragon, fire, 88), Ember (Phoenix, 72), Sylph (Phoenix, 58), Stardust (Unicorn, 45), Moonbeam (Unicorn, 67), Willow (Unicorn, 42), Talon (Griffin, 80), Gorgo (Basilisk, 91) | Handlers: Aldric Stone (level 5), Faye Lumen (4), Brynn Ashford (3), Cael Morrow (2). Veterinarians: Dara Quill, Elio Fenn | Northern Pass (×1.0), Frozen Peaks (×2.0), Shadow Forest (×3.0), Sunlit Valley (×1.0) |

---

## Chapter 1 — Classes, objects & encapsulation

### Exercise 1.1 — The `Creature` class

**Context.** The refuge shelters mythical creatures and sends some of them on missions. You start by building the object at the heart of everything: the creature.

**Tasks.** In `refuge/models/creature.py`, create a `Creature` class with:

1. A **class attribute** `_total_creatures = 0` that counts every creature registered since the program started.
2. An `__init__(self, name, species, origin, power_level)` that stores the four values as instance attributes, sets `_in_refuge` to `True`, and increments `_total_creatures`.
3. `send_on_mission()`, which sets `_in_refuge` to `False`, and `return_to_refuge()`, which sets it back to `True`.
4. A `__str__` returning `Frostbite the Dragon (origin: Nordic Realms) [in refuge]`, or `[on mission]` when the creature is away.

**Verify.**

```python
from refuge.models.creature import Creature

frostbite = Creature("Frostbite", "Dragon", "Nordic Realms", 95)
ember = Creature("Ember", "Phoenix", "Ashlands", 72)

print(frostbite)
frostbite.send_on_mission()
print(frostbite)
frostbite.return_to_refuge()
print(Creature._total_creatures)
```

```
Frostbite the Dragon (origin: Nordic Realms) [in refuge]
Frostbite the Dragon (origin: Nordic Realms) [on mission]
2
```

**Questions.**
1. Replace the increment with `self._total_creatures += 1`. What do you observe? Explain the *shadowing trap*.
2. Why is `_in_refuge` an instance attribute and `_total_creatures` a class attribute?

**Files.** `refuge/models/creature.py`, `playground/ex_1_1.py`

---

### Exercise 1.2 — Class methods and static methods

**Context.** Creature data now reaches the refuge from two sources: rows coming from a database (dictionaries) and old scrolls (comma-separated strings). The keepers also want to reject unknown species.

**Tasks.**

1. Add a class constant `VALID_SPECIES = ("Dragon", "Phoenix", "Unicorn", "Griffin", "Basilisk")`.
2. Add a **static method** `is_valid_species(species: str) -> bool`.
3. `__init__` raises `ValueError(f"Unknown species: {species!r}.")` when the species is invalid.
4. Add the **class method** `from_dict(data)`. The keys are `name`, `species`, `origin` and `power_level`: these are exactly the column names you will use in the database (chapter 3). Extra keys are ignored.
5. Add the **class method** `from_string(text)`, which parses `"Frostbite, Dragon, Nordic Realms, 95"`.
   - It strips the spaces around each field and converts `power_level` to `int`.
   - It raises `ValueError` if the text does not contain exactly 4 fields.
6. Add the **class method** `get_total_creatures() -> int`.

**Verify.**

```python
row = {"id": 1, "name": "Frostbite", "species": "Dragon", "origin": "Nordic Realms", "power_level": 95}
frostbite = Creature.from_dict(row)
ember = Creature.from_string("Ember, Phoenix, Ashlands, 72")

print(frostbite)
print(ember.power_level + 1)
print(Creature.is_valid_species("Griffin"), Creature.is_valid_species("Goblin"))
print(Creature.get_total_creatures())

try:
    Creature.from_string("Grub, Goblin, Dark Caves, 12")
except ValueError as error:
    print(error)
```

```
Frostbite the Dragon (origin: Nordic Realms) [in refuge]
73
True False
2
Unknown species: 'Goblin'.
```

**Questions.**
1. Why must an alternative constructor call `cls(...)` rather than `Creature(...)`? (Keep the answer in mind for 2.1.)
2. Why is `is_valid_species` a static method and not a class method?

**Files.** `refuge/models/creature.py`, `playground/ex_1_2.py`

---

### Exercise 1.3 — Encapsulation

**Context.** Two incidents were reported:
- a creature was registered with a power level of −3;
- the origin of another one was overwritten by mistake, although origins are permanent.

**Tasks.**

1. Create `refuge/exceptions.py` with two classes:
   - `RefugeError(Exception)`, the base of every business error;
   - `ValidationError(RefugeError)`.

   From now on, invalid values raise `ValidationError`. This replaces the `ValueError` of 1.2, including in `from_string`.
2. Make `power_level` **protected** (`_power_level`) and expose it through a `@property` with a **setter**:
   - The value must be an `int`. `bool` is rejected (explain why in the questions). Message: `power_level must be an int, got str.`
   - It must lie between 0 and 100. Message: `power_level must be between 0 and 100, got 150.`
   - `__init__` assigns `self.power_level = power_level`, so validation also applies at creation.
3. Make `origin` **private** (`__origin`) and expose it through a **read-only** property, with no setter.
4. Expose `in_refuge` as a **read-only** property. The state may only change through `send_on_mission()` and `return_to_refuge()`.
5. Add `__repr__`, returning `Creature(name='Frostbite', species='Dragon', origin='Nordic Realms', power_level=95)`. Use `!r` in the f-string.

**Verify.**

```python
from refuge.exceptions import ValidationError

frostbite = Creature("Frostbite", "Dragon", "Nordic Realms", 95)
print(repr(frostbite))

frostbite.power_level = 80
print(frostbite.power_level)

for bad_value in (150, -3, "95", True):
    try:
        frostbite.power_level = bad_value
    except ValidationError as error:
        print(error)

try:
    frostbite.origin = "Elsewhere"
except AttributeError:
    print("origin is read-only")

print(frostbite._Creature__origin)
print(frostbite.in_refuge)
```

```
Creature(name='Frostbite', species='Dragon', origin='Nordic Realms', power_level=95)
80
power_level must be between 0 and 100, got 150.
power_level must be between 0 and 100, got -3.
power_level must be an int, got str.
power_level must be an int, got bool.
origin is read-only
Nordic Realms
True
```

**Questions.**
1. Why is `True` rejected even though `isinstance(True, int)` is `True`?
2. What does the second-to-last line tell you about name mangling? Is `__origin` really private?
3. In the setter, why must you write to `self._power_level` and not to `self.power_level`?
4. In chapter 3 the database will also check `power_level`. Is that duplication useless? (Keep a short answer and come back to it in 3.1.)

**Files.** `refuge/models/creature.py`, `refuge/exceptions.py`, `playground/ex_1_3.py`

---

## Chapter 2 — Inheritance & polymorphism

### Exercise 2.1 — Abstract base class and species

**Context.** Each species now has its own rules. A plain "creature" no longer makes sense: every resident belongs to a concrete species.

**Tasks.**

1. Turn `Creature` into an **abstract base class** (`abc.ABC`) with two abstract methods:
   - `mission_duration_days() -> int`;
   - `special_ability() -> str`.
2. Add `MissionRefusedError(RefugeError)` to `exceptions.py`.
3. Turn `send_on_mission()` into a **template method**. It stays concrete in `Creature` and its docstring states the contract: *"Raises MissionRefusedError when the creature cannot leave."*
   - If the creature is already away, it raises `MissionRefusedError(f"{name} is already on a mission.")`.
   - Otherwise, it calls the **hook** `refusal_reason() -> str | None`. The default implementation returns `None`. If the hook returns a message, `send_on_mission()` raises `MissionRefusedError(message)`.
   - Otherwise, the creature leaves.
4. In `refuge/models/species.py`, create the five subclasses. Their constructors no longer take `species`: each subclass passes its own name to `super().__init__()`. Each one also accepts `**kwargs` and forwards it to `super().__init__()` (you will see why in 2.2 and 5.4).

| Class | Constructor | `mission_duration_days()` | `special_ability()` | Extra |
|---|---|---|---|---|
| `Dragon` | `(name, origin, power_level, element, **kwargs)` | 14 | `"{name} breathes {element} and flies at great speed."` | `__str__` **extends** the parent's with `" - element: {element}"`. `__repr__` returns `Dragon(name='Frostbite', origin='Nordic Realms', power_level=95, element='ice')` |
| `Phoenix` | `(name, origin, power_level, resurrection_count=0, **kwargs)` | 7 | `"{name} radiates a flame aura and rises again from its ashes."` | `resurrect()` increments the counter and returns `"🔥 Ember rises from its ashes! (resurrections: 1)"` |
| `Unicorn` | `(name, origin, power_level, **kwargs)` | 3 | `"{name} heals its allies and gallops faster than the wind."` | Class constant `MIN_MISSION_POWER = 40`. `refusal_reason()` returns `"{name} is too weak for a mission (power 25 < 40)."` below the threshold |
| `Griffin` | `(name, origin, power_level, **kwargs)` | 10 | `"{name} dives from the clouds with razor-sharp talons."` | — |
| `Basilisk` | `(name, origin, power_level, **kwargs)` | 5 | `"{name} petrifies its enemies with a single gaze."` | — |

5. In the playground, write `send_to_field(creature: Creature) -> None`. It prints the ability, then tries to send the creature and prints either `  → away for N days` or `  ❌ refused: <reason>`. Do not check the type anywhere.

**Verify.**

```python
from refuge.models.creature import Creature
from refuge.models.species import Dragon, Phoenix, Unicorn, Griffin

residents = [
    Dragon("Frostbite", "Nordic Realms", 95, "ice"),
    Phoenix("Ember", "Ashlands", 72),
    Unicorn("Pebble", "Misty Hills", 25),
    Griffin("Talon", "Eagle Peaks", 80),
]
for resident in residents:
    send_to_field(resident)

print(residents[0])
print(repr(residents[0]))
print(residents[1].resurrect())

try:
    Creature("Nobody", "Dragon", "Nowhere", 10)
except TypeError:
    print("Creature is abstract")
```

```
Frostbite breathes ice and flies at great speed.
  → away for 14 days
Ember radiates a flame aura and rises again from its ashes.
  → away for 7 days
Pebble heals its allies and gallops faster than the wind.
  ❌ refused: Pebble is too weak for a mission (power 25 < 40).
Talon dives from the clouds with razor-sharp talons.
  → away for 10 days
Frostbite the Dragon (origin: Nordic Realms) [on mission] - element: ice
Dragon(name='Frostbite', origin='Nordic Realms', power_level=95, element='ice')
🔥 Ember rises from its ashes! (resurrections: 1)
Creature is abstract
```

**Questions.**
1. Overriding `send_on_mission()` in `Unicorn` to raise an exception would violate the Liskov Substitution Principle. Why is the `refusal_reason()` hook acceptable?
2. Call `Creature.from_dict(row)`, then `Dragon.from_dict(row)`. What happens in each case, and why? Write it down: you will fix it in 5.4.
3. For `Dragon.__str__`, did you extend the parent's method with `super()` or replace it completely? When would you choose each option?

> 🧩 **Pattern spotlight — Template Method.** The parent class defines the skeleton of an algorithm (`send_on_mission`) and lets subclasses fill one step (`refusal_reason`). In 6.3 you will meet **Strategy**, which solves a similar problem through composition instead of inheritance.

**Files.** `refuge/models/creature.py`, `refuge/models/species.py`, `refuge/exceptions.py`, `playground/ex_2_1.py`

---

### Exercise 2.2 — Mixin and MRO

**Context.** Dragons, phoenixes and griffins fly. Flying is a **capability**, not a species: it should be written once and plugged into several classes.

**Tasks.**

1. Add a concrete method `travel_mode() -> str` to `Creature`, returning `"on foot"`.
2. Make sure `Creature.__init__` ends with `super().__init__()`: this makes the class **cooperative** in a multiple-inheritance chain.
3. In `refuge/models/mixins.py`, create `FlyingMixin`:
   - `__init__(self, *args, **kwargs)` calls `super().__init__(*args, **kwargs)`, then creates `self.flight_log: list[str] = []`;
   - `travel_mode()` returns `"by air"`;
   - `fly(destination: str) -> str` builds the message `"{name} soars toward {destination}."`, appends it to `flight_log` and returns it.
4. Apply the mixin to `Dragon`, `Phoenix` and `Griffin`, placing it **first**: `class Dragon(FlyingMixin, Creature)`.
5. **Experiment** in the playground:
   - create `WrongOrderDragon(Creature, FlyingMixin)` with trivial implementations of the two abstract methods, then compare its MRO and its `travel_mode()`;
   - temporarily remove `super().__init__()` from `Creature.__init__`, call `WrongOrderDragon(...).flight_log`, and observe the error;
   - restore the line.

**Verify.**

```python
from refuge.models.mixins import FlyingMixin

frostbite = Dragon("Frostbite", "Nordic Realms", 95, "ice")
print([cls.__name__ for cls in Dragon.__mro__])
print(frostbite.travel_mode())
print(frostbite.fly("Frozen Peaks"))
print(frostbite.flight_log)
print(Unicorn("Moonbeam", "Crystal Lake", 67).travel_mode())

print([cls.__name__ for cls in WrongOrderDragon.__mro__])
print(WrongOrderDragon("Test", "Dragon", "Lab", 10).travel_mode())

print(isinstance(frostbite, Creature), isinstance(frostbite, FlyingMixin),
      issubclass(Unicorn, FlyingMixin), issubclass(Phoenix, Dragon))
```

```
['Dragon', 'FlyingMixin', 'Creature', 'ABC', 'object']
by air
Frostbite soars toward Frozen Peaks.
['Frostbite soars toward Frozen Peaks.']
on foot
['WrongOrderDragon', 'Creature', 'ABC', 'FlyingMixin', 'object']
on foot
True True False False
```

**Questions.**
1. Explain both MROs. When `Creature` and `FlyingMixin` both define `travel_mode()`, which one wins, and why?
2. Why does the convention place mixins on the **left**?
3. Why does `FlyingMixin.__init__` take `*args, **kwargs`? What breaks if `Creature.__init__` does not call `super().__init__()`?
4. `FlyingMixin.fly()` uses `self.name`, which the mixin does not define. What risk does that create? Which tool from chapter 5 could describe this requirement explicitly?

**Files.** `refuge/models/creature.py`, `refuge/models/mixins.py`, `refuge/models/species.py`, `playground/ex_2_2.py`

---

### Exercise 2.3 — LSP and duck typing

**Context.** The head keeper wrote a generic end-of-day report. **Do not modify it.**

```python
def end_of_day_report(residents: list) -> None:
    for resident in residents:
        print(f"--- {resident.name} ---")
        print(resident.special_ability())
        print(f"Mission duration if sent: {resident.mission_duration_days()} days")
        print(resident)
```

**Tasks.**

1. Call `end_of_day_report()` with a `Dragon`, a `Phoenix` and a `Unicorn`. It must work without any type check.
2. A junior developer added a decorative statue to the refuge:

   ```python
   class StatueDragon(Dragon):
       """A stone dragon displayed at the refuge entrance."""

       def special_ability(self) -> str:
           raise NotImplementedError("Statues have no abilities.")

       def refusal_reason(self) -> str | None:
           return "A statue cannot move."
   ```

   Add a `StatueDragon` to the list and run the report. Explain precisely why this subclass violates the Liskov Substitution Principle.
3. A colleague argues: *"The `refusal_reason()` override is fine, the parent's contract allows refusals."* Is the colleague technically right? Is the design right? (Think about the *is-a* test.)
4. Propose a corrected design in a few lines, with class names and one sentence each. You do not have to implement it.
5. **Duck typing.** Add `RoboticGuard("Sentinel", "RX-7")` to the list and run the report again. The class has **no parent**:

   ```python
   class RoboticGuard:
       def __init__(self, name: str, model: str) -> None:
           self.name = name
           self.model = model

       def special_ability(self) -> str:
           return f"{self.name} patrols the perimeter and fires laser beams."

       def mission_duration_days(self) -> int:
           return 1

       def __str__(self) -> str:
           return f"{self.name} [Robotic Guard — model {self.model}]"
   ```

**Verify.** The report prints four lines per resident and crashes on the statue with `NotImplementedError: Statues have no abilities.` Once the statue is removed, the robotic guard prints:

```
--- Sentinel ---
Sentinel patrols the perimeter and fires laser beams.
Mission duration if sent: 1 days
Sentinel [Robotic Guard — model RX-7]
```

**Questions.**
1. Why does `RoboticGuard` work? What does it tell you about when inheritance is actually needed?
2. If the signature were `end_of_day_report(residents: list[Creature])`, what would mypy say about the robotic guard? Which tool from chapter 5 would let you describe "anything that has these methods"?

**Files.** `playground/ex_2_3.py`, `docs/design_notes.md`

---

### Exercise 2.4 — The staff hierarchy

**Context.** Creatures do not travel alone: handlers escort them, and veterinarians examine them.

**Tasks.** In `refuge/models/employee.py`:

1. Create an abstract class `Employee(ABC)`:
   - `__init__(self, full_name: str, email: str)`, which raises `ValidationError` when the email contains no `@`;
   - class attributes `ROLE = "employee"` and `PERMISSIONS: frozenset[str] = frozenset()`;
   - `can(permission: str) -> bool`;
   - `can_escort(creature) -> bool`, which returns `False` (by default, an employee does not escort);
   - an abstract method `describe_duties() -> str`;
   - `__str__`, returning `"Dara Quill (veterinarian)"` built from `ROLE`.
2. Create `Handler(Employee)`:
   - `ROLE = "handler"`, `PERMISSIONS = frozenset({"escort_mission"})`;
   - a `certification_level` property, validated between 1 and 5. Message: `certification_level must be between 1 and 5, got 7.`
   - `can_escort(creature)`, which returns `certification_level * 20 >= creature.power_level`;
   - `describe_duties()`, returning `"Aldric Stone escorts creatures up to power 100."`;
   - `__str__`, returning `"Aldric Stone (handler, level 5)"`.
3. Create `Veterinarian(Employee)`:
   - `ROLE = "veterinarian"`, `PERMISSIONS = frozenset({"perform_checkup"})`;
   - `describe_duties()`, returning `"Dara Quill examines and treats the creatures."`;
   - `perform_checkup(creature, status: str, diagnosis: str) -> str`, returning `"Dara Quill examined Gorgo: quarantine (Unstable petrifying gaze)."`. It will return a real health record in 5.2.

**Verify.**

```python
from refuge.models.employee import Handler, Veterinarian
from refuge.models.species import Dragon, Basilisk

aldric = Handler("Aldric Stone", "aldric@refuge.example", 5)
brynn = Handler("Brynn Ashford", "brynn@refuge.example", 3)
dara = Veterinarian("Dara Quill", "dara@refuge.example")
frostbite = Dragon("Frostbite", "Nordic Realms", 95, "ice")

for employee in (aldric, brynn, dara):
    print(employee, "|", employee.describe_duties())
print([e.full_name for e in (aldric, brynn, dara) if e.can_escort(frostbite)])
print(dara.can("perform_checkup"), brynn.can("perform_checkup"))
print(dara.perform_checkup(Basilisk("Gorgo", "Serpent Marsh", 91), "quarantine", "Unstable petrifying gaze"))

try:
    Handler("Cael Morrow", "cael@refuge.example", 7)
except ValidationError as error:
    print(error)
```

```
Aldric Stone (handler, level 5) | Aldric Stone escorts creatures up to power 100.
Brynn Ashford (handler, level 3) | Brynn Ashford escorts creatures up to power 60.
Dara Quill (veterinarian) | Dara Quill examines and treats the creatures.
['Aldric Stone']
True False
Dara Quill examined Gorgo: quarantine (Unstable petrifying gaze).
certification_level must be between 1 and 5, got 7.
```

**Questions.**
1. Aldric obtains a veterinary degree and must now perform check-ups too. How do you represent that with inheritance? List at least two options and their drawbacks. Keep your answer: chapter 6 revisits it.
2. `can_escort()` on `Employee` returns `False`. Does this respect LSP? Does it make sense for an `Employee` to know about escorting at all? (Keep this for 6.1.)

**Files.** `refuge/models/employee.py`, `playground/ex_2_4.py`

---

## Chapter 3 — Relational databases

> **Setup.** You need a PostgreSQL server and a SQL client (psql, pgAdmin, DBeaver or the PyCharm database tool).
> - With Docker: `docker run --name refuge-db -e POSTGRES_USER=refuge -e POSTGRES_PASSWORD=refuge -e POSTGRES_DB=refuge -p 5432:5432 -d postgres:16`
> - Without Docker: install PostgreSQL locally, then create a user `refuge` and a database `refuge`.

### Exercise 3.1 — From objects to tables

**Context.** Every creature you created disappears when the program stops. The refuge needs persistence, shared access and guarantees on its data. Your job is to design the database schema from the domain you modelled in Python.

**Tasks.**

1. **Write `sql/schema.sql`** from the data dictionary below.
   - The dictionary imposes the table and column names, because later exercises rely on them.
   - **You** choose the data types, primary keys, foreign keys, `NOT NULL`, `UNIQUE`, `DEFAULT` and `CHECK` constraints, and the `ON DELETE` behaviours.
   - The script must be re-runnable: start with `DROP TABLE IF EXISTS ... CASCADE`, then create the tables in dependency order.

| Table | Column | Meaning and rules |
|---|---|---|
| `enclosures` | `id` | Surrogate key |
| | `name` | Unique |
| | `capacity` | Strictly positive |
| `creatures` | `id` | Surrogate key |
| | `name` | Unique |
| | `species` | One of the 5 valid species |
| | `origin` | Required |
| | `power_level` | Integer between 0 and 100 |
| | `element` | Only for dragons, `NULL` for every other species |
| | `resurrection_count` | ≥ 0, defaults to 0 |
| | `in_refuge` | Boolean, defaults to true |
| | `enclosure_id` | Optional: a creature may not be housed yet |
| | `registered_at` | Timestamp, defaults to now |
| `employees` | `id` | Surrogate key |
| | `full_name` | Unique (a simplification, see the questions) |
| | `email` | Unique |
| | `role` | `handler` or `veterinarian` |
| | `certification_level` | 1 to 5, required for handlers only |
| | `supervisor_id` | Optional, another employee |
| | `hired_on` | Date, defaults to today |
| `destinations` | `id` | Surrogate key |
| | `name` | Unique |
| | `danger_multiplier` | Decimal with one digit after the point, ≥ 1.0, defaults to 1.0 |
| `missions` | `id` | Surrogate key |
| | `creature_id`, `handler_id`, `destination_id` | Required references |
| | `departure_date` | Date |
| | `duration_days` | Strictly positive |
| | `base_reward` | Money, ≥ 0 |
| | `returned_on` | `NULL` while the mission is ongoing, never before the departure |
| | `notes` | Text, defaults to an empty string |
| | — | A creature cannot depart twice on the same day |
| `health_records` | `id` | Surrogate key |
| | `creature_id`, `vet_id` | Required references |
| | `examined_on` | Date, defaults to today |
| | `status` | `healthy`, `under_observation`, `in_treatment` or `quarantine` |
| | `diagnosis` | Required |
| | `treatment` | Defaults to an empty string |

2. **Table-level `CHECK` constraints.** Express two of the rules above as `CHECK` constraints that involve two columns each:
   - only dragons have an `element`;
   - handlers must have a `certification_level`.
3. **`ON DELETE` behaviours.** Choose and justify them for four cases:
   - an enclosure that still houses creatures is deleted;
   - a creature that has missions is deleted;
   - a creature that has health records is deleted;
   - a supervisor leaves the refuge.
4. **ER diagram.** Draw it with the tool of your choice (PlantUML, Mermaid, dbdiagram.io, or the diagram generated by DBeaver or PyCharm) and save it in `docs/`. Cardinalities must be visible.
5. **Python ↔ SQL mapping.** In `docs/design_notes.md`, fill this table:

| Python | SQL |
|---|---|
| A class | ? |
| An attribute | ? |
| A validation in a setter | ? |
| The `Creature` subclasses | ? |
| The `Employee` subclasses | ? |
| An `Enclosure` holding creatures (chapter 5) | ? |

**Verify.**
- Run `psql -h localhost -U refuge -d refuge -f sql/schema.sql` **twice** in a row. Both runs must succeed.
- List your constraints with the query below. You should find at least: the unique names and emails, the species and status lists, the 0–100 range, the two table-level checks, and the uniqueness of (creature, departure date).

```sql
SELECT conrelid::regclass AS table_name, conname, pg_get_constraintdef(oid) AS definition
FROM pg_constraint
WHERE connamespace = 'public'::regnamespace
ORDER BY 1, 2;
```

**Questions.**
1. Python has inheritance; SQL does not. Name the three classic ways to store a class hierarchy in tables (single table, class table, concrete table). Which one did you choose for creatures, and what is the trade-off?
2. Which table is the junction of a many-to-many relationship? Between which tables? What data lives on the relationship itself?
3. Why is `full_name` a fragile natural key? What would you use in a real system?
4. Why store money as `NUMERIC` and not as `FLOAT`? Which Python type matches it?
5. Back to question 4 of 1.3: Python validates `power_level`, and so does the database. Why keep both checks? (Hint: who else writes into the database?)
6. Why does the danger multiplier live in a table rather than in Python code? (Keep the answer for 6.1.)

**Files.** `sql/schema.sql`, `docs/er_diagram.*`, `docs/design_notes.md`

---

### Exercise 3.2 — Seed, CRUD and constraints

**Context.** The refuge's registers have been digitised. You load them, then practise single-table queries.

**Tasks.**

1. Create `sql/seed.sql` with the reference dataset below and run it on a **freshly created** schema (the ids must start at 1).

```sql
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
```

> From now on, **reset the database** whenever an exercise asks for it: `psql ... -f sql/schema.sql -f sql/seed.sql`.

2. In `sql/queries/01_crud.sql`, write the following queries.
   - a. All unicorns, ordered by power, strongest first.
   - b. Creatures whose name starts with `S`.
   - c. Insert the dragon `Cinder` (origin Ashlands, power 60, element fire) and get its id back with `RETURNING`.
   - d. Ember resurrects: increment its `resurrection_count` and return the new value with `RETURNING`.
   - e. Health records of the last 30 days, as of `DATE '2026-03-15'`.
   - f. Ongoing missions with their due date computed in SQL (`departure_date + duration_days`).
   - g. Every creature with its element, or the text `none` when it has no element (use `COALESCE`).
   - h. Delete `Cinder`. Then try to delete `Frostbite` and read the error.
3. **Constraint violations.** Write 7 statements that **must fail**, one per rule:
   - a power level of 150;
   - a duplicate creature name;
   - a unicorn with an element;
   - a mission lasting 0 days;
   - the health status `'sick'`;
   - a handler without a certification level;
   - two missions for the same creature on the same day.

   Copy each error message into your design notes.
4. Inside a transaction, run an `UPDATE creatures SET power_level = 0;` **without** a `WHERE` clause, look at the damage, then `ROLLBACK`.

**Verify.**

| Query | Expected result |
|---|---|
| a | Moonbeam (67), Stardust (45), Willow (42) |
| b | Stardust, Sylph |
| c | `id = 10` |
| e | 6 rows |
| f | 3 rows: Ember (due 2026-03-09), Frostbite (due 2026-03-15), Willow (due 2026-03-15) |
| h | `update or delete on table "creatures" violates foreign key constraint ...` (the constraint name depends on your schema) |

**Questions.**
1. What is the difference between `DELETE`, `TRUNCATE` and `DROP`?
2. Why will `RETURNING` be invaluable once Python inserts the rows (5.4)?
3. What did step 4 teach you about transactions?

**Files.** `sql/seed.sql`, `sql/queries/01_crud.sql`, `docs/design_notes.md`

---

## Chapter 4 — SQL: JOINs & aggregates

> All queries run on the reference dataset (reset it first). "Today" is `DATE '2026-03-15'`.
> Keep your queries: some of them will become repository methods or reports in chapters 5 and 6.

### Exercise 4.1 — JOINs

**Tasks.** In `sql/queries/02_joins.sql`:

1. **Mission log.** For each mission: departure date, creature name, species, handler name and destination, ordered by departure date.
2. **Ongoing missions.** Creature, destination, due date and an `overdue` boolean as of 2026-03-15.
3. **Housing.** Every creature with the name of its enclosure, or `unassigned` when it has none.
4. **Anti-joins** (`LEFT JOIN` + `IS NULL`):
   - creatures that were never sent on a mission;
   - destinations that were never visited;
   - handlers who never escorted anyone.
5. **Self-join.** Every employee with the name of their supervisor, or `-` when they have none.
6. **The NULL trap.** List all creatures together with their missions departed since `2026-02-01`, **keeping the creatures that have none**.
   - First write the naive version, with the date filter in `WHERE`.
   - Explain why it loses rows.
   - Then fix it.
7. **Health alerts.** Creatures that have at least one record with status `quarantine` or `in_treatment`, with the status and the examination date.

**Verify.**

| Query | Expected result |
|---|---|
| 1 | 9 rows. First row: `2026-01-05 \| Frostbite \| Dragon \| Aldric Stone \| Frozen Peaks` |
| 2 | Ember – Frozen Peaks – 2026-03-09 – **true**; Willow – Northern Pass – 2026-03-15 – false; Frostbite – Shadow Forest – 2026-03-15 – false |
| 3 | 9 rows. Only Sylph is `unassigned` |
| 4 | Gorgo and Sylph / Sunlit Valley / Cael Morrow |
| 5 | Aldric Stone (-), Brynn Ashford (Aldric Stone), Cael Morrow (Aldric Stone), Dara Quill (-), Elio Fenn (Dara Quill), Faye Lumen (Aldric Stone) |
| 6 | Naive version: 6 rows. Fixed version: 9 rows, where Moonbeam, Sylph and Gorgo have no mission |
| 7 | Gorgo (quarantine, 2026-02-28), Moonbeam (in_treatment, 2026-03-10) |

**Questions.**
1. Why does a `WHERE` condition on the right-hand table turn a `LEFT JOIN` into an `INNER JOIN`?
2. Stardust was `under_observation`, then `healthy`. Query 7 looks at *every* record. Why is "the latest record per creature" harder to get with a simple join? (Pack A solves it.)

**Files.** `sql/queries/02_joins.sql`

---

### Exercise 4.2 — Aggregates and grouping

**Tasks.** In `sql/queries/03_aggregates.sql`:

1. **Occupancy.** For every enclosure, including empty ones: name, capacity, number of occupants and free slots.
2. **Full enclosures.** The same query, keeping only full enclosures (`HAVING`).
3. **Species.** For each species: number of creatures and average power rounded to one decimal.
4. **Workload.** Number of missions per handler, including handlers with none. Then keep only handlers with at least 3 missions.
5. **Earnings.** Reward earned per creature on **completed** missions (base reward × danger multiplier), highest first.
6. **Monthly activity.** For each month: number of missions and total reward (`DATE_TRUNC`).
7. **`COUNT(*)` vs `COUNT(column)`.** In one query, count all missions and count `returned_on`.
8. **Destinations.** Total reward per destination over all missions, showing 0 for destinations never visited.

**Verify.**

Query 1 (ordered by name):

```
     name      | capacity | occupants | free_slots
---------------+----------+-----------+------------
 Crystal Glade |        4 |         3 |          1
 Ember Caves   |        3 |         3 |          0
 Frozen Hall   |        2 |         0 |          2
 Sky Nest      |        2 |         2 |          0
```

Queries 2 to 8:

| Query | Expected result |
|---|---|
| 2 | Ember Caves, Sky Nest |
| 3 | Basilisk 1 / 91.0, Dragon 2 / 91.5, Griffin 1 / 80.0, Phoenix 2 / 65.0, Unicorn 3 / 51.3 |
| 4 | Faye Lumen 4, Aldric Stone 3, Brynn Ashford 2, Cael Morrow 0. Filtered: Faye Lumen, Aldric Stone |
| 5 | Ignis 1800, Frostbite 1000, Talon 600, Ember 200, Moonbeam 120, Stardust 80 |
| 6 | 2026-01: 3 missions / 1320 · 2026-02: 3 / 2480 · 2026-03: 3 / 2660 |
| 7 | 9 and 6 |
| 8 | Shadow Forest 3900, Frozen Peaks 2100, Northern Pass 460, Sunlit Valley 0 |

**Questions.**
1. What is the difference between `WHERE` and `HAVING`? Show it with query 4.
2. In query 1, why must you write `COUNT(c.id)` and not `COUNT(*)`? What would `COUNT(*)` return for Frozen Hall?
3. Why must every non-aggregated column of the `SELECT` appear in the `GROUP BY`?

**Files.** `sql/queries/03_aggregates.sql`

---

## Chapter 5 — Composition, special methods, interfaces & database connection

> This chapter connects the two worlds. You build richer Python objects (containers, data records), then the connection layer, then the services that use both.
> It is the longest chapter: plan about two days.

### Exercise 5.1 — The `Enclosure` container

**Context.** Creatures live in enclosures, which have a capacity and compatibility rules. An enclosure **has** creatures; it **is not** a list.

**Tasks.** In `refuge/models/enclosure.py`, create `Enclosure`:

1. `__init__(self, name: str, capacity: int)`.
   - It raises `ValidationError` when `capacity <= 0`.
   - The internal storage `_creatures: list[Creature]` is never exposed directly.
2. A class constant `INCOMPATIBLE_PAIRS`, a `frozenset` of `frozenset`s: `{"Dragon", "Unicorn"}`, `{"Basilisk", "Phoenix"}`, `{"Basilisk", "Unicorn"}`.
3. Properties `free_slots`, `is_full` and `species` (the `set` of species currently housed).
4. Add `EnclosureFullError(RefugeError)` and `IncompatibleSpeciesError(RefugeError)` to `exceptions.py`.
5. `add(creature)` runs its checks in this order:
   - a duplicate name raises `ValidationError("Frostbite is already in Ember Caves.")`;
   - a full enclosure raises `EnclosureFullError("Ember Caves is full (3/3).")`;
   - an incompatible species raises `IncompatibleSpeciesError("A Unicorn cannot live with a Dragon in Ember Caves.")`.
6. `can_accept(creature) -> bool` answers the same question without raising. It will be used in 6.3. Do not duplicate the rules between `add` and `can_accept`: extract a private helper.
7. `remove(name) -> Creature`.
8. Special methods:
   - `__len__`;
   - `__contains__(name)`, so that `"Frostbite" in caves` works;
   - `__iter__`, written as a **generator** with `yield`;
   - `__getitem__(name)`, which raises `KeyError` when the name is unknown;
   - `__repr__`, returning `Enclosure('Ember Caves', 2/3: ['Frostbite', 'Ignis'])`.

**Verify.**

```python
from refuge.models.enclosure import Enclosure
from refuge.models.species import Dragon, Unicorn, Basilisk, Griffin
from refuge.exceptions import EnclosureFullError, IncompatibleSpeciesError

caves = Enclosure("Ember Caves", 3)
caves.add(Dragon("Frostbite", "Nordic Realms", 95, "ice"))
caves.add(Dragon("Ignis", "Volcanic Depths", 88, "fire"))

print(len(caves))
print("Frostbite" in caves, "Ember" in caves)
print(caves["Ignis"])
print(repr(caves))
for creature in caves:
    print(creature.name, "-", creature.travel_mode())

try:
    caves.add(Unicorn("Stardust", "Silver Woods", 45))
except IncompatibleSpeciesError as error:
    print("IncompatibleSpeciesError:", error)

caves.add(Basilisk("Gorgo", "Serpent Marsh", 91))
print(caves.is_full, caves.free_slots)

try:
    caves.add(Dragon("Cinder", "Ashlands", 60, "fire"))
except EnclosureFullError as error:
    print("EnclosureFullError:", error)

try:
    caves["Ember"]
except KeyError as error:
    print("KeyError:", error)

print(caves.remove("Ignis").name, repr(caves))
print(caves.can_accept(Unicorn("Pebble", "Misty Hills", 25)), caves.can_accept(Griffin("Talon", "Eagle Peaks", 80)))
```

```
2
True False
Ignis the Dragon (origin: Volcanic Depths) [in refuge] - element: fire
Enclosure('Ember Caves', 2/3: ['Frostbite', 'Ignis'])
Frostbite - by air
Ignis - by air
IncompatibleSpeciesError: A Unicorn cannot live with a Dragon in Ember Caves.
True 0
EnclosureFullError: Ember Caves is full (3/3).
KeyError: 'Ember'
Ignis Enclosure('Ember Caves', 2/3: ['Frostbite', 'Gorgo'])
False True
```

**Questions.**
1. Why not `class Enclosure(list)`? Name three `list` methods that would bypass your rules.
2. Python's contract says `__getitem__` raises `KeyError` (or `IndexError`). Why does it matter to respect it?
3. What does `frostbite in caves` return, where `frostbite` is the object rather than its name? Is that what you want? Decide and justify.
4. Why `frozenset` for the incompatible pairs, and not `tuple` or `set`?

**Files.** `refuge/models/enclosure.py`, `refuge/exceptions.py`, `playground/ex_5_1.py`

---

### Exercise 5.2 — `Mission` and `HealthRecord` dataclasses

**Context.** The refuge must record missions and medical examinations. These are **data records**: `@dataclass` removes the boilerplate.

**Tasks.**

1. In `refuge/models/mission.py`, create `Mission` with `@dataclass(eq=False)`:

   ```python
   creature_name: str
   handler_name: str
   destination: str
   departure_date: date
   duration_days: int
   base_reward: Decimal
   danger_multiplier: Decimal = Decimal("1.0")
   returned_on: date | None = None
   notes: str = ""
   id: int | None = field(default=None, repr=False)
   ```

   - **`__post_init__`**:
     - it rejects an empty destination;
     - it rejects a `duration_days` that is not a positive `int`, with the message `duration_days must be a positive integer, got 0.`;
     - it converts `base_reward` and `danger_multiplier` to `Decimal` (`Decimal(str(value))`, so that `500` is accepted);
     - it rejects a negative reward.
   - **Properties**: `due_date` (departure + duration), `reward` (base × multiplier) and `is_completed`.
   - **Methods**:
     - `is_overdue(today: date | None = None) -> bool`, where `None` means `date.today()`;
     - `mark_returned(on: date)`, which refuses a return before the departure;
     - `days_late() -> int`.
   - **Manual equality.** Two missions are equal when they share `creature_name` and `departure_date`: this mirrors the `UNIQUE` constraint of 3.1. Implement `__eq__` (returning `NotImplemented` for other types) and `__hash__` on the same fields.
2. In `refuge/models/health_record.py`:
   - `HealthStatus(str, Enum)` with values `healthy`, `under_observation`, `in_treatment` and `quarantine`, plus a property `allows_missions`, which is true only for `healthy` and `under_observation`;
   - `HealthRecord` with `@dataclass(frozen=True)`, with fields `creature_name`, `vet_name`, `examined_on: date`, `status: HealthStatus`, `diagnosis: str`, `treatment: str = ""` and `id: int | None = field(default=None, compare=False)`. `__post_init__` rejects an empty diagnosis.
3. Update `Veterinarian.perform_checkup(creature, status: HealthStatus, diagnosis, treatment="", on: date | None = None)` so that it returns a `HealthRecord`.

**Verify.**

```python
from dataclasses import FrozenInstanceError
from datetime import date
from decimal import Decimal
from refuge.models.mission import Mission
from refuge.models.health_record import HealthStatus

m1 = Mission("Frostbite", "Aldric Stone", "Frozen Peaks", date(2026, 1, 5), 14, 500, Decimal("2.0"))
m2 = Mission("Frostbite", "Brynn Ashford", "Northern Pass", date(2026, 1, 5), 3, 80)
m3 = Mission("Ember", "Faye Lumen", "Frozen Peaks", date(2026, 3, 2), 7, 250, Decimal("2.0"))

print(m1 == m2, hash(m1) == hash(m2), len({m1, m2, m3}))
print(m1.due_date, f"{m1.reward:.2f}")
print(m3.is_overdue(today=date(2026, 3, 15)), m3.is_overdue(today=date(2026, 3, 5)))

try:
    Mission("Ember", "Faye Lumen", "Frozen Peaks", date(2026, 3, 2), 0, 250)
except ValidationError as error:
    print(error)

m1.mark_returned(date(2026, 1, 20))
print(m1.is_completed, m1.days_late())

dara = Veterinarian("Dara Quill", "dara@refuge.example")
record = dara.perform_checkup(Basilisk("Gorgo", "Serpent Marsh", 91), HealthStatus.QUARANTINE,
                              "Unstable petrifying gaze", "Isolation", on=date(2026, 2, 28))
print(record.status.value, record.status.allows_missions)
try:
    record.status = HealthStatus.HEALTHY
except FrozenInstanceError:
    print("health records are immutable")
```

```
True True 2
2026-01-19 1000.00
True False
duration_days must be a positive integer, got 0.
True 1
quarantine False
health records are immutable
```

**Questions.**
1. Remove `eq=False`: does anything change? Read the `dataclasses` documentation: when does `@dataclass` leave your own `__eq__` and `__hash__` alone?
2. In a plain class (not a dataclass), what happens to `__hash__` when you define only `__eq__`? Why?
3. `Mission` is mutable, yet it is hashable. Why is it acceptable here? Put a mission in a set, change its `departure_date`, then look for it in the set: explain what happens.
4. Why is `HealthRecord` frozen while `Mission` is not?
5. Why does `is_overdue` accept a `today` parameter instead of always calling `date.today()`? (Chapter 7 will answer this for you.)

**Files.** `refuge/models/mission.py`, `refuge/models/health_record.py`, `refuge/models/employee.py`, `playground/ex_5_2.py`

---

### Exercise 5.3 — `DatabaseConnection`: the first real connection

**Context.** Time to talk to PostgreSQL from Python. A connection is a resource: it must be closed **whatever happens**, and a group of writes must be committed **entirely or not at all**.

**Tasks.**

1. Install `psycopg2-binary` and `python-dotenv`.
   - Create `.env` with `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` and `DB_PASSWORD`.
   - Commit a `.env.example` without the real password.
   - Add `.env` to `.gitignore`.
2. In `refuge/config.py`, write `db_settings(dbname: str | None = None) -> dict[str, str]`. It loads `.env` and returns the connection parameters. The optional argument will be used for the test database in 7.4.
3. In `refuge/db/connection.py`, create `DatabaseConnection(settings: dict | None = None)`:
   - **`__enter__`** opens the connection with `psycopg2.connect(**settings)`, prints `🔌 Connected to <dbname>` and returns `self`;
   - **`__exit__`** rolls back if an exception occurred, **always** closes the connection, prints `🔌 Connection closed` (or `🔌 Connection closed after error: <message>`) and returns `False`;
   - **`cursor()`** returns a cursor that yields rows as dictionaries (`RealDictCursor`). It raises `RuntimeError("Connection is not open.")` when called outside a `with` block;
   - **`transaction()`** is a method decorated with `@contextlib.contextmanager`: it `yield`s, then commits; on any exception it rolls back and re-raises. It raises the same `RuntimeError` when the connection is closed.
4. **Rule for the rest of the project:** `commit()` and `rollback()` exist **only** in this class. Repositories and services never call them.

**Verify.**

```python
from refuge.db.connection import DatabaseConnection

with DatabaseConnection() as db:
    with db.cursor() as cur:
        cur.execute("SELECT COUNT(*) AS n FROM creatures")
        print(cur.fetchone()["n"])
        cur.execute("SELECT name, power_level FROM creatures WHERE species = %s ORDER BY name", ("Dragon",))
        print([dict(row) for row in cur.fetchall()])

    try:
        with db.transaction():
            with db.cursor() as cur:
                cur.execute("UPDATE creatures SET power_level = power_level + 1 WHERE name = %s", ("Ignis",))
                raise RuntimeError("Dispatch system failure!")
    except RuntimeError as error:
        print("Rolled back:", error)

    with db.cursor() as cur:
        cur.execute("SELECT power_level FROM creatures WHERE name = %s", ("Ignis",))
        print(cur.fetchone()["power_level"])

try:
    db.cursor()
except RuntimeError as error:
    print(error)
```

```
🔌 Connected to refuge
9
[{'name': 'Frostbite', 'power_level': 95}, {'name': 'Ignis', 'power_level': 88}]
Rolled back: Dispatch system failure!
88
🔌 Connection closed
Connection is not open.
```

Then check two more behaviours:

- **SQL injection.** With `evil = "x' OR '1'='1"`, compare these two lines:
  - `cur.execute(f"SELECT name FROM creatures WHERE name = '{evil}'")` returns all 9 creatures;
  - `cur.execute("SELECT name FROM creatures WHERE name = %s", (evil,))` returns nothing.
- **Exception safety.** Raise `ValueError("Simulated crash mid-mission!")` inside a `with DatabaseConnection()` block. You must see `🔌 Connection closed after error: Simulated crash mid-mission!`, and the `ValueError` must still propagate.

**Questions.**
1. Why must `__exit__` return `False`? What would `True` do?
2. psycopg2 connections can also be used as `with conn:`. What does that do exactly, and does it close the connection? (Check the psycopg2 documentation.)
3. Why use a class with `__enter__`/`__exit__` for the connection, but `@contextmanager` for the transaction?
4. Why must credentials live in `.env` and never in the code?

> 🧩 **Pattern spotlight — Singleton (discussion only).** "There should be only one connection, so let's make `DatabaseConnection` a Singleton." Argue for and against. Compare with creating the connection **once** in `main` and **passing** it to whoever needs it (dependency injection). When would a Singleton be legitimate? Think of a connection pool with a `reset()` method for tests.

**Files.** `refuge/config.py`, `refuge/db/connection.py`, `.env.example`, `.gitignore`, `playground/ex_5_3.py`

---

### Exercise 5.4 — Repositories and factories

**Context.** The business code must not know whether creatures come from PostgreSQL or from memory. A **repository** hides the storage behind an interface. A **factory** rebuilds the right subclass from a database row, which fixes the `from_dict` problem you noted in 2.1.

**Tasks.**

1. **Constructors.**
   - `Creature.__init__` gets two **keyword-only** parameters: `id: int | None = None` and `in_refuge: bool = True`. Thanks to `**kwargs` (2.1), the subclasses forward them without changes.
   - `Employee.__init__` gets `id: int | None = None`.
2. **Serialisation.**
   - `Creature.to_dict()` returns `id`, `name`, `species`, `origin`, `power_level` and `in_refuge`. `Dragon` extends it with `element` and `Phoenix` with `resurrection_count`, both using `super()`.
   - Each species overrides the class method `from_dict(data)` to call its own constructor (including `id` and `in_refuge`).
3. **Factories.** In `refuge/repositories/factories.py`:
   - `CreatureFactory.create(data) -> Creature` looks up the class in a registry `_REGISTRY: dict[str, type[Creature]]` (species → class) and calls its `from_dict`. An unknown species raises `ValueError`;
   - `EmployeeFactory.create(data) -> Employee` uses the `role` column.
4. **Interfaces.** In `refuge/repositories/protocols.py`, define two `Protocol`s. Add `NotFoundError(RefugeError)` to `exceptions.py`.

   ```python
   class CreatureRepository(Protocol):
       def add(self, creature: Creature) -> Creature: ...      # sets creature.id and returns it
       def get(self, name: str) -> Creature: ...               # raises NotFoundError
       def list_all(self) -> list[Creature]: ...               # ordered by name
       def update(self, creature: Creature) -> None: ...       # persists power_level, in_refuge, resurrection_count

   class EmployeeRepository(Protocol):
       def add(self, employee: Employee) -> Employee: ...
       def get(self, full_name: str) -> Employee: ...          # raises NotFoundError
       def list_all(self) -> list[Employee]: ...
   ```

5. **In-memory implementations.** In `refuge/repositories/in_memory.py`, write `InMemoryCreatureRepository` and `InMemoryEmployeeRepository`:
   - they store objects in a dictionary keyed by name;
   - ids are assigned 1, 2, 3...;
   - adding a duplicate creature name raises `ValidationError`, mirroring the `UNIQUE` constraint.
6. **PostgreSQL implementations.** In `refuge/repositories/postgres.py`, write `PostgresCreatureRepository(db)` and `PostgresEmployeeRepository(db)`:
   - every query is parameterised;
   - rows go through the factories;
   - `add` uses `INSERT ... RETURNING id`;
   - **no repository ever commits.**
7. In the playground, write `describe_refuge(repo: CreatureRepository) -> None`, which prints `"<n> creatures: <names>"`. Call it with both implementations, then run `mypy refuge/`. The result must be zero errors.

**Verify.** Reset the database first.

```python
with DatabaseConnection() as db:
    repo = PostgresCreatureRepository(db)
    for creature in repo.list_all():
        print(creature)
    ember = repo.get("Ember")
    print(repr(ember), ember.resurrection_count)

    with db.transaction():
        cinder = repo.add(Dragon("Cinder", "Ashlands", 60, "fire"))
    print(cinder.id)

    try:
        repo.get("Grub")
    except NotFoundError as error:
        print(error)

memory = InMemoryCreatureRepository()
memory.add(Phoenix("Ember", "Ashlands", 72))
memory.add(Dragon("Frostbite", "Nordic Realms", 95, "ice"))
describe_refuge(memory)
```

```
🔌 Connected to refuge
Ember the Phoenix (origin: Ashlands) [on mission]
Frostbite the Dragon (origin: Nordic Realms) [on mission] - element: ice
Gorgo the Basilisk (origin: Serpent Marsh) [in refuge]
Ignis the Dragon (origin: Volcanic Depths) [in refuge] - element: fire
Moonbeam the Unicorn (origin: Crystal Lake) [in refuge]
Stardust the Unicorn (origin: Silver Woods) [in refuge]
Sylph the Phoenix (origin: Cloud Isles) [in refuge]
Talon the Griffin (origin: Eagle Peaks) [in refuge]
Willow the Unicorn (origin: Moon Meadows) [on mission]
Phoenix(name='Ember', species='Phoenix', origin='Ashlands', power_level=72) 2
10
No creature named 'Grub'.
🔌 Connection closed
2 creatures: Ember, Frostbite
```

Reset the database afterwards: Cinder has really been committed.

**Questions.**
1. How does `PostgresCreatureRepository.add` know whether to store an `element` without using `isinstance`?
2. To add a new species, how many places must change? Write the list down: 6.5 will check it.
3. Why do repositories never commit? Who decides where a transaction starts and ends?
4. `InMemoryCreatureRepository.update` does almost nothing. Why is that correct here, and why is `update` essential for PostgreSQL?
5. What does `Creature._total_creatures` mean now that loading rows also creates objects?

> 🧩 **Pattern spotlight — Repository.** All SQL lives in one place. The rest of the code depends on the `CreatureRepository` abstraction, never on `PostgresCreatureRepository`.
>
> 🧩 **Pattern spotlight — Factory.** The caller provides data (a species name) and the factory chooses the class. Adding a type changes **one** registry line.

**Files.** `refuge/models/creature.py`, `refuge/models/species.py`, `refuge/models/employee.py`, `refuge/exceptions.py`, `refuge/repositories/{protocols,factories,in_memory,postgres}.py`, `playground/ex_5_4.py`

---

### Exercise 5.5 — Notifiers: `Protocol` and Adapter

**Context.** The head keeper wants to be notified of departures and returns. Several channels exist: the console, a log file, and a raven-post service supplied by a third party. These channels share no common parent.

**Tasks.**

1. In `refuge/notifiers/protocol.py`, define the `Notifier` Protocol with a single method, `notify(message: str) -> None`.
2. Write three classes, **none of which inherits from or references `Notifier`**:
   - `ConsoleNotifier` (`console.py`) prints `📜 [REFUGE] <message>`;
   - `FileNotifier(path: str = "mirror_log.txt")` (`file.py`) appends `<message>\n` to the file with `with open(..., "a", encoding="utf-8")`;
   - `SilentNotifier` (`silent.py`) does nothing. It will be your test double in chapter 7.
3. In the playground, write `broadcast(notifier: Notifier, messages: list[str]) -> None` and use it with the three notifiers.
4. **Break it on purpose.**
   - Write `BrokenNotifier` with a `send(message)` method instead of `notify`, and pass it to `broadcast`. What happens at runtime?
   - Run `mypy playground/ex_5_5.py`. You should get `Argument 1 to "broadcast" has incompatible type "BrokenNotifier"; expected "Notifier"  [arg-type]`.
5. **Adapter.** Copy the third-party client below into `refuge/notifiers/raven.py`. **You are not allowed to modify it.**

   ```python
   class RavenPost:
       """Third-party raven-post client (vendored). Do NOT modify."""

       def dispatch_raven(self, recipient: str, scroll: str) -> bool:
           print(f"🐦 Raven flies to {recipient}: «{scroll}»")
           return True
   ```

   In the same file, write `RavenNotifier(raven: RavenPost, recipient: str)`, which satisfies `Notifier`. If `dispatch_raven` returns `False`, it raises `NotificationError(RefugeError)`, which you add to `exceptions.py`.

**Verify.**

```python
messages = ["Frostbite leaves for Shadow Forest.", "Ember is back."]
broadcast(ConsoleNotifier(), messages)
broadcast(SilentNotifier(), messages)
broadcast(FileNotifier("mirror_log.txt"), messages)
broadcast(RavenNotifier(RavenPost(), "Head Keeper"), messages[:1])
```

```
📜 [REFUGE] Frostbite leaves for Shadow Forest.
📜 [REFUGE] Ember is back.
🐦 Raven flies to Head Keeper: «Frostbite leaves for Shadow Forest.»
```

`mirror_log.txt` contains the two messages, one per line.

**Questions.**
1. Why is `BrokenNotifier` caught by mypy, but not when the class is defined? Compare with an ABC.
2. When would you choose an ABC rather than a Protocol for the notifiers?
3. What is the difference between an Adapter and a Facade?
4. Why is a class that does nothing (`SilentNotifier`) valuable?

> 🧩 **Pattern spotlight — Adapter.** It translates an interface you cannot change (`dispatch_raven`) into the one your application expects (`notify`), without touching either side.

**Files.** `refuge/notifiers/{protocol,console,file,silent,raven}.py`, `refuge/exceptions.py`, `playground/ex_5_5.py`

---

### Exercise 5.6 — Mission and health repositories

**Context.** Before writing the mission service, the missions and the medical records need their own repositories.

**Tasks.**

1. In `protocols.py`, add two Protocols:

   ```python
   class MissionRepository(Protocol):
       def add(self, mission: Mission) -> Mission: ...                       # sets id and danger_multiplier
       def get_open_for_creature(self, creature_name: str) -> Mission | None: ...
       def list_open_for_handler(self, handler_name: str) -> list[Mission]: ...
       def list_all(self) -> list[Mission]: ...                              # ordered by departure date
       def update(self, mission: Mission) -> None: ...                       # persists returned_on and notes

   class HealthRecordRepository(Protocol):
       def add(self, record: HealthRecord) -> HealthRecord: ...              # returns a copy with its id
       def latest_for(self, creature_name: str) -> HealthRecord | None: ...
   ```

2. Write the **in-memory** versions:
   - `InMemoryMissionRepository(multipliers: dict[str, Decimal])`:
     - `add` copies the destination's multiplier into the mission and assigns an id;
     - an unknown destination raises `NotFoundError`, mirroring the foreign key;
     - an equal mission raises `ValidationError("Talon already has a mission departing on 2026-02-10.")`, which uses your `__eq__`.
   - `InMemoryHealthRecordRepository`: since `HealthRecord` is frozen, `add` returns `dataclasses.replace(record, id=...)`.
3. Write the **PostgreSQL** versions:
   - **Read with one shared `SELECT`** joining missions, creatures, employees and destinations. Alias the columns to the exact `Mission` field names, so that a row maps with `Mission(**row)`.
   - **Insert with `INSERT INTO missions (...) SELECT c.id, e.id, d.id, ... FROM creatures c, employees e, destinations d WHERE c.name = %s AND ... RETURNING id`**, which resolves the names in SQL. When no row is inserted, raise `NotFoundError("Unknown creature, handler or destination.")`.
   - **`latest_for`** orders by `examined_on DESC, id DESC` with `LIMIT 1`, and converts the status string to `HealthStatus`.
4. In `in_memory.py`, add `NoTransaction`, whose `transaction()` returns `contextlib.nullcontext()`. In-memory and PostgreSQL code now expose the same `transaction()` API.

**Verify.** Reset the database first.

```python
with DatabaseConnection() as db:
    missions = PostgresMissionRepository(db)
    health = PostgresHealthRecordRepository(db)

    for m in missions.list_open_for_handler("Faye Lumen"):
        print(m.creature_name, m.destination, m.due_date, m.is_overdue(date(2026, 3, 15)))
    print(missions.get_open_for_creature("Ignis"))
    all_missions = missions.list_all()
    print(len(all_missions), f"{sum(m.reward for m in all_missions if m.is_completed):.2f}")
    print(health.latest_for("Stardust").status.value, health.latest_for("Gorgo").status.value)
    print(health.latest_for("Sylph"))

    try:
        with db.transaction():
            missions.add(Mission("Ignis", "Aldric Stone", "Northern Pass", date(2026, 3, 15), 14, 300))
            raise RuntimeError("Raven network down!")
    except RuntimeError:
        pass
    print(len(missions.list_all()))

memory = InMemoryMissionRepository({"Northern Pass": Decimal("1.0"), "Frozen Peaks": Decimal("2.0")})
stored = memory.add(Mission("Talon", "Faye Lumen", "Frozen Peaks", date(2026, 2, 10), 10, 300))
print(stored.id, f"{stored.reward:.2f}")
try:
    memory.add(Mission("Talon", "Aldric Stone", "Northern Pass", date(2026, 2, 10), 10, 50))
except ValidationError as error:
    print(error)
```

```
🔌 Connected to refuge
Ember Frozen Peaks 2026-03-09 True
None
9 3800.00
healthy quarantine
None
9
🔌 Connection closed
1 600.00
Talon already has a mission departing on 2026-02-10.
```

**Questions.**
1. Why alias the SQL columns to the dataclass field names?
2. `INSERT ... SELECT` resolves the names inside the database. What would the alternative cost, in number of queries?
3. The *N+1 problem*: what would happen if `list_all()` loaded the missions first, then queried the creature of each mission separately?

**Files.** `refuge/repositories/{protocols,in_memory,postgres}.py`, `playground/ex_5_6.py`

---

### Exercise 5.7 — `MissionService`: dependency injection in action

**Context.** Everything is ready to write the refuge's main business operation: sending a creature on a mission and bringing it back, while enforcing **every** rule.

**Tasks.**

1. **🧮 Algorithm corner.** In `refuge/algorithms/intervals.py` (with `Interval = tuple[date, date]`, half-open `[start, end)`), write three functions:
   - `overlaps(a: Interval, b: Interval) -> bool`;
   - `find_overlapping_pairs_naive(intervals) -> list[tuple[int, int]]`, which compares every pair;
   - `find_overlapping_pairs(intervals)`, which sorts by start date then sweeps once, keeping only the intervals still "active". Both versions return the same sorted list of index pairs `(i, j)` with `i < j`.

   Document the time complexity of each function in its docstring.
2. In `protocols.py`, add `TransactionManager(Protocol)` with `transaction(self) -> AbstractContextManager[None]`. `DatabaseConnection` and `NoTransaction` already satisfy it, without any change.
3. In `refuge/services/mission_service.py`, create `MissionService`.

   ```python
   def __init__(self, creatures: CreatureRepository, employees: EmployeeRepository,
                missions: MissionRepository, health: HealthRecordRepository,
                notifier: Notifier, tx: TransactionManager,
                clock: Callable[[], date] = date.today) -> None: ...
   ```

4. **`dispatch(creature_name, handler_name, destination, base_reward, departure_date=None) -> Mission`.** When no departure date is given, use `clock()`. Load the creature and the handler, then check the rules **in this order**, raising `MissionRefusedError` with these exact messages:

| # | Rule | Message |
|---|---|---|
| 1 | The creature is in the refuge | `Frostbite is already on a mission.` |
| 2 | The latest health record allows missions | `Gorgo cannot leave: health status is 'quarantine'.` |
| 3 | The employee can escort the creature | `Brynn Ashford (handler, level 3) is not allowed to escort Moonbeam (power 67).` |
| 4 | The handler is not busy: none of their open missions overlaps the new one | `Aldric Stone is already escorting Frostbite until 2026-03-29.` |
| 5 | The creature agrees to leave (`send_on_mission()`, hook of 2.1) | `Pebble is too weak for a mission (power 25 < 40).` |

   Then:
   - build the `Mission`, with the duration given by `creature.mission_duration_days()`, which is polymorphic;
   - inside **one** `with self._tx.transaction():` block, call `missions.add(...)` and `creatures.update(...)`;
   - notify: `🐉 Frostbite departed to Shadow Forest with Aldric Stone (due back 2026-03-29).`
5. **`recall(creature_name, returned_on=None) -> Mission`.**
   - Without an open mission, raise `NotFoundError("Moonbeam has no open mission.")`.
   - Otherwise, mark the mission as returned, bring the creature back, and persist both inside one transaction.
   - Notify `🏠 Frostbite returned from Shadow Forest - reward 2100.00 gold.` When the creature is late, add ` (1 day late)` before the final period (`days` in the plural).
6. The service contains no SQL, no `print` and no `isinstance`. It imports no concrete repository.

**Verify (in memory).**

```python
creatures = InMemoryCreatureRepository()
for creature in [Dragon("Frostbite", "Nordic Realms", 95, "ice"), Unicorn("Moonbeam", "Crystal Lake", 67),
                 Unicorn("Pebble", "Misty Hills", 25), Unicorn("Willow", "Moon Meadows", 42),
                 Basilisk("Gorgo", "Serpent Marsh", 91)]:
    creatures.add(creature)

employees = InMemoryEmployeeRepository()
employees.add(Handler("Aldric Stone", "aldric@refuge.example", 5))
employees.add(Handler("Brynn Ashford", "brynn@refuge.example", 3))
dara = employees.add(Veterinarian("Dara Quill", "dara@refuge.example"))

health = InMemoryHealthRecordRepository()
health.add(dara.perform_checkup(creatures.get("Gorgo"), HealthStatus.QUARANTINE,
                                "Unstable petrifying gaze", on=date(2026, 2, 28)))

missions = InMemoryMissionRepository({"Northern Pass": Decimal("1.0"), "Shadow Forest": Decimal("3.0")})
service = MissionService(creatures, employees, missions, health, ConsoleNotifier(), NoTransaction(),
                         clock=lambda: date(2026, 3, 15))

attempts = [
    ("Frostbite", "Aldric Stone", "Shadow Forest", 700),
    ("Gorgo", "Aldric Stone", "Northern Pass", 300),
    ("Willow", "Aldric Stone", "Northern Pass", 60),
    ("Moonbeam", "Brynn Ashford", "Northern Pass", 120),
    ("Pebble", "Brynn Ashford", "Northern Pass", 40),
    ("Frostbite", "Aldric Stone", "Northern Pass", 100),
    ("Willow", "Dara Quill", "Northern Pass", 60),
]
for attempt in attempts:
    try:
        service.dispatch(*attempt)
    except RefugeError as error:
        print(f"❌ {type(error).__name__}: {error}")

service.recall("Frostbite", returned_on=date(2026, 3, 30))
service.dispatch("Willow", "Aldric Stone", "Northern Pass", 60, departure_date=date(2026, 3, 30))
try:
    service.recall("Moonbeam")
except RefugeError as error:
    print(f"❌ {type(error).__name__}: {error}")
print(creatures.get("Frostbite"))
print(creatures.get("Willow"))
```

```
📜 [REFUGE] 🐉 Frostbite departed to Shadow Forest with Aldric Stone (due back 2026-03-29).
❌ MissionRefusedError: Gorgo cannot leave: health status is 'quarantine'.
❌ MissionRefusedError: Aldric Stone is already escorting Frostbite until 2026-03-29.
❌ MissionRefusedError: Brynn Ashford (handler, level 3) is not allowed to escort Moonbeam (power 67).
❌ MissionRefusedError: Pebble is too weak for a mission (power 25 < 40).
❌ MissionRefusedError: Frostbite is already on a mission.
❌ MissionRefusedError: Dara Quill (veterinarian) is not allowed to escort Willow (power 42).
📜 [REFUGE] 🏠 Frostbite returned from Shadow Forest - reward 2100.00 gold (1 day late).
📜 [REFUGE] 🐉 Willow departed to Northern Pass with Aldric Stone (due back 2026-04-02).
❌ NotFoundError: Moonbeam has no open mission.
Frostbite the Dragon (origin: Nordic Realms) [in refuge] - element: ice
Willow the Unicorn (origin: Moon Meadows) [on mission]
```

**Verify (PostgreSQL).** Reset the database, then run **the same service class** with the PostgreSQL repositories. `DatabaseConnection` itself plays the role of `tx`.

```python
with DatabaseConnection() as db:
    service = MissionService(PostgresCreatureRepository(db), PostgresEmployeeRepository(db),
                             PostgresMissionRepository(db), PostgresHealthRecordRepository(db),
                             ConsoleNotifier(), db, clock=lambda: date(2026, 3, 15))
    actions = [
        lambda: service.dispatch("Gorgo", "Aldric Stone", "Northern Pass", 300),
        lambda: service.dispatch("Moonbeam", "Faye Lumen", "Northern Pass", 120),
        lambda: service.recall("Frostbite"),
        lambda: service.dispatch("Ignis", "Aldric Stone", "Northern Pass", 300),
        lambda: service.dispatch("Sylph", "Brynn Ashford", "Frozen Peaks", 150),
        lambda: service.dispatch("Talon", "Aldric Stone", "Frozen Peaks", 300),
    ]
    for action in actions:
        try:
            action()
        except RefugeError as error:
            print(f"❌ {type(error).__name__}: {error}")
```

```
🔌 Connected to refuge
❌ MissionRefusedError: Gorgo cannot leave: health status is 'quarantine'.
❌ MissionRefusedError: Moonbeam cannot leave: health status is 'in_treatment'.
📜 [REFUGE] 🏠 Frostbite returned from Shadow Forest - reward 2100.00 gold.
📜 [REFUGE] 🐉 Ignis departed to Northern Pass with Aldric Stone (due back 2026-03-29).
📜 [REFUGE] 🐉 Sylph departed to Frozen Peaks with Brynn Ashford (due back 2026-03-22).
❌ MissionRefusedError: Aldric Stone is already escorting Ignis until 2026-03-29.
🔌 Connection closed
```

In SQL, check the result: Frostbite's mission now has `returned_on = 2026-03-15`, Ignis and Sylph each have a new mission, and their `in_refuge` is `false`.

**Verify (algorithm).**

```python
march = lambda day: date(2026, 3, day)
intervals = [(march(1), march(15)), (march(10), march(13)), (march(15), march(20)), (march(12), march(16))]
print(overlaps(intervals[0], intervals[2]))
print(find_overlapping_pairs_naive(intervals))
print(find_overlapping_pairs(intervals))
```

```
False
[(0, 1), (0, 3), (1, 3), (2, 3)]
[(0, 1), (0, 3), (1, 3), (2, 3)]
```

**Questions.**
1. Why does the service receive a `clock` instead of calling `date.today()`?
2. `send_on_mission()` changes the Python object **before** the transaction. If the transaction fails, the object and the database disagree. How would you fix that?
3. Faye's mission with Ember is overdue but still open, yet according to rule 4 Faye is free after 2026-03-09. Is that the right business rule? How would you change it?
4. Which modules does `mission_service.py` import? Why does that matter (DIP, chapter 6)?
5. Compare the complexity of the two `find_overlapping_pairs` versions. When does the difference become visible?

**Files.** `refuge/algorithms/intervals.py`, `refuge/repositories/protocols.py`, `refuge/services/mission_service.py`, `playground/ex_5_7.py`

---

## Chapter 6 — SOLID principles & clean code

### Exercise 6.1 — Diagnose the legacy

**Context.** Before you arrived, a developer wrote a first version of the refuge software. It "works", but every change is risky. Copy it into `playground/legacy_refuge_manager.py` and **read it carefully**. You do not need to run it.

```python
import psycopg2


class RefugeManager:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", dbname="refuge", user="admin", password="dragon123")
        self.missions = []

    def register_creature(self, name, species, origin, power):
        if power < 0 or power > 100:
            print("ERROR: bad power")
            return
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO creatures (name, species, origin, power_level) "
                    f"VALUES ('{name}', '{species}', '{origin}', {power})")
        self.conn.commit()

    def send(self, name, handler, destination, reward):
        cur = self.conn.cursor()
        cur.execute(f"SELECT species, power_level FROM creatures WHERE name = '{name}'")
        species, power = cur.fetchone()
        if species == "Dragon":
            days = 14
        elif species == "Phoenix":
            days = 7
        elif species == "Unicorn":
            if power < 40:
                print("ERROR: unicorn too weak")
                return
            days = 3
        else:
            days = 5
        if destination == "Frozen Peaks":
            total = reward * 2
        elif destination == "Shadow Forest":
            total = reward * 3
        else:
            total = reward
        self.missions.append({"creature": name, "handler": handler, "destination": destination,
                              "days": days, "reward": total})
        cur.execute(f"UPDATE creatures SET in_refuge = false WHERE name = '{name}'")
        self.conn.commit()
        print(f"[EMAIL] Head keeper: {name} leaves for {destination}.")
        print(f"[SMS] {handler}: prepare {name} for {days} days.")

    def text_report(self):
        lines = ["=== Missions ==="]
        for m in self.missions:
            lines.append(f"{m['creature']} -> {m['destination']} ({m['days']}d, {m['reward']} gold)")
        return "\n".join(lines)

    def html_report(self):
        rows = "".join(f"<tr><td>{m['creature']}</td><td>{m['destination']}</td><td>{m['reward']}</td></tr>"
                       for m in self.missions)
        return f"<table>{rows}</table>"

    def csv_report(self):
        lines = ["creature,destination,days,reward"]
        for m in self.missions:
            lines.append(f"{m['creature']},{m['destination']},{m['days']},{m['reward']}")
        return "\n".join(lines)

    def save_report(self, path):
        with open(path, "w") as f:
            f.write(self.csv_report())


class ReadOnlyRefugeManager(RefugeManager):
    def register_creature(self, *args):
        raise RuntimeError("This manager is read-only.")

    def send(self, *args):
        raise RuntimeError("This manager is read-only.")
```

**Tasks.** Answer in `docs/design_notes.md`.

1. **SRP.** List every distinct responsibility of `RefugeManager`, and who (which "stakeholder") could ask to change each one.
2. **OCP.**
   - What must you edit to add the destination "Volcanic Rift" (×4), or the species Kraken? Find the **bug** hidden in the `else` branch.
   - How does your schema (3.1) and your design (2.1, 5.4) avoid both edits?
3. **LSP.** Why does `ReadOnlyRefugeManager` violate LSP? What breaks in a function that receives a `RefugeManager`?
4. **ISP.** Which "fat" interface is hiding in this class? Which client needs only part of it?
5. **DIP.** List the concrete dependencies created or hard-coded inside the class.
6. **Clean code.**
   - Find at least five more problems: security, error handling, naming, magic numbers, persistence consistency...
   - Explain the difference between **cohesion** and **coupling** using this class.
7. **Mapping.** For each problem found, give the file and class of your project that already solves it, or write "not yet". Exercises 6.2 to 6.5 handle the "not yet" items.

**Questions.**
1. Back to 2.4, question 1: how would *composition* model employees who hold several roles? Sketch the classes.
2. Back to 2.4, question 2: is `Employee.can_escort()` an ISP problem? Argue both sides.

**Files.** `playground/legacy_refuge_manager.py`, `docs/design_notes.md`

---

### Exercise 6.2 — Observer: decoupling side effects

**Context.**
- The head keeper wants an **audit trail** of every departure, return and refusal.
- Adding it to `MissionService` would give the service a third responsibility after the business rules and the notifications.

The service should only announce *what happened*. Whoever is interested reacts.

**Tasks.**

1. In `refuge/services/events.py`:
   - **Events.** Three frozen dataclasses: `MissionStarted(mission: Mission)`, `MissionCompleted(mission: Mission)` and `MissionRefused(creature_name: str, reason: str, on: date)`.
   - **`EventBus`.** `subscribe(event_type: type, handler: Callable[[Any], None]) -> None` and `publish(event) -> None`. `publish` calls the handlers registered for `type(event)`, in subscription order. An event without subscribers is simply ignored.
   - **`EventPublisher(Protocol)`** with `publish(event) -> None`.
2. **Refactor `MissionService`.**
   - Replace the `notifier` parameter with `events: EventPublisher`.
   - Publish `MissionStarted` after a successful dispatch and `MissionCompleted` after a recall.
   - When a rule refuses a dispatch, including the refusal from `send_on_mission()`, publish `MissionRefused` before re-raising the exception.
3. In `refuge/services/listeners.py`:
   - **`NotificationListener(notifier: Notifier)`** with `on_started` and `on_completed`, producing **exactly** the messages of 5.7.
   - **`AuditTrail(path: str)`** with `on_started`, `on_completed` and `on_refused`. It appends one line per event, in the format `date;EventName;creature;detail`:
     - for `MissionStarted`, the date is the departure date and the detail is the destination;
     - for `MissionCompleted`, the date is the return date and the detail is the destination;
     - for `MissionRefused`, the date is `on` and the detail is the reason.
4. In the playground, wire the bus: two subscriptions for notifications and three for the audit trail. Then replay the in-memory scenario of 5.7.

**Verify.**
- The console output is **identical** to 5.7.
- `audit.log` starts with:

```
2026-03-15;MissionStarted;Frostbite;Shadow Forest
2026-03-15;MissionRefused;Gorgo;Gorgo cannot leave: health status is 'quarantine'.
2026-03-15;MissionRefused;Willow;Aldric Stone is already escorting Frostbite until 2026-03-29.
2026-03-15;MissionRefused;Moonbeam;Brynn Ashford (handler, level 3) is not allowed to escort Moonbeam (power 67).
2026-03-15;MissionRefused;Pebble;Pebble is too weak for a mission (power 25 < 40).
```

- It ends with `2026-03-30;MissionCompleted;Frostbite;Shadow Forest` followed by `2026-03-30;MissionStarted;Willow;Northern Pass`.

**Questions.**
1. Which SOLID principles improved? What does adding a fourth reaction (for example, an SMS to the handler) cost now?
2. What do you lose compared with direct calls (readability, order of execution, debugging)?
3. If a listener raises an exception, should the dispatch fail? Where would you handle it?

> 🧩 **Pattern spotlight — Observer.** The publisher does not know its subscribers. One event can trigger any number of independent reactions, each one testable on its own.

**Files.** `refuge/services/events.py`, `refuge/services/listeners.py`, `refuge/services/mission_service.py`, `playground/ex_6_2.py`

---

### Exercise 6.3 — Strategy: placing newcomers

**Context.** New creatures arrive and must be housed. The keepers disagree on how:
- one wants to use the first enclosure that fits;
- another wants to fill enclosures as tightly as possible;
- a third wants to group creatures of the same species.

The placement rule must be **swappable** without touching the service.

**Tasks.**

1. **Interface.** In `refuge/services/placement.py`, define `PlacementStrategy(Protocol)` with `choose(creature, enclosures: Sequence[Enclosure]) -> Enclosure | None`.
2. **Three strategies.** All of them rely on `Enclosure.can_accept()` (5.1):
   - `FirstFit` returns the first enclosure that accepts the creature;
   - `BestFit` returns, among the enclosures that accept it, the one with the **fewest free slots**. Ties go to the first one;
   - `SameSpeciesFirst(fallback: PlacementStrategy = FirstFit())` prefers an accepting enclosure that already houses the same species, and otherwise delegates to its fallback.
3. **Service.** `PlacementService(strategy)`:
   - `place(creature, enclosures) -> Enclosure` adds the creature to the chosen enclosure, or raises `NoEnclosureAvailableError(RefugeError)`;
   - `set_strategy(strategy)` changes the strategy at runtime.
4. **🧮 Algorithm corner.**
   - Placing items in containers is a **bin-packing** problem, which is NP-hard in general. These strategies are classic heuristics.
   - Give the complexity of one placement with *n* enclosures.
   - Add `place_all(creatures, enclosures, decreasing: bool = False)`. With `decreasing=True`, it places the most powerful creatures first ("First Fit Decreasing"). Explain why that ordering often helps.

**Verify.** Build this layout **from scratch before each strategy**. Then place `Phoenix("Sylph", "Cloud Isles", 58)` followed by `Dragon("Cinder", "Ashlands", 60, "fire")`.
- Frozen Hall (capacity 2): empty.
- Ember Caves (capacity 3): Ignis, Gorgo.
- Crystal Glade (capacity 4): Stardust, Moonbeam, Willow.
- Sky Nest (capacity 2): Talon.

```
FirstFit         Sylph -> Frozen Hall   Cinder -> Frozen Hall
BestFit          Sylph -> Crystal Glade Cinder -> Ember Caves
SameSpeciesFirst Sylph -> Frozen Hall   Cinder -> Ember Caves
```

**Questions.**
1. Strategy (6.3) and Template Method (2.1) both vary one step of a behaviour. What is the difference?
2. When would a plain function (`Callable`) be enough instead of a class per strategy?
3. Which line of the legacy code of 6.1 was asking for a Strategy?

> 🧩 **Pattern spotlight — Strategy.** An algorithm becomes an interchangeable object, injected from outside. An `if/elif` block that selects an algorithm is the classic signal.

**Files.** `refuge/services/placement.py`, `refuge/exceptions.py`, `playground/ex_6_3.py`

---

### Exercise 6.4 — Reports with small interfaces (ISP)

**Context.** The head keeper wants mission reports. A report only **reads** missions: it should not depend on methods that write them.

**Tasks.**

1. **Split the Protocol.** In `protocols.py`, split `MissionRepository` into three small Protocols:
   - `MissionReader` with `list_all`;
   - `MissionFinder` with `get_open_for_creature` and `list_open_for_handler`;
   - `MissionWriter` with `add` and `update`.

   Then redefine `class MissionRepository(MissionReader, MissionFinder, MissionWriter, Protocol)`. Your implementations do not change.
2. **Formatter interface.** In `refuge/services/reports.py`, define `ReportFormatter(Protocol)` with `format(missions: Sequence[Mission]) -> str`.
3. **Text formatter.** Write `TextReportFormatter` in the format shown below, ending with the total earned on completed missions.
4. **Report service.** Write `ReportService(reader: MissionReader)` with `render(formatter: ReportFormatter) -> str`.
5. **Archived missions.** Write `ArchivedMissions(missions: list[Mission])`, a class that only offers `list_all()`. It represents missions imported from an old archive and must **not** be writable. Show that it works with `ReportService`.

**Verify.** Reset the database first.

```python
with DatabaseConnection() as db:
    print(ReportService(PostgresMissionRepository(db)).render(TextReportFormatter()))
```

```
🔌 Connected to refuge
=== Mission report (9 missions) ===
2026-01-05 | Frostbite -> Frozen Peaks  | 14d |  1000.00 gold | returned 2026-01-19
2026-01-10 | Ember     -> Northern Pass |  7d |   200.00 gold | returned 2026-01-17
2026-01-20 | Moonbeam  -> Northern Pass |  3d |   120.00 gold | returned 2026-01-23
2026-02-01 | Ignis     -> Shadow Forest | 14d |  1800.00 gold | returned 2026-02-17
2026-02-10 | Talon     -> Frozen Peaks  | 10d |   600.00 gold | returned 2026-02-20
2026-02-15 | Stardust  -> Northern Pass |  3d |    80.00 gold | returned 2026-02-18
2026-03-01 | Frostbite -> Shadow Forest | 14d |  2100.00 gold | ongoing
2026-03-02 | Ember     -> Frozen Peaks  |  7d |   500.00 gold | ongoing
2026-03-12 | Willow    -> Northern Pass |  3d |    60.00 gold | ongoing
Total earned (completed missions): 3800.00 gold
🔌 Connection closed
```

Format of a line: `f"{departure} | {creature:<9} -> {destination:<13} | {days:>2}d | {reward:>8.2f} gold | {status}"`.

**Questions.**
1. How does `ArchivedMissions` answer the `ReadOnlyRefugeManager` problem of 6.1 better than inheritance?
2. Which of the three small Protocols does `MissionService` really need? Would you narrow its signature?

**Files.** `refuge/repositories/protocols.py`, `refuge/services/reports.py`, `playground/ex_6_4.py`

---

### Exercise 6.5 — Extension test (OCP) and clean-code audit

**Context.** Three new requests arrive the same week:
- the refuge welcomes its first **Kraken**;
- a new, very dangerous destination opens: **Volcanic Rift** (×4.0);
- the accountant wants the reports in **CSV**.

A well-designed system absorbs these by **adding** code, not by editing existing classes.

**Tasks.**

1. **Before you start**, note in your design notes the files you expect to touch, using your answer to 5.4 question 2.
2. **Kraken.**
   - Add the class in `species.py`: mission duration 21 days, ability `"{name} drags whole ships into the abyss."`, does not fly.
   - Register it in the factory.
   - Write `sql/migrations/001_kraken_and_volcanic_rift.sql`:
     - replace the species `CHECK` constraint (find its name with the query of 3.1);
     - insert `Brine` (Kraken, origin Sunken Archipelago, power 89, no enclosure);
     - insert the destination `Volcanic Rift` with a multiplier of 4.0.
3. **Single source of truth.** If you had to edit `Creature.VALID_SPECIES`, that is a second place to change for every new species. Refactor so that the factory registry is the only list in Python.
   - Watch out for circular imports.
   - Bonus B.5 goes one step further.
4. **CSV.** Add `CsvReportFormatter` with header `departure_date,creature,destination,duration_days,reward,returned_on`. `ReportService` must not change.
5. **Audit.**
   - Run `ruff check refuge`, `black refuge` and `mypy refuge` until there are zero findings.
   - Replace the magic numbers with named constants (for example the `20` of `can_escort`).
   - Check that every public class and method has a docstring.

**Verify.** Reset the database, then apply the migration. Use the 5.7 PostgreSQL wiring (with the event bus of 6.2) and `clock=lambda: date(2026, 3, 15)`.

```python
brine = creatures.get("Brine")
print(brine)
print(brine.special_ability())
service.dispatch("Brine", "Aldric Stone", "Volcanic Rift", 400)
service.recall("Brine", returned_on=date(2026, 4, 5))
print(ReportService(missions).render(CsvReportFormatter()).splitlines()[-1])
```

```
Brine the Kraken (origin: Sunken Archipelago) [in refuge]
Brine drags whole ships into the abyss.
📜 [REFUGE] 🐉 Brine departed to Volcanic Rift with Aldric Stone (due back 2026-04-05).
📜 [REFUGE] 🏠 Brine returned from Volcanic Rift - reward 1600.00 gold.
2026-03-15,Brine,Volcanic Rift,21,1600.00,2026-04-05
```

**Questions.**
1. Compare your forecast (step 1) with reality: how many **existing** lines did you modify? Compare with the legacy code of 6.1.
2. The destination needed **zero** Python changes. Why?
3. The species list lives in a `CHECK` constraint, so adding a species required a migration. What would a `species` lookup table change? Is it worth it here?
4. Which tool caught the most issues during the audit? Should these checks run automatically, and when?

**Files.** `refuge/models/species.py`, `refuge/repositories/factories.py`, `refuge/models/creature.py`, `refuge/services/reports.py`, `sql/migrations/001_kraken_and_volcanic_rift.sql`

---

## Chapter 7 — Testing & project structure

### Exercise 7.1 — Structure, logging, Facade and CLI

**Context.** The refuge now works, but only through playground scripts. It needs a clean structure, a real entry point, and logs instead of `print`.

**Tasks.**

1. **`src/` layout.**
   - Move `refuge/` into `src/refuge/`.
   - Create `pyproject.toml` with the name, the version, the dependencies and the development tools (`mypy`, `ruff`, `black`).
   - Install the project with `pip install -e .`.
   - Check that the playground scripts still run.
2. **Logging.**
   - In `utils/logging_config.py`, write `configure_logging(level: int = logging.WARNING)` with the format `%(asctime)s %(levelname)s %(name)s: %(message)s`.
   - Each module uses `logger = logging.getLogger(__name__)`.
   - `MissionService` logs dispatches, returns and refusals at `INFO`.
   - `DatabaseConnection` replaces its `print` calls with `logger.debug`.
   - From now on, `print` is only allowed in `cli.py` and `ConsoleNotifier`.
3. **🧩 Decorator.** In `utils/decorators.py`, write `log_call`:
   - use `functools.wraps`;
   - log `→ dispatch(...)` on entry and `← dispatch done in 3.2 ms` on exit, at `DEBUG` level.
4. **🧩 Facade.** In `services/refuge_app.py`, write `RefugeApp`:
   - methods: `list_creatures()`, `dispatch(...)`, `recall(...)` and `mission_report(fmt: str = "text")`;
   - each one is decorated with `@log_call`;
   - the CLI depends **only** on this class.
5. **Composition root.** In `bootstrap.py`, write `build_app(db: DatabaseConnection, today: date | None = None) -> RefugeApp`. It builds the repositories, the event bus, the listeners (console notifications plus `AuditTrail("audit.log")`) and the services. This is the **only** module that knows the concrete classes.
6. **CLI.** In `cli.py` (with argparse) and `__main__.py`, implement:
   - the commands `python -m refuge [--today YYYY-MM-DD] [--verbose] {list, dispatch, recall, report}`;
   - `dispatch NAME --handler NAME --to DESTINATION --reward AMOUNT`, `recall NAME` and `report [--format text|csv]`;
   - error handling: a `RefugeError` prints `❌ <message>` on stderr and exits with code 1;
   - `--verbose` switches logging to `DEBUG`.
7. **Documentation.**
   - `README.md` covers installation, database setup, `.env`, running the CLI, running the tests and the project structure.
   - `docs/architecture.md` covers:
     - the three layers (presentation → business → data access) and their import rules;
     - the table of patterns used, with *the problem each one solves*;
     - a SOLID summary that points to the files concerned.

**Verify.** Reset the database first.

```
$ python -m refuge --today 2026-03-15 dispatch Gorgo --handler "Aldric Stone" --to "Northern Pass" --reward 300
❌ Gorgo cannot leave: health status is 'quarantine'.
$ echo $?
1
$ python -m refuge --today 2026-03-15 recall Frostbite
📜 [REFUGE] 🏠 Frostbite returned from Shadow Forest - reward 2100.00 gold.
$ python -m refuge --today 2026-03-15 dispatch Ignis --handler "Aldric Stone" --to "Northern Pass" --reward 300
📜 [REFUGE] 🐉 Ignis departed to Northern Pass with Aldric Stone (due back 2026-03-29).
$ python -m refuge report --format csv | head -3
departure_date,creature,destination,duration_days,reward,returned_on
2026-01-05,Frostbite,Frozen Peaks,14,1000.00,2026-01-19
2026-01-10,Ember,Northern Pass,7,200.00,2026-01-17
$ python -m refuge --verbose list
```

The last command also shows the `DEBUG` logs: the connection and the decorator timings.

**Questions.**
1. Why gather all the wiring in a *composition root*? What would happen if the CLI created repositories itself?
2. What is the difference between the `RefugeApp` facade and `MissionService`?
3. Why are logs sent to stderr and command results to stdout?
4. Why does the `src/` layout prevent "it works on my machine" imports?

**Files.** `pyproject.toml`, `README.md`, `docs/architecture.md`, `src/refuge/{__main__,cli,bootstrap}.py`, `src/refuge/services/refuge_app.py`, `src/refuge/utils/*.py`

---

### Exercise 7.2 — Unit tests for the domain

**Context.** Until now you checked your code by reading the playground output. That approach does not scale, does not survive refactoring, and cannot run in a CI pipeline.

**Tasks.**

1. **Setup.** Create `tests/unit/` with one test file per module listed in the final hierarchy, using `unittest`.
   - Test names follow `test_<scenario>_<expected_result>`.
   - `setUp()` builds fresh objects for every test.
2. **Required tests.** Write at least the following, with `subTest` for repeated cases:
   - **Creature:**
     - invalid power levels (`150`, `-3`, `"95"`, `True`) raise `ValidationError`;
     - `origin` is read-only;
     - `__repr__` is reconstructable for a dragon;
     - `Creature` cannot be instantiated.
   - **Species:**
     - durations and abilities of the five species;
     - the unicorn below 40 is refused;
     - the phoenix resurrection counter;
     - the flying species use `travel_mode() == "by air"`.
   - **Employees:** certification bounds; `can_escort` at the exact boundary (level 3 with power 60 succeeds, with 61 fails); a veterinarian never escorts.
   - **Enclosure:** the order of the checks in `add`; `can_accept` gives the same answers as `add`; `KeyError` for an unknown name; iteration.
   - **Mission:**
     - equality and hashing;
     - `__post_init__` validations;
     - `due_date`, `reward`, `days_late`;
     - `is_overdue` with an **injected** date, both before and after the due date.
   - **HealthRecord:** immutability; `allows_missions` for each of the 4 statuses.
   - **Intervals:** the naive and sweep versions return the same result on 5 hand-made cases, including the case where one interval ends exactly when another starts.
   - **Placement:** each strategy on the layout of 6.3; `NoEnclosureAvailableError` when every enclosure refuses.
3. **Run the tests.**
   - From the command line: `python -m unittest discover -s tests -v`.
   - In PyCharm: use the green arrow and the test panel.
4. **Red, then green.** Deliberately break the `power_level` setter. Watch which tests turn red and read the failure messages. Then restore it.
5. **Optional.** Rewrite one test file with `pytest`: plain functions, fixtures, `pytest.raises`.

**Verify.** The final line is `OK` and the run reports at least 40 tests. No unit test opens a database connection or a file.

**Questions.**
1. `Creature._total_creatures` is shared by every test. Which test could become *order-dependent*, and how do you prevent it?
2. What did injecting `today` (5.2) and `clock` (5.7) bring you here?

**Files.** `tests/unit/test_*.py`

---

### Exercise 7.3 — Testing the service with fakes and mocks

**Context.** `MissionService` holds the most valuable logic of the project. Its dependencies are injected, so it can be tested **without any database**.

**Tasks.**

1. **`tests/unit/test_mission_service.py`.**
   - **Fixtures.** `setUp()` builds the in-memory repositories, a `NoTransaction`, a fixed clock (2026-03-15) and a `MagicMock(spec=EventBus)` as the publisher.
   - **Successful dispatch:**
     - check the **state**: the creature is no longer in the refuge, and the mission is stored with the right multiplier and due date;
     - check the **behaviour**: `publish` was called exactly once, with `MissionStarted(mission)`.
   - **One test per refusal path:** already on a mission, quarantine, in treatment, not certified, veterinarian, handler busy, unicorn too weak. Each test checks the exception message, that a `MissionRefused` event was published, and that **no** mission was stored.
   - **Recall:** on time, late (`days_late`), and without an open mission.
   - **The danger of a mock without `spec`.** Misspell `publish` in a test with `spec=` and observe the error, then without `spec=` and observe the silent pass.
2. **`tests/unit/test_listeners.py`.**
   - Test `NotificationListener` with a `MagicMock(spec=Notifier)`, checking the exact message with `assert_called_once_with`.
   - Test `AuditTrail` with a temporary file (`tempfile`).
3. **`tests/unit/test_connection.py`.** Test `DatabaseConnection` **without PostgreSQL**, using `@patch("refuge.db.connection.psycopg2.connect")`:
   - `__exit__` always closes the connection, and rolls back when an exception occurs;
   - `transaction()` commits on success, rolls back and re-raises on failure;
   - `cursor()` outside a `with` block raises `RuntimeError`.

**Verify.** All tests pass in under one second, and the suite still runs with PostgreSQL stopped.

**Questions.**
1. Why patch `refuge.db.connection.psycopg2.connect` and not `psycopg2.connect`? (Patch where the name is *used*.)
2. When do you prefer a *fake* (an in-memory repository) and when a *mock*?
3. Which tests check state, which check behaviour, and why does a good test often check both?

**Files.** `tests/unit/test_mission_service.py`, `tests/unit/test_listeners.py`, `tests/unit/test_connection.py`

---

### Exercise 7.4 — Integration tests against PostgreSQL

**Context.** Unit tests prove the logic. Only a real database proves the **wiring**: the SQL queries, the constraints, the mapping and the transactions.

**Tasks.**

1. **Test database.** Create a database `refuge_test` and add `TEST_DB_NAME=refuge_test` to `.env`. Integration tests are skipped when the variable is missing (`@unittest.skipUnless`).
2. **Fixtures.**
   - `setUpClass` opens a `DatabaseConnection(db_settings(dbname=...))`.
   - `setUp` replays `schema.sql` and `seed.sql` inside a transaction, so every test starts from the reference state.
   - `tearDownClass` closes the connection.
3. **`test_postgres_repositories.py`:**
   - a dragon goes through `add` then `get` and comes back intact, `element` included;
   - adding a duplicate name raises `psycopg2.errors.UniqueViolation`. Decide whether the repository should translate it into `ValidationError`, and justify your choice;
   - missions come back with the right `danger_multiplier`;
   - `latest_for` returns the most recent record.
4. **`test_mission_flow.py`:**
   - **Full dispatch:** after the call, query the tables directly and check that the mission exists and that `in_refuge` is `false`.
   - **Rollback scenario:** wrap the creature repository in a `FailingCreatureRepository` whose `update()` raises `RuntimeError`. The dispatch must fail, and the `missions` table must **still contain 9 rows**.
   - **Full recall:** check `returned_on`.

**Verify.** `python -m unittest discover -s tests -v` runs unit and integration tests. With the PostgreSQL server stopped, the integration tests are reported as *skipped*, never as *errors*.

**Questions.**
1. Unit test versus integration test: what does each one catch that the other misses?
2. Why reset the data before **every** test rather than once per class?
3. In the rollback scenario, what state is the Python creature object in after the failure? Link this to 5.7, question 2.

**Files.** `tests/integration/test_postgres_repositories.py`, `tests/integration/test_mission_flow.py`, `.env.example`

---

### ✅ Definition of done — running exercise

- [ ] `python -m refuge` covers `list`, `dispatch`, `recall` and `report`, with explicit error messages.
- [ ] All SQL lives in `repositories/postgres.py` and `sql/`, and every query is parameterised.
- [ ] Services import no concrete repository. Only `bootstrap.py` wires the concrete classes.
- [ ] No `print` outside `cli.py` and `ConsoleNotifier`. No `isinstance` used to branch on a type.
- [ ] `ruff`, `black --check` and `mypy` report zero findings.
- [ ] Unit tests pass without a database. Integration tests pass with `refuge_test`.
- [ ] `docs/design_notes.md` answers every *Questions* block. `docs/architecture.md` explains the layers, patterns and SOLID choices.
- [ ] Every exercise is committed separately.

---

## Pack A — Advanced SQL (after the final project)

> Optional exercises, to do **after** the final project. They run on the refuge database (reset it first; the expected results assume the reference dataset without the Kraken migration).
> Store the queries in `sql/queries/04_advanced.sql`. Some exercises ask you to port a query into a repository.

### A.1 — Subqueries and CTEs

1. **Above average.** Creatures whose power exceeds the average of **their own** species. Write a correlated subquery version and a CTE version, then compare their readability.
2. **`EXISTS`.** Creatures that have gone at least once to a destination with a multiplier of 3.0 or more.
3. **`NOT EXISTS`.** Rewrite "destinations never visited" (4.1) with `NOT EXISTS`, then compare with the anti-join and with `NOT IN`. What happens with `NOT IN` if the subquery returns a `NULL`?
4. **Scalar subquery.** Missions whose reward exceeds the average reward of all missions.

| Query | Expected result |
|---|---|
| 1 | Ember, Frostbite, Moonbeam |
| 2 | Frostbite, Ignis |
| 3 | Sunlit Valley |
| 4 | Frostbite 2100, Ignis 1800, Frostbite 1000 |

### A.2 — Window functions

1. **Latest health record** per creature, with `ROW_NUMBER() OVER (PARTITION BY ...)`. Keep the creatures without a record and show `no record` for them. Then rewrite the query with PostgreSQL's `DISTINCT ON` and compare.
2. **Ranking.** Rank the creatures by power **within** their species (`DENSE_RANK`). Then find the second highest power overall.
3. **Running total.** Cumulative reward ordered by departure date.
4. **Growth.** Month-over-month growth of the total reward, with `LAG`.
5. **Port to Python.**
   - Add `latest_for_all() -> dict[str, HealthRecord | None]` to `PostgresHealthRecordRepository`, using query 1. It replaces N calls to `latest_for` (the N+1 problem).
   - Add a `health` command to the CLI.

| Query | Expected result |
|---|---|
| 1 | 9 rows: Gorgo is `quarantine`, Moonbeam is `in_treatment`, Stardust is `healthy` (2026-03-05), Sylph is `no record`, all others `healthy` |
| 2 | Dragons: Frostbite 1, Ignis 2. Unicorns: Moonbeam 1, Stardust 2, Willow 3. Second highest overall: Gorgo (91) |
| 3 | The last row reaches 6460 |
| 4 | February +87.88 %, March +7.26 % |

### A.3 — Transactions and concurrency

1. **Race condition.** Open two psql sessions and run the same steps in both:
   - `BEGIN`;
   - read Ignis's `in_refuge` (both sessions see `true`);
   - insert a mission for Ignis with two different departure dates;
   - `UPDATE in_refuge`;
   - `COMMIT`.

   Ignis is now on two missions at once.
2. **Fix.** Replay the scenario with `SELECT ... FOR UPDATE` in the first step. What does the second session experience?
3. **Port to Python.** Add `get_for_update(name)` to the creature repository and use it in `dispatch`, inside the transaction.
4. **Isolation levels.** Demonstrate a *non-repeatable read* under `READ COMMITTED` (PostgreSQL's default), then show that `REPEATABLE READ` prevents it.
5. **`SAVEPOINT`.** In one transaction, insert three health records where the second one is invalid. Use `SAVEPOINT` and `ROLLBACK TO SAVEPOINT` to keep the first and third.

### A.4 — Indexes and `EXPLAIN ANALYZE`

1. **Generate data.** Insert 200,000 historical missions. Run `ANALYZE missions;` afterwards.

```sql
INSERT INTO missions (creature_id, handler_id, destination_id, departure_date, duration_days, base_reward, returned_on)
SELECT 1 + i % 9,
       (ARRAY[1, 2, 3, 6])[1 + i % 4],
       1 + i % 4,
       DATE '1960-01-01' + (i / 9),
       1 + i % 14,
       (i % 500) + 10,
       CASE WHEN i % 50 = 0 THEN NULL ELSE DATE '1960-01-01' + (i / 9) + 1 + i % 14 END
FROM generate_series(1, 200000) AS s(i);
```

2. **Measure.** Run `EXPLAIN ANALYZE` on two queries and note the plan (`Seq Scan`?) and the execution time:
   - the open missions of a handler (the query behind `list_open_for_handler`);
   - the number of missions per handler (4.2, query 4).
3. **Index.** Create an index on `missions(handler_id)`, then a **partial** index `ON missions(handler_id) WHERE returned_on IS NULL`. Measure again and explain which index the planner chooses for each query.
4. **Explain.**
   - Why does the `UNIQUE (creature_id, departure_date)` constraint already give you an index? For which queries is it useful (the leftmost-prefix rule)?
   - Why did no index make a difference with only 9 missions?

### A.5 — UPSERT and import

1. **SQL first.** Write `INSERT ... ON CONFLICT (name) DO UPDATE SET power_level = EXCLUDED.power_level` for a creature that already exists.
2. **Python repository.** Add `upsert(creature)` to `PostgresCreatureRepository`.
3. **Import script.** Write an import of a "scroll" file, with one line per creature in the format `name, species, origin, power_level`.
   - Each line is parsed into a dictionary and goes through `CreatureFactory`, so invalid lines are rejected by the Python validation.
   - Valid lines are upserted.
   - Everything runs in **one** transaction.

```
Talon, Griffin, Eagle Peaks, 84
Nimbus, Griffin, Storm Cliffs, 66
Blaze, Phoenix, Ashlands, 150
Mist, Unicorn, Fog Valley, 39
```

Expected output (format of your choice):

```
✔ Talon updated (power 84)
✔ Nimbus inserted
✘ line 3: power_level must be between 0 and 100, got 150.
✔ Mist inserted
Imported 3/4 lines.
```

4. **Question.** What would happen if an invalid line only failed in the database (for example a `CHECK` that Python does not know about)? How do `SAVEPOINT`s keep the other lines?

---

## Bonus exercises

> Optional, for fast finishers or to deepen a weak area. Keep them in `bonus/` so that the core project stays clean.

### B.1 — Shifts and scheduling

Create a `Shift` dataclass and a `shifts` table, each shift holding `employee_name`, `enclosure_name`, `start: datetime` and `end: datetime`. Then:
- detect, for each employee, every pair of overlapping shifts by reusing `find_overlapping_pairs` (5.7);
- write the SQL version with a self-join on `shifts`;
- bonus: use PostgreSQL's `tsrange` type and the `&&` operator;
- compare the complexity of the Python sweep with the SQL self-join.

### B.2 — Team missions and the knapsack

Some missions need **several** creatures:
- create the junction table `mission_creatures (mission_id, creature_id, role)`. A real many-to-many relationship!
- given a **risk budget** (each creature's risk = its power level ÷ 10, rounded up), choose the subset of available creatures that maximises the total power without exceeding the budget;
- implement the 0/1 knapsack with dynamic programming, and give its complexity O(n·W);
- compare with a greedy heuristic (best power/risk ratio first) on a counter-example where greedy fails.

### B.3 — Command and undo

Wrap `dispatch` and `recall` in `DispatchCommand` and `RecallCommand` objects with `execute()` and `undo()`, and keep a `CommandHistory` (a LIFO stack) with `undo_last()`.
- Undoing a dispatch must delete the mission and bring the creature back, in one transaction.
- What makes undoing a recall harder?

### B.4 — Incidents

Create an `Incident` dataclass (escape, injury, inter-species conflict) and an `IncidentReported` event published on the `EventBus` (6.2). Add a new listener that automatically creates a `quarantine` health record whenever a creature is involved in an injury.
- How many existing classes did you modify?

### B.5 — Self-registering species

Use `__init_subclass__` in `Creature` to register every subclass automatically in the factory registry.
- Adding a species then needs **zero** edits outside its own class (and the SQL migration).
- Discuss the trade-off: what becomes implicit, and what happens if a module is never imported?

---

## Appendix A — Fast-track brief (experienced developers)

> For learners who already master the basics: they receive the **whole specification at once** instead of the step-by-step path. The goal does not change: practise every topic and be able to **justify** every choice.

**Deliverable.** The repository of the [final project hierarchy](#final-project-hierarchy), meeting the [definition of done](#-definition-of-done--running-exercise).

**Rules.**
1. **Same contract.** Names, signatures and messages are the ones in the exercises: every *Verify* block must produce its expected output. You may choose your own path, but not change the contract.
2. **Tests first (TDD).** Turn each *Verify* block into a failing test before writing the code: red, green, refactor. Your test suite becomes your progress tracker.
3. **Questions are mandatory.** Experienced developers usually know *how*. The interview will check *why*. `docs/design_notes.md` must answer every *Questions* block.
4. **Checkpoints.** At the end of each theory chapter, show the trainer the corresponding part of your repository and discuss one design choice in 5 minutes.
5. **When you finish early**, in this order:
   - Pack A;
   - the bonus exercises related to your weak areas;
   - the [mirror milestones](#appendix-b--mirror-milestones-for-your-own-project) on your own project.

**Requirement summary by layer.**

| Layer | Requirements | Details in |
|---|---|---|
| Models | `Creature` ABC with encapsulation, template method and `to_dict`/`from_dict`. Five species plus `FlyingMixin`. `Employee` hierarchy. `Enclosure` container. `Mission` (manual eq/hash) and frozen `HealthRecord` dataclasses | 1.1 – 2.4, 5.1, 5.2, 5.4 |
| Database | Schema with every constraint of 3.1, reference seed, CRUD/JOIN/aggregate queries with the expected results | 3.1 – 4.2 |
| Data access | `DatabaseConnection` (context manager plus transaction), repository Protocols split per ISP, in-memory and PostgreSQL implementations, factories | 5.3 – 5.6, 6.4 |
| Business | `MissionService` (5 ordered rules, one transaction, injected clock), `EventBus` with listeners, placement strategies, reports | 5.7, 6.2 – 6.5 |
| Presentation | CLI with four commands, Facade, composition root, logging plus `log_call` | 7.1 |
| Quality | Unit tests (fakes plus mocks), integration tests with rollback scenario, zero findings from ruff, black and mypy | 6.5, 7.2 – 7.4 |

---

## Appendix B — Mirror milestones for your own project

> Your final project is built on **your own domain**. After each chapter, apply what you just practised to that domain. Use it when you finish early. Everyone can also use it as a head start for the final project.

| After chapter | Milestone on your own project | Output |
|---|---|---|
| 1 | Choose your domain and identify 3 to 5 core entities, with attributes and validation rules | One-page domain description |
| 2 | Find at least one real *is-a* hierarchy and one capability that suits a mixin or a Protocol. Check LSP | Class diagram (draft) |
| 3 | Design the schema: tables, keys, constraints, at least one many-to-many relationship | ER diagram plus `schema.sql` |
| 4 | Write five business questions your application must answer, then the SQL queries that answer them | `queries.sql` |
| 5 | Implement one repository (Protocol, in-memory and PostgreSQL) and one service with injected dependencies | First working vertical slice |
| 6 | Run the SOLID audit of 6.1 on your own design and list what you would change | Notes in your README |
| 7 | Set up the project structure, the logging and a first test for each layer | Skeleton ready for the final project |