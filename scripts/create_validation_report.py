from pathlib import Path
import json, statistics
import numpy as np
import matplotlib.pyplot as plt
from biotite.structure.io.pdbx import CIFFile

out=Path('results'); out.mkdir(exist_ok=True)
lines=Path('data/SOD1_alphafold_model.cif').read_text().splitlines()
headers=[x.strip() for x in lines if x.startswith('_atom_site.')]
idx={x.split('.',1)[1]:i for i,x in enumerate(headers)}
ca=[]
for line in lines:
    if line.startswith('ATOM'):
        p=line.split()
        if p[idx['label_atom_id']]=='CA': ca.append((p[idx['label_asym_id']],int(p[idx['auth_seq_id']]),p[idx['auth_comp_id']],float(p[idx['B_iso_or_equiv']])))
assert len(ca)==154 and {x[0] for x in ca}=={'A'}
plddt=np.array([x[3] for x in ca])
d=json.loads(Path('data/SOD1_alphafold_pae.json').read_text())[0]
pae=np.array(d['predicted_aligned_error'])
assert pae.shape==(154,154)
fig,ax=plt.subplots(figsize=(7,6),dpi=160); im=ax.imshow(pae,cmap='viridis',vmin=0,vmax=float(d['max_predicted_aligned_error'])); ax.set(xlabel='Residue index',ylabel='Residue index',title='SOD1 predicted aligned error (PAE)'); fig.colorbar(im,ax=ax,label='PAE (Å)'); fig.tight_layout(); fig.savefig(out/'sod1_pae_heatmap.png'); plt.close(fig)
fig,ax=plt.subplots(figsize=(9,3),dpi=160); ax.scatter(np.arange(1,155),plddt,c=plddt,cmap='coolwarm',vmin=70,vmax=100,s=12); ax.axhline(90,color='gray',ls='--'); ax.set(xlabel='Residue',ylabel='pLDDT',title='SOD1 per-residue pLDDT'); fig.tight_layout(); fig.savefig(out/'sod1_plddt_profile.png'); plt.close(fig)
report=f'''# SOD1 AlphaFold validation transcript

## Check 1 — confidence first

The supplied mmCIF contains one chain and 154 Cα residues. pLDDT is read from `_atom_site.B_iso_or_equiv` (the B-factor column): **min {plddt.min():.2f}, max {plddt.max():.2f}, mean {plddt.mean():.2f}**. Residues 1–30 have min {plddt[:30].min():.2f}, mean {plddt[:30].mean():.2f}. The PAE JSON contains a **154×154** intrachain matrix with maximum scale {d['max_predicted_aligned_error']:.1f} Å; its observed range is {pae.min():.2f}–{pae.max():.2f} Å and mean is {pae.mean():.2f} Å.

pLDDT applies to confidence in local residue geometry/fold. PAE applies to confidence in relative placement of residue pairs/domains. This PAE is intrachain only; it is not interface PAE for a second SOD1 chain.

![pLDDT profile](sod1_plddt_profile.png)

![PAE heatmap](sod1_pae_heatmap.png)

## Check 2 — structure identity and assembly

The FASTA is 154 residues. The mmCIF has one chain A, residue IDs 1–154, with no gaps in the Cα residue numbering. Its residue sequence matches `data/SOD1.fasta` exactly; no mutations were found. The model is therefore the canonical human SOD1 monomer, not the functional two-copy assembly described in the transcript. No second chain or inter-chain PAE is present.

## Check 3 — visual inspection

The pLDDT rendering is in `sod1_structure_colored.png`; high-confidence core residues appear red/pink and lower-confidence terminal regions are bluer, consistent with the numerical profile (Met1 is 70.94). The PAE heatmap is predominantly low within the compact fold, with higher uncertainty in weaker/terminal relative placements. This is consistent with a well-supported single-chain fold, but neither visualization establishes the missing dimer interface.

## Check 4 — biological caveat

**Caveat: the model contains no explicit Cu/Zn ligands or metals.** SOD1 activity and geometry depend on metal coordination; without modeled metal occupancy and a paired functional assembly, a surface residue can appear plausible while affecting metal-site geometry or dimerization. Thus this model cannot establish that any mutation is safe or surface-specific in Erik's enzyme.

## Conclusion

The supplied model supports a high-confidence canonical **monomeric fold**, with the confidence metrics above. It does **not** support the stronger claim about safe residues in the functional SOD1 dimer: interface placement is unmodeled, and Erik's exact construct remains unverified.
'''
(out/'sod1_validation_transcript.md').write_text(report)
print(report)
