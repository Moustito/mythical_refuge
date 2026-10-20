# Design notes — Exercise 2.3

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


## Exercise 2.4 : questions kept for chapter 6

### Aldric becomes a veterinarian too
- A: combined class (HandlerVeterinarian): combinatorial explosion, incompatible __init__,
  ROLE/PERMISSIONS conflicts, describe_duties collision.
- B: capability mixin: role still fixed at class definition, permissions merged by hand.
- C: everything in Employee: bloated base class, methods that mostly refuse.
- D: Handler inherits Veterinarian: fails the is-a test.
- Root issue: inheritance expresses "is", but a degree is something a person "has", acquired later.

### can_escort() on Employee
- LSP: respected (returns a bool, default is not an invariant), but Handler needs creature.power_level.
- Design smell: the base class knows a capability of one subclass; it duplicates can("escort_mission").
- Fix to explore in chapter 6: move the capability out of Employee (mixin / Protocol / composition).