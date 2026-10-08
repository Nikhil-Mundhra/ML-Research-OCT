# Reading notes: augmented-reality contrast-sensitivity paper

**Source reviewed:** the user-supplied 47-page PDF whose first page titles the manuscript *Rapid, Robust, and Reliable Assessment of Contrast Sensitivity in Augmented Reality*, by Abraiz Azhar, Katja Cundric, Namrata Bangera, and Bas Rokers. The attachment's filename abbreviates this title. These notes cite the **PDF's printed page numbers**. The manuscript itself is not redistributed in this repository.

## The useful result in one sentence

In a mostly healthy young sample, an adaptive headset contrast threshold was more repeatable than a Pelli-Robson chart score, and the headset measure showed a **modest** association with inferior-temporal peripapillary RNFL thickness that the chart did not detect. This makes a careful RNFL measurement–visual function comparison worth testing; it does **not** establish which segmentation algorithm is best or diagnose optic neuritis or MS.

## What the paper did

| Component | Reported design or result | Where |
| --- | --- | --- |
| People | 99 recruited, mean age 23 ± 5 years; OCT acquired in 98. After OCT QC, 93 contributed GCC analysis and 77 RNFL analysis. These are participant counts, not guaranteed eye-linked records for our study. | pp. 5, 8, 14 |
| Functional test | Monocular AR headset task with adaptively sampled Sloan letters and a fitted continuous contrast threshold; 30 participants completed test–retest sessions. Pelli-Robson chart measured a coarser threshold. | pp. 5–7, 9–11 |
| Test–retest | Headset r = 0.80 versus chart r = 0.49 in the 30-person repeat subset; reported 95% Bland–Altman limits were ±0.83% versus ±1.04% contrast. A correlation alone is not a full agreement statistic, so both are relevant. | pp. 9–11 |
| OCT | Visionix Solix; 6 × 6 mm optic-disc scan for RNFL and 6.4 × 6.4 mm macular scan for GCC. RNFL analysis used the disc-centered 2.5–4.5 mm **diameter** annulus and eight Garway-Heath sectors. | p. 8 |
| OCT QC and labels | Two trained raters inspected scans; SSI < 60, motion, incomplete coverage, or retinal integrity issues led to exclusion (21 RNFL scans). Commercial segmentation was manually refined for 10 RNFL scans. The paper does not present those refinements as independent fully manual tracings. | p. 8 |
| RNFL association | Inferior-temporal RNFL thickness and headset contrast threshold: r = -0.23, FDR-adjusted p ≈ 0.04. Greater thickness corresponded to a lower (better) threshold. No chart-based sector association reached significance. | pp. 15–17 |
| Other structure | Nasal and temporal 1–3 mm macular GCC sectors were also associated with headset threshold; the strongest listed was nasal GCC r = -0.29, FDR-adjusted p = 0.005. | pp. 15–16 |
| Robustness caveat | After discretizing headset thresholds to the chart's grid, the inferior-temporal RNFL result became a nonsignificant trend (r = -0.20, FDR-adjusted p = 0.058); GCC associations remained significant. | pp. 16–17 |
| Limitations | Axial length was unmeasured; the stimulus used one fixed letter size, rather than a full contrast-sensitivity function; the sample was young, healthy, and narrow. Clinical utility in patient populations was explicitly left for future testing. | p. 20 |

The sector findings were from linear mixed-effects analyses with participant as a random effect and FDR correction across sectors (pp. 7–8, 15). They are **within-sample associations**, not estimates of out-of-sample predictive gain from an ML segmentation method. The negative correlation is expected for a threshold outcome: a smaller required contrast is better.

## How to use it in our study

| Transfer from the paper | Required adaptation |
| --- | --- |
| Use the 2.5–4.5 mm peripapillary annulus and eight Garway-Heath sectors so sector labels are comparable. | Verify physical scale, disc center, laterality restoration, scan protocol, and how sector maps are generated from our volumes. |
| Prespecify the inferior-temporal sector as a biologically motivated analysis. | Test all methods on the same eyes, avoid selecting a sector after seeing our outcome, and adjust exploratory sector comparisons. |
| Prefer the continuous monocular headset threshold as the functional outcome. | Confirm participant–eye–visit IDs, timing, calibration, psychometric exclusions, and data-sharing rights before any model claim. |
| Include commercial Solix output as a baseline. | Preserve the **raw** uncorrected export separately from the 10 manually refined paper scans. A corrected curve cannot serve as both raw baseline and independent reference. |
| Treat a function link as a measure of potential utility. | Compare **held-out prediction** against a covariate-only model and raw commercial features. A stronger correlation on a selected cohort is insufficient. |

## What the paper cannot support

- It provides no comparison of residual U-Net, dense 3D U-Net, TransUNet, or raw commercial boundaries against independent expert traces.
- It does not show that reducing RNFL boundary error improves headset contrast-threshold prediction. That is our proposed experiment.
- It did not recruit an ON diagnostic cohort or follow participants for MS conversion. Its findings cannot estimate early ON detection, diagnostic sensitivity, or individual MS risk.
- The manuscript's 77 RNFL participants cannot be combined by assumption with the sibling repository's 40 held-out segmentation eyes. Match identities, laterality, visits, and access rights first.
- The result does not mean ON “causes 25% of MS.” A separate 127-person MS cohort reported ON as the initial symptom in 25.53%; that is a specific frequency, not a causal fraction ([source](https://pubmed.ncbi.nlm.nih.gov/39410602/)).

## Useful clinical framing for the introduction

RNFL thinning after ON and in MS without ON is supported by a [systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/20723847/). However, at acute ON presentation, RNFL swelling can obscure early loss, while ganglion-cell/inner-plexiform measures can thin earlier ([prospective ON study](https://pubmed.ncbi.nlm.nih.gov/26362894/); [systematic review](https://pubmed.ncbi.nlm.nih.gov/28567539/)). A structural marker therefore cannot be presented as a universal early ON detector without symptom timing and a clinical reference diagnosis. MRI findings at ON presentation are also a strong predictor of later MS in the [Optic Neuritis Treatment Trial follow-up](https://pubmed.ncbi.nlm.nih.gov/18541792/), so any OCT-based MS model must test incremental value over MRI and other standard variables.

## Questions to take to the paper team

1. Can the headset threshold, OCT volume, raw Solix boundary export, scan QC, laterality, and visit date be linked by participant and eye?
2. Which ten RNFL scans were manually refined, and are both pre- and post-refinement boundaries available?
3. Were axial length, refractive correction, acuity, disease history, or repeat headset sessions recorded for the linked OCT subset?
4. Are the corrected boundaries licensed for our secondary analysis, and may de-identified derived figures be published?
5. Can a masked expert adjudicate a fresh subset independently of commercial curves and model output?
