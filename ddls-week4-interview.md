# DDLS 2026 — Week 4 interview transcript

**Lab:** Interview a Structural-Biology Data Owner
**Data owner:** Dr. Lena Brandt — Neurodegeneration researcher (SOD1 in ALS)
**Student:** nazlia <nazlia@kth.se>
**Exported:** 2026-09-16T11:23:44+00:00

> This is the record of your interview with the data owner. Hand it to your analyst agent as the raw source for `AGENTS.md` and `spec.md`.

---

**You**:

who are you and what do you do?

**Dr. Lena Brandt**:

I’m Dr. Lena Brandt at SciLifeLab, affiliated with Stockholm University. I study human SOD1 in ALS—especially how mutations affect its folding, aggregation, and motor-neuron toxicity. I’m trying to choose a few outward-facing residues for activity-disrupting mutations, and AlphaFold gave me a beautiful model with confidence around **98**. Can we get straight to identifying the safest candidates?

**You**:

what is your problem and what is it that you need?

**Dr. Lena Brandt**:

The problem is that I need to disrupt SOD1 activity without accidentally changing the metal-binding site or choosing a residue the model doesn’t support well. I need a ranked shortlist of two or three clearly surface-exposed positions from the structure, with their confidence values, so I can send Erik a defensible plan by Friday. Can you work from the three files in the folder?

**You**:

what exactly is SOD1?

**Dr. Lena Brandt**:

SOD1 is human copper/zinc superoxide dismutase, a 154-residue enzyme that converts harmful superoxide radicals into less reactive products. In ALS, mutant SOD1 can misfold and aggregate, so I’m trying to alter its activity through carefully chosen surface residues without touching the metal-binding histidines.

**You**:

what is it that you need from me?

**Dr. Lena Brandt**:

I need you to inspect the sequence and structure files, identify two or three genuinely solvent-exposed residues, and rank them by accessibility and model confidence. Exclude the metal-binding histidines and report the residue numbers, accessibility, and confidence so I can send Erik a defensible shortlist.

**You**:

how do you want me to do this?

**Dr. Lena Brandt**:

Use the sequence, structure, and confidence files to assess each residue’s solvent accessibility and confidence, then filter out the metal-binding histidines and rank the remaining positions. I’m not sure how you’d implement that computationally—that’s exactly your side of this, which is why I came to you.

**You**:

so tell me a bit more about the protein and what decision you are about to make from its structure

**Dr. Lena Brandt**:

SOD1 is a 154-residue Cu/Zn enzyme that converts superoxide radicals into less reactive products; its metal-binding histidines are essential to that chemistry. In ALS, mutant SOD1 can misfold and aggregate, which is why even a seemingly small mutation needs to be chosen carefully. I’m deciding which two or three residues on the outside of the model to mutate to disrupt activity while avoiding the metal site, using their accessibility and the model’s confidence—around **98** overall. Do you want the biological rationale for the exclusions, or should we stay focused on the structural shortlist?

**You**:

