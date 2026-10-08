# Study protocol: boundary accuracy, visual function, clinical extension

**Version:** proposal, 8 October 2026. All hypotheses, eligibility rules, endpoints, and analysis choices below should be frozen before a new final test set is inspected. Existing retrospective benchmarks are context, not results of this protocol.

## 1. Study logic and hypotheses

| Stage | Question | Primary evidence needed | Status |
| --- | --- | --- | --- |
| A. Imaging | Which automated method most closely matches expert-adjudicated RNFL boundaries? | Paired boundary error on the same held-out eyes with raw commercial output and independent manual review | Preliminary model-only and 10-eye commercial analyses exist |
| B. Function | Do its regional thickness measurements predict monocular contrast threshold better? | Lower out-of-sample prediction error than commercial-derived features on the same participant–eye–visit records | Linked outcomes not yet verified |
| C. Clinical | Does it add information about ON and future MS beyond clinical variables? | Independently validated ON labels and longitudinal MS conversion with clinical baselines | Separate future study |

**H1 (imaging):** At least one ML method reduces mean per-eye posterior RNFL boundary absolute error versus raw commercial output on a shared, independently adjudicated test set. A null or worse result is informative.

**H2 (function):** Thickness features from the method selected using imaging data reduce held-out monocular log contrast-threshold prediction error versus raw commercial features. The imaging selection must not use the final function-test labels.

The two hypotheses can disagree. Better traces may make little difference to sector averages, and RNFL thickness explains only part of visual function. The study should report both outcomes even if only one improves.

## 2. Study populations and data linkage

| Set | Required records | Unit of analysis | Main restriction |
| --- | --- | --- | --- |
| A: paired imaging | Optic-disc DICOM, raw Solix curve, expert-adjudicated ILM/RNFL boundaries, scan QC | Eye/scan, clustered by participant | Every method evaluated on the same scans |
| B: structure–function | Set A plus monocular headset threshold and test date, with eye and visit linkage | Participant–eye–visit | Same-visit window fixed before analysis; both eyes stay in one fold |
| C: clinical extension | New or linked clinical cohort with ON diagnosis and onset date, treatment, MRI, relevant ocular disorders, longitudinal MS diagnosis | Participant and eye over time | Separate study plan and independent validation |

The attached manuscript reports 77 participants retained for RNFL analysis after QC. That number is **not** the available sample size for Set B until records are linked and data access is confirmed. The existing 40-eye segmentation benchmark is likewise not automatically the manuscript's contrast-sensitivity cohort. Publish a de-identified flow table: screened participants → OCT acquired → QC retained → raw-commercial available → independently annotated → headset linked → final paired set, with eye and participant counts at every step.

### Eligibility and quality control

- Use the manuscript's optic-disc scan geometry where possible: 6 × 6 mm disc scan and a disc-centered annulus with **2.5–4.5 mm diameters**, divided into eight Garway-Heath sectors. Document the disc center, physical calibration, eye laterality, and sector orientation.
- Apply a fixed scan-quality policy before model results are opened. The manuscript excluded SSI < 60, obvious motion artifacts, incomplete field of view, or retinal integrity issues (p. 8). Record exact reasons and inspect how exclusions affect representativeness.
- Keep technical segmentation failures in the denominator and report their rate. A method must not improve its mean error by silently dropping its hardest eyes.
- Confirm headset psychometric QC and outcome definition from the source data. Use one continuous monocular log contrast threshold per prespecified eye/visit; lower threshold means better sensitivity. Do not conflate threshold with log contrast sensitivity, whose sign is reversed.
- Record axial length if available, refractive error, acuity, age, scan quality, and relevant ocular disease. The manuscript did not measure axial length, leaving possible confounding (p. 20).

## 3. Reference standard and bias controls

**Target reference:** A trained annotator traces both ILM and posterior RNFL boundaries using a written protocol, blinded to commercial/ML outputs, headset outcome, and clinical status. A neurobiology or neuro-ophthalmology expert reviews uncertain regions and signs off adjudications. Save original traces, revisions, reviewer identity, and reasons for change. Repeat a masked subset after a washout period; add a second independent reader if feasible, reporting intra- and inter-reader boundary agreement.

