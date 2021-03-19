import { MongoClient } from "https://deno.land/x/mongo@v0.21.0/mod.ts"

const client = new MongoClient()

await client.connect({
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
})

const db = client.database("schedule-planner")

export default db