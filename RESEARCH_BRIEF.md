# Research question and prospective abstract

**Status: study proposal, 8 October 2026.** This abstract claims no new results. See the [study protocol](STUDY_PROTOCOL.md), [paper notes](PAPER_NOTES.md), and [overview](README.md).

## Research question

Among raw commercial Solix output and prespecified machine-learning methods applied to the same held-out optic-disc OCT scans, which produces peripapillary RNFL measurements closest to an independently adjudicated manual reference, and do its measurements improve out-of-sample prediction of monocular contrast threshold?

The clinical extension is separate: in a cohort with confirmed optic-neuritis labels and longitudinal MS outcomes, do these measurements add predictive information beyond established clinical variables? Without those labels and follow-up, this study cannot estimate early optic-neuritis detection or an individual MS risk score.

## Why the attached contrast-sensitivity paper matters

Azhar et al., *Rapid, Robust, and Reliable Assessment of Contrast Sensitivity in Augmented Reality* (attached manuscript), studied mostly healthy young participants, not an optic-neuritis or MS diagnostic cohort. It reports headset test-retest correlation 0.80 versus 0.49 for Pelli-Robson charts. In its retained OCT analyses, n=93 contributed GCC data and n=77 RNFL data after scan quality exclusions. Headset contrast threshold was associated with inferior-temporal peripapillary RNFL thickness (r=-0.23, FDR-adjusted p about 0.04), while chart-based contrast sensitivity showed no significant sector association. Negative r reflects lower, better contrast thresholds with thicker tissue. The RNFL result weakened to a nonsignificant trend when headset thresholds were discretized (pFDR=0.058). These are modest associations, not evidence that a particular segmentation model improves function prediction or diagnoses disease.

The manuscript used a 2.5-4.5 mm diameter peripapillary annulus, eight Garway-Heath sectors, and manual review/refinement of Solix segmentation (10 RNFL scans refined). Our comparisons should reproduce this geometry and laterality mapping exactly where possible. The paper's contrast-sensitivity data must be linked at the participant-eye level to the OCT volumes before a structure-function comparison is feasible.

## Prespecified comparison

1. **Reference:** trained-annotator RNFL boundary traces, reviewed by the neurobiology expert, with a written annotation protocol, masked adjudication, and a repeat-read subset to quantify intra-observer agreement. Call this an *expert-adjudicated reference standard*, not a biological ground truth. Where the corrected TSV is derived from the commercial curve, quantify edited columns separately and avoid treating unedited accepted curves as independent manual labels.
2. **Methods:** raw Solix segmentation; the existing biplanar 2.5D residual U-Net with boundary heads; the existing dense 3D U-Net; and the existing hybrid CNN-transformer/TransUNet variant. Implementations live in the sibling train-cnn-models repository. Compare frozen checkpoints and pipelines; an architecture-specific claim would require matched training and inference conditions.
3. **Fair test set:** same eyes/scans for every method, with subject-level isolation across pretraining, fine-tuning, model selection, and evaluation. Historical checkpoints trained on different subjects belong in a mutually unseen intersection analysis. Preserve native OS orientation, surface-guided clamping, and cup-reach settings used in the established evaluation pipeline.
4. **Segmentation endpoints:** primary peripapillary RNFL boundary mean absolute error in micrometers on the adjudicated scans; secondary 95th-percentile error, thickness bias and limits of agreement, sector errors, failure/QC rates, and Dice where meaningful. Report paired effect sizes and subject-bootstrap confidence intervals. Evaluate both all reference columns and corrected/problematic columns.
5. **Functional endpoint:** on eyes with same-visit headset testing, compare out-of-sample prediction of monocular log contrast threshold from identical sector RNFL features for each segmentation method. Use the same regression specification and covariates for every method, keep both eyes from a participant in one fold, and report cross-validated MAE/R² with paired confidence intervals. Compare against commercial output and a covariate-only model; a manual-reference feature analysis is context, not an algorithmic competitor or guaranteed upper bound. Prespecify inferior-temporal RNFL as a key sector from the attached paper; adjust for multiple exploratory sectors.
6. **Clinical extension, only with suitable data:** adjudicated optic-neuritis diagnosis, symptom timing, treatment, MRI/clinical variables, and longitudinal MS conversion. Acute swelling can complicate RNFL interpretation, so specify the post-event time window and consider macular GCC/GCIPL separately. A calibrated MS-risk model needs enough incident events, fixed prediction horizon, external validation, and comparison with standard clinical predictors. Do not produce patient-facing scores from the current segmentation cohort.

## Prospective abstract (proposal, not results)

**Background:** Peripapillary RNFL thickness is an OCT biomarker of optic nerve injury, but automated boundary errors may obscure subtle structure-function relationships. A recent augmented-reality contrast-sensitivity study identified a modest association with inferior-temporal RNFL thickness in healthy adults.

**Objective:** To determine whether alternative OCT segmentation methods improve agreement with expert-adjudicated RNFL boundaries and prediction of monocular contrast sensitivity relative to raw commercial segmentation.

**Methods:** We will compare raw commercial Solix output with prespecified biplanar residual U-Net, dense 3D U-Net, and hybrid CNN-transformer segmentation approaches on identical optic-disc OCT volumes. Evaluation will use subject-disjoint held-out scans and an expert-adjudicated reference, emphasizing boundary error, regional thickness bias, and failure rates. In participants with paired headset contrast-sensitivity measurements, we will compare cross-validated structure-function prediction using identical sector definitions and covariates.

**Expected contribution:** The study will establish whether gains in boundary accuracy translate into measurable functional value. Optic-neuritis detection and MS-risk prediction will be assessed only in a separate, appropriately labeled clinical cohort.

## Immediate dependencies

- Confirm the attached manuscript's data sharing permission and obtain eye-linked headset contrast thresholds, visit dates, Solix OCT volumes, and QC exclusions.
- Inventory independent manual annotations, adjudication records, and any second-reader/repeat-read data.
- Freeze the common held-out subject manifest and model checkpoints, then run the paired commercial-versus-model evaluation.
- Ask the neurobiologist to approve the annotation protocol, clinically important sectors, optic-neuritis definition, and disease timing before finalizing the analysis plan.

## Clinical context for the eventual introduction

- [Petzold et al., Lancet Neurology 2010](https://pubmed.ncbi.nlm.nih.gov/20723847/): RNFL thinning after optic neuritis and in MS without optic neuritis.
- [A 2024 cohort of 127 MS patients](https://pubmed.ncbi.nlm.nih.gov/39410602/) reported optic neuritis as an initial symptom in 25.53%. This is cohort-specific, not a claim that 25% of MS cases are caused by optic neuritis.
- [A systematic review](https://pubmed.ncbi.nlm.nih.gov/28567539/) found that ganglion-cell thinning can be detected earlier than RNFL thinning after acute optic neuritis; timing is essential to any early-detection claim.
