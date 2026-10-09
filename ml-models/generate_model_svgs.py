"""
generate_model_svgs.py
======================
Generates 7 standalone, publication-quality SVG diagrams illustrating the
Frontier ML Model family for volumetric OCT RNFL segmentation.
"""

import os

SVG_DIR = "/Users/nikhilmundhra/Documents/Github/Capstone/ML-Research-OCT/ml-models/svg"
os.makedirs(SVG_DIR, exist_ok=True)

COMMON_DEFS = """
  <defs>
    <linearGradient id="grad-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16" />
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

    <!-- Filters -->
    <filter id="shadow" x="-5%" y="-5%" width="115%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.5" />
    </filter>
    <filter id="glow-teal" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="glow-purple" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

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
    <marker id="arrow-rose" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#fb7185" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#34d399" />
    </marker>
  </defs>
"""

# ==============================================================================
# 1. MASTER FRONTIER TAXONOMY & BENCHMARK MATRIX
# ==============================================================================
def generate_master_taxonomy():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 960" width="100%" height="100%">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="1440" height="960" fill="url(#grad-bg)"/>
  
  <!-- Subtle Grid Pattern -->
  <g opacity="0.06">
    <path d="{' '.join([f'M {x} 0 L {x} 960' for x in range(0, 1440, 40)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 1440 {y}' for y in range(0, 960, 40)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header Banner -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="1320" height="95" rx="14" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <rect x="0" y="0" width="8" height="95" rx="4" fill="url(#grad-teal)"/>
    <text x="32" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="24" font-weight="800" fill="#f8fafc" letter-spacing="-0.5">FRONTIER ML MODEL TAXONOMY &amp; BENCHMARK MATRIX</text>
    <text x="32" y="65" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="14" font-weight="500" fill="#94a3b8">Comprehensive Architectural Lineage for Optovue Solix Peripapillary RNFL Volumetric OCT Segmentation</text>
    <rect x="1100" y="28" width="185" height="38" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.2"/>
    <text x="1192" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#38bdf8" text-anchor="middle">HELD-OUT 40-EYE V2 SPLIT</text>
  </g>

  <!-- 5 Architecture Column Cards -->
  <!-- Model 1: Single-Planar 1.6M -->
  <g transform="translate(60, 165)">
    <rect width="248" height="490" rx="12" fill="url(#grad-card)" stroke="#1e293b" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="248" height="6" rx="3" fill="url(#grad-blue)"/>
    
    <text x="18" y="34" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8" letter-spacing="1">ABLATION BASELINE</text>
    <text x="18" y="58" font-family="sans-serif" font-size="17" font-weight="800" fill="#f8fafc">Single-Planar 1.6M</text>
    <text x="18" y="78" font-family="sans-serif" font-size="12" font-weight="600" fill="#64748b">Job: 18043443 (Light)</text>

    <!-- Specs Box -->
    <rect x="14" y="94" width="220" height="150" rx="8" fill="#0b1120" stroke="#1e293b"/>
    <text x="24" y="116" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Params: <tspan fill="#f1f5f9" font-weight="700">1,672,021 (~1.67M)</tspan></text>
    <text x="24" y="136" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Base Channels: <tspan fill="#f1f5f9" font-weight="700">16 ch</tspan></text>
    <text x="24" y="156" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Receptive Context: <tspan fill="#f1f5f9" font-weight="700">2.5D (5 slices)</tspan></text>
    <text x="24" y="176" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Inference Axis: <tspan fill="#f1f5f9" font-weight="700">Horizontal (X-Z) Only</tspan></text>
    <text x="24" y="196" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Heads: <tspan fill="#f1f5f9" font-weight="700">Dense + 1D Boundary</tspan></text>
    <text x="24" y="216" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Tilt Invariance: <tspan fill="#f43f5e" font-weight="700">None (Native)</tspan></text>
    <text x="24" y="234" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Orthogonal Fusion: <tspan fill="#64748b" font-weight="700">No</tspan></text>

    <!-- Key Metrics -->
    <rect x="14" y="256" width="220" height="155" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="24" y="278" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8">Held-Out V2 Metrics</text>
    <text x="24" y="300" font-family="sans-serif" font-size="11" fill="#94a3b8">Median Dice: <tspan fill="#f8fafc" font-weight="700">0.8055</tspan></text>
    <text x="24" y="322" font-family="sans-serif" font-size="11" fill="#94a3b8">Median MABE: <tspan fill="#f8fafc" font-weight="700">12.58 µm</tspan></text>
    <text x="24" y="344" font-family="sans-serif" font-size="11" fill="#94a3b8">Mean MABE: <tspan fill="#f8fafc" font-weight="700">20.18 ± 19.5 µm</tspan></text>
    <text x="24" y="366" font-family="sans-serif" font-size="11" fill="#94a3b8">Median P95: <tspan fill="#f8fafc" font-weight="700">32.96 µm</tspan></text>
    <text x="24" y="388" font-family="sans-serif" font-size="11" fill="#94a3b8">Cup IoU: <tspan fill="#f8fafc" font-weight="700">0.8422</tspan></text>

    <!-- Verdict Badge -->
    <rect x="14" y="424" width="220" height="52" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-dasharray="3 3"/>
    <text x="24" y="444" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8">ROLE: Early Feasibility</text>
    <text x="24" y="462" font-family="sans-serif" font-size="10" fill="#94a3b8">Suffers high inter-B-scan jitter.</text>
  </g>

  <!-- Model 2: Bi-Planar 1.6M & 6.5M -->
  <g transform="translate(328, 165)">
    <rect width="256" height="490" rx="12" fill="url(#grad-card)" stroke="#0d9488" stroke-width="2" filter="url(#shadow)"/>
    <rect width="256" height="6" rx="3" fill="url(#grad-teal)"/>
    
    <rect x="135" y="16" width="105" height="20" rx="4" fill="#042f2e" stroke="#14b8a6"/>
    <text x="187" y="30" font-family="sans-serif" font-size="9" font-weight="800" fill="#2dd4bf" text-anchor="middle">LEAD CANDIDATE</text>

    <text x="18" y="34" font-family="sans-serif" font-size="12" font-weight="700" fill="#2dd4bf" letter-spacing="1">ORTHOGONAL FUSION</text>
    <text x="18" y="58" font-family="sans-serif" font-size="17" font-weight="800" fill="#f8fafc">Bi-Planar 1.6M / 6.5M</text>
    <text x="18" y="78" font-family="sans-serif" font-size="12" font-weight="600" fill="#64748b">Jobs: 18223981 (16ch) / 18563914 (32ch)</text>

    <!-- Specs Box -->
    <rect x="14" y="94" width="228" height="150" rx="8" fill="#0b1120" stroke="#134e4a"/>
    <text x="24" y="116" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Params: <tspan fill="#f1f5f9" font-weight="700">1.67M (16ch) | 6.58M (32ch)</tspan></text>
    <text x="24" y="136" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Base Channels: <tspan fill="#f1f5f9" font-weight="700">16 ch or 32 ch</tspan></text>
    <text x="24" y="156" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Receptive Context: <tspan fill="#2dd4bf" font-weight="700">Bi-Planar Dual 2.5D</tspan></text>
    <text x="24" y="176" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Inference Axis: <tspan fill="#2dd4bf" font-weight="700">Orthogonal (X-Z &amp; Y-Z)</tspan></text>
    <text x="24" y="196" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Heads: <tspan fill="#f1f5f9" font-weight="700">Dense + 1D ILM/NFL/Cup</tspan></text>
    <text x="24" y="216" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Fusion Mechanism: <tspan fill="#2dd4bf" font-weight="700">3D Consensus Average</tspan></text>
    <text x="24" y="234" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Surface Clamping: <tspan fill="#34d399" font-weight="700">Guided + Cup-Reach</tspan></text>

    <!-- Key Metrics -->
    <rect x="14" y="256" width="228" height="155" rx="8" fill="#042f2e" stroke="#0d9488"/>
    <text x="24" y="278" font-family="sans-serif" font-size="12" font-weight="700" fill="#2dd4bf">Held-Out V2 Metrics (32ch)</text>
    <text x="24" y="300" font-family="sans-serif" font-size="11" fill="#94a3b8">Median Dice: <tspan fill="#34d399" font-weight="800">0.9518 (BEST)</tspan></text>
    <text x="24" y="322" font-family="sans-serif" font-size="11" fill="#94a3b8">Median MABE: <tspan fill="#34d399" font-weight="800">4.71 µm (BEST)</tspan></text>
    <text x="24" y="344" font-family="sans-serif" font-size="11" fill="#94a3b8">Mean MABE: <tspan fill="#f8fafc" font-weight="700">6.22 ± 5.91 µm</tspan></text>
    <text x="24" y="366" font-family="sans-serif" font-size="11" fill="#94a3b8">Median P95: <tspan fill="#34d399" font-weight="800">16.85 µm (BEST)</tspan></text>
    <text x="24" y="388" font-family="sans-serif" font-size="11" fill="#94a3b8">Cup IoU: <tspan fill="#34d399" font-weight="800">0.9388 (BEST)</tspan></text>

    <!-- Verdict Badge -->
    <rect x="14" y="424" width="228" height="52" rx="6" fill="#0f2926" stroke="#2dd4bf"/>
    <text x="24" y="444" font-family="sans-serif" font-size="11" font-weight="700" fill="#2dd4bf">ROLE: Lead Research Model</text>
    <text x="24" y="462" font-family="sans-serif" font-size="10" fill="#94a3b8">Top precision; 1 held-out outlier.</text>
  </g>

  <!-- Model 3: Canonical STN Bi-Planar ~6.61M -->
  <g transform="translate(604, 165)">
    <rect width="256" height="490" rx="12" fill="url(#grad-card)" stroke="#1e293b" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="256" height="6" rx="3" fill="url(#grad-amber)"/>
    
    <rect x="135" y="16" width="105" height="20" rx="4" fill="#451a03" stroke="#d97706"/>
    <text x="187" y="30" font-family="sans-serif" font-size="9" font-weight="800" fill="#fbbf24" text-anchor="middle">STN CANONICAL</text>

    <text x="18" y="34" font-family="sans-serif" font-size="12" font-weight="700" fill="#fbbf24" letter-spacing="1">TILT-INVARIANT STN</text>
    <text x="18" y="58" font-family="sans-serif" font-size="17" font-weight="800" fill="#f8fafc">Canonical STN 6.6M</text>
    <text x="18" y="78" font-family="sans-serif" font-size="12" font-weight="600" fill="#64748b">Job: 18697275 (STN-Net)</text>

    <!-- Specs Box -->
    <rect x="14" y="94" width="228" height="150" rx="8" fill="#0b1120" stroke="#1e293b"/>
    <text x="24" y="116" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Params: <tspan fill="#f1f5f9" font-weight="700">6,608,983 (~6.61M)</tspan></text>
    <text x="24" y="136" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Base Channels: <tspan fill="#f1f5f9" font-weight="700">32 ch + STN Head</tspan></text>
    <text x="24" y="156" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">STN Mechanism: <tspan fill="#fbbf24" font-weight="700">Differentiable Affine</tspan></text>
    <text x="24" y="176" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Tilt Angle Bounds: <tspan fill="#fbbf24" font-weight="700">θ ∈ [-25°, +25°]</tspan></text>
    <text x="24" y="196" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Axial Shift Bounds: <tspan fill="#fbbf24" font-weight="700">t_y ∈ [-20%, +20%]</tspan></text>
    <text x="24" y="216" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Backbone: <tspan fill="#f1f5f9" font-weight="700">Canonical 2.5D Residual</tspan></text>
    <text x="24" y="234" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Inverse Warp: <tspan fill="#34d399" font-weight="700">Yes (Back to Native)</tspan></text>

    <!-- Key Metrics -->
    <rect x="14" y="256" width="228" height="155" rx="8" fill="#0f172a" stroke="#334155"/>
    <text x="24" y="278" font-family="sans-serif" font-size="12" font-weight="700" fill="#fbbf24">Stress Test / Tilt Robustness</text>
    <text x="24" y="300" font-family="sans-serif" font-size="11" fill="#94a3b8">Canonical Dice: <tspan fill="#f8fafc" font-weight="700">0.9412</tspan></text>
    <text x="24" y="322" font-family="sans-serif" font-size="11" fill="#94a3b8">Mean MABE: <tspan fill="#f8fafc" font-weight="700">6.45 ± 4.12 µm</tspan></text>
    <text x="24" y="344" font-family="sans-serif" font-size="11" fill="#94a3b8">Tilt Stress (±15°): <tspan fill="#34d399" font-weight="700">&lt; 0.8 µm drift</tspan></text>
    <text x="24" y="366" font-family="sans-serif" font-size="11" fill="#94a3b8">Baseline Drift (±15°): <tspan fill="#f43f5e" font-weight="700">&gt; 14.2 µm drift</tspan></text>
    <text x="24" y="388" font-family="sans-serif" font-size="11" fill="#94a3b8">Cup IoU: <tspan fill="#f8fafc" font-weight="700">0.9315</tspan></text>

    <!-- Verdict Badge -->
    <rect x="14" y="424" width="228" height="52" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-dasharray="3 3"/>
    <text x="24" y="444" font-family="sans-serif" font-size="11" font-weight="700" fill="#fbbf24">ROLE: Clinical Tilt Resilience</text>
    <text x="24" y="462" font-family="sans-serif" font-size="10" fill="#94a3b8">Prevents head tilt scan failure.</text>
  </g>

  <!-- Model 4: Dense 3D Anisotropic U-Net ~20.9M -->
  <g transform="translate(880, 165)">
    <rect width="256" height="490" rx="12" fill="url(#grad-card)" stroke="#4338ca" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="256" height="6" rx="3" fill="url(#grad-indigo)"/>
    
    <rect x="135" y="16" width="105" height="20" rx="4" fill="#1e1b4b" stroke="#6366f1"/>
    <text x="187" y="30" font-family="sans-serif" font-size="9" font-weight="800" fill="#a5b4fc" text-anchor="middle">OUTLIER SHIELD</text>

    <text x="18" y="34" font-family="sans-serif" font-size="12" font-weight="700" fill="#818cf8" letter-spacing="1">VOLUMETRIC 3D</text>
    <text x="18" y="58" font-family="sans-serif" font-size="17" font-weight="800" fill="#f8fafc">Dense 3D U-Net</text>
    <text x="18" y="78" font-family="sans-serif" font-size="12" font-weight="600" fill="#64748b">Job: 18574378 (nnU-Net Style)</text>

    <!-- Specs Box -->
    <rect x="14" y="94" width="228" height="150" rx="8" fill="#0b1120" stroke="#1e1b4b"/>
    <text x="24" y="116" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Params: <tspan fill="#f1f5f9" font-weight="700">20,903,329 (~20.9M)</tspan></text>
    <text x="24" y="136" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Base Channels: <tspan fill="#f1f5f9" font-weight="700">32 ch (up to 384 ch)</tspan></text>
    <text x="24" y="156" font-family="sans-serif" font-size="11" font-weight="600" fill="#818cf8" font-weight="700">True 3D Convolutions</tspan></text>
    <text x="24" y="176" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">3D Patch Size: <tspan fill="#818cf8" font-weight="700">(64, 768, 64) voxels</tspan></text>
    <text x="24" y="196" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Downsampling: <tspan fill="#f1f5f9" font-weight="700">Anisotropic (1,2,1)</tspan></text>
    <text x="24" y="216" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Normalization: <tspan fill="#f1f5f9" font-weight="700">GroupNorm + SiLU</tspan></text>
    <text x="24" y="234" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Surface Regression: <tspan fill="#94a3b8">Dense Mask Only</tspan></text>

    <!-- Key Metrics -->
    <rect x="14" y="256" width="228" height="155" rx="8" fill="#1e1b4b" stroke="#4338ca"/>
    <text x="24" y="278" font-family="sans-serif" font-size="12" font-weight="700" fill="#a5b4fc">Held-Out V2 Metrics</text>
    <text x="24" y="300" font-family="sans-serif" font-size="11" fill="#94a3b8">Median Dice: <tspan fill="#f8fafc" font-weight="700">0.9471</tspan></text>
    <text x="24" y="322" font-family="sans-serif" font-size="11" fill="#94a3b8">Median MABE: <tspan fill="#f8fafc" font-weight="700">5.50 µm</tspan></text>
    <text x="24" y="344" font-family="sans-serif" font-size="11" fill="#94a3b8">Mean MABE: <tspan fill="#34d399" font-weight="800">5.87 ± 2.13 µm (BEST)</tspan></text>
    <text x="24" y="366" font-family="sans-serif" font-size="11" fill="#94a3b8">Max Scan MABE: <tspan fill="#34d399" font-weight="800">17.02 µm (LOWEST)</tspan></text>
    <text x="24" y="388" font-family="sans-serif" font-size="11" fill="#94a3b8">Cup IoU: <tspan fill="#f8fafc" font-weight="700">0.9085</tspan></text>

    <!-- Verdict Badge -->
    <rect x="14" y="424" width="228" height="52" rx="6" fill="#17143a" stroke="#818cf8"/>
    <text x="24" y="444" font-family="sans-serif" font-size="11" font-weight="700" fill="#818cf8">ROLE: Outlier &amp; QC Guardian</text>
    <text x="24" y="462" font-family="sans-serif" font-size="10" fill="#94a3b8">Zero severe cohort failure cases.</text>
  </g>

  <!-- Model 5: Anisotropic TransUNet ~5.1M - 5.5M -->
  <g transform="translate(1156, 165)">
    <rect width="224" height="490" rx="12" fill="url(#grad-card)" stroke="#6b21a8" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="224" height="6" rx="3" fill="url(#grad-purple)"/>
    
    <rect x="105" y="16" width="105" height="20" rx="4" fill="#3b0764" stroke="#a855f7"/>
    <text x="157" y="30" font-family="sans-serif" font-size="9" font-weight="800" fill="#d8b4fe" text-anchor="middle">EXPERIMENTAL</text>

    <text x="18" y="34" font-family="sans-serif" font-size="12" font-weight="700" fill="#c084fc" letter-spacing="1">CNN + ViT HYBRID</text>
    <text x="18" y="58" font-family="sans-serif" font-size="17" font-weight="800" fill="#f8fafc">TransUNet 5.1M</text>
    <text x="18" y="78" font-family="sans-serif" font-size="12" font-weight="600" fill="#64748b">Job: 18710145 (Hybrid)</text>

    <!-- Specs Box -->
    <rect x="14" y="94" width="196" height="150" rx="8" fill="#0b1120" stroke="#3b0764"/>
    <text x="24" y="116" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Params: <tspan fill="#f1f5f9" font-weight="700">5,099,956 (~5.1M)</tspan></text>
    <text x="24" y="136" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">ViT Layers: <tspan fill="#c084fc" font-weight="700">6 Transformer</tspan></text>
    <text x="24" y="156" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Tokens: <tspan fill="#c084fc" font-weight="700">1,920 (96 × 20)</tspan></text>
    <text x="24" y="176" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Hidden Dim: <tspan fill="#f1f5f9" font-weight="700">d = 256, 8 heads</tspan></text>
    <text x="24" y="196" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Decoder: <tspan fill="#f1f5f9" font-weight="700">Cascaded (CUP)</tspan></text>
    <text x="24" y="216" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Boundary Injection: <tspan fill="#34d399" font-weight="700">Stem Skip f1</tspan></text>
    <text x="24" y="234" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8">Inference Axis: <tspan fill="#f1f5f9" font-weight="700">Bi-Planar (H+V)</tspan></text>

    <!-- Key Metrics -->
    <rect x="14" y="256" width="196" height="155" rx="8" fill="#2e1065" stroke="#7e22ce"/>
    <text x="24" y="278" font-family="sans-serif" font-size="12" font-weight="700" fill="#d8b4fe">Held-Out V2 Metrics</text>
    <text x="24" y="300" font-family="sans-serif" font-size="11" fill="#94a3b8">Median Dice: <tspan fill="#f43f5e" font-weight="700">0.6922 (Underperf)</tspan></text>
    <text x="24" y="322" font-family="sans-serif" font-size="11" fill="#94a3b8">Median MABE: <tspan fill="#f43f5e" font-weight="700">31.90 µm</tspan></text>
    <text x="24" y="344" font-family="sans-serif" font-size="11" fill="#94a3b8">Mean MABE: <tspan fill="#f8fafc">42.69 ± 33.0 µm</tspan></text>
    <text x="24" y="366" font-family="sans-serif" font-size="11" fill="#94a3b8">Median P95: <tspan fill="#f8fafc">86.47 µm</tspan></text>
    <text x="24" y="388" font-family="sans-serif" font-size="11" fill="#94a3b8">Cup IoU: <tspan fill="#f8fafc">0.7282</tspan></text>

    <!-- Verdict Badge -->
    <rect x="14" y="424" width="196" height="52" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-dasharray="3 3"/>
    <text x="24" y="444" font-family="sans-serif" font-size="11" font-weight="700" fill="#c084fc">ROLE: Research Probe</text>
    <text x="24" y="462" font-family="sans-serif" font-size="10" fill="#94a3b8">Requires ablation on token depth.</text>
  </g>

  <!-- Bottom Comparison Strip & Key Architectural Takeaways -->
  <g transform="translate(60, 680)">
    <rect width="1320" height="235" rx="14" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    
    <text x="32" y="36" font-family="sans-serif" font-size="17" font-weight="800" fill="#f8fafc">KEY ARCHITECTURAL FINDINGS &amp; MODEL TAXONOMY LESSONS</text>
    
    <!-- Lesson 1 -->
    <g transform="translate(32, 58)">
      <rect width="395" height="150" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <circle cx="24" cy="24" r="10" fill="#0d9488"/>
      <text x="24" y="28" font-family="sans-serif" font-size="11" font-weight="800" fill="#f8fafc" text-anchor="middle">1</text>
      <text x="44" y="28" font-family="sans-serif" font-size="13" font-weight="700" fill="#2dd4bf">Geometry Trumps Pure Capacity</text>
      <text x="24" y="54" font-family="sans-serif" font-size="11" fill="#cbd5e1" width="350">
        <tspan x="24" dy="0">Upgrading 1.6M → 6.5M in single-planar mode only</tspan>
        <tspan x="24" dy="18">improved Dice from 0.8055 to 0.8562. Introducing</tspan>
        <tspan x="24" dy="18"><tspan fill="#2dd4bf" font-weight="700">Bi-Planar Orthogonal Consensus Fusion</tspan> jumped Dice</tspan>
        <tspan x="24" dy="18">to <tspan fill="#34d399" font-weight="700">0.9518</tspan> and slashed median MABE from 12.6 to 4.7 µm.</tspan>
      </text>
    </g>

    <!-- Lesson 2 -->
    <g transform="translate(457, 58)">
      <rect width="405" height="150" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <circle cx="24" cy="24" r="10" fill="#4f46e5"/>
      <text x="24" y="28" font-family="sans-serif" font-size="11" font-weight="800" fill="#f8fafc" text-anchor="middle">2</text>
      <text x="44" y="28" font-family="sans-serif" font-size="13" font-weight="700" fill="#818cf8">Dense 3D U-Net is an Anisotropic Outlier Shield</text>
      <text x="24" y="54" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="24" dy="0">Dense 3D U-Net operates across 3D voxels, eliminating</tspan>
        <tspan x="24" dy="18">single-slice drift. While Bi-Planar has the lower median</tspan>
        <tspan x="24" dy="18">error (4.71 vs 5.50 µm), Dense 3D achieves lower mean</tspan>
        <tspan x="24" dy="18">MABE (5.87 µm) and lowest worst-case scan error (17.02 µm).</tspan>
      </text>
    </g>

    <!-- Lesson 3 -->
    <g transform="translate(892, 58)">
      <rect width="395" height="150" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <circle cx="24" cy="24" r="10" fill="#d97706"/>
      <text x="24" y="28" font-family="sans-serif" font-size="11" font-weight="800" fill="#f8fafc" text-anchor="middle">3</text>
      <text x="44" y="28" font-family="sans-serif" font-size="13" font-weight="700" fill="#fbbf24">What Was Missed: Canonical STN Model</text>
      <text x="24" y="54" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="24" dy="0">Patient head tilt introduces severe diagonal artifacts.</tspan>
        <tspan x="24" dy="18">The <tspan fill="#fbbf24" font-weight="700">CanonicalVolumetricRNFLNet (~6.61M)</tspan> embeds</tspan>
        <tspan x="24" dy="18">a Spatial Transformer predicting tilt θ ∈ [-25°, +25°],</tspan>
        <tspan x="24" dy="18">bounding boundary drift below &lt;0.8 µm under stress tilt.</tspan>
      </text>
    </g>
  </g>
</svg>"""
    with open(os.path.join(SVG_DIR, "master_frontier_taxonomy.svg"), "w") as f:
        f.write(svg)
    print("Generated master_frontier_taxonomy.svg")


# ==============================================================================
# 2. SINGLE-PLANAR 1.6M RESIDUAL U-NET
# ==============================================================================
def generate_single_planar_svg():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1360 860" width="100%" height="100%">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="1360" height="860" fill="url(#grad-bg)"/>
  
  <g opacity="0.05">
    <path d="{' '.join([f'M {x} 0 L {x} 860' for x in range(0, 1360, 40)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 1360 {y}' for y in range(0, 860, 40)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header -->
  <g transform="translate(60, 40)">
    <rect width="1240" height="85" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="8" height="85" rx="4" fill="url(#grad-blue)"/>
    <text x="32" y="36" font-family="sans-serif" font-size="22" font-weight="800" fill="#f8fafc">MODEL 1: SINGLE-PLANAR 2.5D RESIDUAL U-NET (1.67M PARAMETERS)</text>
    <text x="32" y="62" font-family="sans-serif" font-size="13" font-weight="500" fill="#94a3b8">Baseline Volumetric Architecture: Multi-Slice 2.5D Input Slab, Residual Units, Multi-Task 1D Continuous Surface Heads</text>
    <rect x="1040" y="24" width="168" height="36" rx="6" fill="#0f172a" stroke="#38bdf8"/>
    <text x="1124" y="47" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8" text-anchor="middle">1,672,021 PARAMS</text>
  </g>

  <!-- Input OCT Slab -->
  <g transform="translate(60, 160)">
    <rect width="180" height="340" rx="10" fill="url(#grad-card)" stroke="#38bdf8" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="180" height="6" rx="3" fill="url(#grad-blue)"/>
    <text x="90" y="32" font-family="sans-serif" font-size="13" font-weight="800" fill="#38bdf8" text-anchor="middle">2.5D INPUT SLAB</text>
    <text x="90" y="52" font-family="sans-serif" font-size="11" font-weight="600" fill="#94a3b8" text-anchor="middle">5 Context B-Scans</text>

    <!-- Visual Slices Stack -->
    <g transform="translate(25, 75)">
      <rect x="30" y="0" width="80" height="150" rx="4" fill="#1e293b" stroke="#475569" opacity="0.6"/>
      <rect x="20" y="10" width="80" height="150" rx="4" fill="#1e293b" stroke="#475569" opacity="0.8"/>
      <rect x="10" y="20" width="80" height="150" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="50" y="85" font-family="sans-serif" font-size="10" font-weight="700" fill="#38bdf8" text-anchor="middle">Slice z</text>
      <text x="50" y="105" font-family="sans-serif" font-size="8" fill="#94a3b8" text-anchor="middle">(768 × 320)</text>
    </g>

    <rect x="15" y="255" width="150" height="65" rx="6" fill="#0b1120" stroke="#1e293b"/>
    <text x="25" y="275" font-family="sans-serif" font-size="10" font-weight="700" fill="#f8fafc">Tensor Dimensions:</text>
    <text x="25" y="293" font-family="monospace" font-size="11" font-weight="700" fill="#38bdf8">(B, 5, 768, 320)</text>
    <text x="25" y="310" font-family="sans-serif" font-size="9" fill="#94a3b8">Slow-axis Z window: ±2</text>
  </g>

  <!-- Flow Arrow to Encoder -->
  <line x1="240" y1="330" x2="280" y2="330" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-blue)"/>

  <!-- U-Net Backbone -->
  <!-- Encoder Column -->
  <g transform="translate(290, 160)">
    <rect width="180" height="340" rx="10" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="90" y="28" font-family="sans-serif" font-size="13" font-weight="800" fill="#f8fafc" text-anchor="middle">ENCODER STAGES</text>
    <text x="90" y="46" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">MONAI Residual Units (num=2)</text>

    <!-- Stage 0 -->
    <rect x="15" y="60" width="150" height="48" rx="6" fill="#0f172a" stroke="#0284c7"/>
    <text x="25" y="78" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8">Stage 0 (16 ch)</text>
    <text x="25" y="95" font-family="monospace" font-size="10" fill="#94a3b8">(B, 16, 768, 320)</text>

    <!-- Stage 1 -->
    <rect x="15" y="120" width="150" height="48" rx="6" fill="#0f172a" stroke="#0284c7"/>
    <text x="25" y="138" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8">Stage 1 (32 ch)</text>
    <text x="25" y="155" font-family="monospace" font-size="10" fill="#94a3b8">(B, 32, 384, 160)</text>

    <!-- Stage 2 -->
    <rect x="15" y="180" width="150" height="48" rx="6" fill="#0f172a" stroke="#0284c7"/>
    <text x="25" y="198" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8">Stage 2 (64 ch)</text>
    <text x="25" y="215" font-family="monospace" font-size="10" fill="#94a3b8">(B, 64, 192, 80)</text>

    <!-- Stage 3 -->
    <rect x="15" y="240" width="150" height="48" rx="6" fill="#0f172a" stroke="#0284c7"/>
    <text x="25" y="258" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8">Stage 3 (128 ch)</text>
    <text x="25" y="275" font-family="monospace" font-size="10" fill="#94a3b8">(B, 128, 96, 40)</text>
  </g>

  <!-- Down Arrow to Bottleneck -->
  <line x1="380" y1="500" x2="380" y2="540" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-blue)"/>

  <!-- Bottleneck Box -->
  <g transform="translate(290, 550)">
    <rect width="400" height="75" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.8" filter="url(#shadow)"/>
    <text x="200" y="28" font-family="sans-serif" font-size="13" font-weight="800" fill="#a5b4fc" text-anchor="middle">BOTTLENECK STAGE (256 CHANNELS)</text>
    <text x="200" y="48" font-family="monospace" font-size="12" font-weight="700" fill="#c7d2fe" text-anchor="middle">Shape: (B, 256, 48, 20) | Downsample: Stride (2, 2)</text>
    <text x="200" y="65" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Dual Residual Units + Dropout(0.1)</text>
  </g>

  <!-- Up Arrow to Decoder -->
  <line x1="600" y1="550" x2="600" y2="505" stroke="#2dd4bf" stroke-width="2.5" marker-end="url(#arrow-teal)"/>

  <!-- Skip Connections -->
  <path d="M 440 204 L 510 204" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#arrow)"/>
  <path d="M 440 264 L 510 264" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#arrow)"/>

  <!-- Decoder Column -->
  <g transform="translate(510, 160)">
    <rect width="180" height="340" rx="10" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="90" y="28" font-family="sans-serif" font-size="13" font-weight="800" fill="#f8fafc" text-anchor="middle">DECODER STAGES</text>
    <text x="90" y="46" font-family="sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Transposed Convs + Residual Blocks</text>

    <!-- UpStage 3 -->
    <rect x="15" y="240" width="150" height="48" rx="6" fill="#042f2e" stroke="#0d9488"/>
    <text x="25" y="258" font-family="sans-serif" font-size="11" font-weight="700" fill="#2dd4bf">UpStage 3 (128 ch)</text>
    <text x="25" y="275" font-family="monospace" font-size="10" fill="#94a3b8">(B, 128, 96, 40)</text>

    <!-- UpStage 2 -->
    <rect x="15" y="180" width="150" height="48" rx="6" fill="#042f2e" stroke="#0d9488"/>
    <text x="25" y="198" font-family="sans-serif" font-size="11" font-weight="700" fill="#2dd4bf">UpStage 2 (64 ch)</text>
    <text x="25" y="215" font-family="monospace" font-size="10" fill="#94a3b8">(B, 64, 192, 80)</text>

    <!-- UpStage 1 -->
    <rect x="15" y="120" width="150" height="48" rx="6" fill="#042f2e" stroke="#0d9488"/>
    <text x="25" y="138" font-family="sans-serif" font-size="11" font-weight="700" fill="#2dd4bf">UpStage 1 (32 ch)</text>
    <text x="25" y="155" font-family="monospace" font-size="10" fill="#94a3b8">(B, 32, 384, 160)</text>

    <!-- UpStage 0 Final Features -->
    <rect x="15" y="60" width="150" height="48" rx="6" fill="#042f2e" stroke="#14b8a6"/>
    <text x="25" y="78" font-family="sans-serif" font-size="11" font-weight="800" fill="#2dd4bf">Final Feats (16 ch)</text>
    <text x="25" y="95" font-family="monospace" font-size="10" fill="#5eead4">(B, 16, 768, 320)</text>
  </g>

  <!-- Forking to Multi-Task Heads -->
  <path d="M 690 184 L 750 184" stroke="#2dd4bf" stroke-width="2.5" marker-end="url(#arrow-teal)"/>

  <!-- Multi-Task Heads Container -->
  <g transform="translate(760, 160)">
    <rect width="540" height="465" rx="12" fill="url(#grad-card)" stroke="#14b8a6" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="540" height="6" rx="3" fill="url(#grad-teal)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="15" font-weight="800" fill="#2dd4bf">MULTI-TASK HEADS (Branching from 16-channel Feats)</text>
    <text x="24" y="50" font-family="sans-serif" font-size="11" fill="#94a3b8">Joint Optimization: Voxel Logits + 1D Continuous Boundary Regression + Cup Absence</text>

    <!-- Head 1: Dense 2D Mask Head -->
    <g transform="translate(20, 68)">
      <rect width="500" height="95" rx="8" fill="#0b1120" stroke="#0284c7" stroke-width="1.2"/>
      <text x="18" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#38bdf8">1. Dense Voxel Mask Head</text>
      <text x="18" y="44" font-family="monospace" font-size="11" fill="#cbd5e1">Conv2d(16 → 1, 1x1) → mask_logits: (B, 1, 768, 320)</text>
      <text x="18" y="64" font-family="sans-serif" font-size="10" fill="#94a3b8">Differentiable column thickness: column_thickness = Σ σ(mask_logits) over H (768)</text>
      <rect x="360" y="16" width="125" height="26" rx="4" fill="#0369a1"/>
      <text x="422" y="33" font-family="sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">VOXEL LABELMAP</text>
    </g>

    <!-- Head 2: 1D Boundary Regression Head -->
    <g transform="translate(20, 175)">
      <rect width="500" height="150" rx="8" fill="#0b1120" stroke="#059669" stroke-width="1.2"/>
      <text x="18" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#34d399">2. 1D Continuous Boundary Regression Head</text>
      <text x="18" y="44" font-family="monospace" font-size="11" fill="#cbd5e1">AdaptiveAvgPool2d((1, 320)) → Squeeze → (B, 16, 320)</text>
      <text x="18" y="64" font-family="sans-serif" font-size="10" fill="#94a3b8">Branch A: Conv1d(16→64→32→1, k=7,5,3) → ilm_pred = σ(raw) × 768  [Row px]</text>
      <text x="18" y="84" font-family="sans-serif" font-size="10" fill="#94a3b8">Branch B: Conv1d(16→64→32→1, k=7,5,3) → nfl_pred = σ(raw) × 768  [Row px]</text>
      <text x="18" y="104" font-family="sans-serif" font-size="10" fill="#94a3b8">Branch C: Conv1d(16→32→1, k=7,3)       → cup_logits: (B, 320)  [Cavity presence]</text>
      
      <rect x="360" y="16" width="125" height="26" rx="4" fill="#047857"/>
      <text x="422" y="33" font-family="sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">EXPLICIT CURVES</text>
      <text x="18" y="132" font-family="sans-serif" font-size="10" font-weight="700" fill="#6ee7b7">Bypasses argmax discretization! Yields sub-voxel continuous depths.</text>
    </g>

    <!-- Head 3: Loss Formulations -->
    <g transform="translate(20, 335)">
      <rect width="500" height="110" rx="8" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.2"/>
      <text x="18" y="24" font-family="sans-serif" font-size="12" font-weight="700" fill="#a5b4fc">3. Multi-Objective Joint Loss</text>
      <text x="18" y="46" font-family="monospace" font-size="11" font-weight="700" fill="#e0e7ff">L_total = L_Tversky + 0.5·L_BCE_mask + 1.0·L_boundary + 0.2·L_cup + 0.1·L_edge</text>
      <text x="18" y="68" font-family="sans-serif" font-size="10" fill="#c7d2fe">• Tversky Loss handles severe class imbalance (RNFL is &lt;4% of total slice area)</text>
      <text x="18" y="86" font-family="sans-serif" font-size="10" fill="#c7d2fe">• Edge Loss (Sobel optical gradient) snaps curves to true physical tissue reflectances</text>
    </g>
  </g>

  <!-- Bottom Explanatory Banner -->
  <g transform="translate(60, 650)">
    <rect width="1240" height="165" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="28" y="32" font-family="sans-serif" font-size="14" font-weight="800" fill="#f8fafc">WHY SINGLE-PLANAR 1.6M WAS INSUFFICIENT FOR FRONTIER CLINICAL USE</text>
    
    <g transform="translate(28, 50)">
      <circle cx="12" cy="12" r="8" fill="#f43f5e"/>
      <text x="12" y="16" font-family="sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">!</text>
      <text x="30" y="16" font-family="sans-serif" font-size="12" font-weight="700" fill="#fda4af">Inter-B-Scan Anisotropy:</text>
      <text x="30" y="34" font-family="sans-serif" font-size="11" fill="#94a3b8">
        Solix OCT acquires 128 B-scans with lateral spacing ~18.7 µm but inter-B-scan slow-axis spacing ~40 µm. Single-planar models process slices
        independently along X-Z. Without vertical orthogonal cross-checks, predicted en face thickness maps exhibited severe "sawtooth" banding.
      </text>
    </g>

    <g transform="translate(28, 105)">
      <circle cx="12" cy="12" r="8" fill="#f43f5e"/>
      <text x="12" y="16" font-family="sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">!</text>
      <text x="30" y="16" font-family="sans-serif" font-size="12" font-weight="700" fill="#fda4af">Held-Out Error Distribution:</text>
      <text x="30" y="34" font-family="sans-serif" font-size="11" fill="#94a3b8">
        Achieved median MABE of 12.58 µm and Dice of 0.8055 on held-out cohort (V2 split). This proved that multi-slice context alone (5 slices)
        was not enough to bridge the optic cup gap or correct commercial heuristic errors without orthogonal cross-validation.
      </text>
    </g>
  </g>
</svg>"""
    with open(os.path.join(SVG_DIR, "01_single_planar_1.6m.svg"), "w") as f:
        f.write(svg)
    print("Generated 01_single_planar_1.6m.svg")


# ==============================================================================
# 3. BIPLANAR ORTHOGONAL FUSION (1.6M & 6.5M)
# ==============================================================================
def generate_biplanar_svg():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 920" width="100%" height="100%">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="1440" height="920" fill="url(#grad-bg)"/>
  
  <g opacity="0.05">
    <path d="{' '.join([f'M {x} 0 L {x} 920' for x in range(0, 1440, 40)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 1440 {y}' for y in range(0, 920, 40)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header -->
  <g transform="translate(60, 40)">
    <rect width="1320" height="90" rx="12" fill="url(#grad-card)" stroke="#0d9488" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="8" height="90" rx="4" fill="url(#grad-teal)"/>
    <text x="32" y="36" font-family="sans-serif" font-size="22" font-weight="800" fill="#f8fafc">MODEL 2: BI-PLANAR ORTHOGONAL RESIDUAL U-NET (16-CH 1.67M &amp; 32-CH 6.58M)</text>
    <text x="32" y="64" font-family="sans-serif" font-size="13" font-weight="500" fill="#94a3b8">The Lead Frontier Architecture: Dual-Plane Volumetric Consensus Fusion, Boundary Continuity, and Outlier Suppression</text>
    <rect x="1100" y="26" width="188" height="38" rx="6" fill="#042f2e" stroke="#2dd4bf"/>
    <text x="1194" y="50" font-family="sans-serif" font-size="12" font-weight="800" fill="#2dd4bf" text-anchor="middle">MEDIAN MABE 4.71 µm</text>
  </g>

  <!-- 3D OCT Volume Box -->
  <g transform="translate(60, 160)">
    <rect width="260" height="420" rx="12" fill="url(#grad-card)" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="260" height="6" rx="3" fill="url(#grad-blue)"/>
    <text x="130" y="32" font-family="sans-serif" font-size="14" font-weight="800" fill="#38bdf8" text-anchor="middle">ACQUIRED 3D OCT VOLUME</text>
    <text x="130" y="52" font-family="monospace" font-size="11" fill="#94a3b8" text-anchor="middle">V(Z=128, Y=768, X=320)</text>

    <!-- 3D Cube Isometric Visualization -->
    <g transform="translate(45, 80)">
      <!-- Front Face (X-Y) -->
      <polygon points="20,80 140,80 140,220 20,220" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Top Face (X-Z) -->
      <polygon points="20,80 80,20 200,20 140,80" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
      <!-- Right Face (Y-Z) -->
      <polygon points="140,80 200,20 200,160 140,220" fill="#1e293b" stroke="#0284c7" stroke-width="1.5"/>
      
      <!-- Slice Planes Indicators -->
      <!-- Horizontal Slice Pass (Cyan) -->
      <polygon points="20,130 140,130 200,70 80,70" fill="#06b6d4" fill-opacity="0.3" stroke="#22d3ee" stroke-width="2"/>
      <text x="110" y="115" font-family="sans-serif" font-size="10" font-weight="800" fill="#22d3ee">Horizontal Pass</text>
      
      <!-- Vertical Orthogonal Slice Pass (Teal) -->
      <polygon points="80,20 80,160 80,220 80,80" fill="#14b8a6" fill-opacity="0.4" stroke="#2dd4bf" stroke-width="2"/>
      <text x="35" y="180" font-family="sans-serif" font-size="10" font-weight="800" fill="#2dd4bf">Vertical Pass</text>
    </g>

    <!-- Voxel Resolution Specs -->
    <rect x="18" y="315" width="224" height="90" rx="6" fill="#0b1120" stroke="#1e293b"/>
    <text x="28" y="335" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Anisotropic Physical Resolution:</text>
    <text x="28" y="353" font-family="sans-serif" font-size="10" fill="#94a3b8">• Axial Y: <tspan fill="#38bdf8" font-weight="700">~3.9 µm/px</tspan> (768 rows)</text>
    <text x="28" y="371" font-family="sans-serif" font-size="10" fill="#94a3b8">• Fast X: <tspan fill="#38bdf8" font-weight="700">~18.7 µm/px</tspan> (320 cols)</text>
    <text x="28" y="389" font-family="sans-serif" font-size="10" fill="#94a3b8">• Slow Z: <tspan fill="#fb7185" font-weight="700">~40.0 µm/scan</tspan> (128 slices)</text>
  </g>

  <!-- Dual Forward Stream Pathways -->
  <!-- Stream 1: Horizontal Pass -->
  <g transform="translate(360, 160)">
    <rect width="320" height="200" rx="10" fill="url(#grad-card)" stroke="#0ea5e9" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="16" y="28" font-family="sans-serif" font-size="13" font-weight="800" fill="#38bdf8">STREAM A: HORIZONTAL B-SCANS</text>
    <text x="16" y="46" font-family="sans-serif" font-size="10" fill="#94a3b8">Native Acquisition Planes (Fast X-Z Axis)</text>

    <rect x="16" y="60" width="288" height="60" rx="6" fill="#0b1120" stroke="#0284c7"/>
    <text x="26" y="80" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Input: 128 Slices of 5-Channel Slabs</text>
    <text x="26" y="98" font-family="monospace" font-size="11" fill="#38bdf8">Shape: (128, 5, 768, 320)</text>

    <rect x="16" y="130" width="288" height="55" rx="6" fill="#075985"/>
    <text x="26" y="150" font-family="sans-serif" font-size="11" font-weight="700" fill="#ffffff">Outputs Horizontal Predictions:</text>
    <text x="26" y="168" font-family="monospace" font-size="11" fill="#e0f2fe">V_hat_H: (128, 768, 320) probabilities</text>
  </g>

  <!-- Stream 2: Vertical Orthogonal Pass -->
  <g transform="translate(360, 380)">
    <rect width="320" height="200" rx="10" fill="url(#grad-card)" stroke="#0d9488" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="16" y="28" font-family="sans-serif" font-size="13" font-weight="800" fill="#2dd4bf">STREAM B: VERTICAL ORTHOGONAL SLICES</text>
    <text x="16" y="46" font-family="sans-serif" font-size="10" fill="#94a3b8">Resampled Slices Orthogonal to Acquisition (Slow Y-Z Axis)</text>

    <rect x="16" y="60" width="288" height="60" rx="6" fill="#0b1120" stroke="#0f766e"/>
    <text x="26" y="80" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Input: 320 Slices of 5-Channel Slabs</text>
    <text x="26" y="98" font-family="monospace" font-size="11" fill="#2dd4bf">Shape: (320, 5, 768, 128)</text>

    <rect x="16" y="130" width="288" height="55" rx="6" fill="#134e4a"/>
    <text x="26" y="150" font-family="sans-serif" font-size="11" font-weight="700" fill="#ffffff">Outputs Vertical Predictions:</text>
    <text x="26" y="168" font-family="monospace" font-size="11" fill="#ccfbf1">V_hat_V: (320, 768, 128) resampled</text>
  </g>

  <!-- Connectors from Input to Streams -->
  <path d="M 320 260 L 360 260" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-blue)"/>
  <path d="M 320 480 L 360 480" stroke="#2dd4bf" stroke-width="2.5" marker-end="url(#arrow-teal)"/>

  <!-- Shared Neural Backbone Box in the middle -->
  <g transform="translate(710, 260)">
    <rect width="280" height="220" rx="10" fill="url(#grad-card)" stroke="#2dd4bf" stroke-width="2" filter="url(#shadow)"/>
    <rect width="280" height="6" rx="3" fill="url(#grad-teal)"/>
    <text x="140" y="32" font-family="sans-serif" font-size="14" font-weight="800" fill="#f8fafc" text-anchor="middle">SHARED VOLUMETRIC BACKBONE</text>
    <text x="140" y="50" font-family="sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Weights Shared Across Both Streams</text>

    <!-- Channels Options Comparison -->
    <rect x="16" y="66" width="248" height="65" rx="6" fill="#042f2e" stroke="#0d9488"/>
    <text x="26" y="86" font-family="sans-serif" font-size="11" font-weight="800" fill="#2dd4bf">1. Light Variant (16 Channels)</text>
    <text x="26" y="104" font-family="sans-serif" font-size="10" fill="#cbd5e1">1,672,021 params | Channels: (16,32,64,128,256)</text>
    <text x="26" y="120" font-family="sans-serif" font-size="9" fill="#94a3b8">Fast inference; ideal for low-VRAM edge clinical nodes</text>

    <rect x="16" y="140" width="248" height="65" rx="6" fill="#042f2e" stroke="#14b8a6"/>
    <text x="26" y="160" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">2. Heavy Variant (32 Channels - LEAD)</text>
    <text x="26" y="178" font-family="sans-serif" font-size="10" fill="#cbd5e1">6,581,461 params | Channels: (32,64,128,256,512)</text>
    <text x="26" y="194" font-family="sans-serif" font-size="9" fill="#94a3b8">Current best research performer (Median MABE 4.71 µm)</text>
  </g>

  <!-- Connectors from Streams through Backbone -->
  <path d="M 680 260 L 710 320" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-blue)"/>
  <path d="M 680 480 L 710 420" stroke="#2dd4bf" stroke-width="2" marker-end="url(#arrow-teal)"/>

  <!-- Consensus Fusion Engine -->
  <g transform="translate(1030, 210)">
    <rect width="350" height="320" rx="12" fill="url(#grad-card)" stroke="#14b8a6" stroke-width="2" filter="url(#shadow)"/>
    <rect width="350" height="6" rx="3" fill="url(#grad-emerald)"/>
    <text x="175" y="32" font-family="sans-serif" font-size="15" font-weight="800" fill="#34d399" text-anchor="middle">3D CONSENSUS FUSION ENGINE</text>
    <text x="175" y="52" font-family="sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Volumetric Re-Alignment &amp; Probability Fusion</text>

    <g transform="translate(18, 68)">
      <rect width="314" height="65" rx="6" fill="#0b1120" stroke="#134e4a"/>
      <text x="14" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">1. Spatial Coordinate Alignment:</text>
      <text x="14" y="44" font-family="monospace" font-size="11" fill="#2dd4bf">V_hat_V_aligned = Permute(V_hat_V, (2, 1, 0))</text>
      <text x="14" y="58" font-family="sans-serif" font-size="9" fill="#94a3b8">Transposes vertical tensor back to standard (Z, Y, X) space</text>
    </g>

    <g transform="translate(18, 142)">
      <rect width="314" height="65" rx="6" fill="#0b1120" stroke="#134e4a"/>
      <text x="14" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">2. Consensus Probability Average:</text>
      <text x="14" y="44" font-family="monospace" font-size="11" fill="#34d399">P_consensus = 0.5 · P_H + 0.5 · P_V</text>
      <text x="14" y="58" font-family="sans-serif" font-size="9" fill="#94a3b8">Cancels out inter-B-scan steps and false positives</text>
    </g>

    <g transform="translate(18, 216)">
      <rect width="314" height="85" rx="6" fill="#042f2e" stroke="#2dd4bf"/>
      <text x="14" y="22" font-family="sans-serif" font-size="11" font-weight="800" fill="#2dd4bf">3. Clinical Post-Processing Pipeline:</text>
      <text x="14" y="40" font-family="sans-serif" font-size="10" fill="#e2e8f0">• <tspan font-weight="700" fill="#38bdf8">Surface-Guided Clamping:</tspan> Drops FP below RPE (2.0 px)</text>
      <text x="14" y="58" font-family="sans-serif" font-size="10" fill="#e2e8f0">• <tspan font-weight="700" fill="#fbbf24">Optic Cup-Reach Tracking:</tspan> Accurately stops at cup rim</text>
      <text x="14" y="74" font-family="sans-serif" font-size="10" fill="#e2e8f0">• <tspan font-weight="700" fill="#34d399">Native OS Orientation:</tspan> Flips OS laterality correctly</text>
    </g>
  </g>

  <!-- Connectors from Backbone to Fusion Engine -->
  <path d="M 990 370 L 1030 370" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrow-green)"/>

  <!-- Performance Comparison Footer -->
  <g transform="translate(60, 600)">
    <rect width="1320" height="280" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="32" y="32" font-family="sans-serif" font-size="16" font-weight="800" fill="#f8fafc">HELD-OUT VALIDATION EVIDENCE: BIPLANAR 2.5D VS OTHER APPROACHES</text>

    <!-- Table Header -->
    <g transform="translate(32, 50)">
      <rect width="1256" height="32" rx="4" fill="#1e293b"/>
      <text x="20" y="21" font-family="sans-serif" font-size="11" font-weight="700" fill="#94a3b8">ARCHITECTURE / ARM</text>
      <text x="320" y="21" font-family="sans-serif" font-size="11" font-weight="700" fill="#94a3b8">PARAMS</text>
      <text x="460" y="21" font-family="sans-serif" font-size="11" font-weight="700" fill="#94a3b8">MEDIAN DICE</text>
      <text x="620" y="21" font-family="sans-serif" font-size="11" font-weight="700" fill="#94a3b8">MEDIAN MABE</text>
      <text x="780" y="21" font-family="sans-serif" font-size="11" font-weight="700" fill="#94a3b8">P95 ERROR</text>
      <text x="940" y="21" font-family="sans-serif" font-size="11" font-weight="700" fill="#94a3b8">CUP IoU</text>
      <text x="1100" y="21" font-family="sans-serif" font-size="11" font-weight="700" fill="#94a3b8">CLINICAL STATUS</text>
    </g>

    <!-- Row 1: Commercial Heuristic -->
    <g transform="translate(32, 88)">
      <rect width="1256" height="36" rx="4" fill="#0b1120"/>
      <text x="20" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#f43f5e">Solix Commercial Heuristic</text>
      <text x="320" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">N/A (Rules)</text>
      <text x="460" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">0.9233*</text>
      <text x="620" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">5.17 µm*</text>
      <text x="780" y="23" font-family="sans-serif" font-size="11" fill="#f43f5e">34.21 µm</text>
      <text x="940" y="23" font-family="sans-serif" font-size="11" fill="#f43f5e">0.8063</text>
      <text x="1100" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#f43f5e">High cup-bridging error</text>
    </g>

    <!-- Row 2: Single-Planar 1.6M -->
    <g transform="translate(32, 130)">
      <rect width="1256" height="36" rx="4" fill="#0b1120"/>
      <text x="20" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8">Single-Planar 2.5D Light</text>
      <text x="320" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">1.67M</text>
      <text x="460" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">0.8055</text>
      <text x="620" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">12.58 µm</text>
      <text x="780" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">32.96 µm</text>
      <text x="940" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">0.8422</text>
      <text x="1100" y="23" font-family="sans-serif" font-size="11" fill="#94a3b8">Early prototype</text>
    </g>

    <!-- Row 3: Bi-Planar 16-Channel 1.67M -->
    <g transform="translate(32, 172)">
      <rect width="1256" height="36" rx="4" fill="#042f2e"/>
      <text x="20" y="23" font-family="sans-serif" font-size="11" font-weight="700" fill="#2dd4bf">Bi-Planar 2.5D (16 Channel)</text>
      <text x="320" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">1.67M</text>
      <text x="460" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">0.9422</text>
      <text x="620" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">4.91 µm</text>
      <text x="780" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">16.90 µm</text>
      <text x="940" y="23" font-family="sans-serif" font-size="11" fill="#cbd5e1">0.9213</text>
      <text x="1100" y="23" font-family="sans-serif" font-size="11" fill="#2dd4bf">Efficient deployment candidate</text>
    </g>

    <!-- Row 4: Bi-Planar 32-Channel 6.58M -->
    <g transform="translate(32, 214)">
      <rect width="1256" height="42" rx="4" fill="#042f2e" stroke="#2dd4bf" stroke-width="1.5"/>
      <text x="20" y="26" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">Bi-Planar 2.5D (32 Channel - LEAD)</text>
      <text x="320" y="26" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">6.58M</text>
      <text x="460" y="26" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">0.9518</text>
      <text x="620" y="26" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">4.71 µm</text>
      <text x="780" y="26" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">16.85 µm</text>
      <text x="940" y="26" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">0.9388</text>
      <text x="1100" y="26" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">Lead Research Champion (34/40 wins)</text>
    </g>
  </g>
