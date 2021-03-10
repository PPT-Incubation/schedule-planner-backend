import { MongoClient } from "https://deno.land/x/mongo@v0.21.0/mod.ts";

const client = new MongoClient();
await client.connect("mongodb://localhost:27017");

const db = client.database("schedule-planner");
const schedules = db.collection ("schedules");

const insertId = await schedules.insertOne({
    matkul: "Data Mining",
    dosen: "Bu Dini",
    sks : 3,
  });