**Current label caveat:** In the Solix data, paired bad/good TSV curves often represent *commercial output followed by human correction*, and good-only curves may have been accepted unchanged. Those are valuable training and stress-test labels, but their unchanged columns are not independent manual observations. Report edited columns separately from unedited columns. If fresh independent traces cannot be obtained, describe the reference as a **human-reviewed commercial-derived reference** and limit the strength of the conclusion.

Mask annotation and adjudication from the final model predictions. Do not use final test-set traces to fine-tune models, choose a threshold, or redesign postprocessing.

## 4. Comparison arms and reproducibility

| Arm | Implementation in sibling training repo | Frozen item |
| --- | --- | --- |
| Raw Solix | Original uncorrected device boundaries, before manual refinement | Export version and original TSV/XML |
| Biplanar 2.5D | Residual U-Net with five-slice context, orthogonal fusion, mask and boundary heads | Checkpoint, fusion, threshold, preprocessing |
| Dense 3D | Anisotropic dense 3D U-Net | Checkpoint, tiling/inference, preprocessing |
| Hybrid CNN-transformer | Existing TransUNetRNFLNet with CNN encoder, transformer bottleneck, decoder, boundary heads | Checkpoint, fusion, preprocessing |

The 2.5D and hybrid implementations are in train-cnn-models/model_training/train_rnfl_volumetric; the dense 3D implementation is in train-cnn-models/model_training/train_rnfl_3d. These are **architectural families**, not four generic U-Nets. A future simple baseline may be added only if its selection and training budget are declared before final testing. The evaluated TransUNet checkpoint's performance cannot establish a general verdict on transformers.

Use native-coordinate restoration for left eyes (OS orientation mode corrected), surface-guided clamping, and cup-reach disc handling where the evaluation pipeline requires them. Make sector thickness calculations identical across arms; retain a reproducible export of each boundary and per-eye feature. Record code commit, checkpoint hash, training manifest, inference settings, and data version.

### Split firewall

- Split at participant level across **all** training, pretraining, fine-tuning, model selection, and final evaluation. An eye from a held-out participant cannot enter any earlier phase.
- A historical checkpoint with a different training split is comparable only on the intersection of participants unseen by every candidate. Do not pool in-sample and held-out eyes.
- Freeze a common final test manifest. Set B must keep both eyes and repeated visits from each participant in the same cross-validation fold.
- If models are retrained for a controlled architecture comparison, match available data, training budget, augmentation policy, and inference procedure as closely as possible. Otherwise label results as a **checkpoint/pipeline comparison**, not an isolated architectural effect.

## 5. Outcomes and analysis

### Stage A: segmentation and thickness

**Primary imaging endpoint:** Per-eye mean absolute posterior RNFL boundary error in µm within the common 2.5–4.5 mm diameter annulus, relative to the adjudicated reference. Choose the summary over eyes (mean and paired difference) before testing. Report the per-eye distribution as well.

**Secondary endpoints:** ILM boundary error, 95th-percentile column error, RNFL thickness bias (predicted minus reference), sector-specific error, Bland–Altman limits of agreement, mask Dice where interpretable, optic-cup-region error, QC/failure rate, and computational cost. Analyze all eligible columns and the human-corrected/problematic columns separately. The latter is a sensitivity/stress analysis, not a substitute for the full scan.

Each method–commercial contrast uses **paired eyes**. Estimate confidence intervals by resampling participants, keeping both eyes together. If formal significance tests are used for multiple ML-versus-commercial contrasts, prespecify a family-wise correction (for example Holm). Show clinically meaningful error magnitude, not just p-values. A “best” method requires a declared primary ranking rule and uncertainty; ties or tradeoffs should be reported plainly.

### Stage B: contrast-threshold prediction

**Primary functional endpoint:** Difference in participant-held-out mean absolute error (MAE) for continuous monocular log contrast threshold between RNFL features from the Stage-A-selected method and raw Solix features. A covariate-only model establishes whether RNFL features add value at all. Report out-of-fold R² as a secondary metric, including negative values.

Use exactly the same participants, eyes, visits, annulus, sectors, covariates, missing-data rule, and regression family for each segmentation arm. Fit imputation, scaling, hyperparameters, and feature selection *inside* training folds. Keep all records from one participant together; use nested grouped validation if tuning is necessary. Estimate paired MAE differences and participant-bootstrap intervals on out-of-fold predictions. Run a reference-derived feature analysis as context, **not as a guaranteed upper bound** or automated competitor.

