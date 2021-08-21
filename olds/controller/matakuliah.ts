import { Request, Response, NextFunction } from "https://deno.land/x/opine@1.3.2/mod.ts"
import db from '../db.ts'

const matkul = db.collection ("mata-kuliah")
// const schedules = db.collection ("schedules")

interface Context{
    req:Request,
    res:Response,
    next:NextFunction,
}

// Interface for mata kuliah
interface Matkul{
    nama : string
    kelas : string
    sks : number
    waktu : string       // also can use Date interface, use string for now
    ruangan : string
    dosen : string      // consider make Dosen interface for team teaching system
}

interface Semester{
    semester: number
    listMatkul : Matkul
}

export const addMatkul = async (req:Request, res:Response) => {
    const data = await req.body
    console.log(req.body)
    res.json({
        status : "success"
    })
    // console.log(body)
}

export const getMatkul = async (req:Request, res:Response) => {
    // @ts-ignore
    const data: Semester[] = await matkul.find( {},  { noCursorTimeout:false }).toArray()
    console.log(data)
    res.json({
        body: data,
        status: data.length > 0 ? "Success found "+data.length.toString()+" data": "No data Found"
    })
}

