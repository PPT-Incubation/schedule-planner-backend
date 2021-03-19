import { Request, Response, NextFunction } from "https://deno.land/x/opine@1.2.0/mod.ts"
import db from '../db.ts'

const jadwal = db.collection ("schedules")

interface Jadwal{
    nama : string
    kelas : string
    waktu : string
    ruang : string
}

interface DataJadwal{
    nrp : string
    judul : string
    listJadwal : Jadwal[]
}

export const addJadwal = async (req:Request, res:Response) => {
    const data: DataJadwal = await req.body
    try {
        jadwal.insertOne(data)
        res.json({
            body : "Success add new jadwal",
            status : 201
        })
    } catch (error) {
        console.log(error)
        res.json({
            body : "Failed insert new data",
            status : 500
        })
    }
}

export const getJadwal = async (req:Request, res:Response) => {
    // @ts-ignore
    const data: DataJadwal[] = await jadwal.find( {},  { noCursorTimeout:false }).toArray()
    console.log(data)
    res.json({
        body: data,
        status: data.length > 0 ? "Success found "+data.length.toString()+" data": "No data Found"
    })
}

export const editJadwal = async (req:Request, res:Response) => {
    res.json({
        body : "Soon to be implemented"
    })
}

export const deleteJadwal = async (req:Request, res:Response) => {
    res.json({
        body : "Soon to be implemented"
    })
}