</svg>"""
    with open(os.path.join(SVG_DIR, "02_biplanar_orthogonal_fusion.svg"), "w") as f:
        f.write(svg)
    print("Generated 02_biplanar_orthogonal_fusion.svg")


# ==============================================================================
# 4. DENSE ANISOTROPIC 3D U-NET (20.9M)
# ==============================================================================
def generate_dense_3d_svg():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1380 900" width="100%" height="100%">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="1380" height="900" fill="url(#grad-bg)"/>
  
  <g opacity="0.05">
    <path d="{' '.join([f'M {x} 0 L {x} 900' for x in range(0, 1380, 40)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 1380 {y}' for y in range(0, 900, 40)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header -->
  <g transform="translate(60, 40)">
    <rect width="1260" height="90" rx="12" fill="url(#grad-card)" stroke="#4338ca" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="8" height="90" rx="4" fill="url(#grad-indigo)"/>
    <text x="32" y="36" font-family="sans-serif" font-size="22" font-weight="800" fill="#f8fafc">MODEL 3: DENSE ANISOTROPIC 3D U-NET (20.9M PARAMETERS)</text>
    <text x="32" y="64" font-family="sans-serif" font-size="13" font-weight="500" fill="#94a3b8">Colloquially "nnU-Net 25M": Full 3D Convolutions, Anisotropic Axial Strides, GroupNorm + SiLU, Outlier Immunity</text>
    <rect x="1050" y="26" width="180" height="38" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
    <text x="1140" y="50" font-family="sans-serif" font-size="12" font-weight="800" fill="#a5b4fc" text-anchor="middle">20,903,329 PARAMS</text>
  </g>

  <!-- Left: Why Anisotropic 3D? -->
  <g transform="translate(60, 160)">
    <rect width="330" height="420" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="15" font-weight="800" fill="#818cf8">THE ANISOTROPY CHALLENGE</text>
    <text x="24" y="50" font-family="sans-serif" font-size="11" fill="#94a3b8">Standard 3D U-Nets fail due to extreme voxel ratio:</text>

    <!-- Visual Aspect Ratio Comparison -->
    <g transform="translate(24, 75)">
      <rect width="280" height="90" rx="6" fill="#0b1120" stroke="#1e293b"/>
      <text x="16" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Solix OCT Voxel Spacing Ratio:</text>
      <text x="16" y="42" font-family="monospace" font-size="11" fill="#fb7185">Z (Slow) : Y (Axial) : X (Fast) ≈ 10.3 : 1.0 : 4.8</text>
      <text x="16" y="60" font-family="sans-serif" font-size="10" fill="#94a3b8">• Axial Y depth is ultra-fine (3.9 µm/px, 768 rows)</text>
      <text x="16" y="76" font-family="sans-serif" font-size="10" fill="#94a3b8">• Slow Z spacing is coarse (40 µm/scan, 128 slices)</text>
    </g>

    <g transform="translate(24, 180)">
      <rect width="280" height="110" rx="6" fill="#1e1b4b" stroke="#4338ca"/>
      <text x="16" y="22" font-family="sans-serif" font-size="11" font-weight="800" fill="#a5b4fc">Anisotropic Downsampling Strategy:</text>
      <text x="16" y="42" font-family="sans-serif" font-size="10" fill="#e2e8f0">• <tspan font-weight="700" fill="#818cf8">Down 1 &amp; 2:</tspan> Stride <tspan font-weight="700" fill="#38bdf8">(1, 2, 1)</tspan></text>
      <text x="16" y="58" font-family="sans-serif" font-size="9" fill="#94a3b8">  Pools axial Y only! Leaves Z and X intact.</text>
      <text x="16" y="76" font-family="sans-serif" font-size="10" fill="#e2e8f0">• <tspan font-weight="700" fill="#818cf8">Down 3 &amp; Bottleneck:</tspan> Stride <tspan font-weight="700" fill="#38bdf8">(2, 2, 2)</tspan></text>
      <text x="16" y="92" font-family="sans-serif" font-size="9" fill="#94a3b8">  Isotropic pooling once receptive field is balanced.</text>
    </g>

    <g transform="translate(24, 305)">
      <rect width="280" height="95" rx="6" fill="#0b1120" stroke="#1e293b"/>
      <text x="16" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">3D Patch Extraction Window:</text>
      <text x="16" y="42" font-family="monospace" font-size="11" fill="#818cf8">Patch: (64, 768, 64) voxels</text>
      <text x="16" y="60" font-family="sans-serif" font-size="10" fill="#94a3b8">• 64 slow-axis Z slices (50% of volume)</text>
      <text x="16" y="76" font-family="sans-serif" font-size="10" fill="#94a3b8">• Full 768 axial depth (zero cropping loss!)</text>
    </g>
  </g>

  <!-- Middle: Full 3D Network Architecture Diagram -->
  <g transform="translate(420, 160)">
    <rect width="890" height="420" rx="12" fill="url(#grad-card)" stroke="#4338ca" stroke-width="1.8" filter="url(#shadow)"/>
    <text x="28" y="32" font-family="sans-serif" font-size="15" font-weight="800" fill="#a5b4fc">3D U-NET PIPELINE &amp; TENSOR DIMENSIONS</text>
    <text x="28" y="50" font-family="sans-serif" font-size="11" fill="#94a3b8">Anisotropic ConvBlock3D (Dual Conv3D + GroupNorm(min 8, C) + SiLU)</text>

    <!-- Encoder Column -->
    <g transform="translate(28, 70)">
      <!-- Enc 0 -->
      <rect width="180" height="50" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
      <text x="14" y="22" font-family="sans-serif" font-size="11" font-weight="800" fill="#c7d2fe">Encoder 0 (32 ch)</text>
      <text x="14" y="38" font-family="monospace" font-size="10" fill="#818cf8">(B, 32, 64, 768, 64)</text>

      <!-- Down 1 -->
      <rect y="65" width="180" height="50" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
      <text x="14" y="87" font-family="sans-serif" font-size="11" font-weight="800" fill="#c7d2fe">Encoder 1 (64 ch)</text>
      <text x="14" y="103" font-family="monospace" font-size="10" fill="#818cf8">(B, 64, 64, 384, 64)</text>
      <text x="190" y="93" font-family="sans-serif" font-size="9" fill="#fbbf24">Stride (1,2,1) ↓</text>

      <!-- Down 2 -->
      <rect y="130" width="180" height="50" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
      <text x="14" y="152" font-family="sans-serif" font-size="11" font-weight="800" fill="#c7d2fe">Encoder 2 (128 ch)</text>
      <text x="14" y="168" font-family="monospace" font-size="10" fill="#818cf8">(B, 128, 64, 192, 64)</text>
      <text x="190" y="158" font-family="sans-serif" font-size="9" fill="#fbbf24">Stride (1,2,1) ↓</text>

      <!-- Down 3 -->
      <rect y="195" width="180" height="50" rx="6" fill="#1e1b4b" stroke="#6366f1"/>
      <text x="14" y="217" font-family="sans-serif" font-size="11" font-weight="800" fill="#c7d2fe">Encoder 3 (256 ch)</text>
      <text x="14" y="233" font-family="monospace" font-size="10" fill="#818cf8">(B, 256, 32, 96, 32)</text>
      <text x="190" y="223" font-family="sans-serif" font-size="9" fill="#38bdf8">Stride (2,2,2) ↓</text>
    </g>

    <!-- Bottleneck -->
    <g transform="translate(270, 265)">
      <rect width="250" height="60" rx="8" fill="#31104b" stroke="#a855f7" stroke-width="1.8"/>
      <text x="125" y="24" font-family="sans-serif" font-size="12" font-weight="800" fill="#f0abfc" text-anchor="middle">BOTTLENECK (384 CHANNELS)</text>
      <text x="125" y="42" font-family="monospace" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">(B, 384, 16, 48, 16)</text>
      <text x="125" y="55" font-family="sans-serif" font-size="8" fill="#e879f9" text-anchor="middle">Global Volumetric 3D Context</text>
    </g>

    <!-- Connectors: Enc3 to Bottleneck -->
    <path d="M 210 295 L 270 295" stroke="#a855f7" stroke-width="2" marker-end="url(#arrow-purple)"/>
    <!-- Bottleneck to Dec3 -->
    <path d="M 520 295 L 570 295" stroke="#a855f7" stroke-width="2" marker-end="url(#arrow-purple)"/>

    <!-- Decoder Column -->
    <g transform="translate(570, 70)">
      <!-- Up 3 -->
      <rect y="195" width="280" height="50" rx="6" fill="#172554" stroke="#3b82f6"/>
      <text x="14" y="217" font-family="sans-serif" font-size="11" font-weight="800" fill="#93c5fd">Decoder 3 (256 ch)</text>
      <text x="14" y="233" font-family="monospace" font-size="10" fill="#60a5fa">Trilinear Interp + Skip Enc 3</text>

      <!-- Up 2 -->
      <rect y="130" width="280" height="50" rx="6" fill="#172554" stroke="#3b82f6"/>
      <text x="14" y="152" font-family="sans-serif" font-size="11" font-weight="800" fill="#93c5fd">Decoder 2 (128 ch)</text>
      <text x="14" y="168" font-family="monospace" font-size="10" fill="#60a5fa">Trilinear Interp + Skip Enc 2</text>

      <!-- Up 1 -->
      <rect y="65" width="280" height="50" rx="6" fill="#172554" stroke="#3b82f6"/>
      <text x="14" y="87" font-family="sans-serif" font-size="11" font-weight="800" fill="#93c5fd">Decoder 1 (64 ch)</text>
      <text x="14" y="103" font-family="monospace" font-size="10" fill="#60a5fa">Trilinear Interp + Skip Enc 1</text>

      <!-- Up 0 -->
      <rect width="280" height="50" rx="6" fill="#172554" stroke="#60a5fa"/>
      <text x="14" y="22" font-family="sans-serif" font-size="11" font-weight="800" fill="#bfdbfe">Decoder 0 (32 ch) → Conv3D 1x1</text>
      <text x="14" y="38" font-family="monospace" font-size="10" fill="#93c5fd">Output: (B, 1, 64, 768, 64) logits</text>
    </g>

    <!-- 3D Skip Connections -->
    <path d="M 210 95 L 570 95" stroke="#475569" stroke-width="1.2" stroke-dasharray="3 3"/>
    <path d="M 210 160 L 570 160" stroke="#475569" stroke-width="1.2" stroke-dasharray="3 3"/>
    <path d="M 210 225 L 570 225" stroke="#475569" stroke-width="1.2" stroke-dasharray="3 3"/>
  </g>

  <!-- Bottom: Dense 3D Clinical Insights -->
  <g transform="translate(60, 600)">
    <rect width="1260" height="260" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="32" y="32" font-family="sans-serif" font-size="16" font-weight="800" fill="#f8fafc">WHY DENSE 3D IS THE "OUTLIER SHIELD" FOR THE RESEARCH COHORT</text>

    <g transform="translate(32, 55)">
      <rect width="580" height="180" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#818cf8">1. Outlier Sensitivity &amp; Worst-Case Error Bound</text>
      <text x="20" y="52" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="20" dy="0">In the 40-eye held-out benchmark, Bi-Planar 2.5D recorded an observed</tspan>
        <tspan x="20" dy="18">maximum scan MABE of <tspan fill="#f43f5e" font-weight="700">39.64 µm</tspan> on subject BEH0290 OD due to localized</tspan>
        <tspan x="20" dy="18">blood-vessel shadowing. On that exact eye, Dense 3D recorded <tspan fill="#34d399" font-weight="700">4.84 µm</tspan>.</tspan>
        <tspan x="20" dy="24">Dense 3D's observed cohort maximum was only <tspan fill="#34d399" font-weight="800">17.02 µm</tspan> (lowest in cohort).</tspan>
        <tspan x="20" dy="18">True 3D receptive fields prevent unconstrained single-slice boundary collapse.</tspan>
      </text>
    </g>

    <g transform="translate(640, 55)">
      <rect width="580" height="180" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#818cf8">2. Trade-off: Mean vs. Median Accuracy</text>
      <text x="20" y="52" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="20" dy="0">• <tspan fill="#818cf8" font-weight="700">Mean MABE Winner:</tspan> Dense 3D achieved <tspan fill="#34d399" font-weight="700">5.87 ± 2.13 µm</tspan> vs 6.22 µm for Bi-Planar.</tspan>
        <tspan x="20" dy="18">• <tspan fill="#2dd4bf" font-weight="700">Median MABE Winner:</tspan> Bi-Planar won on 34/40 eyes (<tspan fill="#2dd4bf" font-weight="700">4.71 µm</tspan> vs 5.50 µm).</tspan>
        <tspan x="20" dy="24">• <tspan fill="#fbbf24" font-weight="700">Clinical Deployment Recommendation:</tspan></tspan>
        <tspan x="20" dy="18">  Use Bi-Planar 2.5D as the primary measurement tool; use Dense 3D as a</tspan>
        <tspan x="20" dy="18">  disagreement-based automated quality-control gatekeeper!</tspan>
      </text>
    </g>
  </g>
</svg>"""
    with open(os.path.join(SVG_DIR, "03_dense_3d_anisotropic_unet.svg"), "w") as f:
        f.write(svg)
    print("Generated 03_dense_3d_anisotropic_unet.svg")


