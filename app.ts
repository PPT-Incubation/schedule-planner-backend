import opine from "https://deno.land/x/opine@1.2.0/mod.ts";
const app = opine();

app.get("/", function (req,res){
    res.send("Hello Deno");
});

app.listen(3000);
console.log("Opine started on port 3000");