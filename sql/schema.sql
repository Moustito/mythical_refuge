CREATE TYPE "species_enum" AS ENUM (
  'Dragon',
  'Phoenix',
  'Unicorn',
  'Griffin',
  'Basilisk'
);

CREATE TYPE "employee_role" AS ENUM (
  'handler',
  'veterinarian'
);

CREATE TYPE "health_status" AS ENUM (
  'healthy',
  'under_observation',
  'in_treatment',
  'quarantine'
);

CREATE TABLE "enclosures" (
  "id" serial PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "capacity" integer NOT NULL,
  CONSTRAINT "enclosures_capacity_positive" CHECK (capacity > 0)
);

CREATE TABLE "creatures" (
  "id" serial PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "species" species_enum NOT NULL,
  "origin" varchar NOT NULL,
  "power_level" integer NOT NULL,
  "element" varchar,
  "resurrection_count" integer NOT NULL DEFAULT 0,
  "in_refuge" boolean NOT NULL DEFAULT true,
  "enclosure_id" integer,
  "registered_at" timestamptz NOT NULL DEFAULT (now()),
  CONSTRAINT "creatures_power_level_range" CHECK (power_level BETWEEN 0 AND 100),
  CONSTRAINT "creatures_resurrection_count_positive" CHECK (resurrection_count >= 0),
  CONSTRAINT "creatures_element_dragons_only" CHECK (element IS NULL OR species = 'Dragon')
);

CREATE TABLE "employees" (
  "id" serial PRIMARY KEY,
  "full_name" varchar UNIQUE NOT NULL,
  "email" varchar UNIQUE NOT NULL,
  "role" employee_role NOT NULL,
  "certification_level" integer,
  "supervisor_id" integer,
  "hired_on" date NOT NULL DEFAULT (current_date),
  CONSTRAINT "employees_handler_requires_certification" CHECK (role <> 'handler' OR certification_level IS NOT NULL),
  CONSTRAINT "employees_certification_range" CHECK (certification_level IS NULL OR certification_level BETWEEN 1 AND 5)
);

CREATE TABLE "destinations" (
  "id" serial PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "danger_multiplier" numeric(3,1) NOT NULL DEFAULT 1,
  CONSTRAINT "destinations_danger_multiplier_min" CHECK (danger_multiplier >= 1.0)
);

CREATE TABLE "missions" (
  "id" serial PRIMARY KEY,
  "creature_id" integer NOT NULL,
  "handler_id" integer NOT NULL,
  "destination_id" integer NOT NULL,
  "departure_date" date NOT NULL,
  "duration_days" integer NOT NULL,
  "base_reward" numeric(10,2) NOT NULL,
  "returned_on" date,
  "notes" text NOT NULL DEFAULT '',
  CONSTRAINT "missions_duration_positive" CHECK (duration_days > 0),
  CONSTRAINT "missions_reward_positive" CHECK (base_reward >= 0),
  CONSTRAINT "missions_return_after_departure" CHECK (returned_on IS NULL OR returned_on >= departure_date)
);

CREATE TABLE "health_records" (
  "id" serial PRIMARY KEY,
  "creature_id" integer NOT NULL,
  "vet_id" integer NOT NULL,
  "examined_on" date NOT NULL DEFAULT (current_date),
  "status" health_status NOT NULL,
  "diagnosis" text NOT NULL,
  "treatment" text NOT NULL DEFAULT ''
);

CREATE UNIQUE INDEX "missions_one_departure_per_day" ON "missions" ("creature_id", "departure_date");

COMMENT ON COLUMN "creatures"."element" IS 'Dragons only, NULL for every other species';

COMMENT ON COLUMN "creatures"."enclosure_id" IS 'Optional: not housed yet';

COMMENT ON COLUMN "employees"."full_name" IS 'Unique: a simplification';

COMMENT ON COLUMN "employees"."certification_level" IS '1 to 5, handlers only';

COMMENT ON COLUMN "employees"."supervisor_id" IS 'Optional: another employee';

COMMENT ON COLUMN "missions"."returned_on" IS 'NULL while the mission is ongoing';

ALTER TABLE "creatures" ADD FOREIGN KEY ("enclosure_id") REFERENCES "enclosures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "employees" ADD FOREIGN KEY ("supervisor_id") REFERENCES "employees" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "missions" ADD FOREIGN KEY ("creature_id") REFERENCES "creatures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "missions" ADD FOREIGN KEY ("handler_id") REFERENCES "employees" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "missions" ADD FOREIGN KEY ("destination_id") REFERENCES "destinations" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "health_records" ADD FOREIGN KEY ("creature_id") REFERENCES "creatures" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "health_records" ADD FOREIGN KEY ("vet_id") REFERENCES "employees" ("id") DEFERRABLE INITIALLY IMMEDIATE;
