import {opine} from "https://deno.land/x/opine@1.2.0/mod.ts";
import db from './db.ts';

const app = opine();
const PORT = 3000;

const schedules = db.collection ("schedules");

// mongo module bug, still have to use @ts-ignore and set noCursorTimeout:false for find data
app.get("/jadwal", async (req,res) => {
    // @ts-ignore
    const jadwal = await schedules.find({semester:6}, {noCursorTimeout:false}).toArray();
    console.log(jadwal);
    res.send(jadwal);
});

app.get('/', function (req,res){
    res.send("Hello Deno");
});

app.listen(PORT);
console.log("Opine started on port 3000");