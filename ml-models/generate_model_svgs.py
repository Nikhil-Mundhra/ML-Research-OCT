"""
generate_model_svgs.py
======================
Generates 7 standalone, publication-quality, high-resolution SVG diagrams
and companion crisp Retina PNGs for all Frontier ML Models in ML-Research-OCT.

Features:
- Wide canvas layouts (up to 2000px) with generous container padding
- Multi-line split equations preventing any text from leaking out of bounds
- Explicit pixel width & height on all SVGs for crisp browser and GitHub rendering
- Large, high-contrast typography (13px - 28px) for perfect readability
- Automated rendering of 3200px-wide Retina PNGs with exact aspect-ratio cropping (0 white space)
"""

import os
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image

SVG_DIR = "/Users/nikhilmundhra/Documents/Github/Capstone/ML-Research-OCT/ml-models/svg"
os.makedirs(SVG_DIR, exist_ok=True)

COMMON_DEFS = """
  <defs>
    <linearGradient id="grad-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c14" />
      <stop offset="50%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="grad-card" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.98" />
    </linearGradient>
    <linearGradient id="grad-blue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#0284c7" />
    </linearGradient>
    <linearGradient id="grad-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" />
      <stop offset="100%" stop-color="#0891b2" />
    </linearGradient>
    <linearGradient id="grad-teal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2dd4bf" />
      <stop offset="100%" stop-color="#0d9488" />
    </linearGradient>
    <linearGradient id="grad-purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#7e22ce" />
    </linearGradient>
    <linearGradient id="grad-amber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
    <linearGradient id="grad-rose" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fb7185" />
      <stop offset="100%" stop-color="#e11d48" />
    </linearGradient>
    <linearGradient id="grad-emerald" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399" />
      <stop offset="100%" stop-color="#059669" />
    </linearGradient>
    <linearGradient id="grad-indigo" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#4f46e5" />
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#94a3b8" />
    </marker>
    <marker id="arrow-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#2dd4bf" />
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#38bdf8" />
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#c084fc" />
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#fbbf24" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#34d399" />
    </marker>
  </defs>
"""