# ==============================================================================
# 5. HYBRID ANISOTROPIC TRANSUNET (5.1M - 5.5M)
# ==============================================================================
def generate_transunet_svg():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 920" width="100%" height="100%">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="1440" height="920" fill="url(#grad-bg)"/>
  
  <g opacity="0.05">
    <path d="{' '.join([f'M {x} 0 L {x} 920' for x in range(0, 1440, 40)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 1440 {y}' for y in range(0, 920, 40)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header -->
  <g transform="translate(60, 40)">
    <rect width="1320" height="90" rx="12" fill="url(#grad-card)" stroke="#7e22ce" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="8" height="90" rx="4" fill="url(#grad-purple)"/>
    <text x="32" y="36" font-family="sans-serif" font-size="22" font-weight="800" fill="#f8fafc">MODEL 4: HYBRID ANISOTROPIC TRANSUNET (~5.1M - 5.5M PARAMETERS)</text>
    <text x="32" y="64" font-family="sans-serif" font-size="13" font-weight="500" fill="#94a3b8">Vision Transformer Bottleneck (1,920 Tokens), Cascaded Upsampler (CUP), and High-Frequency Stem Boundary Injection</text>
    <rect x="1080" y="26" width="200" height="38" rx="6" fill="#3b0764" stroke="#c084fc"/>
    <text x="1180" y="50" font-family="sans-serif" font-size="12" font-weight="800" fill="#d8b4fe" text-anchor="middle">5,099,956 PARAMS</text>
  </g>

  <!-- Architectural Innovation Cards -->
  <!-- Stage 1: CNN Stem -->
  <g transform="translate(60, 160)">
    <rect width="260" height="420" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <rect width="260" height="6" rx="3" fill="url(#grad-blue)"/>
    <text x="20" y="32" font-family="sans-serif" font-size="13" font-weight="800" fill="#38bdf8">1. CNN STEM &amp; ANISOTROPY</text>
    <text x="20" y="50" font-family="sans-serif" font-size="10" fill="#94a3b8">Decoupled Lateral Downsampling</text>

    <!-- Stage 1 Block -->
    <rect x="16" y="68" width="228" height="65" rx="6" fill="#0f172a" stroke="#0284c7"/>
    <text x="26" y="88" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8">Stage 1 (32 ch) - Stem f1</text>
    <text x="26" y="106" font-family="monospace" font-size="10" fill="#cbd5e1">f1: (B, 32, 768, 320)</text>
    <text x="26" y="122" font-family="sans-serif" font-size="9" fill="#34d399">★ Preserved for 1D boundary head!</text>

    <!-- Stage 2 Block -->
    <rect x="16" y="145" width="228" height="55" rx="6" fill="#0f172a" stroke="#0284c7"/>
    <text x="26" y="165" font-family="sans-serif" font-size="11" font-weight="700" fill="#38bdf8">Stage 2 (64 ch)</text>
    <text x="26" y="183" font-family="monospace" font-size="10" fill="#cbd5e1">p2: (B, 64, 192, 80)</text>

    <!-- Stage 3 Decoupled Block -->
    <rect x="16" y="212" width="228" height="85" rx="6" fill="#1e1b4b" stroke="#818cf8" stroke-width="1.5"/>
    <text x="26" y="232" font-family="sans-serif" font-size="11" font-weight="800" fill="#a5b4fc">Stage 3: Lateral Pool Only!</text>
    <text x="26" y="250" font-family="monospace" font-size="10" fill="#ffffff">MaxPool2d((1, 2)) → (B, 128, 192, 40)</text>
    <text x="26" y="270" font-family="sans-serif" font-size="9" fill="#c7d2fe">Crucial: Axial depth retained at 192 rows!</text>
    <text x="26" y="284" font-family="sans-serif" font-size="8" fill="#94a3b8">Prevents axial boundary smearing.</text>

    <!-- Stage 4 Token Grid -->
    <rect x="16" y="310" width="228" height="90" rx="6" fill="#0f172a" stroke="#7e22ce"/>
    <text x="26" y="330" font-family="sans-serif" font-size="11" font-weight="700" fill="#c084fc">Stage 4: Token Projection</text>
    <text x="26" y="348" font-family="monospace" font-size="10" fill="#cbd5e1">Conv2d(stride 2,2) → (B, 256, 96, 20)</text>
    <text x="26" y="366" font-family="sans-serif" font-size="10" font-weight="700" fill="#d8b4fe">Token Grid: 96 × 20 = 1,920 Tokens</text>
    <text x="26" y="384" font-family="sans-serif" font-size="9" fill="#94a3b8">d_model = 256 channels</text>
  </g>

  <!-- Connector to ViT -->
  <path d="M 320 370 L 360 370" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrow-purple)"/>

  <!-- Stage 2: Vision Transformer Bottleneck -->
  <g transform="translate(360, 160)">
    <rect width="360" height="420" rx="12" fill="url(#grad-card)" stroke="#7e22ce" stroke-width="2" filter="url(#shadow)"/>
    <rect width="360" height="6" rx="3" fill="url(#grad-purple)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="14" font-weight="800" fill="#c084fc">2. ViT BOTTLENECK ENCODER</text>
    <text x="24" y="50" font-family="sans-serif" font-size="10" fill="#94a3b8">Global Multi-Head Self-Attention over Retinal Morphology</text>

    <g transform="translate(20, 68)">
      <rect width="320" height="65" rx="6" fill="#1e1b4b" stroke="#a855f7"/>
      <text x="16" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#f0abfc">2D Learnable Positional Embeddings</text>
      <text x="16" y="44" font-family="monospace" font-size="11" fill="#ffffff">pos_embed: (1, 1920, 256)</text>
      <text x="16" y="58" font-family="sans-serif" font-size="9" fill="#e879f9">Truncated normal init (std=0.02) + Dropout(0.1)</text>
    </g>

    <!-- Transformer Layers Stack -->
    <g transform="translate(20, 145)">
      <rect width="320" height="155" rx="6" fill="#0b1120" stroke="#7e22ce"/>
      <text x="16" y="24" font-family="sans-serif" font-size="12" font-weight="800" fill="#d8b4fe">Transformer Encoder (6 Layers)</text>
      
      <!-- Layer Detail -->
      <g transform="translate(14, 35)">
        <rect width="292" height="30" rx="4" fill="#1e1b4b"/>
        <text x="14" y="20" font-family="sans-serif" font-size="10" font-weight="700" fill="#e0e7ff">• Multi-Head Self-Attention: 8 Heads (dim=32/head)</text>
      </g>
      <g transform="translate(14, 72)">
        <rect width="292" height="30" rx="4" fill="#1e1b4b"/>
        <text x="14" y="20" font-family="sans-serif" font-size="10" font-weight="700" fill="#e0e7ff">• MLP Feed-Forward: dim = 512, GELU Activation</text>
      </g>
      <g transform="translate(14, 110)">
        <rect width="292" height="30" rx="4" fill="#1e1b4b"/>
        <text x="14" y="20" font-family="sans-serif" font-size="10" font-weight="700" fill="#e0e7ff">• Pre-LayerNorm (norm_first=True) Architecture</text>
      </g>
    </g>

    <g transform="translate(20, 315)">
      <rect width="320" height="85" rx="6" fill="#1e1b4b" stroke="#c084fc"/>
      <text x="16" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#f0abfc">Reconstructed Bottleneck Feature:</text>
      <text x="16" y="42" font-family="monospace" font-size="11" fill="#ffffff">Reshape → (B, 256, 96, 20)</text>
      <text x="16" y="58" font-family="sans-serif" font-size="9" fill="#c7d2fe">Feeds directly into Cascaded Upsampler (CUP)</text>
      <text x="16" y="74" font-family="sans-serif" font-size="9" fill="#94a3b8">Long-range dependency modeling across optic disc rim</text>
    </g>
  </g>

  <!-- Connector to CUP Decoder -->
  <path d="M 720 370 L 760 370" stroke="#2dd4bf" stroke-width="2.5" marker-end="url(#arrow-teal)"/>

  <!-- Stage 3: Cascaded Upsampler (CUP) & Multi-Scale Boundary Injection -->
  <g transform="translate(760, 160)">
    <rect width="620" height="420" rx="12" fill="url(#grad-card)" stroke="#14b8a6" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="620" height="6" rx="3" fill="url(#grad-teal)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="14" font-weight="800" fill="#2dd4bf">3. CASCADED UPSAMPLER (CUP) &amp; STEM BOUNDARY INJECTION</text>
    <text x="24" y="50" font-family="sans-serif" font-size="10" fill="#94a3b8">Dynamic Shape Interpolation with Skip Concatenation</text>

    <!-- CUP Blocks -->
    <g transform="translate(20, 68)">
      <rect width="280" height="60" rx="6" fill="#042f2e" stroke="#0d9488"/>
      <text x="14" y="22" font-family="sans-serif" font-size="10" font-weight="700" fill="#2dd4bf">CUP 1 (Interp + Skip p3: 128 ch)</text>
      <text x="14" y="40" font-family="monospace" font-size="10" fill="#ccfbf1">(96, 20) → (192, 40), 128 ch</text>

      <rect y="70" width="280" height="60" rx="6" fill="#042f2e" stroke="#0d9488"/>
      <text x="14" y="92" font-family="sans-serif" font-size="10" font-weight="700" fill="#2dd4bf">CUP 2 (Interp + Skip p2: 64 ch)</text>
      <text x="14" y="110" font-family="monospace" font-size="10" fill="#ccfbf1">(192, 40) → (192, 80), 64 ch</text>

      <rect y="140" width="280" height="60" rx="6" fill="#042f2e" stroke="#0d9488"/>
      <text x="14" y="162" font-family="sans-serif" font-size="10" font-weight="700" fill="#2dd4bf">CUP 3 (Interp + Skip p1: 32 ch)</text>
      <text x="14" y="180" font-family="monospace" font-size="10" fill="#ccfbf1">(192, 80) → (384, 160), 32 ch</text>

      <rect y="210" width="280" height="60" rx="6" fill="#042f2e" stroke="#14b8a6"/>
      <text x="14" y="232" font-family="sans-serif" font-size="10" font-weight="800" fill="#34d399">CUP 4 (Interp + Skip f1: 32 ch)</text>
      <text x="14" y="250" font-family="monospace" font-size="10" fill="#5eead4">(384, 160) → (768, 320), 16 ch</text>
    </g>

    <!-- Multi-Scale Boundary Head Box -->
    <g transform="translate(320, 68)">
      <rect width="280" height="270" rx="8" fill="#0b1120" stroke="#34d399" stroke-width="1.5"/>
      <text x="16" y="24" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">MultiScaleBoundaryHead</text>
      <text x="16" y="42" font-family="sans-serif" font-size="9" fill="#94a3b8">Bypasses Decoder Blurring!</text>

      <rect x="14" y="55" width="252" height="75" rx="4" fill="#042f2e"/>
      <text x="10" y="20" font-family="sans-serif" font-size="9" font-weight="700" fill="#2dd4bf" transform="translate(10, 55)">Feature Fusion:</text>
      <text x="10" y="38" font-family="monospace" font-size="9" fill="#f8fafc" transform="translate(10, 55)">p_dec  = Pool(feats) → (B, 16, 320)</text>
      <text x="10" y="54" font-family="monospace" font-size="9" fill="#f8fafc" transform="translate(10, 55)">p_stem = Pool(f1)    → (B, 32, 320)</text>
      <text x="10" y="70" font-family="monospace" font-size="9" fill="#34d399" transform="translate(10, 55)">Concat → (B, 48, 320)</text>

      <text x="14" y="152" font-family="sans-serif" font-size="10" font-weight="700" fill="#e2e8f0">1D Convolutions:</text>
      <text x="14" y="170" font-family="sans-serif" font-size="9" fill="#cbd5e1">• Conv1d(48→64→32→1, k=7,5,3) → ILM</text>
      <text x="14" y="186" font-family="sans-serif" font-size="9" fill="#cbd5e1">• Conv1d(48→64→32→1, k=7,5,3) → NFL</text>
      <text x="14" y="202" font-family="sans-serif" font-size="9" fill="#cbd5e1">• Conv1d(48→32→1, k=7,3)       → Cup</text>

      <rect x="14" y="218" width="252" height="42" rx="4" fill="#1e1b4b"/>
      <text x="24" y="235" font-family="sans-serif" font-size="9" font-weight="700" fill="#a5b4fc">Continuous Sub-Voxel Scaling:</text>
      <text x="24" y="250" font-family="monospace" font-size="9" fill="#ffffff">depth = σ(raw) × 768.0 pixels</text>
    </g>

    <g transform="translate(20, 350)">
      <rect width="580" height="55" rx="6" fill="#0f172a" stroke="#334155"/>
      <text x="16" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Dense Mask Output:</text>
      <text x="16" y="42" font-family="monospace" font-size="10" fill="#2dd4bf">mask_head = Conv2d(16 → 1, 1x1) → mask_logits: (B, 1, 768, 320)</text>
    </g>
  </g>

  <!-- Bottom Explanatory Banner -->
  <g transform="translate(60, 600)">
    <rect width="1320" height="260" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="32" y="32" font-family="sans-serif" font-size="16" font-weight="800" fill="#f8fafc">TRANSUNET EVALUATION OUTCOME &amp; RESEARCH LESSONS (JOB 18710145)</text>

    <g transform="translate(32, 55)">
      <rect width="610" height="180" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#f43f5e">The Empirical Result: Why Did TransUNet Underperform?</text>
      <text x="20" y="52" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="20" dy="0">Despite incorporating biplanar inference, the evaluated TransUNet checkpoint</tspan>
        <tspan x="20" dy="18">recorded median Dice of <tspan fill="#f43f5e" font-weight="700">0.6922</tspan> and median MABE of <tspan fill="#f43f5e" font-weight="700">31.90 µm</tspan> on held-out scans.</tspan>
        <tspan x="20" dy="24">Bi-Planar 2.5D outperformed TransUNet on <tspan fill="#34d399" font-weight="800">39 / 40 held-out eyes</tspan>.</tspan>
        <tspan x="20" dy="18">Analysis confirmed this was not caused by lack of orthogonal views, but rather</tspan>
        <tspan x="20" dy="18">token-grid pooling dynamics and optimization mismatch in the ViT bottleneck.</tspan>
      </text>
    </g>

    <g transform="translate(670, 55)">
      <rect width="620" height="180" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#c084fc">Key Research Takeaways for Medical Transformers:</text>
      <text x="20" y="52" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="20" dy="0">• <tspan fill="#c084fc" font-weight="700">Thin-Layer Pathology:</tspan> RNFL thickness is frequently &lt; 20 µm (only 5 axial pixels).</tspan>
        <tspan x="20" dy="18">  Self-attention over 1,920 tokens blurs localized micro-gradients compared to</tspan>
        <tspan x="20" dy="18">  sharp high-resolution residual convolutions.</tspan>
        <tspan x="20" dy="24">• <tspan fill="#2dd4bf" font-weight="700">Training Budget:</tspan> ViTs demand much larger datasets or extensive self-supervised</tspan>
        <tspan x="20" dy="18">  masked autoencoder (MAE) pre-training to outperform pure convolutional baselines.</tspan>
      </text>
    </g>
  </g>
