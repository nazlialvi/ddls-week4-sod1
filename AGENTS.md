# AGENTS.md

## Operating instructions

- Use `uv` for the Python environment: create it with `uv venv` and run all Python with `uv run`. Do not rely on a system Python installation.
- Treat the interview transcript and supplied data files as the source of truth. Do not infer missing construct, paired-structure, accessibility, or experimental information.

## Data

- Inputs are in `data/`:
  - `SOD1.fasta`: supplied 154-residue human SOD1 sequence (UniProt P00441).
  - `SOD1_alphafold_model.cif`: AlphaFold prediction for one 154-residue chain. The mmCIF stores per-residue pLDDT in the B-factor column (`_atom_site.B_iso_or_equiv`).
  - `SOD1_alphafold_pae.json`: accompanying pairwise-error/confidence matrix (PAE). It describes the modeled single chain and does not validate contacts to a missing second chain.
- Load the structure from the mmCIF, preserving chain and residue numbering. Read pLDDT from the B-factor column and PAE from the JSON. Verify the sequence-to-structure mapping before joining values.
- The functional SOD1 enzyme is described as two identical copies, but the supplied CIF contains only one chain. Do not call a residue safe or free in the functional assembly from this CIF alone.
- The files describe the supplied canonical sequence, not necessarily Erik's bench construct. Obtain and verify the construct sequence/map before treating residue numbers as ordering-ready.

## Outputs

- Write generated analyses, tables, plots, and other deliverables under `results/`.
- Preserve input files unchanged and retain an audit trail of mappings, settings, exclusions, and assumptions.

## Folding sequences not in the AlphaFold DB

- Read and follow the course fold-service instructions at `https://ddls-structure-api-8a7d6803.svc.hypha.aicell.io/skill.md` before folding a sequence that is not in the AlphaFold DB.
- The fold key is stored in the untracked `DDLS_FOLD_KEY` variable in `.env`. Load it with `set -a; source .env; set +a`, then send it as the Bearer token required by the service. Never print, commit, or write the key into this file or any other committed file.

## Version control

- This folder is a git repository. Commit the current state before any big change.
- Commit again whenever something starts working, using short, clear messages.
- Never commit secrets; `.env` is ignored.

## Confidence and reporting rule

Never report an answer about a structure without first reporting the confidence that matches the claim and confirming that the model is actually this protein. For a fold or region claim, report per-residue pLDDT. For a claim about how parts sit together or an interface, report PAE/interface evidence and distinguish the supplied one-chain evidence from the unmodeled SOD1 dimer. The overall reported ~98 score is not a substitute for local evidence.
