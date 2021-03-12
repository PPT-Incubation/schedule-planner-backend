import { MongoClient } from "https://deno.land/x/mongo@v0.21.0/mod.ts";

const client = new MongoClient();
// await client.connect("mongodb://localhost:27017");

try {
  const connectionResult = await client.connect({
    db: "schedule-planner",
    // mongodb+srv://ppt:parapencarituhan@cluster0.m5kxu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    tls: true,
    servers: [
      {
        host: "cluster0-shard-00-01.m5kxu.mongodb.net",
        port: 27017,
      }
    ],
    credential: {
      username: "ppt",
      password: "parapencarituhan",
      db: "schedule-planner",
      mechanism: "SCRAM-SHA-1"
    }
  });

  const db = client.database("schedule-planner");
  const schedules = db.collection ("schedules");

  schedules.insertOne({
      matkul: "Data Mining",
      dosen: "Bu Dini",
      sks : 3,
  }).then((success) => {
    console.log(success);
  }).catch((error) => {
    console.log(error);
  });
  
  // @ts-ignore
  const jadwal = await schedules.findOne({ semester:6 }, { noCursorTimeout:false });
  console.log(jadwal);
  
} catch (e){
  console.log(e);
}