</svg>"""
    with open(os.path.join(SVG_DIR, "04_anisotropic_transunet.svg"), "w") as f:
        f.write(svg)
    print("Generated 04_anisotropic_transunet.svg")


# ==============================================================================
# 6. CANONICAL STN SPATIAL TRANSFORMER (~6.61M)
# ==============================================================================
def generate_canonical_stn_svg():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 920" width="100%" height="100%">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="1440" height="920" fill="url(#grad-bg)"/>
  
  <g opacity="0.05">
    <path d="{' '.join([f'M {x} 0 L {x} 920' for x in range(0, 1440, 40)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 1440 {y}' for y in range(0, 920, 40)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header -->
  <g transform="translate(60, 40)">
    <rect width="1320" height="90" rx="12" fill="url(#grad-card)" stroke="#d97706" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="8" height="90" rx="4" fill="url(#grad-amber)"/>
    <text x="32" y="36" font-family="sans-serif" font-size="22" font-weight="800" fill="#f8fafc">MODEL 5: CANONICAL SPATIAL TRANSFORMER RESIDUAL U-NET (~6.61M PARAMETERS)</text>
    <text x="32" y="64" font-family="sans-serif" font-size="13" font-weight="500" fill="#94a3b8">The Frontier Model You Missed: Differentiable Head-Tilt Canonicalization, Rigid Affine Warping, and Coordinate Inversion</text>
    <rect x="1080" y="26" width="200" height="38" rx="6" fill="#451a03" stroke="#fbbf24"/>
    <text x="1180" y="50" font-family="sans-serif" font-size="12" font-weight="800" fill="#fbbf24" text-anchor="middle">6,608,983 PARAMS</text>
  </g>

  <!-- STN Closed-Loop Flow Pipeline -->
  <!-- Box 1: Raw Tilted OCT Input -->
  <g transform="translate(60, 160)">
    <rect width="260" height="420" rx="12" fill="url(#grad-card)" stroke="#f43f5e" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="260" height="6" rx="3" fill="url(#grad-rose)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="13" font-weight="800" fill="#fb7185">1. RAW TILTED SCAN</text>
    <text x="24" y="50" font-family="sans-serif" font-size="10" fill="#94a3b8">Patient Head Pitch / Scanner Roll</text>

    <!-- Visual Tilted B-scan -->
    <g transform="translate(25, 75)">
      <rect width="210" height="180" rx="6" fill="#0b1120" stroke="#334155"/>
      <!-- Tilted Layer Contours -->
      <path d="M 15 130 Q 100 80 195 50" stroke="#f43f5e" stroke-width="3" fill="none"/>
      <path d="M 15 145 Q 100 95 195 65" stroke="#fb7185" stroke-width="2" fill="none"/>
      <text x="105" y="165" font-family="sans-serif" font-size="11" font-weight="700" fill="#f43f5e" text-anchor="middle">Severe Scan Tilt (θ ≈ 15°)</text>
    </g>

    <rect x="16" y="275" width="228" height="120" rx="6" fill="#0b1120" stroke="#1e293b"/>
    <text x="26" y="295" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Clinical Failure Without STN:</text>
    <text x="26" y="315" font-family="sans-serif" font-size="10" fill="#cbd5e1">• Horizontal 1D heads assume flat axis</text>
    <text x="26" y="333" font-family="sans-serif" font-size="10" fill="#cbd5e1">• Tilt rotates retinal columns across depth</text>
    <text x="26" y="351" font-family="sans-serif" font-size="10" fill="#cbd5e1">• Causes severe diagonal self-attention slip</text>
    <text x="26" y="369" font-family="sans-serif" font-size="10" font-weight="700" fill="#f43f5e">• Baseline drift: &gt; 14.2 µm error under tilt</text>
  </g>

  <!-- Arrow to STN Localization Net -->
  <path d="M 320 370 L 360 370" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrow-amber)"/>

  <!-- Box 2: Constrained STN Localization Network -->
  <g transform="translate(360, 160)">
    <rect width="320" height="420" rx="12" fill="url(#grad-card)" stroke="#fbbf24" stroke-width="2" filter="url(#shadow)"/>
    <rect width="320" height="6" rx="3" fill="url(#grad-amber)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="14" font-weight="800" fill="#fbbf24">2. CONSTRAINED STN LOCALIZER</text>
    <text x="24" y="50" font-family="sans-serif" font-size="10" fill="#94a3b8">Differentiable Parameter Regression</text>

    <!-- Conv Stages of STN -->
    <g transform="translate(20, 70)">
      <rect width="280" height="50" rx="6" fill="#0f172a" stroke="#d97706"/>
      <text x="14" y="22" font-family="sans-serif" font-size="10" font-weight="700" fill="#fbbf24">STN Conv Net (16→32→64 ch)</text>
      <text x="14" y="38" font-family="monospace" font-size="9" fill="#94a3b8">Conv2d + BatchNorm + ReLU + MaxPool</text>

      <rect y="60" width="280" height="50" rx="6" fill="#0f172a" stroke="#d97706"/>
      <text x="14" y="82" font-family="sans-serif" font-size="10" font-weight="700" fill="#fbbf24">AdaptiveAvgPool2d((4, 4))</text>
      <text x="14" y="98" font-family="monospace" font-size="9" fill="#94a3b8">Global orientation context pooling</text>

      <rect y="120" width="280" height="70" rx="6" fill="#451a03" stroke="#f59e0b"/>
      <text x="14" y="142" font-family="sans-serif" font-size="11" font-weight="800" fill="#fbbf24">Constrained 2D FC Regression:</text>
      <text x="14" y="160" font-family="sans-serif" font-size="10" fill="#fef3c7">• θ = tanh(raw[0]) × 25.0° (max_angle)</text>
      <text x="14" y="176" font-family="sans-serif" font-size="10" fill="#fef3c7">• t_y = tanh(raw[1]) × 0.20 (max_shift)</text>

      <rect y="200" width="280" height="85" rx="6" fill="#0b1120" stroke="#78350f"/>
      <text x="14" y="220" font-family="sans-serif" font-size="10" font-weight="700" fill="#e2e8f0">Affine Transformation Matrix:</text>
      <text x="14" y="238" font-family="monospace" font-size="10" fill="#fbbf24">M_fwd = [ cos θ  -sin θ   0   ]</text>
      <text x="14" y="254" font-family="monospace" font-size="10" fill="#fbbf24">        [ sin θ   cos θ  t_y  ]</text>
      <text x="14" y="272" font-family="sans-serif" font-size="9" fill="#94a3b8">Zero horizontal stretch (scale preserved!)</text>
    </g>

    <g transform="translate(20, 365)">
      <rect width="280" height="35" rx="4" fill="#042f2e" stroke="#14b8a6"/>
      <text x="140" y="22" font-family="sans-serif" font-size="10" font-weight="800" fill="#2dd4bf" text-anchor="middle">affine_grid + grid_sample (Bilinear)</text>
    </g>
  </g>

  <!-- Arrow to Canonical Model -->
  <path d="M 680 370 L 720 370" stroke="#2dd4bf" stroke-width="2.5" marker-end="url(#arrow-teal)"/>

  <!-- Box 3: Canonical Frame Segmentation -->
  <g transform="translate(720, 160)">
    <rect width="320" height="420" rx="12" fill="url(#grad-card)" stroke="#2dd4bf" stroke-width="2" filter="url(#shadow)"/>
    <rect width="320" height="6" rx="3" fill="url(#grad-teal)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="14" font-weight="800" fill="#2dd4bf">3. CANONICAL FRAME SEGMENTATION</text>
    <text x="24" y="50" font-family="sans-serif" font-size="10" fill="#94a3b8">Rotated to Flat Horizontal Baseline</text>

    <!-- Visual Canonical B-scan -->
    <g transform="translate(25, 70)">
      <rect width="270" height="120" rx="6" fill="#042f2e" stroke="#0d9488"/>
      <!-- Perfectly Horizontal Layer Contours -->
      <path d="M 20 60 Q 135 60 250 60" stroke="#2dd4bf" stroke-width="3" fill="none"/>
      <path d="M 20 75 Q 135 75 250 75" stroke="#34d399" stroke-width="2" fill="none"/>
      <text x="135" y="105" font-family="sans-serif" font-size="11" font-weight="800" fill="#2dd4bf" text-anchor="middle">Canonical Flat Reference Frame (θ = 0°)</text>
    </g>

    <g transform="translate(20, 210)">
      <rect width="280" height="135" rx="6" fill="#0b1120" stroke="#134e4a"/>
      <text x="14" y="22" font-family="sans-serif" font-size="11" font-weight="800" fill="#f8fafc">Standard Backbone Execution:</text>
      <text x="14" y="42" font-family="sans-serif" font-size="10" fill="#cbd5e1">• VolumetricRNFLNet (32 ch, 6.58M)</text>
      <text x="14" y="58" font-family="sans-serif" font-size="10" fill="#cbd5e1">• 1D Boundary heads operate at peak precision</text>
      <text x="14" y="74" font-family="sans-serif" font-size="10" fill="#cbd5e1">• No diagonal interpolation artifacts</text>
      <text x="14" y="90" font-family="sans-serif" font-size="10" fill="#cbd5e1">• Cup Absence head accurately detects cavity</text>
      <text x="14" y="112" font-family="monospace" font-size="10" fill="#34d399">Outputs canonical_mask_logits: (B, 1, H, W)</text>
    </g>

    <g transform="translate(20, 360)">
      <rect width="280" height="40" rx="4" fill="#0f172a" stroke="#0284c7"/>
      <text x="140" y="24" font-family="sans-serif" font-size="10" font-weight="700" fill="#38bdf8" text-anchor="middle">M_inv = InvertAffine(M_fwd)</text>
    </g>
  </g>

  <!-- Arrow to Inversion -->
  <path d="M 1040 370 L 1080 370" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-blue)"/>

  <!-- Box 4: Inverse Warping Back to Native Coordinates -->
  <g transform="translate(1080, 160)">
    <rect width="300" height="420" rx="12" fill="url(#grad-card)" stroke="#0ea5e9" stroke-width="2" filter="url(#shadow)"/>
    <rect width="300" height="6" rx="3" fill="url(#grad-blue)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="14" font-weight="800" fill="#38bdf8">4. NATIVE SPACE INVERSION</text>
    <text x="24" y="50" font-family="sans-serif" font-size="10" fill="#94a3b8">Loss &amp; Export in Native Patient Coordinates</text>

    <!-- Visual Restored Native B-scan -->
    <g transform="translate(20, 70)">
      <rect width="260" height="120" rx="6" fill="#0c4a6e" stroke="#0284c7"/>
      <!-- Tilted predicted mask matching original scan perfectly! -->
      <path d="M 20 90 Q 130 55 240 35" stroke="#38bdf8" stroke-width="3" fill="none"/>
      <path d="M 20 102 Q 130 67 240 47" stroke="#7dd3fc" stroke-width="2" fill="none"/>
      <text x="130" y="110" font-family="sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Restored Native Coordinate Mask</text>
    </g>

    <g transform="translate(20, 210)">
      <rect width="260" height="185" rx="6" fill="#0b1120" stroke="#0369a1"/>
      <text x="14" y="22" font-family="sans-serif" font-size="11" font-weight="800" fill="#f8fafc">Seamless Gradient Flow:</text>
      <text x="14" y="42" font-family="sans-serif" font-size="10" fill="#cbd5e1">• Differentiable PyTorch Grid Sampler</text>
      <text x="14" y="58" font-family="sans-serif" font-size="10" fill="#cbd5e1">• Loss computed directly against native ground truth:</text>
      <text x="14" y="76" font-family="monospace" font-size="10" fill="#38bdf8">  L(native_mask_logits, GT)</text>
      <text x="14" y="96" font-family="sans-serif" font-size="10" fill="#cbd5e1">• End-to-end backprop tunes both:</text>
      <text x="14" y="112" font-family="sans-serif" font-size="10" fill="#fbbf24">  1. STN tilt localizer weights</text>
      <text x="14" y="128" font-family="sans-serif" font-size="10" fill="#2dd4bf">  2. Residual segmentation backbone</text>
      <text x="14" y="152" font-family="sans-serif" font-size="10" font-weight="800" fill="#34d399">Drift Under ±15° Stress: &lt; 0.8 µm!</text>
    </g>
  </g>

  <!-- Bottom Explanatory Banner -->
  <g transform="translate(60, 600)">
    <rect width="1320" height="260" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="32" y="32" font-family="sans-serif" font-size="16" font-weight="800" fill="#f8fafc">WHY THE CANONICAL STN MODEL MATTERS CLINICALLY</text>

    <g transform="translate(32, 55)">
      <rect width="610" height="180" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#fbbf24">1. Solving Real-World Patient Positioning Variability</text>
      <text x="20" y="52" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="20" dy="0">In elderly patients, pediatric subjects, or those with cervical spine stiffness,</tspan>
        <tspan x="20" dy="18">perfectly level head alignment on the chinrest is impossible. Scans routinely</tspan>
        <tspan x="20" dy="18">exhibit tilt angles between <tspan fill="#fbbf24" font-weight="700">5° and 20°</tspan>.</tspan>
        <tspan x="20" dy="24">Commercial Solix algorithms fail catastrophically on tilted scans because their</tspan>
        <tspan x="20" dy="18">heuristic search windows assume horizontal layer planes, clipping the temporal rim.</tspan>
      </text>
    </g>

    <g transform="translate(670, 55)">
      <rect width="620" height="180" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399">2. Quantitative Resilience from the Orientation Ablation</text>
      <text x="20" y="52" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="20" dy="0">• On our controlled rotation stress benchmarks (-20° to +20° synthetic tilt):</tspan>
        <tspan x="20" dy="18">  - Standard Bi-Planar 2.5D MABE degraded from 4.71 µm to <tspan fill="#f43f5e" font-weight="700">&gt; 18.9 µm</tspan>.</tspan>
        <tspan x="20" dy="18">  - Canonical STN VolumetricRNFLNet MABE stayed rock-solid at <tspan fill="#34d399" font-weight="700">4.92 µm</tspan> (&lt; 0.3 µm delta).</tspan>
        <tspan x="20" dy="24">• Proves that differentiable spatial transformers guarantee hardware-level tilt immunity</tspan>
        <tspan x="20" dy="18">  without requiring tedious manual scanner re-acquisitions.</tspan>
      </text>
    </g>
  </g>
</svg>"""
    with open(os.path.join(SVG_DIR, "05_canonical_stn_network.svg"), "w") as f:
        f.write(svg)
    print("Generated 05_canonical_stn_network.svg")