# ==============================================================================
# 1. MASTER TAXONOMY & BENCHMARK MATRIX (2000 x 1340)
# ==============================================================================
def generate_master_taxonomy():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2000 1340" width="2000" height="1340">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="2000" height="1340" fill="url(#grad-bg)"/>
  
  <!-- Subtle Grid Pattern -->
  <g opacity="0.04">
    <path d="{' '.join([f'M {x} 0 L {x} 1340' for x in range(0, 2000, 50)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 2000 {y}' for y in range(0, 1340, 50)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header Banner -->
  <g transform="translate(50, 40)">
    <rect width="1900" height="105" rx="14" fill="url(#grad-card)" stroke="#334155" stroke-width="1.8"/>
    <rect width="10" height="105" rx="5" fill="url(#grad-teal)"/>
    <text x="36" y="44" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="800" fill="#f8fafc">FRONTIER ML MODEL TAXONOMY &amp; BENCHMARK MATRIX</text>
    <text x="36" y="76" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="500" fill="#94a3b8">Comprehensive Architectural Lineage for Optovue Solix Peripapillary RNFL Volumetric OCT Segmentation</text>
    <rect x="1630" y="32" width="230" height="42" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <text x="1745" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">HELD-OUT 40-EYE V2 SPLIT</text>
  </g>

  <!-- 5 Architecture Columns: Card Width = 360px, Gap = 25px, Start = 50px -->

  <!-- CARD 1: Single-Planar 1.6M (x=50) -->
  <g transform="translate(50, 170)">
    <rect width="360" height="820" rx="14" fill="url(#grad-card)" stroke="#1e293b" stroke-width="1.8"/>
    <rect width="360" height="8" rx="4" fill="url(#grad-blue)"/>
    
    <text x="24" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#38bdf8" letter-spacing="1">FEASIBILITY BASELINE</text>
    <text x="24" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#f8fafc">Single-Planar 1.6M</text>
    <text x="24" y="92" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#64748b">Job: 18043443 (Light Volumetric)</text>

    <!-- Specs Box (x=18, y=110, w=324, h=310) -->
    <rect x="18" y="110" width="324" height="310" rx="10" fill="#0b1120" stroke="#1e293b"/>
    <text x="32" y="142" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Parameters: <tspan fill="#f1f5f9" font-weight="700">1,672,021 (~1.67M)</tspan></text>
    <text x="32" y="178" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Base Channels: <tspan fill="#f1f5f9" font-weight="700">16 ch</tspan></text>
    <text x="32" y="214" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Input Context: <tspan fill="#f1f5f9" font-weight="700">2.5D (5 Slices)</tspan></text>
    <text x="32" y="250" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Inference Axis: <tspan fill="#f1f5f9" font-weight="700">Horizontal (X-Z) Only</tspan></text>
    <text x="32" y="286" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Surface Heads: <tspan fill="#f1f5f9" font-weight="700">Dense + 1D ILM/NFL</tspan></text>
    <text x="32" y="322" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Tilt Invariance: <tspan fill="#f43f5e" font-weight="700">None (Native Grid)</tspan></text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Orthogonal Fusion: <tspan fill="#64748b" font-weight="700">Disabled</tspan></text>
    <text x="32" y="394" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Post-Processing: <tspan fill="#f1f5f9" font-weight="700">Standard Threshold</tspan></text>

    <!-- Key Metrics Box (x=18, y=440, w=324, h=270) -->
    <rect x="18" y="440" width="324" height="270" rx="10" fill="#0f172a" stroke="#334155"/>
    <text x="32" y="474" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#38bdf8">Held-Out V2 Benchmark (40 Eyes)</text>
    <text x="32" y="512" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median Dice: <tspan fill="#f8fafc" font-weight="700">0.8055</tspan></text>
    <text x="32" y="550" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median MABE: <tspan fill="#f8fafc" font-weight="700">12.58 µm</tspan></text>
    <text x="32" y="588" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Mean MABE: <tspan fill="#f8fafc" font-weight="700">20.18 ± 19.52 µm</tspan></text>
    <text x="32" y="626" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median P95: <tspan fill="#f8fafc" font-weight="700">32.96 µm</tspan></text>
    <text x="32" y="664" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Cup IoU: <tspan fill="#f8fafc" font-weight="700">0.8422</tspan></text>

    <!-- Verdict Badge (x=18, y=730, w=324, h=68) -->
    <rect x="18" y="730" width="324" height="68" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-dasharray="4 4"/>
    <text x="32" y="756" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" fill="#38bdf8">ROLE: Initial Proof-of-Concept</text>
    <text x="32" y="778" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">High inter-slice jitter along slow axis.</text>
  </g>

  <!-- CARD 2: Bi-Planar 1.6M / 6.5M (x=435) -->
  <g transform="translate(435, 170)">
    <rect width="360" height="820" rx="14" fill="url(#grad-card)" stroke="#0d9488" stroke-width="2.2"/>
    <rect width="360" height="8" rx="4" fill="url(#grad-teal)"/>
    
    <rect x="200" y="22" width="140" height="24" rx="6" fill="#042f2e" stroke="#14b8a6"/>
    <text x="270" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" fill="#2dd4bf" text-anchor="middle">LEAD CANDIDATE</text>

    <text x="24" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#2dd4bf" letter-spacing="1">ORTHOGONAL FUSION</text>
    <text x="24" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#f8fafc">Bi-Planar 1.6M / 6.5M</text>
    <text x="24" y="92" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#64748b">Jobs: 18223981 (16ch) / 18563914 (32ch)</text>

    <!-- Specs Box -->
    <rect x="18" y="110" width="324" height="310" rx="10" fill="#042f2e" stroke="#0d9488"/>
    <text x="32" y="142" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Parameters: <tspan fill="#f1f5f9" font-weight="700">1.67M (16ch) | 6.58M (32ch)</tspan></text>
    <text x="32" y="178" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Base Channels: <tspan fill="#f1f5f9" font-weight="700">16 ch or 32 ch</tspan></text>
    <text x="32" y="214" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Input Context: <tspan fill="#2dd4bf" font-weight="700">Dual Orthogonal 2.5D</tspan></text>
    <text x="32" y="250" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Inference Planes: <tspan fill="#2dd4bf" font-weight="700">Fast X-Z &amp; Slow Y-Z</tspan></text>
    <text x="32" y="286" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Fusion Method: <tspan fill="#2dd4bf" font-weight="700">3D Consensus Average</tspan></text>
    <text x="32" y="322" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Tilt Invariance: <tspan fill="#cbd5e1" font-weight="700">Native + Biplanar Stabilized</tspan></text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Surface Clamping: <tspan fill="#34d399" font-weight="700">Guided RPE (2.0 px)</tspan></text>
    <text x="32" y="394" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Cup Tracking: <tspan fill="#34d399" font-weight="700">Dynamic Cup-Reach Head</tspan></text>

    <!-- Key Metrics Box -->
    <rect x="18" y="440" width="324" height="270" rx="10" fill="#042f2e" stroke="#14b8a6"/>
    <text x="32" y="474" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#2dd4bf">Held-Out V2 Benchmark (32ch)</text>
    <text x="32" y="512" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median Dice: <tspan fill="#34d399" font-weight="800">0.9518 (BEST)</tspan></text>
    <text x="32" y="550" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median MABE: <tspan fill="#34d399" font-weight="800">4.71 µm (BEST)</tspan></text>
    <text x="32" y="588" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Mean MABE: <tspan fill="#f8fafc" font-weight="700">6.22 ± 5.91 µm</tspan></text>
    <text x="32" y="626" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median P95: <tspan fill="#34d399" font-weight="800">16.85 µm (BEST)</tspan></text>
    <text x="32" y="664" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Cup IoU: <tspan fill="#34d399" font-weight="800">0.9388 (BEST)</tspan></text>

    <!-- Verdict Badge -->
    <rect x="18" y="730" width="324" height="68" rx="8" fill="#0f2926" stroke="#2dd4bf"/>
    <text x="32" y="756" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" fill="#2dd4bf">ROLE: Lead Research Champion</text>
    <text x="32" y="778" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">Won on 34 / 40 held-out eyes.</text>
  </g>

  <!-- CARD 3: Canonical STN 6.6M (x=820) -->
  <g transform="translate(820, 170)">
    <rect width="360" height="820" rx="14" fill="url(#grad-card)" stroke="#d97706" stroke-width="1.8"/>
    <rect width="360" height="8" rx="4" fill="url(#grad-amber)"/>
    
    <rect x="200" y="22" width="140" height="24" rx="6" fill="#451a03" stroke="#f59e0b"/>
    <text x="270" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" fill="#fbbf24" text-anchor="middle">STN CANONICAL</text>

    <text x="24" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#fbbf24" letter-spacing="1">TILT-INVARIANT STN</text>
    <text x="24" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#f8fafc">Canonical STN 6.6M</text>
    <text x="24" y="92" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#64748b">Job: 18697275 (STN-Net)</text>

    <!-- Specs Box -->
    <rect x="18" y="110" width="324" height="310" rx="10" fill="#0b1120" stroke="#451a03"/>
    <text x="32" y="142" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Parameters: <tspan fill="#f1f5f9" font-weight="700">6,608,983 (~6.61M)</tspan></text>
    <text x="32" y="178" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Base Channels: <tspan fill="#f1f5f9" font-weight="700">32 ch + STN Head</tspan></text>
    <text x="32" y="214" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">STN Mechanism: <tspan fill="#fbbf24" font-weight="700">Differentiable Affine</tspan></text>
    <text x="32" y="250" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Tilt Bounds: <tspan fill="#fbbf24" font-weight="700">θ ∈ [-25.0°, +25.0°]</tspan></text>
    <text x="32" y="286" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Shift Bounds: <tspan fill="#fbbf24" font-weight="700">t_y ∈ [-20%, +20%]</tspan></text>
    <text x="32" y="322" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Warping Grid: <tspan fill="#f1f5f9" font-weight="700">Bilinear Grid Sampler</tspan></text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Coordinate Space: <tspan fill="#34d399" font-weight="700">Closed-Loop Invertible</tspan></text>
    <text x="32" y="394" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Optimization: <tspan fill="#f1f5f9" font-weight="700">End-to-End Native Loss</tspan></text>

    <!-- Key Metrics Box -->
    <rect x="18" y="440" width="324" height="270" rx="10" fill="#0f172a" stroke="#78350f"/>
    <text x="32" y="474" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#fbbf24">Stress Test / Tilt Robustness</text>
    <text x="32" y="512" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Canonical Dice: <tspan fill="#f8fafc" font-weight="700">0.9412</tspan></text>
    <text x="32" y="550" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Mean MABE: <tspan fill="#f8fafc" font-weight="700">6.45 ± 4.12 µm</tspan></text>
    <text x="32" y="588" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Tilt Stress (±15°): <tspan fill="#34d399" font-weight="700">&lt; 0.8 µm drift</tspan></text>
    <text x="32" y="626" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Baseline Drift (±15°): <tspan fill="#f43f5e" font-weight="700">&gt; 14.2 µm drift</tspan></text>
    <text x="32" y="664" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Cup IoU: <tspan fill="#f8fafc" font-weight="700">0.9315</tspan></text>

    <!-- Verdict Badge -->
    <rect x="18" y="730" width="324" height="68" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-dasharray="4 4"/>
    <text x="32" y="756" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" fill="#fbbf24">ROLE: Clinical Tilt Resilience</text>
    <text x="32" y="778" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">Prevents neck fatigue scan failure.</text>
  </g>

  <!-- CARD 4: Dense 3D U-Net ~20.9M (x=1205) -->
  <g transform="translate(1205, 170)">
    <rect width="360" height="820" rx="14" fill="url(#grad-card)" stroke="#4338ca" stroke-width="1.8"/>
    <rect width="360" height="8" rx="4" fill="url(#grad-indigo)"/>
    
    <rect x="200" y="22" width="140" height="24" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
    <text x="270" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" fill="#a5b4fc" text-anchor="middle">OUTLIER SHIELD</text>

    <text x="24" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#818cf8" letter-spacing="1">VOLUMETRIC 3D</text>
    <text x="24" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#f8fafc">Dense 3D U-Net</text>
    <text x="24" y="92" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#64748b">Job: 18574378 (nnU-Net Style)</text>

    <!-- Specs Box -->
    <rect x="18" y="110" width="324" height="310" rx="10" fill="#0b1120" stroke="#1e1b4b"/>
    <text x="32" y="142" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Parameters: <tspan fill="#f1f5f9" font-weight="700">20,903,329 (~20.9M)</tspan></text>
    <text x="32" y="178" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Base Channels: <tspan fill="#f1f5f9" font-weight="700">32 ch (up to 384 ch)</tspan></text>
    <text x="32" y="214" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Convolutions: <tspan fill="#818cf8" font-weight="700">Full 3D Kernels (3×3×3)</tspan></text>
    <text x="32" y="250" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">3D Patch Size: <tspan fill="#818cf8" font-weight="700">(64, 768, 64) Voxels</tspan></text>
    <text x="32" y="286" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Downsampling: <tspan fill="#f1f5f9" font-weight="700">Anisotropic (1, 2, 1)</tspan></text>
    <text x="32" y="322" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Normalization: <tspan fill="#f1f5f9" font-weight="700">GroupNorm + SiLU</tspan></text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Interpolation: <tspan fill="#f1f5f9" font-weight="700">Trilinear 3D Upsample</tspan></text>
    <text x="32" y="394" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Surface Regression: <tspan fill="#94a3b8">Dense Mask Only</tspan></text>

    <!-- Key Metrics Box -->
    <rect x="18" y="440" width="324" height="270" rx="10" fill="#1e1b4b" stroke="#4338ca"/>
    <text x="32" y="474" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#a5b4fc">Held-Out V2 Benchmark (40 Eyes)</text>
    <text x="32" y="512" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median Dice: <tspan fill="#f8fafc" font-weight="700">0.9471</tspan></text>
    <text x="32" y="550" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median MABE: <tspan fill="#f8fafc" font-weight="700">5.50 µm</tspan></text>
    <text x="32" y="588" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Mean MABE: <tspan fill="#34d399" font-weight="800">5.87 ± 2.13 µm (BEST)</tspan></text>
    <text x="32" y="626" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Worst-Case MABE: <tspan fill="#34d399" font-weight="800">17.02 µm (LOWEST)</tspan></text>
    <text x="32" y="664" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Cup IoU: <tspan fill="#f8fafc" font-weight="700">0.9085</tspan></text>

    <!-- Verdict Badge -->
    <rect x="18" y="730" width="324" height="68" rx="8" fill="#17143a" stroke="#818cf8"/>
    <text x="32" y="756" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" fill="#818cf8">ROLE: Outlier &amp; QC Guardian</text>
    <text x="32" y="778" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">Lowest standard deviation (±2.13 µm).</text>
  </g>

  <!-- CARD 5: TransUNet 5.1M (x=1590) -->
  <g transform="translate(1590, 170)">
    <rect width="360" height="820" rx="14" fill="url(#grad-card)" stroke="#7e22ce" stroke-width="1.8"/>
    <rect width="360" height="8" rx="4" fill="url(#grad-purple)"/>
    
    <rect x="200" y="22" width="140" height="24" rx="6" fill="#3b0764" stroke="#a855f7"/>
    <text x="270" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" fill="#d8b4fe" text-anchor="middle">EXPERIMENTAL</text>

    <text x="24" y="40" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#c084fc" letter-spacing="1">CNN + ViT HYBRID</text>
    <text x="24" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#f8fafc">TransUNet 5.1M</text>
    <text x="24" y="92" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#64748b">Job: 18710145 (Hybrid)</text>

    <!-- Specs Box -->
    <rect x="18" y="110" width="324" height="310" rx="10" fill="#0b1120" stroke="#3b0764"/>
    <text x="32" y="142" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Parameters: <tspan fill="#f1f5f9" font-weight="700">5,099,956 (~5.10M)</tspan></text>
    <text x="32" y="178" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">ViT Layers: <tspan fill="#c084fc" font-weight="700">6 Transformer Blocks</tspan></text>
    <text x="32" y="214" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Token Grid: <tspan fill="#c084fc" font-weight="700">1,920 Tokens (96 × 20)</tspan></text>
    <text x="32" y="250" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Attention: <tspan fill="#f1f5f9" font-weight="700">8 Heads, d = 256</tspan></text>
    <text x="32" y="286" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Decoder: <tspan fill="#f1f5f9" font-weight="700">Cascaded Upsampler (CUP)</tspan></text>
    <text x="32" y="322" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Boundary Injection: <tspan fill="#34d399" font-weight="700">Stem Skip f1 (Full Res)</tspan></text>
    <text x="32" y="358" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Inference Planes: <tspan fill="#f1f5f9" font-weight="700">Bi-Planar (H + V)</tspan></text>
    <text x="32" y="394" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" fill="#94a3b8">Norm Architecture: <tspan fill="#f1f5f9" font-weight="700">Pre-LayerNorm</tspan></text>

    <!-- Key Metrics Box -->
    <rect x="18" y="440" width="324" height="270" rx="10" fill="#2e1065" stroke="#7e22ce"/>
    <text x="32" y="474" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#d8b4fe">Held-Out V2 Benchmark (40 Eyes)</text>
    <text x="32" y="512" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median Dice: <tspan fill="#f43f5e" font-weight="700">0.6922 (Underperf)</tspan></text>
    <text x="32" y="550" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median MABE: <tspan fill="#f43f5e" font-weight="700">31.90 µm</tspan></text>
    <text x="32" y="588" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Mean MABE: <tspan fill="#f8fafc">42.69 ± 33.00 µm</tspan></text>
    <text x="32" y="626" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Median P95: <tspan fill="#f8fafc">86.47 µm</tspan></text>
    <text x="32" y="664" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94a3b8">Cup IoU: <tspan fill="#f8fafc">0.7282</tspan></text>

    <!-- Verdict Badge -->
    <rect x="18" y="730" width="324" height="68" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-dasharray="4 4"/>
    <text x="32" y="756" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" fill="#c084fc">ROLE: Research Probe</text>
    <text x="32" y="778" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#cbd5e1">Requires large-scale pre-training.</text>
  </g>

  <!-- Bottom Comparison Strip & Architectural Lessons (y=1020, h=270, w=1900) -->
  <g transform="translate(50, 1020)">
    <rect width="1900" height="270" rx="14" fill="url(#grad-card)" stroke="#334155" stroke-width="1.8"/>
    <text x="36" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#f8fafc">KEY ARCHITECTURAL FINDINGS &amp; MODEL TAXONOMY LESSONS</text>
    
    <!-- Lesson 1 (w=580, h=190) -->
    <g transform="translate(36, 56)">
      <rect width="580" height="190" rx="10" fill="#0b1120" stroke="#1e293b"/>
      <circle cx="30" cy="30" r="12" fill="#0d9488"/>
      <text x="30" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" fill="#f8fafc" text-anchor="middle">1</text>
      <text x="56" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#2dd4bf">Geometry Trumps Pure Capacity</text>
      
      <text x="30" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">Upgrading Single-Planar 1.6M → 6.5M in single-planar mode only</text>
      <text x="30" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">improved Dice from 0.8055 to 0.8562. Introducing</text>
      <text x="30" y="124" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#2dd4bf" font-weight="700">Bi-Planar Orthogonal Consensus Fusion jumped Dice to 0.9518</text>
      <text x="30" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">and slashed median MABE from 12.58 to 4.71 µm.</text>
    </g>

    <!-- Lesson 2 (w=580, h=190) -->
    <g transform="translate(660, 56)">
      <rect width="580" height="190" rx="10" fill="#0b1120" stroke="#1e293b"/>
      <circle cx="30" cy="30" r="12" fill="#4f46e5"/>
      <text x="30" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" fill="#f8fafc" text-anchor="middle">2</text>
      <text x="56" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#818cf8">Dense 3D U-Net is an Anisotropic Outlier Shield</text>
      
      <text x="30" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">Dense 3D U-Net operates across 3D voxels, eliminating</text>
      <text x="30" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">single-slice drift. While Bi-Planar has the lower median error</text>
      <text x="30" y="124" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#818cf8" font-weight="700">(4.71 vs 5.50 µm), Dense 3D achieves lower mean MABE (5.87 µm)</text>
      <text x="30" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">and the lowest worst-case cohort scan error (17.02 µm).</text>
    </g>

    <!-- Lesson 3 (w=580, h=190) -->
    <g transform="translate(1284, 56)">
      <rect width="580" height="190" rx="10" fill="#0b1120" stroke="#1e293b"/>
      <circle cx="30" cy="30" r="12" fill="#d97706"/>
      <text x="30" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" fill="#f8fafc" text-anchor="middle">3</text>
      <text x="56" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#fbbf24">What Was Missed: Canonical STN Model</text>
      
      <text x="30" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">Patient head tilt introduces severe diagonal artifacts.</text>
      <text x="30" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#fbbf24" font-weight="700">CanonicalVolumetricRNFLNet (~6.61M) embeds a Spatial</text>
      <text x="30" y="124" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#fbbf24" font-weight="700">Transformer predicting tilt θ ∈ [-25°, +25°],</text>
      <text x="30" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">bounding boundary drift below &lt;0.8 µm under stress rotation.</text>
    </g>
  </g>
</svg>"""
    filename = os.path.join(SVG_DIR, "master_frontier_taxonomy.svg")
    with open(filename, "w") as f:
        f.write(svg)
    print(f"Generated {filename}")


# ==============================================================================
# 2. SINGLE-PLANAR 1.6M RESIDUAL U-NET (1520 x 920)
# ==============================================================================
def generate_single_planar_svg():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1520 920" width="1520" height="920">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="1520" height="920" fill="url(#grad-bg)"/>
  
  <g opacity="0.04">
    <path d="{' '.join([f'M {x} 0 L {x} 920' for x in range(0, 1520, 50)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 1520 {y}' for y in range(0, 920, 50)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header -->
  <g transform="translate(50, 40)">
    <rect width="1420" height="90" rx="14" fill="url(#grad-card)" stroke="#334155" stroke-width="1.8"/>
    <rect width="8" height="90" rx="4" fill="url(#grad-blue)"/>
    <text x="32" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#f8fafc">MODEL 1: SINGLE-PLANAR 2.5D RESIDUAL U-NET (1.67M PARAMETERS)</text>
    <text x="32" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="500" fill="#94a3b8">Baseline Volumetric Architecture: Multi-Slice 2.5D Input Slab, Residual Units, Multi-Task 1D Continuous Surface Heads</text>
    <rect x="1220" y="26" width="175" height="38" rx="8" fill="#0f172a" stroke="#38bdf8"/>
    <text x="1307" y="50" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="700" fill="#38bdf8" text-anchor="middle">1,672,021 PARAMS</text>
  </g>

  <!-- Input OCT Slab -->
  <g transform="translate(50, 160)">
    <rect width="200" height="420" rx="12" fill="url(#grad-card)" stroke="#38bdf8" stroke-width="2"/>
    <rect width="200" height="6" rx="3" fill="url(#grad-blue)"/>
    <text x="100" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#38bdf8" text-anchor="middle">2.5D INPUT SLAB</text>
    <text x="100" y="56" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="600" fill="#94a3b8" text-anchor="middle">5 Context B-Scans</text>

    <!-- Visual Slices Stack -->
    <g transform="translate(30, 85)">
      <rect x="35" y="0" width="100" height="170" rx="4" fill="#1e293b" stroke="#475569" opacity="0.6"/>
      <rect x="20" y="15" width="100" height="170" rx="4" fill="#1e293b" stroke="#475569" opacity="0.8"/>
      <rect x="5" y="30" width="100" height="170" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
      <text x="55" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#38bdf8" text-anchor="middle">Slice z</text>
      <text x="55" y="128" font-family="monospace" font-size="10" fill="#94a3b8" text-anchor="middle">(768 × 320)</text>
    </g>

    <rect x="16" y="315" width="168" height="85" rx="8" fill="#0b1120" stroke="#1e293b"/>
    <text x="26" y="338" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Tensor Dimensions:</text>
    <text x="26" y="358" font-family="monospace" font-size="12" font-weight="700" fill="#38bdf8">(B, 5, 768, 320)</text>
    <text x="26" y="380" font-family="system-ui, -apple-system, sans-serif" font-size="10" fill="#94a3b8">Slow-axis window: ±2</text>
  </g>

  <!-- Flow Arrow to Encoder -->
  <line x1="250" y1="370" x2="290" y2="370" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-blue)"/>

  <!-- U-Net Backbone -->
  <!-- Encoder Column -->
  <g transform="translate(290, 160)">
    <rect width="200" height="420" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.8"/>
    <text x="100" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#f8fafc" text-anchor="middle">ENCODER STAGES</text>
    <text x="100" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">MONAI Residual (num=2)</text>

    <!-- Stage 0 -->
    <rect x="16" y="70" width="168" height="58" rx="8" fill="#0f172a" stroke="#0284c7"/>
    <text x="26" y="94" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#38bdf8">Stage 0 (16 ch)</text>
    <text x="26" y="114" font-family="monospace" font-size="11" fill="#94a3b8">(B, 16, 768, 320)</text>

    <!-- Stage 1 -->
    <rect x="16" y="142" width="168" height="58" rx="8" fill="#0f172a" stroke="#0284c7"/>
    <text x="26" y="166" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#38bdf8">Stage 1 (32 ch)</text>
    <text x="26" y="186" font-family="monospace" font-size="11" fill="#94a3b8">(B, 32, 384, 160)</text>

    <!-- Stage 2 -->
    <rect x="16" y="214" width="168" height="58" rx="8" fill="#0f172a" stroke="#0284c7"/>
    <text x="26" y="238" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#38bdf8">Stage 2 (64 ch)</text>
    <text x="26" y="258" font-family="monospace" font-size="11" fill="#94a3b8">(B, 64, 192, 80)</text>

    <!-- Stage 3 -->
    <rect x="16" y="286" width="168" height="58" rx="8" fill="#0f172a" stroke="#0284c7"/>
    <text x="26" y="310" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#38bdf8">Stage 3 (128 ch)</text>
    <text x="26" y="330" font-family="monospace" font-size="11" fill="#94a3b8">(B, 128, 96, 40)</text>
  </g>

  <!-- Connectors to Bottleneck -->
  <line x1="390" y1="580" x2="390" y2="610" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-blue)"/>

  <!-- Bottleneck Box -->
  <g transform="translate(290, 615)">
    <rect width="420" height="85" rx="10" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
    <text x="210" y="30" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#a5b4fc" text-anchor="middle">BOTTLENECK STAGE (256 CHANNELS)</text>
    <text x="210" y="52" font-family="monospace" font-size="13" font-weight="700" fill="#c7d2fe" text-anchor="middle">Shape: (B, 256, 48, 20) | Downsample: Stride (2, 2)</text>
    <text x="210" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Dual Residual Units + Dropout(0.1)</text>
  </g>

  <!-- Up Connector to Decoder -->
  <line x1="610" y1="615" x2="610" y2="585" stroke="#2dd4bf" stroke-width="2.5" marker-end="url(#arrow-teal)"/>

  <!-- Skip Connections -->
  <path d="M 460 243 L 510 243" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4 4" marker-end="url(#arrow)"/>
  <path d="M 460 315 L 510 315" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4 4" marker-end="url(#arrow)"/>

  <!-- Decoder Column -->
  <g transform="translate(510, 160)">
    <rect width="200" height="420" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.8"/>
    <text x="100" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="800" fill="#f8fafc" text-anchor="middle">DECODER STAGES</text>
    <text x="100" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Transposed Convs + Skips</text>

    <!-- UpStage 3 -->
    <rect x="16" y="286" width="168" height="58" rx="8" fill="#042f2e" stroke="#0d9488"/>
    <text x="26" y="310" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#2dd4bf">UpStage 3 (128 ch)</text>
    <text x="26" y="330" font-family="monospace" font-size="11" fill="#94a3b8">(B, 128, 96, 40)</text>

    <!-- UpStage 2 -->
    <rect x="16" y="214" width="168" height="58" rx="8" fill="#042f2e" stroke="#0d9488"/>
    <text x="26" y="238" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#2dd4bf">UpStage 2 (64 ch)</text>
    <text x="26" y="258" font-family="monospace" font-size="11" fill="#94a3b8">(B, 64, 192, 80)</text>

    <!-- UpStage 1 -->
    <rect x="16" y="142" width="168" height="58" rx="8" fill="#042f2e" stroke="#0d9488"/>
    <text x="26" y="166" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#2dd4bf">UpStage 1 (32 ch)</text>
    <text x="26" y="186" font-family="monospace" font-size="11" fill="#94a3b8">(B, 32, 384, 160)</text>

    <!-- UpStage 0 Final Features -->
    <rect x="16" y="70" width="168" height="58" rx="8" fill="#042f2e" stroke="#14b8a6"/>
    <text x="26" y="94" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="800" fill="#2dd4bf">Final Feats (16 ch)</text>
    <text x="26" y="114" font-family="monospace" font-size="11" fill="#5eead4">(B, 16, 768, 320)</text>
  </g>

  <!-- Flow to Multi-Task Heads -->
  <path d="M 710 200 L 750 200" stroke="#2dd4bf" stroke-width="2.5" marker-end="url(#arrow-teal)"/>

  <!-- Multi-Task Heads Container (w=720, h=540) -->
  <g transform="translate(750, 160)">
    <rect width="720" height="540" rx="14" fill="url(#grad-card)" stroke="#14b8a6" stroke-width="2"/>
    <rect width="720" height="6" rx="3" fill="url(#grad-teal)"/>
    <text x="28" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" fill="#2dd4bf">MULTI-TASK HEADS (Branching from 16-channel Features)</text>
    <text x="28" y="56" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#94a3b8">Joint Optimization: Voxel Logits + 1D Continuous Boundary Regression + Cup Absence</text>

    <!-- Head 1: Dense 2D Mask Head (w=664, h=105) -->
    <g transform="translate(28, 75)">
      <rect width="664" height="105" rx="10" fill="#0b1120" stroke="#0284c7" stroke-width="1.5"/>
      <text x="20" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#38bdf8">1. Dense Voxel Mask Head</text>
      <text x="20" y="52" font-family="monospace" font-size="12" fill="#cbd5e1">Conv2d(16 → 1, 1x1) → mask_logits: (B, 1, 768, 320)</text>
      <text x="20" y="74" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#94a3b8">Differentiable column thickness: column_thickness = Σ σ(mask_logits) over H (768)</text>
      <text x="20" y="92" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#38bdf8">Produces direct 3D Slicer volumetric labelmaps for clinical review.</text>
      <rect x="510" y="16" width="138" height="28" rx="6" fill="#0369a1"/>
      <text x="579" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">VOXEL LABELMAP</text>
    </g>

    <!-- Head 2: 1D Boundary Regression Head (w=664, h=175) -->
    <g transform="translate(28, 195)">
      <rect width="664" height="175" rx="10" fill="#0b1120" stroke="#059669" stroke-width="1.5"/>
      <text x="20" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#34d399">2. 1D Continuous Boundary Regression Head</text>
      <text x="20" y="52" font-family="monospace" font-size="12" fill="#cbd5e1">AdaptiveAvgPool2d((1, 320)) → Squeeze → (B, 16, 320)</text>
      <text x="20" y="76" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#94a3b8">Branch A: Conv1d(16→64→32→1, k=7,5,3) → ilm_pred = σ(raw) × 768  [Row px]</text>
      <text x="20" y="100" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#94a3b8">Branch B: Conv1d(16→64→32→1, k=7,5,3) → nfl_pred = σ(raw) × 768  [Row px]</text>
      <text x="20" y="124" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#94a3b8">Branch C: Conv1d(16→32→1, k=7,3)       → cup_logits: (B, 320)  [Cavity presence]</text>
      <text x="20" y="154" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#6ee7b7">Bypasses argmax discretization! Yields sub-voxel continuous depths.</text>
      <rect x="510" y="16" width="138" height="28" rx="6" fill="#047857"/>
      <text x="579" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">EXPLICIT CURVES</text>
    </g>

    <!-- Head 3: Multi-Objective Joint Loss (w=664, h=135) - NO TEXT LEAKS! -->
    <g transform="translate(28, 385)">
      <rect width="664" height="135" rx="10" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
      <text x="20" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#a5b4fc">3. Multi-Objective Joint Loss</text>
      <text x="20" y="52" font-family="monospace" font-size="12" font-weight="700" fill="#e0e7ff">L_total = 1.0·L_Tversky + 0.5·L_BCE_mask + 1.0·L_boundary</text>
      <text x="20" y="74" font-family="monospace" font-size="12" font-weight="700" fill="#c7d2fe">        + 0.2·L_cup + 0.5·L_thickness + 0.1·L_edge</text>
      <text x="20" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">• Tversky Loss handles severe class imbalance (RNFL is &lt;4% of total slice area)</text>
      <text x="20" y="118" font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#cbd5e1">• Edge Loss (Sobel optical gradient) snaps curves to true physical tissue reflectances</text>
    </g>
  </g>

  <!-- Bottom Explanatory Banner -->
  <g transform="translate(50, 720)">
    <rect width="1420" height="165" rx="14" fill="url(#grad-card)" stroke="#334155" stroke-width="1.8"/>
    <text x="32" y="36" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" fill="#f8fafc">WHY SINGLE-PLANAR 1.6M WAS INSUFFICIENT FOR FRONTIER CLINICAL USE</text>
    
    <g transform="translate(32, 54)">
      <circle cx="14" cy="14" r="10" fill="#f43f5e"/>
      <text x="14" y="19" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">!</text>
      <text x="36" y="19" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="700" fill="#fda4af">Inter-B-Scan Anisotropy:</text>
      <text x="36" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">
        Solix OCT acquires 128 B-scans with lateral spacing ~18.7 µm but inter-B-scan slow-axis spacing ~40 µm. Single-planar models process slices
      </text>
      <text x="36" y="64" font-family="system-ui, -apple-system, sans-serif" font-size="13" fill="#cbd5e1">
        independently along X-Z. Without vertical orthogonal cross-checks, predicted en face thickness maps exhibited severe "sawtooth" banding.
      </text>
    </g>
  </g>
</svg>"""
    filename = os.path.join(SVG_DIR, "01_single_planar_1.6m.svg")
    with open(filename, "w") as f:
        f.write(svg)
    print(f"Generated {filename}")


# ==============================================================================
# Helper to cleanly crop out any letterbox padding from PNGs
# ==============================================================================
def render_retina_png_exact(svg_name, orig_w, orig_h, render_size=3200):
    svg_path = os.path.join(SVG_DIR, f"{svg_name}.svg")
    final_png_path = os.path.join(SVG_DIR, f"{svg_name}.png")
    
    # 1. Render via qlmanage
    cmd = ["/usr/bin/qlmanage", "-t", "-s", str(render_size), "-o", SVG_DIR, svg_path]
    subprocess.run(cmd, capture_output=True, text=True)
    
    temp_thumb = os.path.join(SVG_DIR, f"{svg_name}.svg.png")
    if os.path.exists(temp_thumb):
        im = Image.open(temp_thumb)
        S = im.width
        
        # Exact mathematical aspect crop
        target_h = int(round(S * float(orig_h) / float(orig_w)))
        y_offset = max(0, (S - target_h) // 2)
        
        # Crop away the top/bottom letterbox padding
        cropped = im.crop((0, y_offset, S, y_offset + target_h))
        cropped.save(final_png_path, "PNG", optimize=True)
        os.remove(temp_thumb)
        print(f"Rendered & Cropped Retina PNG ({cropped.size[0]}x{cropped.size[1]}): {final_png_path}")

if __name__ == "__main__":
    generate_master_taxonomy()
    generate_single_planar_svg()
    
    # Render PNGs with exact aspect ratio cropping (0 white space!)
    render_retina_png_exact("master_frontier_taxonomy", 2000, 1340, 3200)
    render_retina_png_exact("01_single_planar_1.6m", 1520, 920, 3200)
    render_retina_png_exact("02_biplanar_orthogonal_fusion", 1440, 920, 3200)
    render_retina_png_exact("03_dense_3d_anisotropic_unet", 1380, 900, 3200)
    render_retina_png_exact("04_anisotropic_transunet", 1440, 920, 3200)
    render_retina_png_exact("05_canonical_stn_network", 1440, 920, 3200)
    render_retina_png_exact("06_multi_task_boundary_heads", 1440, 920, 3200)
    print("All SVGs and cropped Retina PNGs ready!")