Predeclare inferior-temporal RNFL as the anatomical sector of interest because the attached paper found an association there. Any full eight-sector search is exploratory and needs multiplicity control. Avoid reusing the paper's p-value as proof of improved prediction. If the paired sample is small, simplify the regression and report imprecision rather than overfit.

### Stage C: ON and MS, separate clinical validation

The optic-neuritis question needs an adjudicated disease label, symptom onset, time from event to OCT, treatment, fellow-eye history, and differential diagnoses. Acute RNFL swelling may reverse or mask the expected thinning; stratify by a clinician-approved post-event window and consider macular GCIPL/GCL as a complementary biomarker. Evaluate detection against a clinical baseline with sensitivity at a prespecified specificity, discrimination, calibration, and subgroup/failure analysis.

An MS-risk analysis needs a defined starting population (for example first ON episode), baseline date, fixed horizon, incident conversion definition, enough events, complete follow-up, MRI and other established predictors, and external validation. Compare incremental value of OCT measurements against a clinical/MRI model. Do not issue patient-facing risk scores from the current segmentation or healthy contrast-sensitivity cohorts.

## 6. Existing evidence and what it does not show

The local 8 October 2026 three-way report in OCT-Analyser-Capstone/docs/cohort_reports/three_way_architecture_comparison evaluated 20 mutually held-out subjects / 40 eyes against the available human-reviewed curves:

| Metric | Biplanar 2.5D | Dense 3D | Evaluated TransUNet |
| --- | ---: | ---: | ---: |
| Median boundary MABE | **4.71 µm** | 5.50 µm | 31.90 µm |
| Mean boundary MABE | 6.22 µm | **5.87 µm** | 42.69 µm |
| Mean cup IoU | **0.9388** | 0.9085 | 0.7282 |

On the **10 corrected eyes with raw commercial curves**, mean MABE was 5.17 µm commercial, 5.13 µm biplanar, 6.12 µm dense 3D, and 35.71 µm TransUNet; biplanar beat commercial per eye in 4/10. The reference was partly derived by correcting commercial output. Therefore these data identify promising checkpoints and failure modes but do not establish a general ML advantage over commercial output, independent gold-standard agreement, visual-function gain, or clinical benefit. The older multi-model benchmark also documented split asymmetry; use only mutually unseen subjects when reusing historical checkpoints.

## 7. Decision gates and deliverables

1. **Linkage gate:** a validated participant–eye–visit crosswalk, data rights, and a flow table.
2. **Reference gate:** annotation protocol, masked adjudication, repeat-read agreement, and explicit independent-versus-commercial-derived label counts.
3. **Freeze gate:** final participant split, checkpoints, model hashes, endpoints, annulus/sector mapping, covariates, and analysis plan.
4. **Imaging report:** paired method table, uncertainty, per-sector error map, representative successes and failures, and complete denominators.
5. **Function report:** out-of-fold predictions, paired MAE/R², covariate-only comparison, sensitivity analyses, and failure/selection audit.
6. **Clinical decision:** with a clinician, determine whether a separate ON/MS cohort is adequate; only then draft diagnostic and risk claims.

## Source pointers

- Supplied manuscript: Azhar, Cundric, Bangera, and Rokers, *Rapid, Robust, and Reliable Assessment of Contrast Sensitivity in Augmented Reality*, especially pp. 8, 10–11, 15–17, 20. See [paper notes](PAPER_NOTES.md).
- Local model benchmark: OCT-Analyser-Capstone/docs/cohort_reports/three_way_architecture_comparison/research_report_tri_model_comparison.md (uncommitted sibling-repo artifact at this writing).
- Local split warning: OCT-Analyser-Capstone/docs/cohort_reports/multi_model_validation_benchmark/multi_model_validation_benchmark_report.md.
- Clinical context: [RNFL meta-analysis](https://pubmed.ncbi.nlm.nih.gov/20723847/), [early GCL/GCIPL changes after ON](https://pubmed.ncbi.nlm.nih.gov/28567539/), [acute ON swelling study](https://pubmed.ncbi.nlm.nih.gov/26362894/), [ONTT long-term MS risk](https://pubmed.ncbi.nlm.nih.gov/18541792/), and [OSCAR-IB OCT QC validation](https://pubmed.ncbi.nlm.nih.gov/24948688/).