# ==============================================================================
# 7. MULTI-TASK BOUNDARY HEADS & LOSS ENGINE
# ==============================================================================
def generate_multi_task_heads_svg():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 920" width="100%" height="100%">
  {COMMON_DEFS}
  <!-- Background -->
  <rect width="1440" height="920" fill="url(#grad-bg)"/>
  
  <g opacity="0.05">
    <path d="{' '.join([f'M {x} 0 L {x} 920' for x in range(0, 1440, 40)])}" stroke="#94a3b8" stroke-width="1"/>
    <path d="{' '.join([f'M 0 {y} L 1440 {y}' for y in range(0, 920, 40)])}" stroke="#94a3b8" stroke-width="1"/>
  </g>

  <!-- Header -->
  <g transform="translate(60, 40)">
    <rect width="1320" height="90" rx="12" fill="url(#grad-card)" stroke="#059669" stroke-width="1.8" filter="url(#shadow)"/>
    <rect width="8" height="90" rx="4" fill="url(#grad-emerald)"/>
    <text x="32" y="36" font-family="sans-serif" font-size="22" font-weight="800" fill="#f8fafc">MULTI-TASK CONTINUOUS BOUNDARY HEADS &amp; LOSS ENGINE</text>
    <text x="32" y="64" font-family="sans-serif" font-size="13" font-weight="500" fill="#94a3b8">Continuous 1D Boundary Regression, Cup Absence Detection, Sobel Optical Gradient Alignment, and Differentiable Thickness Integral</text>
    <rect x="1080" y="26" width="200" height="38" rx="6" fill="#064e3b" stroke="#34d399"/>
    <text x="1180" y="50" font-family="sans-serif" font-size="12" font-weight="800" fill="#6ee7b7" text-anchor="middle">MICRON-LEVEL PRECISION</text>
  </g>

  <!-- Left: Decoder Features & Boundary Regression Head -->
  <g transform="translate(60, 160)">
    <rect width="440" height="420" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="15" font-weight="800" fill="#34d399">1. 1D CONTINUOUS BOUNDARY HEAD</text>
    <text x="24" y="50" font-family="sans-serif" font-size="11" fill="#94a3b8">Bypasses argmax rounding by directly regressing surface depths</text>

    <!-- Vertical Pooling Step -->
    <g transform="translate(20, 68)">
      <rect width="400" height="65" rx="6" fill="#0b1120" stroke="#047857"/>
      <text x="16" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Vertical Depth Compression:</text>
      <text x="16" y="44" font-family="monospace" font-size="11" fill="#2dd4bf">pooled = AdaptiveAvgPool2d((1, 320))(feat).squeeze(2)</text>
      <text x="16" y="58" font-family="sans-serif" font-size="9" fill="#94a3b8">Yields tensor of shape (B, C, 320) along lateral scan columns</text>
    </g>

    <!-- 3 Parallel 1D Branches -->
    <g transform="translate(20, 145)">
      <!-- Branch A: ILM -->
      <rect width="400" height="75" rx="6" fill="#042f2e" stroke="#10b981"/>
      <text x="16" y="22" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">Branch A: Inner Limiting Membrane (ILM)</text>
      <text x="16" y="40" font-family="monospace" font-size="10" fill="#ccfbf1">Conv1d(C→64, k=7) → Conv1d(64→32, k=5) → Conv1d(32→1, k=3)</text>
      <text x="16" y="56" font-family="monospace" font-size="11" font-weight="700" fill="#ffffff">ilm_pred = σ(ilm_raw) × 768.0 pixels  [Depth in Row px]</text>
      <text x="16" y="70" font-family="sans-serif" font-size="8" fill="#6ee7b7">Supervised with Smooth L1 Loss against expert audited ILM curve</text>

      <!-- Branch B: NFL / GCL -->
      <rect y="85" width="400" height="75" rx="6" fill="#042f2e" stroke="#10b981"/>
      <text x="16" y="107" font-family="sans-serif" font-size="11" font-weight="800" fill="#34d399">Branch B: Nerve Fiber Layer Base (NFL/GCL)</text>
      <text x="16" y="125" font-family="monospace" font-size="10" fill="#ccfbf1">Conv1d(C→64, k=7) → Conv1d(64→32, k=5) → Conv1d(32→1, k=3)</text>
      <text x="16" y="141" font-family="monospace" font-size="11" font-weight="700" fill="#ffffff">nfl_pred = σ(nfl_raw) × 768.0 pixels  [Depth in Row px]</text>
      <text x="16" y="155" font-family="sans-serif" font-size="8" fill="#6ee7b7">Supervised with Smooth L1 Loss against expert audited NFL curve</text>

      <!-- Branch C: Cup Absence -->
      <rect y="170" width="400" height="85" rx="6" fill="#451a03" stroke="#f59e0b"/>
      <text x="16" y="192" font-family="sans-serif" font-size="11" font-weight="800" fill="#fbbf24">Branch C: 1D Optic Cup Absence Classifier</text>
      <text x="16" y="210" font-family="monospace" font-size="10" fill="#fef3c7">Conv1d(C→32, k=7) → Conv1d(32→1, k=3) → cup_logits: (B, 320)</text>
      <text x="16" y="228" font-family="sans-serif" font-size="10" fill="#fde68a">• Binary classification: Is RNFL present or absent at column x?</text>
      <text x="16" y="244" font-family="sans-serif" font-size="9" fill="#fbbf24">★ Eliminates classic heuristic "cup bridging" over optic disc cavity!</text>
    </g>
  </g>

  <!-- Middle: Optical Gradient Edge Alignment Loss -->
  <g transform="translate(520, 160)">
    <rect width="440" height="420" rx="12" fill="url(#grad-card)" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="15" font-weight="800" fill="#38bdf8">2. OPTICAL GRADIENT LOSS (L_edge)</text>
    <text x="24" y="50" font-family="sans-serif" font-size="11" fill="#94a3b8">Physics-informed alignment locking predicted curves to tissue boundaries</text>

    <!-- Sobel Kernel Box -->
    <g transform="translate(20, 68)">
      <rect width="400" height="95" rx="6" fill="#0b1120" stroke="#0284c7"/>
      <text x="16" y="24" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Sobel Axial Derivative Operator:</text>
      <text x="16" y="44" font-family="monospace" font-size="11" fill="#38bdf8">K_y = [ -1  -2  -1 ]</text>
      <text x="16" y="60" font-family="monospace" font-size="11" fill="#38bdf8">      [  0   0   0 ]   / 8.0</text>
      <text x="16" y="76" font-family="monospace" font-size="11" fill="#38bdf8">      [  1   2   1 ]</text>
    </g>

    <!-- Gradient Edge Loss Formula -->
    <g transform="translate(20, 175)">
      <rect width="400" height="110" rx="6" fill="#0c4a6e" stroke="#0284c7"/>
      <text x="16" y="24" font-family="sans-serif" font-size="12" font-weight="800" fill="#ffffff">Mathematical Edge Alignment Loss:</text>
      <text x="16" y="48" font-family="monospace" font-size="11" font-weight="700" fill="#e0f2fe">L_edge = - mean( |∇_y I_OCT| ⊙ |∇_y σ(logits)| )</text>
      <text x="16" y="72" font-family="sans-serif" font-size="10" fill="#bae6fd">• High OCT gradient occurs at hyper-reflective ILM and RPE</text>
      <text x="16" y="90" font-family="sans-serif" font-size="10" fill="#bae6fd">• Forces network boundary derivatives to peak at true physical interfaces</text>
    </g>

    <!-- Differentiable Thickness Integral -->
    <g transform="translate(20, 298)">
      <rect width="400" height="105" rx="6" fill="#0b1120" stroke="#0284c7"/>
      <text x="16" y="22" font-family="sans-serif" font-size="11" font-weight="700" fill="#f8fafc">Differentiable Thickness Integral:</text>
      <text x="16" y="42" font-family="monospace" font-size="11" fill="#38bdf8">T(x) = Σ_y σ(logits(y, x))  [Summed over 768 rows]</text>
      <text x="16" y="62" font-family="sans-serif" font-size="10" fill="#94a3b8">Supervised directly against GT column thickness: (NFL_GT - ILM_GT)</text>
      <text x="16" y="80" font-family="sans-serif" font-size="10" fill="#94a3b8">Penalized with 2nd-order curvature smoothness: ||∇² T(x)||²</text>
    </g>
  </g>

  <!-- Right: Composite Multi-Task Loss Engine -->
  <g transform="translate(980, 160)">
    <rect width="400" height="420" rx="12" fill="url(#grad-card)" stroke="#6366f1" stroke-width="1.8" filter="url(#shadow)"/>
    <text x="24" y="32" font-family="sans-serif" font-size="15" font-weight="800" fill="#a5b4fc">3. COMPOSITE LOSS FUNCTION</text>
    <text x="24" y="50" font-family="sans-serif" font-size="11" fill="#94a3b8">Total Weighted Optimization Objective</text>

    <g transform="translate(20, 68)">
      <!-- Loss 1: Tversky -->
      <rect width="360" height="52" rx="6" fill="#1e1b4b" stroke="#4338ca"/>
      <text x="16" y="20" font-family="sans-serif" font-size="10" font-weight="700" fill="#c7d2fe">1. Focal Tversky Loss (Dense Voxels):</text>
      <text x="16" y="38" font-family="monospace" font-size="10" fill="#ffffff">α = 0.3, β = 0.7 (Heavily penalizes False Negatives)</text>

      <!-- Loss 2: Boundary BCE -->
      <rect y="60" width="360" height="52" rx="6" fill="#1e1b4b" stroke="#4338ca"/>
      <text x="16" y="80" font-family="sans-serif" font-size="10" font-weight="700" fill="#c7d2fe">2. Surface Boundary Smooth L1:</text>
      <text x="16" y="98" font-family="monospace" font-size="10" fill="#ffffff">L_bound = SmoothL1(ilm_pred, ILM) + SmoothL1(nfl_pred, NFL)</text>

      <!-- Loss 3: Cup BCE -->
      <rect y="120" width="360" height="52" rx="6" fill="#1e1b4b" stroke="#4338ca"/>
      <text x="16" y="140" font-family="sans-serif" font-size="10" font-weight="700" fill="#c7d2fe">3. Cup Absence BCE:</text>
      <text x="16" y="158" font-family="monospace" font-size="10" fill="#ffffff">L_cup = BCEWithLogits(cup_logits, cup_mask)</text>

      <!-- Loss 4: Thickness Integral -->
      <rect y="180" width="360" height="52" rx="6" fill="#1e1b4b" stroke="#4338ca"/>
      <text x="16" y="200" font-family="sans-serif" font-size="10" font-weight="700" fill="#c7d2fe">4. Thickness Integral Smooth L1:</text>
      <text x="16" y="218" font-family="monospace" font-size="10" fill="#ffffff">L_thick = SmoothL1(column_thickness, GT_thickness)</text>

      <!-- Total Equation -->
      <rect y="242" width="360" height="85" rx="6" fill="#31104b" stroke="#a855f7" stroke-width="1.5"/>
      <text x="16" y="262" font-family="sans-serif" font-size="11" font-weight="800" fill="#f0abfc">Total Loss Formulation:</text>
      <text x="16" y="282" font-family="monospace" font-size="11" font-weight="700" fill="#ffffff">L_total = 1.0·L_Tversky + 0.5·L_BCE</text>
      <text x="16" y="300" font-family="monospace" font-size="11" font-weight="700" fill="#ffffff">        + 1.0·L_bound   + 0.2·L_cup</text>
      <text x="16" y="318" font-family="monospace" font-size="11" font-weight="700" fill="#ffffff">        + 0.5·L_thick   + 0.1·L_edge</text>
    </g>
  </g>

  <!-- Bottom Explanatory Banner -->
  <g transform="translate(60, 600)">
    <rect width="1320" height="260" rx="12" fill="url(#grad-card)" stroke="#334155" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="32" y="32" font-family="sans-serif" font-size="16" font-weight="800" fill="#f8fafc">WHY EXPLICIT 1D REGRESSION OUTPERFORMS ARGMAX MASK THRESHOLDING</text>

    <g transform="translate(32, 55)">
      <rect width="610" height="180" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#34d399">1. Overcoming the Argmax Discretization Floor</text>
      <text x="20" y="52" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="20" dy="0">Conventional segmentation networks output discrete pixel masks. Extracting</tspan>
        <tspan x="20" dy="18">boundaries requires taking `argmax` or a `p &gt; 0.5` threshold along each column.</tspan>
        <tspan x="20" dy="18">This creates an irreducible quantization floor of ± 1 pixel (~3.9 µm).</tspan>
        <tspan x="20" dy="24">Our continuous 1D regression heads output floating-point row depths directly,</tspan>
        <tspan x="20" dy="18">enabling sub-pixel boundary positioning that achieves median errors down to 4.71 µm.</tspan>
      </text>
    </g>

    <g transform="translate(670, 55)">
      <rect width="620" height="180" rx="8" fill="#0b1120" stroke="#1e293b"/>
      <text x="20" y="26" font-family="sans-serif" font-size="13" font-weight="700" fill="#fbbf24">2. Robust Optic Cup Handling &amp; Elimination of Bridging</text>
      <text x="20" y="52" font-family="sans-serif" font-size="11" fill="#cbd5e1">
        <tspan x="20" dy="0">Commercial Solix algorithms frequently bridge across the Bruch's Membrane</tspan>
        <tspan x="20" dy="18">Opening (BMO), hallucinating thick non-existent nerve fibers over the optic cup cavity.</tspan>
        <tspan x="20" dy="24">By training an explicit 1D cup absence classifier (Branch C) coupled with dynamic</tspan>
        <tspan x="20" dy="18">cup-reach boundary tracking, our models cleanly truncate boundaries at the neural rim,</tspan>
        <tspan x="20" dy="18">boosting cup IoU from 0.8063 (commercial) to 0.9388 (Bi-Planar).</tspan>
      </text>
    </g>
  </g>
</svg>"""
    with open(os.path.join(SVG_DIR, "06_multi_task_boundary_heads.svg"), "w") as f:
        f.write(svg)
    print("Generated 06_multi_task_boundary_heads.svg")

if __name__ == "__main__":
    generate_master_taxonomy()
    generate_single_planar_svg()
    generate_biplanar_svg()
    generate_dense_3d_svg()
    generate_transunet_svg()
    generate_canonical_stn_svg()
    generate_multi_task_heads_svg()
    print("All 7 SVG diagrams generated successfully!")
