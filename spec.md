# Specification

## Decision

Provide Dr. Lena Brandt/Dr. Erik Lindström with a defensible ranked shortlist of at most two or three SOD1 positions for surface-mutagenesis testing, or explicitly report **no defensible candidate**. The intended effect is to disrupt SOD1 activity without simply disrupting metal coordination, folding, pairing, or aggregation. The requested delivery is Friday, 18 September 2026, at 09:00 Europe/Stockholm, but the shortlist is not ready for ordering while the stated blockers remain unresolved.

## Protein and assembly

- Target: human copper/zinc superoxide dismutase 1 (SOD1), UniProt P00441.
- Supplied sequence: 154 amino acids, wild-type human SOD1.
- Supplied structure: predicted by AlphaFold from the supplied 154-residue sequence; not experimental and not downloaded from the AlphaFold Database.
- Model contents: one chain, one 154-residue copy.
- Functional biology in the transcript: two identical SOD1 copies form the active enzyme. The supplied one-chain model is therefore not the complete functional assembly.
- Construct status: the files show no indicated tags, mutations, or truncations, and the AlphaFold input matches the supplied FASTA; Erik's actual construct has not been provided or verified.

## Files

- `data/SOD1.fasta`: 154-residue human SOD1 sequence, UniProt P00441.
- `data/SOD1_alphafold_model.cif`: AlphaFold-predicted coordinates for one SOD1 chain. Per-residue pLDDT is carried in the B-factor column.
- `data/SOD1_alphafold_pae.json`: accompanying pairwise-error/confidence matrix (PAE) for the modeled chain. It cannot establish the interface with a second SOD1 copy that is absent from the model.
- There is no supplied PDB, experimental structure, construct map, plasmid sequence, activity dataset, or experimental validation.

## Exact claim and residues concerned

The owner wants to choose **two or three genuinely solvent-accessible positions on the functional two-copy SOD1 enzyme**, with local confidence of at least 90, for mutations intended to disrupt activity while avoiding an uninterpretable metal-site effect. The claim concerns the selected residue positions and their accessibility, local structural support, relation to the Cu/Zn site, and whether they contact the second SOD1 copy—not merely whether they look exposed in the supplied monomer model.

The following metal-binding histidines must be excluded: **His46, His48, His63, His71, His80, and His120**. Positions that could affect metal coordination, or that contact the second SOD1 copy, are also to be excluded for an ordinary outer-surface shortlist. The exact amino-acid substitutions are not specified.

## Evidence and confidence matched to claims

- For a fold or candidate-region claim, use and report the matching per-residue pLDDT from the mmCIF B-factor column; retain only pLDDT ≥90.
- For a claim about how parts sit together, use PAE/interface evidence and an explicitly identified paired structure or model. The supplied PAE is intrachain only and cannot validate the missing dimer interface.
- “Accessible” must be numerical and prespecified: choose one metric (for example, relative SASA in %) with units, probe/calculation settings, structural context, software/version, and cutoff before ranking. The transcript does not fix the numerical accessibility cutoff.
- Do not use the reported overall confidence of approximately 98 as a substitute for residue-level confidence.

## Checks that could break the decision

1. **Construct/numbering:** obtain Erik's exact sequence or plasmid map, SOD1 boundaries, tags, linkers/cloning residues, engineered mutations, truncations, and numbering convention; align it to the canonical 154-residue FASTA and map every reported position.
2. **Assembly:** identify an experimental two-copy SOD1 structure or an approved paired model. Record structure/model identifier, chain mapping, sequence correspondence, missing residues, and the contact rule and measurements. The supplied one-chain CIF cannot determine whether an apparent surface residue is covered by the other copy.
3. **Accessibility:** fix the metric, units, probe, calculation context (paired structure), software/version, and cutoff before inspecting/ranking candidates.
4. **Metal site:** exclude the six named histidines and define/document a distance or other rule for residues that could alter metal coordination or nearby geometry.
5. **Mutation effects:** a changed activity readout could instead reflect altered expression, folding, metal binding, dimerization, or aggregation. The substitution and controls must be specified.
6. **Model limitations:** no experimental structure or assay validates these exact coordinates or candidates.

## Definition of done

- Erik's construct and numbering are verified against canonical SOD1.
- A paired-structure source or approved modeling plan is documented, with chain mapping and a numerical contact rule.
- One accessibility metric, units, context, settings, and cutoff are fixed before ranking.
- Correct residue-level confidence is joined to the correct residue numbers; candidates meet pLDDT ≥90.
- Metal-site and paired-copy-contact exclusions are applied and logged.
- A ranked Markdown table contains no more than three candidates, or states that fewer than two/no defensible candidates pass. Required fields are: rank; construct and canonical position; wild-type residue; proposed substitution; accessibility metric/value; local confidence; second-copy contact and minimum distance; metal-site relation; and rationale.
- Exclusions, assumptions, input files, structure identifiers, and reproducibility settings are recorded.
- Controls cover construct confirmation, expression/folding, activity, and aggregation. The result is labeled a provisional structural shortlist, not proof that a mutation is safe or surface-specific.
- Delivery is by Friday, 18 September 2026, at 09:00 Europe/Stockholm.
