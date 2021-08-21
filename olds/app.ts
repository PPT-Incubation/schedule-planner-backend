import {opine, Router, json, urlencoded} from "https://deno.land/x/opine@1.3.2/mod.ts"
import db from './db.ts'

import {
    addMatkul,
    getMatkul
} from './controller/matakuliah.ts'

import{
    getJadwal,
    addJadwal,
    editJadwal,
    deleteJadwal
} from './controller/jadwal.ts'

const app = opine()
const router = Router()
const PORT = 3000

app.use(json())
app.use(urlencoded())

router
    .route("/api/list-matkul")
    .get(getMatkul)
    .post(addMatkul)

router
    .get("/api/list-jadwal", getJadwal)
    .post("/api/insert-jadwal", addJadwal)
    .put("/api/edit-jadwal", editJadwal)
    .delete("/api/delete-jadwal", deleteJadwal)

app.use(router)


const schedules = db.collection ("schedules")

// mongo module bug, still have to use @ts-ignore and set noCursorTimeout:false for find data
app.get("/jadwal", async (req,res) => {
    // @ts-ignore
    const jadwal = await schedules.find({semester:6}, {noCursorTimeout:false}).toArray()
    console.log(jadwal)
    res.send(jadwal)
})

app.get('/', function (req,res){
    res.send("Hello Deno")
})

app.listen(PORT)
console.log("Opine started on port 3000")