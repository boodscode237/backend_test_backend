CREATE TABLE "nanoparticle" (
  "id" serial PRIMARY KEY,
  "np_str" text,
  "size" float,
  "article_id" integer,
  "mat_id" integer,
  "mep_id" integer,
  "user_id" integer
);

CREATE TABLE "synthesis" (
  "id" serial PRIMARY KEY,
  "np_id" integer,
  "method" text,
  "article_id" integer,
  FOREIGN KEY ("np_id") REFERENCES "nanoparticle" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "NOVA" (
  "id" serial PRIMARY KEY,
  "np_id" integer,
  "method" text,
  "absorbat" text,
  "pore_size" float,
  "density" float,
  "ads_desorb_curve" text,
  "pore_distr_curve" text,
  FOREIGN KEY ("np_id") REFERENCES "nanoparticle" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "material" (
  "mat_id" serial PRIMARY KEY,
  "name" text,
  "synonyms" text,
  "chem_form" text,
  "cas_num" text
);

CREATE TABLE "user" (
  "id" serial PRIMARY KEY,
  "name" text,
  "email" text
);

ALTER TABLE "nanoparticle" ADD FOREIGN KEY ("mat_id") REFERENCES "material" ("mat_id");
ALTER TABLE "nanoparticle" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");
