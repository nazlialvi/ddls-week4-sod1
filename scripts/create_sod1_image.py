"""Create a static pLDDT-colored SOD1 image from the supplied mmCIF."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from biotite.structure.io.pdbx import CIFFile, get_structure

INPUT = Path("data/SOD1_alphafold_model.cif")
OUTPUT = Path("results/sod1_structure_colored.png")

cif = CIFFile.read(str(INPUT))
structure = get_structure(cif, model=1)
ca = structure[(structure.chain_id == "A") & (structure.atom_name == "CA")]
if len(ca) != 154:
    raise ValueError(f"Expected 154 chain-A CA atoms, found {len(ca)}")

# The supplied mmCIF stores pLDDT in _atom_site.B_iso_or_equiv. Biotite's
# generic AtomArray does not expose that field, so read it from the atom_site loop.
block = next(iter(cif.values()))
headers = [line.strip() for line in INPUT.read_text().splitlines() if line.startswith("_atom_site.")]
idx = {h.split(".", 1)[1]: i for i, h in enumerate(headers)}
ca_plddt = []
for line in INPUT.read_text().splitlines():
    if not line.startswith("ATOM"):
        continue
    p = line.split()
    if p[idx["label_atom_id"]] == "CA" and p[idx["label_asym_id"]] == "A":
        ca_plddt.append(float(p[idx["B_iso_or_equiv"]]))
plddt = np.asarray(ca_plddt)
if len(plddt) != len(ca):
    raise ValueError("pLDDT and CA residue counts do not match")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
fig = plt.figure(figsize=(10, 8), dpi=180)
ax = fig.add_subplot(111, projection="3d")
ax.plot(ca.coord[:, 0], ca.coord[:, 1], ca.coord[:, 2], color="#777777", linewidth=1.0, alpha=0.35)
sc = ax.scatter(ca.coord[:, 0], ca.coord[:, 1], ca.coord[:, 2], c=plddt, cmap="coolwarm", vmin=70, vmax=100, s=32, depthshade=True)
ax.scatter(*ca.coord[0], c="#3050f8", s=65, edgecolors="black", linewidths=.5)
ax.text(*ca.coord[0], "  Met1", fontsize=8)
ax.set_title("Human SOD1 AlphaFold monomer — pLDDT by residue", pad=16)
ax.set_xlabel("X (Å)"); ax.set_ylabel("Y (Å)"); ax.set_zlabel("Z (Å)")
ax.set_box_aspect(np.ptp(ca.coord, axis=0))
ax.view_init(elev=20, azim=35)
cb = fig.colorbar(sc, ax=ax, shrink=.7, pad=.08)
cb.set_label("pLDDT confidence")
fig.text(.5, .02, "Chain A · 154 residues · pLDDT in mmCIF B-factor column · monomer only", ha="center", fontsize=9)
fig.tight_layout(rect=(0, .04, 1, 1))
fig.savefig(OUTPUT, bbox_inches="tight")
plt.close(fig)
print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes); residues={len(ca)}, pLDDT={plddt.min():.2f}-{plddt.max():.2f}")
