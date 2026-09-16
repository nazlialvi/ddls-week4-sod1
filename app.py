from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse

ROOT = Path(__file__).parent
RESULTS = ROOT / "results"
DATA = ROOT / "data"
app = FastAPI(title="SOD1 validation viewer")

@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse((ROOT / "index.html").read_text())

@app.get("/api/results")
def results():
    return JSONResponse(json.loads((RESULTS / "results.json").read_text()))

@app.get("/api/pae")
def pae():
    return JSONResponse(json.loads((DATA / "SOD1_alphafold_pae.json").read_text()))

@app.get("/structure/{name}")
def structure(name: str):
    if name not in {"SOD1_alphafold_model.cif", "SOD1.fasta"}:
        raise HTTPException(404, "Structure not found")
    path = DATA / name
    return FileResponse(path, media_type="chemical/x-cif" if name.endswith(".cif") else "text/plain")
