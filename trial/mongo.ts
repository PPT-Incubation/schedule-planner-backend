import { MongoClient } from "https://deno.land/x/mongo@v0.22.0/mod.ts";

const client = new MongoClient();

// @ts-ignore
await client.connect("mongodb://127.0.0.1:27017");
const db = client.database("schedule-planner");
const schedules = db.collection("schedules");


schedules.insertOne({
  matkul: "PBKK",
  dosen: "Pak Fajar",
  sks: 3,
}).then((success) => {
  console.log(success);
}).catch((error) => {
  console.log(error);
});

// @ts-ignore
const jadwal = await schedules.find({}, { noCursorTimeout: false }).toArray();
console.log(jadwal);

// try {
//   const connectionResult = await client.connect({
//     db: "schedule-planner",
//     // mongodb+srv://ppt:parapencarituhan@cluster0.m5kxu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
//     tls: true,
//     servers: [
//       {
//         // host: "cluster0-shard-00-01.m5kxu.mongodb.net",
//         host: "localhost",
//         port: 27017,
//       }
//     ],
//     credential: {
//       username: "ppt",
//       password: "parapencarituhan",
//       db: "schedule-planner",
//       mechanism: "SCRAM-SHA-1"
//     }
//   });

//   const db = client.database("schedule-planner");
//   const schedules = db.collection ("schedules");

//   schedules.insertOne({
//       matkul: "PBKK",
//       dosen: "Pak Fajar",
//       sks : 3,
//   }).then((success) => {
//     console.log(success);
//   }).catch((error) => {
//     console.log(error);
//   });

//   // @ts-ignore
//   const jadwal = await schedules.findOne({ semester:6 }, { noCursorTimeout:false });
//   console.log(jadwal);

// } catch (e){
//   console.log(e);
// }
