DROP EXTENSION IF EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE "farms" (
  "name" varchar,
  "boundary" geometry,
  "id" uuid DEFAULT uuid_generate_v1 ()
);

CREATE TABLE "robots" (
  "name" varchar,
  "location" geometry,
  "farm_id" uuid,
  "id" uuid DEFAULT uuid_generate_v1 ()
);

INSERT INTO farms (name, boundary) VALUES (
    'Carzalia Produce',
    ST_GeometryFromText('POLYGON((50.6373 3.0750,50.6374 3.0750,50.6374 3.0749,50.63 3.07491,50.6373 3.0750))')
);

-- PostgREST uses schemas to abstract the API interface from the implementation.
-- At the beginning, the API will be close to the core tables.
CREATE SCHEMA api;

-- ... very close
CREATE VIEW api.farms AS
SELECT * from farms
;

create role api_user nologin;
grant api_user to authenticator;

grant usage on schema api to api_user;
grant all on api.farms to api_user;

ALTER TABLE "robots" ADD FOREIGN KEY ("farm_id") REFERENCES "farms" ("id");

-- UUID IDs are not sequential
-- grant usage, select on sequence api.farm to todo_user;

/*
CREATE TABLE "plots" (
  "boundary" POLYGON,
  "name" varchar,
  "farm_id" int,
  "id" int
);

CREATE TABLE "tasks" (
  "action_type_id" int,
  "plot_id" int,
  "robot_id" UUID,
  "status" int
);

CREATE TABLE "action_types" (
  "name" varchar,
  "id" int
);

CREATE TABLE "task_statuses" (
  "name" varchar,
  "id" int
);

CREATE TABLE "robot_statuses" (
  "robot_id" int,
  "status_time" datetime,
  "status_data" varchar,
  "id" int
);

ALTER TABLE "robots" ADD FOREIGN KEY ("owner_farm_id") REFERENCES "farms" ("id");

ALTER TABLE "plots" ADD FOREIGN KEY ("farm_id") REFERENCES "farms" ("id");

ALTER TABLE "tasks" ADD FOREIGN KEY ("action_type_id") REFERENCES "action_types" ("id");

ALTER TABLE "tasks" ADD FOREIGN KEY ("plot_id") REFERENCES "plots" ("id");

ALTER TABLE "tasks" ADD FOREIGN KEY ("robot_id") REFERENCES "robots" ("id");

ALTER TABLE "tasks" ADD FOREIGN KEY ("status") REFERENCES "task_statuses" ("id");

ALTER TABLE "robot_statuses" ADD FOREIGN KEY ("robot_id") REFERENCES "robots" ("id");

 */