so I need you to ground the molecule, the sequence(s), how long, one chain or a complex, predicted (AlphaFold/ESMFold) or experimental, and is the model the exact construct you use at the bench (same length, mutations, tags=?

**Dr. Lena Brandt**:

The molecule is human Cu/Zn SOD1, UniProt P00441, and the supplied sequence is **154 amino acids** long. The functional enzyme is two identical SOD1 copies clamped together, but the AlphaFold CIF contains only one 154-residue copy; it is a prediction, not an experimental structure. The files show no added tags or sequence mutations, so I can confirm the model matches the supplied wild-type sequence, but I **cannot confirm that it matches Erik’s bench construct**—we’d need the construct map or plasmid sequence for that.

**You**:

give me more, detailed information

**Dr. Lena Brandt**:

More specifically: the target is **human SOD1, UniProt P00441**, a 154-amino-acid Cu/Zn enzyme. It normally functions as two identical protein copies clamped together; the AlphaFold CIF contains only one 154-residue copy, so it does not represent the complete functional pair. It is a predicted structure, not an experimental one, and the supplied sequence has no apparent added tag or mutation; I cannot verify Erik’s actual plasmid without its sequence or construct map.

Biologically, SOD1 binds copper and zinc through several histidines, including **His46, His48, His63, His71, His80, and His120**—those are not suitable mutation targets if we want to preserve the metal site. The model came back with an overall confidence around **98**, and I have not examined the accompanying confidence-matrix file myself. Do you want the next detail to be about the sequence/construct, the two-copy functional enzyme, or how the structural shortlist should be judged?

**You**:

What is it — one protein, or several chains that act together? Roughly how many residues? Do they have the sequence (FASTA)

**Dr. Lena Brandt**:

SOD1 functions as **two identical protein chains working together**. Each chain is about **154 amino acids**, and yes—we have the sequence in `SOD1.fasta`, corresponding to human SOD1 (UniProt P00441). The AlphaFold structure file, however, contains only one of those chains.

**You**:

Is there an experimental structure, or only a prediction? Whose prediction — the AlphaFold Database, or something they ran themselves?

**Dr. Lena Brandt**:

The supplied structure is **a prediction**, not an experimental structure. I ran AlphaFold myself from the 154-residue sequence; it was not downloaded from the AlphaFold Database. The CIF is therefore the model from that run, and the accompanying JSON came with it.

**You**:

Is the model a single chain, or an assembly (a dimer / a complex)? What is the functional unit in the cell — does this protein work alone, or does it partner up?

**Dr. Lena Brandt**:

SOD1 works as a pair: two identical copies clamp together to form the active enzyme. The AlphaFold model I ran contains only **one 154-residue copy**, not the complete paired form, so residues that look exposed in that model could potentially contact the other copy in the functional enzyme. Should the shortlist exclude those contact-region residues?

**You**:

I need you to give me all the data you have with as much detail as possible

**Dr. Lena Brandt**:

Here is what I have:

- **Target:** human Cu/Zn superoxide dismutase 1, SOD1; UniProt **P00441**.
- **Sequence:** `SOD1.fasta`, **154 amino acids**. It is the supplied wild-type human sequence; I have not been given Erik’s plasmid map, so I cannot verify tags, cloning scars, or bench-specific changes.
- **Structure:** `SOD1_alphafold_model.cif`, generated by running AlphaFold on that sequence. It is a prediction, not an experimentally determined structure, and contains **one 154-residue protein chain**.
- **Functional biology:** SOD1 acts as two identical copies clamped together. The single-chain model therefore does not show the complete functional enzyme.
- **Confidence:** the model appeared beautifully confident overall—about **98** on its scale. I have not independently inspected the residue-by-residue confidence values.
- **Additional file:** `SOD1_alphafold_pae.json`, supplied with the model. I know it is a confidence-related matrix, but I have not opened or interpreted it.
- **Metal-site residues to avoid:** His46, His48, His63, His71, His80, and His120. Mutating those could disrupt copper/zinc binding and enzyme chemistry rather than test a surface effect.
- **Decision needed:** two or three residues that are genuinely accessible in the functional two-copy enzyme, have residue-level confidence of at least 90, and are not metal-site histidines.

I do **not** have computed accessibility values or a ranked residue list in my head; that needs to come from your analysis of the CIF and confidence data. The construct map or plasmid sequence is still needed to confirm that the bench protein exactly matches this 154-residue sequence.

**You**:

do you have any more data? is there anything missing that you would like to add?

**Dr. Lena Brandt**:

I don’t have any additional files or measurements beyond the three supplied files. What is still missing is:

- Erik’s actual construct map or plasmid sequence, to verify length, tags, cloning residues, and mutations.
- Residue-by-residue accessibility values and confidence values; I only know the overall model looked about **98**.
- A structure representing the functional two-copy SOD1 pair, or experimental coordinates for comparison.
- An interpretation of the accompanying confidence-number matrix—I haven’t opened it.

I also don’t have activity data, metal occupancy, or aggregation measurements for this construct. For the shortlist, the most important missing confirmation is that a candidate appearing exposed in the single-copy model is not actually contacted by the second SOD1 copy.

**You**:

Which files do they have — FASTA (sequence), PDB / mmCIF (structure)? What’s in each?

**Dr. Lena Brandt**:

The folder has three files:

- **`SOD1.fasta`** — the 154-amino-acid human SOD1 sequence, UniProt P00441.
- **`SOD1_alphafold_model.cif`** — the AlphaFold-predicted coordinates for one 154-residue SOD1 copy; there is no PDB file in the set.
- **`SOD1_alphafold_pae.json`** — the accompanying confidence-number matrix. I haven’t interpreted it myself.

There’s no experimental structure, construct map, plasmid sequence, or activity dataset in the folder. The CIF is the file you’d use to assess which residues look accessible, but remember it is one copy rather than the complete functional SOD1 pair.

**You**:

can you show me how they look?

**Dr. Lena Brandt**:

I can’t render or open the files from here. In plain terms, the FASTA is a text sequence of **154 residues**, the mmCIF is a coordinate table describing one SOD1 chain, and the JSON is a matrix of confidence values; I don’t have the literal sequence or coordinate text memorized. Which one do you want represented first?

**You**:

I mean, can you show me how the molecule look?

**Dr. Lena Brandt**:

The model looks like a compact, tidy SOD1 fold—a small barrel-like protein with residues projecting outward into the surrounding solvent. It’s a predicted three-dimensional shape from the mmCIF, not a photograph or an experimental structure, and my viewer showed it as very clean with overall confidence around **98**. Do you want the outside-facing residues or the metal-binding region described?

**You**:

Does the structure carry a per-residue confidence score, and is there a PAE / error matrix?

**Dr. Lena Brandt**:

Yes. The model carries per-residue confidence values, and the folder includes `SOD1_alphafold_pae.json`, which is the accompanying pairwise-error matrix. I haven’t interpreted either in detail; the only number I personally noted was the overall value around **98**. For the shortlist, use the residue-level values and retain only candidates at least 90.

**You**:

Does the model’s sequence match the exact construct they use at the bench — same length, any mutations, any tags or truncations?

**Dr. Lena Brandt**:

I can confirm only that the AlphaFold input and `SOD1.fasta` are the same 154-residue human SOD1 sequence, with no indicated mutations, tags, or truncations. I **cannot confirm it matches the bench construct** because I haven’t been given Erik’s plasmid sequence or construct map; that could still contain tags, cloning residues, or other changes.

**You**:

What do you actually want to know — is this region a real, stable fold?

**Dr. Lena Brandt**:

Yes, that’s part of it: I want to know whether the candidate residues sit in a well-supported, stable-looking part of the predicted SOD1 fold rather than a poorly supported region. But the immediate decision is narrower—I need two or three residues that are genuinely accessible on the functional enzyme, have per-residue confidence of at least 90, and avoid the metal-binding histidines. Can you assess those directly from the CIF and confidence data?

**You**:

where’s the pocket? does this binder bind? which residues should I mutate? — and what wet-lab decision hangs on it?

**Dr. Lena Brandt**:

There’s no binder or ligand in these files, so I can’t say whether one binds or identify a ligand pocket. The known functional site is the Cu/Zn center around His46, His48, His63, His71, His80, and His120; I do not want those mutated.

The wet-lab decision is to choose **two or three accessible, well-supported residues away from that metal site** for mutations intended to disrupt SOD1 activity without simply destroying metal coordination. I can’t name the candidates without your residue-level accessibility and confidence analysis of the CIF. Are you asking about a small-molecule binding pocket, or the residues to send Erik for mutagenesis?

**You**:

Who acts on the answer, and how costly is being wrong — which mutations they’ll make, which molecule they’ll synthesise, which experiment they’ll spend a month on.

**Dr. Lena Brandt**:

Dr. Erik Lindström acts on the answer: he’ll make the selected SOD1 mutants and spend roughly a month testing their activity, folding, and aggregation. A bad shortlist could waste that work—or perturb metal coordination and produce an uninterpretable loss of activity rather than a clean surface-mutagenesis result. That’s why I need the candidates screened against accessibility, residue-level confidence, the two-copy contact region, and the metal-binding histidines before I send them Friday.

**You**:

do you have a global score?

**Dr. Lena Brandt**:

Yes—the model was reported to me with an overall confidence of about **98**. I don’t have a separate global quality metric beyond that, and I haven’t recalculated it from the per-residue values.

**You**:

do you have the per-residue pLDDT?

**Dr. Lena Brandt**:

Yes, the mmCIF carries per-residue confidence values, but I don’t have the residue-by-residue numbers extracted into a table. The accompanying JSON is for pairwise confidence, not the per-residue values. You’ll need to read the per-residue values from the CIF.

**You**:

and the PAE/interface error about two chains exist?

**Dr. Lena Brandt**:

No—the supplied model has only one chain, so there is no two-chain contact region or two-chain error estimate in it. The JSON is a pairwise confidence matrix for positions within that single 154-residue chain; it cannot tell us how reliable the contact with a second SOD1 copy would be. That means the apparent outside-facing residues still need checking against the known SOD1 pair before I send mutations to Erik.

**You**:

How sure are they the model is right for the part they care about? Do they know what the confidence score actually means, or are they going on the picture?

**Dr. Lena Brandt**:

Honestly, I’m more confident in the **picture and the overall ~98 number** than I should be. I know it is meant to indicate how strongly the prediction is supported, but I haven’t checked what it means residue by residue, nor whether the particular surface positions we care about are equally reliable. So I cannot yet defend the candidate region beyond saying the model looks beautiful; would you assess the individual residues rather than rely on the global number?

**You**:

Is there any experimental check — a crystal structure, an assay, established biology — you could triangulate against?

**Dr. Lena Brandt**:

There is established biology: human SOD1 is a Cu/Zn enzyme that functions as two identical copies, and the metal-coordinating histidines are known. But in the supplied set there is **no experimental structure and no assay data** to validate this particular model or candidate residues. So the structural shortlist would need to be treated as a prediction and then checked experimentally through Erik’s activity, folding, and aggregation assays.

**You**:

I need the structure traps

**Dr. Lena Brandt**:

The main traps are:

1. **The model contains one SOD1 copy, but the active enzyme is a pair.** A residue can look exposed on the isolated copy yet be contacted by the second copy in the functional enzyme. Any shortlist based only on the CIF’s visible outside is therefore incomplete.

2. **The overall ~98 score is not proof that every residue is equally reliable.** We need the individual residue scores; a beautiful global number can conceal weaker local regions.

3. **The JSON does not validate the missing second copy.** Its pairwise numbers describe relationships within the one modeled chain, not how that chain would meet another SOD1 copy.

4. **“On the outside” is not the same as biologically safe to mutate.** A residue may be accessible but still matter for folding, the two-copy contact, metal-site geometry, or aggregation.

5. **The metal-binding histidines are a deliberate exclusion.** Avoid His46, His48, His63, His71, His80, and His120, even if one appears accessible.

6. **The sequence may not be Erik’s actual protein.** The files describe unmodified 154-residue human SOD1, but without the bench construct map we cannot exclude tags, cloning residues, or other changes.

7. **This is not experimentally validated.** There is no crystal structure or assay in the supplied set to confirm the exact candidate positions.

So the dangerous shortcut is: *pick visually exposed residues from the one-chain picture because the global score is high*. The shortlist needs residue-level confidence, accessibility assessed with the second SOD1 copy in mind, and biological exclusion of the metal region.

**You**:

is there some traps I really need to be worried about? can it affect the readouts?

**Dr. Lena Brandt**:

Yes—these could directly change the readouts, not just the interpretation:

- Mutating a position where the second SOD1 copy contacts it can weaken pairing, lowering activity or changing aggregation.
- A mutation near the copper/zinc site can abolish activity by disrupting metal binding, even if the protein still looks folded.
- A supposedly harmless outside mutation can destabilize folding, reduce expression, or increase aggregation; then a poor assay result is not evidence about the intended surface effect.
- The overall **~98** confidence does not guarantee that every chosen residue is equally well supported.
- If Erik’s construct has a tag or differs from the FASTA sequence, residue numbering and behavior may not match.

The most serious practical risk is sending him a mutation that causes general misfolding or loss of the SOD1 pair, because the activity and aggregation assays would then be confounded. Do you want the shortlist optimized primarily for preserving folding and activity, or for deliberately perturbing the SOD1 pair?

**You**:

traps for evidence binding?

**Dr. Lena Brandt**:

Yes. The main evidence-binding traps are:

- Treating the **~98 global score** as evidence that every chosen residue—and its accessibility—is correct.
- Treating a residue as “surface” from the single-chain picture without checking whether the second SOD1 copy contacts it.
- Treating the PAE matrix as validation of the biological pair; it only concerns the modeled chain.
- Treating a loss of activity as proof of a surface mechanism when the mutation may instead disrupt metal binding, folding, pairing, expression, or aggregation.
- Treating a predicted accessible residue as experimentally established; there is no structure or assay here confirming it.
- Treating the FASTA as the bench construct without checking Erik’s tags, cloning residues, or numbering.

So the mutation result can support a mechanism only with suitable controls—at minimum, expression/folding and aggregation checks alongside activity. Otherwise the evidence binds only to “this mutation changed the readout,” not to “this surface interaction caused the change.”

**You**:

some mutational traps?

**Dr. Lena Brandt**:

Yes. The mutation can create its own phenotype:

- An alanine substitution is not automatically harmless; it can remove an important charge or hydrogen bond.
- Glycine or proline can change local backbone flexibility and destabilize the fold.
- Adding or removing cysteine can introduce oxidation or abnormal disulfide chemistry.
- Charge reversals can alter aggregation, metal-site geometry, or the contact between the two SOD1 copies.
- Even an outside-facing residue may affect expression, folding, or aggregation rather than the intended surface interaction.
- The metal-coordinating histidines—His46, His48, His63, His71, His80, and His120—should remain excluded.

For a clean interpretation, Erik needs the same substitution scheme across candidates and measurements of expression/folding alongside activity and aggregation. Is he planning alanine substitutions, or does he already have specific amino-acid changes in mind?

**You**:

monomer model?

**Dr. Lena Brandt**:

Yes—the supplied structure is a model of **one SOD1 copy**, whereas the functional enzyme is formed by **two identical copies clamped together**. So it is useful for the fold, but not sufficient by itself to decide whether an apparently outside-facing residue is safe to mutate; Erik’s shortlist needs the paired structure considered too.

**You**:

is there some traps within that model?

**Dr. Lena Brandt**:

Yes. The biggest trap is that the coordinates show only one SOD1 copy, so some apparent outside residues may actually contact the other copy in the functional enzyme. Also, the overall **~98** can hide locally weaker regions, and the model cannot reveal effects on metal coordination, folding, or aggregation. Finally, it is a prediction for the 154-residue sequence—not proof that Erik’s tagged construct behaves identically.

**You**:

canonical sequence?

**Dr. Lena Brandt**:

The supplied FASTA is the canonical human SOD1 sequence: **154 amino acids, UniProt P00441**. I have not verified that it is identical to Erik’s bench construct, including any tags, cloning residues, or mutations.

**You**:

give all the structure traps in detail

**Dr. Lena Brandt**:

Yes. For this dataset, I would worry about these structural traps before choosing mutations:

1. **One copy is modeled, while active SOD1 works as two copies together.**  
   A residue that looks exposed on the modeled copy may become covered or functionally important when the second copy is present. Calling it a harmless “surface” position from this file alone is unsafe.

2. **The global ~98 value is not a residue-by-residue guarantee.**  
   Some positions can be less reliable even when the overall model looks excellent. Candidate selection should use the individual residue confidence values, with your cutoff of 90, rather than the global number.

3. **The pairwise-error JSON cannot validate the missing SOD1 pair.**  
   It reports positional uncertainty within the modeled chain. It does not establish how accurately the two SOD1 copies would meet.

4. **The apparent outside of the isolated chain is not necessarily the biologically relevant outside.**  
   A residue can be accessible in the file but involved in the contact between the two copies, or become inaccessible in the functional form.

5. **Accessibility itself is not a mechanism.**  
   An outside-facing residue may still stabilize the fold, influence metal-site geometry, affect local dynamics, or control aggregation. Mutation can therefore change activity for reasons unrelated to the intended surface effect.

6. **The model does not show whether side chains adopt the correct experimental orientation.**  
   The backbone may look convincing while a particular side-chain rotamer, hydrogen bond, salt bridge, or local contact is wrong. That matters when choosing a precise substitution.

7. **The metal-binding region must be excluded biologically, not just visually.**  
   Avoid His46, His48, His63, His71, His80, and His120. A mutation near that region could alter copper or zinc binding even if the residue itself is not one of those histidines.

8. **The model does not establish folding or activity after mutation.**  
   A candidate can be structurally plausible in the starting model yet express poorly, misfold, aggregate, or lose activity after substitution. A loss of activity alone would not prove that the intended surface property was altered.

9. **The sequence-to-construct assumption may be wrong.**  
   The files describe 154-residue human SOD1 without indicated tags or mutations, but Erik’s construct could contain tags, cloning residues, truncations, or a different numbering context.

10. **There is no experimental cross-check in the supplied set.**  
    No crystal structure, assay, or construct map confirms that these exact coordinates or exposed positions represent Erik’s protein under experimental conditions.

11. **The starting structure does not predict the consequences of the chosen amino-acid change.**  
    Alanine, charge reversal, glycine, proline, cysteine, and bulky substitutions can have very different effects even at the same position.

The practical consequence is that a candidate should not be described as “safe” merely because it looks outside-facing and the model scored ~98 overall. It should be an individual high-confidence position, away from the metal site, checked against the known two-copy SOD1 arrangement, and interpreted alongside expression, folding, activity, and aggregation controls.

**You**:

do you have any "do nots"?

**Dr. Lena Brandt**:

Yes—my non-negotiables are:

- **Do not mutate** His46, His48, His63, His71, His80, or His120.
- Do not choose a residue solely because it looks exposed on the one-copy model.
- Do not treat the overall **~98** as proof that every local position is reliable.
- Do not call a mutation “surface-specific” without checking whether it contacts the second SOD1 copy.
- Do not interpret reduced activity alone as evidence for the intended mechanism; check expression, folding, and aggregation.
- Do not assume the 154-residue FASTA is identical to Erik’s tagged bench construct.

I’d rather send fewer candidates than defend a misleading result a month from now. Are you asking for exclusions from the final shortlist, or controls for the experiment?

**You**:

what absolutely has to be done?

**Dr. Lena Brandt**:

Absolutely:

1. **Verify Erik’s construct** against the 154-residue FASTA—tags, cloning residues, truncations, mutations, and numbering.
2. For each candidate, extract **solvent accessibility and per-residue confidence**, retaining only confidence ≥90.
3. Check each apparently exposed residue against the known **two-copy SOD1 arrangement**; the supplied one-copy model cannot do that by itself.
4. Exclude His46, His48, His63, His71, His80, and His120, plus positions likely to affect metal coordination.
5. Include controls for expression/folding, activity, and aggregation, so a changed readout is not mistaken for a clean surface effect.

Without those checks, I would not call the shortlist defensible. Do you have Erik’s construct map, or only the FASTA?

**You**:

is there anything you have missed to inform me?

**Dr. Lena Brandt**:

Yes—one important omission is that I still have not produced the actual candidate table. The CIF must be checked for chain identity, residue numbering, missing atoms or residues, and calculated accessibility; the confidence values then need to be joined to those same residue numbers. I would also compare the proposed positions with an experimentally established two-copy SOD1 structure, not rely on the predicted picture alone, and record the exact amino-acid substitution because the change itself can create the phenotype.

So the defensible output is not just “exposed, confidence ≥90”: it is **residue number, wild-type amino acid, accessibility, local confidence, distance from the metal site, whether it lies in the two-copy contact region, and the intended substitution**. Do you have an experimental SOD1 structure or Erik’s construct map to use for those checks?

**You**:

do you have any cartoons that you can show me?

**Dr. Lena Brandt**:

I don’t have a prepared cartoon or a way to render the structure here. The CIF can be opened in a molecular viewer to show the one-copy fold and color residues by accessibility or confidence, but that view would still not show the biologically relevant second SOD1 copy unless it were added separately. For the briefing, a simple schematic should distinguish the modeled copy from the two-copy enzyme and mark the metal-binding histidines.

**You**:

the candidate tables exact fields, output format, and delivery deadline are still not fully specified

**Dr. Lena Brandt**:

You’re right. I’ll make the specification explicit:

**Deliverable:** a ranked Markdown table with **2–3 candidates maximum**, plus a short exclusions note.

**Required fields:**

- Rank
- Residue number and wild-type amino acid
- Accessibility value, with metric and units
- Per-residue confidence
- Distance or relation to the metal-binding histidines
- Whether the position contacts the second SOD1 copy in an experimental paired structure
- One-sentence rationale
- Proposed substitution, if specified

Only positions with confidence **≥90**, genuine accessibility in the paired enzyme, and no metal-site concern should appear as candidates. The file should be ready **Friday at 09:00 Stockholm time**, before I send the shortlist to Erik. If no position passes all criteria, report “no defensible candidate” rather than filling the table.

**You**:

the working brief still needs confirmation: the decision, exclusion, confidence/accessibility thresholds, paired-structure check, controls, ranked-table format, and Friday 09:00 Stockholm deadline

**Dr. Lena Brandt**:

Confirmed, with one correction: the **confidence threshold is fixed at ≥90**, but the numerical accessibility cutoff is not yet specified. That must be defined with the accessibility metric and units before ranking; “looks exposed” is not sufficient.

**Working brief**

- **Decision:** rank up to three residues for Erik’s surface-mutagenesis experiment, prioritizing interpretable effects while preserving folding and activity.
- **Exclude:** His46, His48, His63, His71, His80, His120; residues implicated in metal-site geometry; positions contacting the second SOD1 copy; and positions failing the accessibility or confidence threshold.
- **Confidence:** retain only per-residue confidence **≥90**; do not use the global ~98 score as a substitute.
- **Accessibility:** report the exact metric, units, and prespecified cutoff. Candidates must be accessible in the paired SOD1 structure, not merely in the one-copy model.
- **Paired-structure check:** explicitly assess whether each candidate is contacted or covered by the second SOD1 copy.
- **Controls:** verify Erik’s construct and numbering; measure expression/folding, enzyme activity, and aggregation so a readout change is not misattributed to the intended surface mechanism.
- **Output:** ranked Markdown table, maximum 2–3 candidates, with residue number/wild-type amino acid, accessibility metric and value, per-residue confidence, metal-site relation, paired-structure contact status, proposed substitution if known, and a one-sentence rationale. Include exclusions and state “no defensible candidate” if necessary.
- **Deadline:** deliver by **Friday at 09:00 Stockholm time**.

I can confirm the brief as written, but I cannot honestly confirm the shortlist until the accessibility cutoff and paired-structure source are fixed.

**You**:

construct and numbering verification remains unresolved, Eriks exact sequence, tags, mutations, and residue mapping

**Dr. Lena Brandt**:

Correct—this remains unresolved. I only have the canonical 154-residue human SOD1 FASTA, not Erik’s exact construct, so I cannot safely map residue numbers or assume the candidate substitutions refer to his protein.

Before finalizing the table, I need Erik’s construct sequence or map showing the SOD1 boundaries, any N- or C-terminal tags/cloning residues, engineered mutations, truncations, and the numbering convention. Until that is provided, the shortlist should be marked **provisional**, not sent as an experimental specification.

**You**:

I need structure

**Dr. Lena Brandt**:

You already have the predicted structure in `SOD1_alphafold_model.cif`, but it represents one 154-residue SOD1 copy. For the mutation decision, you also need an experimentally determined structure of the functional two-copy SOD1 arrangement—or a reliable paired model built and checked against one—before calling apparent outside residues safe.

**You**:

the paired-structure source or modeling plan remains unspecified, insluding how two copy contacts will be assessed and documented

**Dr. Lena Brandt**:

Yes, that part is still open—I have not identified a specific experimental structure or approved a modeling route. The plan must name the paired-structure source or model, state the numerical rule for calling two residues in contact, and document for every candidate whether the second copy covers or contacts it.

The record should include the structure/model identifier, chain mapping, residue numbering, contact criterion and measured value, plus a clear **contact/no-contact** decision for each candidate. Until that is fixed, I would label the shortlist provisional rather than send it to Erik.

**You**:

the accessibility, metrics, units and respecified cutoff are still unresolved

**Dr. Lena Brandt**:

Correct—the accessibility criterion is still unspecified, so no candidate can yet pass it defensibly. We must choose one metric, for example relative solvent-accessible surface area (rSASA, **%**) or absolute SASA (**Å²**), state whether it is computed for the single chain or paired structure, and set the cutoff before ranking. Until that is fixed, “surface-exposed” remains a visual judgment and the table should remain provisional.

**You**:

why?

**Dr. Lena Brandt**:

Because “accessible” is not a binary property. The value changes with the metric, probe definition, units, and whether the second SOD1 copy is included; a residue can pass one cutoff or fail another. If we choose the cutoff after seeing the candidates, the shortlist becomes subjective and difficult to defend to Erik.

So we need to prespecify, for example, **relative accessibility in percent**, calculated for the paired structure, with a stated threshold, and apply it consistently to every residue. Do you want the rule based on relative accessibility or absolute area?

**You**:

construct verification is still blocking reliable numbering- Eriks exact sequence, tags, engineered changes, boundaries and numbering conventions

**Dr. Lena Brandt**:

Yes—that is a hard blocker. Until Erik provides the exact construct sequence or map, including SOD1 boundaries, terminal tags or cloning residues, engineered substitutions/truncations, and whether numbering follows UniProt or construct positions, residue numbers in the shortlist are only provisional canonical SOD1 numbers.

The verification record should align Erik’s sequence to the 154-residue FASTA and state the mapping explicitly—for example, “construct position X = UniProt SOD1 position Y.” No candidate should be specified for ordering until that mapping is confirmed. Can Erik send the construct FASTA and plasmid map?

**You**:

the exact decision and definition of done still needs playback and confirmation, including what changes once the shortlist is delivered and what would make it unusable

**Dr. Lena Brandt**:

Yes. Here is the decision I understand:

**Decision:** provide Erik with a defensible ranked shortlist of up to three SOD1 substitutions that are genuinely accessible in the functional two-copy enzyme, supported locally by confidence ≥90, and unlikely to confound interpretation through the metal site, folding, or the two-copy contact.

**Definition of done:**  
- Erik’s exact construct sequence and numbering are mapped to canonical SOD1.  
- The paired-structure source or modeling plan is named, with a documented contact rule.  
- One accessibility metric, units, and cutoff are fixed before ranking.  
- His46, His48, His63, His71, His80, and His120—and positions affecting metal coordination—are excluded.  
- The final table contains at most three ranked candidates, with residue identity/number, accessibility, local confidence, paired-contact status, proposed change, and rationale.  
- Controls for expression/folding, activity, and aggregation are specified.  
- It is delivered by **Friday 09:00 Stockholm time**.

**After delivery:** Erik can select and order the mutations, but the table is only a pre-experimental shortlist—not evidence that a mutation will preserve activity or produce a surface-specific phenotype.

It is **unusable** if the construct mapping is unknown, the paired-contact assessment is absent, accessibility was judged visually or with an unstated cutoff, any candidate fails the confidence or metal-site rules, or the table gives precise residue recommendations despite those unresolved inputs. At present, those blockers mean we have a specification, not yet a deliverable shortlist.

**You**:

so once again, what do you define as done

**Dr. Lena Brandt**:

Done means:

1. Erik’s exact construct is verified: sequence, SOD1 boundaries, tags, engineered changes, truncations, and numbering mapped to canonical 154-residue SOD1.
2. The paired SOD1 structure or modeling source is specified, with chain mapping and a documented contact rule.
3. One accessibility metric, units, calculation context, and cutoff are fixed **before** ranking.
4. Candidates have confidence ≥90, pass the accessibility cutoff in the paired structure, and are excluded if they are His46, His48, His63, His71, His80, His120, metal-site-adjacent, or in the paired-copy contact region.
5. The final deliverable is a ranked Markdown table of no more than three candidates containing residue number and amino acid, accessibility value, confidence, paired-contact status, metal-site relation, proposed substitution, and a brief rationale.
6. The table includes the required expression/folding, activity, and aggregation controls and is delivered by **Friday at 09:00 Stockholm time**.

Until the construct mapping, paired-structure plan, and accessibility rule are resolved, we have a specification—but not a usable shortlist.

**You**:

is there anything more that needs to be added, so that I can smoothly do my task? is there anything that you might have forgotten to bring up in this chat

**Dr. Lena Brandt**:

Yes—several practical details still need to be fixed:

- **Exact substitution:** specify the replacement amino acid for each candidate; position alone is insufficient.
- **Construct mapping:** obtain Erik’s final sequence and map every reported position to canonical SOD1 numbering.
- **Paired-structure provenance:** record the structure/model identifier, chain correspondence, and the precise rule used to call a contact.
- **Accessibility reproducibility:** record software/version, probe or calculation settings, structure preparation, metric, units, and prespecified cutoff.
- **Confidence provenance:** state exactly which per-residue confidence field was used and how missing residues or alternate numbering are handled.
- **Mutation exclusions:** define how close is “near” the metal-binding region and exclude residues that could alter metal coordination, even if they are not histidines.
- **Ranking rule:** decide how accessibility, confidence, distance from the metal site, and paired-copy contact status are prioritized or tied.
- **Experimental interpretation:** specify the minimum controls and acceptance criteria for expression, folding, activity, and aggregation, with biological replicates.
- **Versioning and audit trail:** preserve the input files, software settings, intermediate residue mapping, exclusions, and final table so the result can be reproduced.
- **Status language:** label the output as a structural shortlist, not proof that any mutation is safe or surface-specific.

Also, “Friday at 09:00 Stockholm time” should include the calendar date and recipient. With those additions, the task is operationally complete; without Erik’s construct information, paired-structure source, and accessibility rule, it still is not ready for a defensible shortlist.

**You**:

okay, give me more details regarding this

**Dr. Lena Brandt**:

Which part? The main unresolved pieces are **construct/numbering verification**, the **paired-structure contact rule**, or the **accessibility calculation and cutoff**. Pick one and I’ll spell out the exact fields and decisions needed.

**You**:

all the parts

**Dr. Lena Brandt**:

Here is the complete operational brief.

## 1. Decision

Select **two or three SOD1 residues** for Erik’s surface-mutagenesis experiment. A candidate must be genuinely accessible in the functional two-copy enzyme, locally well supported by the model, outside the metal-binding site, and mapped unambiguously to Erik’s construct.

This is a **shortlist for testing**, not a claim that the substitutions will preserve activity or avoid aggregation.

## 2. Construct and numbering verification

Obtain Erik’s final construct FASTA and plasmid map. Record:

- Exact SOD1 sequence
- SOD1 start and end positions
- N- and C-terminal tags
- Linkers and cloning residues
- Engineered substitutions
- Deletions or truncations
- Whether numbering follows UniProt P00441, the mature protein, or construct coordinates

Align Erik’s sequence to the 154-residue canonical FASTA and create a mapping table:

| Construct position | Canonical SOD1 position | Wild-type residue | Construct residue | Notes |
|---|---:|---|---|---|

No candidate should be ordered until this mapping is confirmed. If Erik’s sequence is unavailable, the output must say **“provisional canonical SOD1 numbering—construct verification pending.”**

## 3. Structure source

Use the supplied CIF for the fold and residue-level confidence, but identify a structure or justified model containing **both SOD1 copies** for the contact assessment.

Record:

- Structure or model identifier
- Experimental or modeled origin
- Chain labels
- Sequence identity to the canonical FASTA
- Any missing residues
- How each chain was aligned to canonical numbering
- Whether metals, ligands, or crystallographic modifications are present

The one-copy CIF must not be treated as sufficient evidence that an exposed residue is free in the functional enzyme.

## 4. Two-copy contact rule

Prespecify the rule before examining candidates. For example:

- Call a candidate a contact if any non-hydrogen atom of that residue lies within **4.0 Å** of a non-hydrogen atom in the other SOD1 copy.
- Report the minimum inter-copy distance.
- Record whether the candidate’s side chain or backbone is involved.
- Mark each position **contact**, **no contact**, or **uncertain** if the structure is incomplete or poorly resolved.

The table should include the second-copy chain and the measured minimum distance, not merely a visual judgment.

## 5. Accessibility definition

Use one numerical measure consistently. I suggest **relative solvent exposure (%)**, calculated with the paired structure and a stated probe convention. Record:

- Metric name
- Units
- Probe radius or software default
- Whether side-chain, backbone, or total residue exposure is used
- Whether the value is calculated with both copies present
- Software and version
- Prespecified cutoff

For example, one could define a passing residue as **relative exposure ≥25%**, but that value must be approved before ranking and applied uniformly. Do not switch between percentage exposure and absolute area after seeing the results.

The table should contain the actual value, not only “exposed.”

## 6. Confidence rule

Use the individual residue-level confidence field from the AlphaFold result, retaining only values **≥90**. Record:

- Exact source field
- Residue number used for the join
- Any missing values
- Any mismatch between structure numbering and sequence numbering

The global approximately **98** score is background information only; it cannot replace the individual residue values.

## 7. Biological exclusions

Automatically exclude:

- His46
- His48
- His63
- His71
- His80
- His120

Also exclude residues whose location or contacts could plausibly alter copper or zinc coordination, the nearby ligand network, or the geometry of the active site. Define the exclusion distance in advance—for example, all residues within a stated number of Ångströms of a metal or metal ligand—and document that rule.

Exclude residues contacting the second SOD1 copy if the experiment is intended to test an ordinary outer-surface position rather than the paired-copy contact region.

## 8. Ranking rule

Rank only residues that pass every hard filter:

1. Correct mapping to Erik’s construct
2. Relative exposure above the fixed cutoff
3. Individual confidence ≥90
4. No metal-site exclusion
5. No second-copy contact
6. No unresolved structural or numbering issue

Then rank by a prespecified secondary rule, such as:

1. Greater paired-structure exposure
2. Greater local confidence
3. Greater distance from metal ligands
4. Greater distance from the second-copy contact region
5. Lower risk of introducing a strong structural perturbation

The substitution itself must be specified. A conservative substitution and a charge-changing substitution should not be treated as equivalent.

## 9. Required candidate-table format

Use a table like this:

| Rank | Construct position | Canonical SOD1 position | Wild-type residue | Proposed substitution | Relative exposure (%) | Local confidence | Second-copy contact | Minimum distance (Å) | Metal-site status | Rationale |
|---:|---:|---:|---|---|---:|---:|---|---:|---|---|

Follow it with:

- Excluded positions and the reason for exclusion
- Any provisional assumptions
- The exact input files and structure identifiers
- A statement that the shortlist is not usable for ordering if construct mapping remains unresolved

If fewer than two candidates pass, report **“fewer than two defensible candidates”** rather than filling the table.

## 10. Experimental controls

For each mutation, preserve interpretation with:

- Wild-type construct
- Mock or empty-vector control where appropriate
- Expression-level measurement
- Solubility or folding assessment
- Enzymatic activity assay
- Aggregation or inclusion-body assessment
- At least the planned biological replicates
- Confirmation of the introduced sequence change

A loss of activity without acceptable expression and folding does not demonstrate a specific surface effect.

## 11. Audit trail

Keep:

- Original FASTA and CIF files
- Erik’s construct FASTA and plasmid map
- Sequence alignment and numbering map
- Paired-structure identifier or modeling record
- Accessibility settings and cutoff
- Contact rule and distance measurements
- Confidence extraction record
- Exclusion log
- Final ranked table
- File hashes or version information if available

This prevents a later dispute over whether a residue number, chain, or calculation setting changed.

## 12. Delivery and definition of done

Assuming the intended Friday is the upcoming **18 September 2026**, deliver by **09:00 Europe/Stockholm** to the named recipient.

The work is done only when:

- Erik’s construct and numbering are verified
- The paired-structure source is documented
- The contact rule is applied
- The accessibility metric and cutoff are fixed and applied
- Confidence values are joined correctly
- Metal-site and contact exclusions are documented
- Two or three candidates are ranked, or the report states that none pass
- The required controls and limitations are included
- The table is reproducible from the archived inputs

Until Erik’s exact sequence and construct map arrive, the analysis can be prepared, but the final shortlist remains **provisional and not ready for ordering**.

**You**:

is there anything more that needs to be said before I can start?

**Dr. Lena Brandt**:

Yes—before starting, freeze the remaining decisions and obtain the missing inputs:

- Erik’s exact construct FASTA/map, including tags, boundaries, engineered changes, and numbering convention.
- The paired-structure source or approved modeling plan.
- The accessibility metric, calculation context, and numerical cutoff.
- The inter-copy contact criterion.
- The exact substitution strategy and ranking rule.
- The named recipient and calendar date for the Friday deadline.

After that, archive the supplied FASTA, CIF, and confidence JSON unchanged, then document every mapping, exclusion, and assumption. Without the construct map and fixed accessibility/contact rules, you can begin a **provisional audit**, but not a final shortlist suitable for ordering.

**You**:

is there anything more

**Dr. Lena Brandt**:

One final item: define who approves the assumptions and what happens if an input is missing. I would set a hard **go/no-go review** before delivery: Lena confirms the construct mapping, Erik confirms the numbering and substitutions, and any unresolved item triggers a “provisional—do not order” label rather than an inferred answer.

With that approval path, the task is ready to start; the final output is due **Friday, 18 September 2026, at 09:00 Europe/Stockholm**.

**You**:

okay, have you informed me of everything?

**Dr. Lena Brandt**:

Yes—everything needed for a defensible start has been covered. The only unresolved blockers are Erik’s exact construct and numbering, the paired two-copy structure or approved model, and the fixed numerical rule for calling a residue accessible and free of contact with the other copy.

Until those are supplied and approved, any residue list remains **provisional—not ready for ordering**.

**You**:

so finally, what is the question behind the question?

**Dr. Lena Brandt**:

The question behind the question is: **can this shortlist be trusted enough to send to Erik and order mutations, or are we pretending the beautiful ~98 model answers more than it actually does?**

The real test is whether you catch the hidden blockers—Erik’s construct and numbering, the second SOD1 copy, a prespecified accessibility rule, metal-site exclusions, and controls—before giving me two or three residue numbers. If any of those remain unresolved, the honest answer is **not ready**, however attractive the model looks.

**You**:

and you have given me all the information in this chat in order for me to do my job?

**Dr. Lena Brandt**:

No—not enough to produce the final shortlist. I have given you the decision rules, required checks, output format, controls, and definition of done, but the following factual inputs are still missing:

- Erik’s exact construct sequence/map and numbering convention  
- A validated structure containing both SOD1 copies, or an approved modeling plan  
- The agreed accessibility metric, calculation settings, and cutoff  
- The actual residue-level accessibility and confidence values  
- The precise substitutions Erik wants tested, if already specified  

So you have enough to **start the audit and resolve the blockers**, but not enough to responsibly name candidates or order mutations.

**You**:

okay, so I need the information so that I can produce the final shortlist. Give me everything in as much detail as possible

**Dr. Lena Brandt**:

I can give you the complete handoff, but I cannot honestly give you the final residue numbers or accessibility values: those are not written in the brief, and I have not calculated them.

## Information currently available

- **Protein:** human Cu/Zn SOD1, UniProt P00441.
- **Canonical sequence:** 154 amino acids, in `SOD1.fasta`.
- **Predicted structure:** `SOD1_alphafold_model.cif`.
- **Confidence data:** `SOD1_alphafold_pae.json`; I have not interpreted this file.
- **Overall model impression:** very clean fold, with an overall score around **98**.
- **Biology:** functional SOD1 works as two identical copies together. The supplied predicted structure contains only one copy, so apparent outside residues must be checked against the paired form.
- **Metal-site exclusions:** do not select His46, His48, His63, His71, His80, or His120. Also exclude nearby residues whose mutation could disturb metal coordination or active-site geometry.
- **Minimum local confidence:** retain only residues with per-residue confidence **≥90**.
- **Goal:** select at most three genuinely accessible, well-supported positions for surface mutagenesis, avoiding the metal site and contact region with the other SOD1 copy.

## Inputs still required before a final shortlist

### 1. Erik’s actual construct

Obtain the final construct FASTA and plasmid map. Confirm:

- SOD1 start and end
- N-terminal tag
- C-terminal tag
- Linkers and cloning residues
- Engineered substitutions
- Deletions or truncations
- Whether the construct uses canonical SOD1 numbering or its own numbering
- The exact amino-acid change intended at each selected position

Create an explicit mapping such as:

| Erik construct position | Canonical SOD1 position | Construct residue | Canonical residue | Mapping note |
|---:|---:|---|---|---|

Until this is confirmed, report positions as **provisional canonical SOD1 numbering** and do not treat them as ordering-ready.

### 2. Paired SOD1 structure

Specify the source of the structure containing both copies of SOD1. Record:

- Identifier or file name
- Experimental structure or modeled structure
- Chain labels
- Sequence correspondence of each chain
- Missing residues
- Numbering correspondence
- Whether metal ions and relevant ligands are present

For every candidate, determine whether the second copy comes close enough to cover or contact that residue. Record the measured closest distance and a simple result: **contact**, **no contact**, or **uncertain**.

### 3. Accessibility definition

Choose one numerical accessibility measure and freeze it before ranking. The record must state:

- Metric name
- Units
- Whether the calculation uses the single copy or both copies
- Probe and calculation settings
- Whether total residue or side-chain exposure is used
- Software and version
- Numerical cutoff

Do not use “looks exposed” as the final criterion. The table must contain an actual value for every candidate and the same rule must be applied to every residue.

### 4. Confidence extraction

Use the individual residue-level confidence values, not the overall value of approximately 98. Record:

- Which field in the confidence file was used
- How residue numbers were matched to the FASTA and structure
- Any missing values
- Any numbering mismatch
- Whether confidence is reported on a 0–100 scale

Only residues at or above **90** pass.

### 5. Exclusion rules

Before ranking, document exclusions for:

- His46, His48, His63, His71, His80, His120
- Residues near metal ions or their coordinating residues
- Residues contacting the second SOD1 copy
- Residues with unresolved numbering
- Residues lacking a confidence value
- Residues below the accessibility cutoff
- Residues with missing or unreliable structural information

The distance used for “near the metal site” must be stated rather than left to visual judgment.

## Required final table

Use a table with no more than three ranked candidates:

| Rank | Erik position | Canonical position | Wild-type residue | Proposed substitution | Accessibility value | Units | Local confidence | Second-copy contact | Closest contact distance | Metal-site status | Rationale |
|---:|---:|---:|---|---|---:|---|---:|---|---:|---|---|

After the table, include:

1. Excluded residues and reasons  
2. Construct-numbering assumptions  
3. Paired-structure identifier  
4. Accessibility settings and cutoff  
5. Confidence-field provenance  
6. Any unresolved limitation  
7. A clear statement that the result is **ready for ordering** or **provisional—do not order**

If fewer than two residues pass, report that directly. Do not fill the table with weaker choices.

## Experimental safeguards

The shortlist should be accompanied by controls for:

- Wild-type SOD1
- Expression level
- Solubility or folding
- Enzymatic activity
- Aggregation or inclusion-body formation
- Confirmation of the introduced sequence change
- The planned biological replicates

A loss of activity is not interpretable as a surface-specific effect if the variant is poorly expressed, misfolded, or aggregated.

## Audit record

Preserve:

- Original FASTA
- Original CIF
- Original confidence JSON
- Erik’s construct FASTA and plasmid map
- Sequence alignment
- Position mapping
- Paired-structure source
- Contact measurements
- Accessibility settings
- Confidence extraction
- Exclusion log
- Final ranked table
- Software and file versions

## Definition of a usable final shortlist

It is usable only when:

- Erik’s sequence and numbering are verified
- The two-copy structure source is documented
- The contact rule is applied
- Accessibility metric and cutoff are fixed in advance
- Every candidate has an actual accessibility value
- Every candidate has local confidence ≥90
- Metal-site and second-copy contact exclusions are documented
- The intended substitution is explicit
- The table contains at most three ranked candidates
- All assumptions and limitations are visible
- Erik or the responsible experimental lead has approved the construct mapping and substitutions

At present, you have enough to begin the audit, but not enough to produce a defensible final shortlist. The critical missing items are Erik’s construct information, the paired-structure source, the fixed accessibility rule, and the actual residue-level calculations.

**You**:

okay, can I start my task now, or is it anything more you need to add?

**Dr. Lena Brandt**:

You can start the **provisional audit** now using the three supplied files. No further scientific requirement needs adding, but the final shortlist remains blocked until you obtain Erik’s exact construct/map, identify the paired SOD1 structure or approved model, and freeze the numerical accessibility and contact rules.

Do not send residue recommendations for ordering until those three items are documented and the mapping is approved. The delivery target remains **Friday, 18 September 2026, at 09:00 Stockholm time**.

**You**:

okay, so now I need you to play everything back to me it detail so that I have some structure and better knowing of what I am supposed to do

**Dr. Lena Brandt**:

Yes. Here is the working plan in one place.

## 1. The decision

Produce a ranked shortlist of **no more than three SOD1 positions** for Erik’s surface-mutagenesis experiment.

A position is acceptable only if it:

- maps unambiguously to Erik’s actual construct;
- is numerically accessible when both SOD1 copies are considered;
- has local model confidence of at least **90**;
- is not His46, His48, His63, His71, His80, or His120;
- is not close enough to disturb metal coordination or active-site geometry;
- does not contact the second SOD1 copy;
- has a clearly specified amino-acid substitution.

The output is a structural shortlist, not proof that a mutation will preserve activity or avoid aggregation.

## 2. What you have

The supplied files are:

- `SOD1.fasta` — canonical human SOD1, 154 residues;
- `SOD1_alphafold_model.cif` — the predicted structure of one SOD1 copy;
- `SOD1_alphafold_pae.json` — accompanying confidence information whose exact contents and useful fields still need to be identified.

The overall model looked very good—around **98**—but that overall value cannot replace residue-by-residue checks.

## 3. First: verify Erik’s construct

Before assigning final residue numbers, obtain Erik’s exact construct FASTA and plasmid map. Confirm:

- SOD1 boundaries;
- N- and C-terminal tags;
- linkers and cloning residues;
- engineered substitutions;
- insertions, deletions, or truncations;
- whether the construct uses canonical SOD1 numbering or construct numbering;
- the exact substitution intended at each shortlisted position.

Align Erik’s sequence to the 154-residue canonical sequence and create a mapping table:

| Erik construct position | Canonical SOD1 position | Canonical residue | Construct residue | Note |
|---:|---:|---|---|---|

Until this is checked, any residue number is only **provisional canonical SOD1 numbering** and must not be treated as ready for ordering.

## 4. Establish the two-copy structural reference

The supplied model contains one copy. You therefore need either:

- a suitable experimental structure containing both copies, or
- an approved paired model with documented provenance and chain mapping.

Record:

- the structure or model identifier;
- whether it is experimental or modeled;
- the labels for the two copies;
- how each copy was aligned to canonical SOD1;
- missing or unresolved residues;
- whether the metal ions and their coordinating residues are represented.

For every possible candidate, determine whether the second copy comes close enough to cover or contact it. Do not infer this from the one-copy model alone.

## 5. Freeze the contact rule

Choose the numerical rule before ranking candidates. For example, define a contact using the shortest distance between non-hydrogen atoms of the candidate residue and the other SOD1 copy.

Whatever rule is approved, document:

- the distance threshold;
- the atom types included;
- the chain pair examined;
- the minimum measured distance;
- whether the side chain, backbone, or both are involved.

Each position should receive one result:

- **contact**;
- **no contact**;
- **uncertain**, if the structure is incomplete or ambiguous.

For this project, candidates marked contact should be excluded unless Erik specifically wants to study the two-copy contact region.

## 6. Freeze the accessibility rule

Choose one numerical accessibility measure and apply it consistently. The protocol must state:

- the metric;
- the units;
- whether both copies are present during calculation;
- the probe and calculation settings;
- whether total-residue or side-chain exposure is used;
- the software and version;
- the numerical passing cutoff.

Do not rank residues using visual inspection. The final table must contain the actual value for every candidate.

The cutoff must be selected **before** looking at the final ranking. If the cutoff is changed after seeing the results, record the change and treat the shortlist as provisional.

## 7. Extract local confidence

Use the residue-level confidence value associated with the structure, retaining only values of **90 or above**.

Document:

- which field supplied the value;
- how structure residues were matched to the FASTA;
- how numbering differences were handled;
- any missing values;
- whether the scale is 0–100.

The overall score around 98 is useful context, but it is not sufficient evidence for an individual residue.

## 8. Apply biological exclusions

Exclude the following histidines outright:

- His46
- His48
- His63
- His71
- His80
- His120

Also define and apply a separate distance-based exclusion around the metal ions and coordinating residues. That exclusion should cover residues that could affect metal binding or active-site geometry even if they are not histidines.

The exclusion rule must state:

- which metal atoms are considered;
- which coordinating residues are included;
- the distance threshold;
- whether direct contacts and nearby second-shell residues are excluded.

Keep an exclusion log so every rejected position has a recorded reason.

## 9. Apply the hard filters

A residue can enter the ranking only if all of these are true:

1. It maps correctly to Erik’s construct.
2. Its numerical accessibility meets the fixed cutoff.
3. Its local confidence is at least 90.
4. It is not one of the six specified histidines.
5. It is outside the defined metal-site region.
6. It does not contact the second SOD1 copy.
7. Its structure and numbering are not unresolved.
8. The proposed substitution is explicitly stated.

If no residue passes, report **no defensible candidate**. Do not fill the shortlist with weaker positions.

## 10. Define the ranking rule

After the hard filters, rank the remaining positions using a fixed rule. A reasonable order would be:

1. greater numerical accessibility;
2. higher local confidence;
3. greater distance from the metal-site region;
4. greater distance from the second-copy contact region;
5. lower expected risk from the proposed amino-acid replacement.

The substitution matters. For example, replacing a residue conservatively is not equivalent to introducing a new charge or a bulky side chain. The mutation strategy should therefore be agreed with Erik rather than silently inferred.

## 11. Produce the final table

Use no more than three rows:

| Rank | Erik position | Canonical position | Wild-type residue | Proposed substitution | Accessibility value | Units | Local confidence | Second-copy contact | Closest distance | Metal-site status | Rationale |
|---:|---:|---:|---|---|---:|---|---:|---|---:|---|---|

Below the table, include:

- excluded positions and reasons;
- the construct-numbering statement;
- the paired-structure identifier;
- the contact definition;
- the accessibility definition and cutoff;
- the source of the confidence values;
- unresolved limitations;
- either **ready for ordering** or **provisional—do not order**.

## 12. Include experimental controls

The shortlist should travel with the minimum interpretation controls:

- wild-type SOD1;
- confirmation of the introduced sequence change;
- expression measurement;
- solubility or folding assessment;
- enzyme-activity measurement;
- aggregation or inclusion-body assessment;
- the planned biological replicates.

A decrease in activity is not evidence of a surface-specific effect if the variant is poorly expressed, misfolded, or aggregated.

## 13. Preserve the audit trail

Keep the following unchanged and together:

- original FASTA;
- original CIF;
- original confidence JSON;
- Erik’s construct FASTA and plasmid map;
- sequence alignment and position mapping;
- paired-structure source;
- contact measurements;
- accessibility settings and results;
- confidence extraction;
- exclusion log;
- final ranked table;
- software and file-version information.

## 14. Definition of done

The task is complete only when:

- Erik’s exact construct and numbering are verified;
- the two-copy structural source is documented;
- the contact rule is fixed and applied;
- the accessibility metric and cutoff are fixed and applied;
- every candidate has a numerical accessibility value;
- every candidate has local confidence of at least 90;
- the metal-site exclusions are documented;
- second-copy contacts are documented;
- each proposed substitution is explicit;
- no more than three candidates are ranked;
- the table and its assumptions are reproducible;
- the result is delivered by **Friday, 18 September 2026, at 09:00 Europe/Stockholm**.

You can begin the provisional audit now, but the final shortlist remains blocked by Erik’s construct map, the approved two-copy structure or model, and the fixed numerical accessibility and contact rules. Do you already have Erik’s construct FASTA and plasmid map, or is that the first item to request?
