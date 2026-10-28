# — Design notes — 

# Exercise 2.3

## Why StatueDragon breaks the LSP
- `special_ability()` raises `NotImplementedError`: the parent contract promises a `str`.
- `mission_duration_days()` still says 14 days for an object that can never leave.
- A statue is not a dragon (is-a test fails): it has no ability, no mission, no power.
- The `refusal_reason()` override alone is legal (refusals are in the contract),
  but it does not fix the other violations.

## Corrected design
- `Decoration`: an exhibited object (name, description). No abilities.
- `Statue(Decoration)`: a stone decoration; it *depicts* a species (composition, not inheritance).
- `Creature` and its subclasses: living residents only.
- `Reportable` (Protocol): anything with `name`, `special_ability()`, `mission_duration_days()`.

## Duck typing
- `RoboticGuard` has no parent but works in the report: only the methods used matter.
- Inheritance is for sharing code and enforcing a contract, not for interchangeability.
- With `list[Creature]`, mypy rejects `RoboticGuard`; `Sequence[Reportable]` accepts it.


# Exercise 2.4 : questions kept for chapter 6

## Aldric becomes a veterinarian too
- A: combined class (HandlerVeterinarian): combinatorial explosion, incompatible __init__,
  ROLE/PERMISSIONS conflicts, describe_duties collision.
- B: capability mixin: role still fixed at class definition, permissions merged by hand.
- C: everything in Employee: bloated base class, methods that mostly refuse.
- D: Handler inherits Veterinarian: fails the is-a test.
- Root issue: inheritance expresses "is", but a degree is something a person "has", acquired later.

## can_escort() on Employee
- LSP: respected (returns a bool, default is not an invariant), but Handler needs creature.power_level.
- Design smell: the base class knows a capability of one subclass; it duplicates can("escort_mission").
- Fix to explore in chapter 6: move the capability out of Employee (mixin / Protocol / composition).

# Chapter 3: Relational Databases

## 1. Python ↔ SQL Mapping (Task 3.4)

| Python Concept | SQL Equivalent / Implementation |
| :--- | :--- |
| **A class** | A **Table** (e.g., `creatures`, `employees`) |
| **An attribute** | A **Column** (e.g., `name`, `power_level`) |
| **A validation in a setter** | A **`CHECK` constraint** or `NOT NULL` constraint at the database level |
| **The `Creature` subclasses** | A **Single Table Inheritance** pattern using a `species` discriminator column combined with conditional check constraints (e.g., `CHECK (species = 'Dragon' OR element IS NULL)`) |
| **The Employee subclasses** | A single table (`employees`) using a `role` discriminator column (`handler` or `veterinarian`) with conditional constraints (e.g., certification level required only for handlers) |
| **An Enclosure holding creatures** | A **Foreign Key relationship** (`enclosure_id`) in the `creatures` table referencing `enclosures(id)` with an `ON DELETE SET NULL` behavior |

---

## 2. Answers to Exercise 3.1 Questions

### 1. Class Hierarchy Inheritance in SQL
* **The three classic ways:** Single Table Inheritance (all subclasses in one table with nullable columns), Class Table Inheritance (one table per class joined by foreign keys), and Concrete Table Inheritance (one separate table per subclass containing all attributes).
* **Chosen approach for creatures:** **Single Table Inheritance**.
* **Trade-off:** It is simple to query and avoids costly `JOIN` operations, but it results in sparse tables with nullable columns that do not natively apply exclusively to certain subclasses (requiring `CHECK` constraints to enforce rules like "only dragons have an element").

### 2. Junction Tables and Relationships
* **Junction table:** While the schema handles many-to-one and simple references, tables like `missions` act as relationship managers linking creatures, handlers, and destinations.
* **Data living on the relationship:** Attributes specific to the interaction itself rather than the entities alone, such as `departure_date`, `duration_days`, `base_reward`, `returned_on`, and `notes`.

### 3. Fragility of `full_name` as a Natural Key
* **Why it's fragile:** Names are prone to typos, duplication (homonyms), and legal changes (such as marriage or renaming). 
* **Real-world alternative:** A surrogate key (an auto-incrementing integer `id` or a `UUID`) combined with a unique corporate email or employee ID code.

### 4. `NUMERIC` vs `FLOAT` for Money
* **Why NUMERIC:** `FLOAT` uses approximate binary floating-point representation, which introduces minor rounding inaccuracies unacceptable in financial calculations. `NUMERIC` guarantees exact precision for decimal numbers.
* **Matching Python type:** `decimal.Decimal` from the built-in `decimal` module.

### 5. Redundant Validation (Python and Database)
* **Why keep both:** Defense in depth. While Python validates data on application input, other sources (such as direct administrative scripts, database migrations, backup restorations, or other client applications) may write directly to the database. The database serves as the final, immutable guardian of data integrity.

### 6. Danger Multiplier in a Table
* **Why store it in a table:** It separates configuration and reference data from application code. This allows multipliers to be updated, added, or audited dynamically without modifying or redeploying the Python codebase.

---

## 3. Answers to Exercise 3.2 Questions

### 1. Difference between DELETE, TRUNCATE, and DROP
* **`DELETE`:** Removes specific rows based on a `WHERE` clause, triggers row-level actions, logs operations, and can be rolled back.
* **`TRUNCATE`:** Rapidly empties an entire table by clearing its data pages without scanning rows, resetting identity sequences efficiently.
* **`DROP`:** Completely destroys the table structure, its schema, constraints, and all associated data from the database.

### 2. Value of RETURNING in Python
* The `RETURNING` clause allows PostgreSQL to send back generated surrogate primary keys (like auto-incremented `id`s) or updated default values immediately in a single database round-trip, making it straightforward to synchronize newly created Python object instances with the database.

### 3. Lessons Learned from Transactions (Step 4)
* Running an unconstrained update inside a transaction highlights the absolute necessity of **atomicity and safety checks**. Transactions prevent accidental partial failures from corrupting persistent storage, and `ROLLBACK` provides an essential safety net to undo unintended mass modifications instantly.

---

## 4. Constraint Violation Error Messages (Exercise 3.2, Step 3)

1. **Power level of 150:**
   `ERROR: new row for relation "creatures" violates check constraint "creatures_power_level_check"`
2. **Duplicate creature name:**
   `ERROR: duplicate key value violates unique constraint "creatures_name_key"`
3. **Unicorn with an element:**
   `ERROR: new row for relation "creatures" violates check constraint "chk_dragon_element"`
4. **Mission lasting 0 days:**
   `ERROR: new row for relation "missions" violates check constraint "missions_duration_days_check"`
5. **Health status 'sick':**
   `ERROR: new row for relation "health_records" violates check constraint "health_records_status_check"`
6. **Handler without a certification level:**
   `ERROR: new row for relation "employees" violates check constraint "chk_handler_certification"`
7. **Two missions for the same creature on the same day:**
   `ERROR: duplicate key value violates unique constraint "unique_creature_departure"`