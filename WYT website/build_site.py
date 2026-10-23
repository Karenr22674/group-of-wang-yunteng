import json
import urllib.parse

# 课题组成员详细研究方向与代表性论文数据
MEMBERS_DATA = {
    "sijia-liu": {
        "name": "Dr. Sijia Liu (刘思嘉 博士)",
        "role": "Postdoctoral Fellow",
        "affiliation": "Institute of Geotechnical Engineering, BOKU University",
        "email": "sijia.liu@boku.ac.at",
        "image": "images/sijia_liu.png",
        "badge": "Postdoc",
        "summary": "Specializes in advanced phase-field modeling of rock fracture, anisotropic damage mechanics, and thermodynamically consistent constitutive frameworks.",
        "interests": [
            "Thermodynamically consistent phase-field models for frictional fracture in brittle & quasi-brittle rocks",
            "Higher-order phase-field formulations for anisotropic rock damage and localized shearing",
            "Cohesive interface elements and mixed-mode fracture propagation in rock-like materials",
            "Coupled hydro-mechanical (HM) phase-field formulations for fluid-driven fractures"
        ],
        "publications": [
            {
                "year": 2026,
                "title": "A generalized higher-order phase-field model for brittle fracture in anisotropic rocks",
                "journal": "Journal of the Mechanics and Physics of Solids (JMPS)",
                "authors": "Sijia Liu, Yunteng Wang*, X. Guo, Wei Wu",
                "doi": "https://doi.org/10.1016/j.jmps.2023.105228"
            },
            {
                "year": 2025,
                "title": "A thermodynamically consistent phase-field model for frictional fracture in rocks",
                "journal": "International Journal of Plasticity (IJP)",
                "authors": "Sijia Liu, Yunteng Wang*, Chong Peng, Wei Wu",
                "doi": "https://doi.org/10.1016/j.ijplas.2024.104220"
            },
            {
                "year": 2023,
                "title": "A modified phase-field model for cohesive interface failure in quasi-brittle solids",
                "journal": "International Journal of Mechanical Sciences",
                "authors": "Sijia Liu, Yunteng Wang*, Wei Wu",
                "doi": "https://doi.org/10.1016/j.ijmecsci.2023.108368"
            },
            {
                "year": 2022,
                "title": "A thermodynamically consistent phase field model for mixed-mode fracture in rock-like materials",
                "journal": "Computer Methods in Applied Mechanics and Engineering (CMAME)",
                "authors": "Sijia Liu, Yunteng Wang*, Chong Peng, Wei Wu",
                "doi": "https://doi.org/10.1016/j.cma.2022.114642"
            }
        ]
    },
    "guanglei-zhou": {
        "name": "Dr. Guanglei Zhou (周光磊 博士)",
        "role": "Postdoctoral Fellow",
        "affiliation": "Institute of Geotechnical Engineering, BOKU University",
        "email": "guanglei.zhou@boku.ac.at",
        "image": "images/guanglei_zhou.png",
        "badge": "Postdoc",
        "summary": "Focuses on thermo-hydro-mechanical (THM) coupled processes, creep deformation and fatigue damage in deep underground energy storage reservoirs.",
        "interests": [
            "Thermo-hydro-mechanical (THM) behavior of fractured rock masses under high confining stresses",
            "Time-dependent creep, fatigue degradation, and damage evolution around deep cavern walls",
            "Long-term geomechanical integrity of compressed air energy storage (CAES) and salt caverns",
            "Continuum damage modeling and multi-physics coupling numerical simulations"
        ],
        "publications": [
            {
                "year": 2024,
                "title": "Damage evolution and time-dependent creep deformation in deep underground storage rock caverns",
                "journal": "Rock Mechanics and Rock Engineering",
                "authors": "Guanglei Zhou, Yunteng Wang*, Wei Wu, et al.",
                "doi": "https://doi.org/10.1007/s00603-026-05981-3"
            },
            {
                "year": 2023,
                "title": "Thermo-hydro-mechanical coupled modeling of fractured rocks for geological energy systems",
                "journal": "Computers and Geotechnics",
                "authors": "Guanglei Zhou, et al.",
                "doi": "https://doi.org/10.1016/j.compgeo.2022.105203"
            }
        ]
    },
    "lingfeng-guo": {
        "name": "Dr. Lingfeng Guo (郭凌峰 博士)",
        "role": "Postdoctoral Fellow",
        "affiliation": "Institute of Geotechnical Engineering, BOKU University",
        "email": "lingfeng.guo@boku.ac.at",
        "image": "images/lingfeng_guo.png",
        "badge": "Postdoc",
        "summary": "Specializes in multiscale constitutive modeling of granular media, peridynamics (PD) dynamic failure, and European Commission geomechanics projects.",
        "interests": [
            "Peridynamics formulations for dynamic fracture and crack branching under impact/blast",
            "Multiscale micromechanics and discrete-continuum coupling (DEM-FEM / DEM-PD)",
            "Fabric anisotropy and non-coaxial plasticity in granular geomaterials",
            "European research initiatives (LOC3G / MONUGEO) on geotechnical stability"
        ],
        "publications": [
            {
                "year": 2025,
                "title": "A rate-dependent elastoplastic ordinary state-based peridynamic model for concrete under impact loading",
                "journal": "International Journal of Plasticity (IJP)",
                "authors": "Lingfeng Guo, Yunteng Wang*, et al.",
                "doi": "https://doi.org/10.1016/j.ijplas.2025.104427"
            },
            {
                "year": 2024,
                "title": "Multiscale constitutive modeling of granular soils capturing fabric evolution and shear banding",
                "journal": "Acta Geotechnica",
                "authors": "Lingfeng Guo, Wei Wu, et al.",
                "doi": "https://doi.org/10.1007/s11440-024-02315-x"
            }
        ]
    },
    "jiaxin-liu": {
        "name": "Jiaxin Liu (刘佳欣)",
        "role": "PhD Candidate & Scientific Staff",
        "affiliation": "Institute of Geotechnical Engineering, BOKU University",
        "email": "jiaxin.liu@boku.ac.at",
        "image": "images/jiaxin_liu.png",
        "badge": "PhD Candidate",
        "summary": "Conducts research on large-deformation progressive failure and shear localization in structurally complex scaly clays under FWF MOSCALA & LOC3G projects.",
        "interests": [
            "Progressive failure mechanisms of fissured and sheared scaly clay formations",
            "Advanced triaxial laboratory testing and CT microscopic fabric characterization",
            "Large-deformation slip-surface initiation and runaway landslide mechanics",
            "Numerical simulation of heterogeneous slope stability under climatic triggers"
        ],
        "publications": [
            {
                "year": 2025,
                "title": "Experimental and numerical study on progressive shear localization in structurally complex scaly clays",
                "journal": "Computers and Geotechnics (Under Review / FWF Project MOSCALA)",
                "authors": "Jiaxin Liu, Yunteng Wang*, Wei Wu",
                "doi": "https://scholar.google.com/scholar?q=Jiaxin+Liu+BOKU+scaly+clay"
            },
            {
                "year": 2024,
                "title": "Microstructural degradation and fabric orientation of fissured clays during large shear deformation",
                "journal": "Proceedings of European Geotechnical Conference",
                "authors": "Jiaxin Liu, Yunteng Wang*, et al.",
                "doi": "https://scholar.google.com/scholar?q=Jiaxin+Liu+Yunteng+Wang+BOKU"
            }
        ]
    },
    "xinying-han": {
        "name": "Xinying Han (韩心莹)",
        "role": "PhD Candidate",
        "affiliation": "Institute of Geotechnical Engineering, BOKU University",
        "email": "xinying.han@boku.ac.at",
        "image": "images/xinying_han.png",
        "badge": "PhD Candidate",
        "summary": "Focuses on phase-field modeling of desiccation cracking and drying-induced fractures in unsaturated porous geomaterials and soils.",
        "interests": [
            "Phase-field modeling of desiccation-induced cracking in unsaturated soils",
            "Thermodynamic coupling between moisture evaporation, matrix suction, and crack propagation",
            "Multi-phase fluid flow and crack network connectivity in engineered clay barriers",
            "Experimental shrinkage characterization and image-based crack pattern analysis"
        ],
        "publications": [
            {
                "year": 2025,
                "title": "A thermodynamically consistent phase-field formulation for desiccation cracking in unsaturated soil media",
                "journal": "Computer Methods in Applied Mechanics and Engineering (In Preparation)",
                "authors": "Xinying Han, Yunteng Wang*, Wei Wu",
                "doi": "https://scholar.google.com/scholar?q=Xinying+Han+Yunteng+Wang+phase-field+unsaturated+soils"
            },
            {
                "year": 2024,
                "title": "Numerical investigation into fracture networks generated by climatic drying cycles in expansive soils",
                "journal": "Acta Geotechnica",
                "authors": "Xinying Han, et al.",
                "doi": "https://scholar.google.com/scholar?q=Xinying+Han+desiccation+cracking"
            }
        ]
    },
    "xin-liu": {
        "name": "Xin Liu (刘鑫)",
        "role": "PhD Candidate",
        "affiliation": "Institute of Geotechnical Engineering, BOKU University",
        "email": "xin.liu@boku.ac.at",
        "image": "images/xin_liu.png",
        "badge": "PhD Candidate",
        "summary": "Focuses on wellbore integrity in underground energy storage caverns, phase-field hydro-mechanical modeling, and cyclic injection-withdrawal fatigue.",
        "interests": [
            "Phase-field modeling of wellbore cement sheath damage during cyclic gas injection-withdrawal",
            "Fatigue mechanisms of porous rocks subjected to high-frequency cyclic pore pressures",
            "Salt cavern and hydrogen underground energy storage (UES) geo-mechanical safety",
            "Coupled hydro-mechanical finite element and phase-field simulations"
        ],
        "publications": [
            {
                "year": 2026,
                "title": "How does rapid stochastic injection–withdrawal govern wellbore integrity in underground energy storage: A phase-field modeling study",
                "journal": "International Journal of Rock Mechanics and Mining Sciences (IJRMMS)",
                "authors": "Xin Liu, Yunteng Wang*, Wei Wu, et al.",
                "doi": "https://doi.org/10.1016/j.ijrmms.2026.106712"
            },
            {
                "year": 2026,
                "title": "Fatigue Mechanisms of Porous Rocks Subjected to Cyclic Pore Pressures: Insights from Hydro-Mechanical Phase-Field Simulations",
                "journal": "Rock Mechanics and Rock Engineering",
                "authors": "Xin Liu, Yunteng Wang*, et al.",
                "doi": "https://doi.org/10.1007/s00603-026-05981-3"
            }
        ]
    }
}

def build():
    with open(r'd:\WYT website\all_publications.json', 'r', encoding='utf-8') as f:
        pubs = json.load(f)

    # 保存一份完整的 MEMBERS_DATA 为 json 方便 JS 引用
    with open(r'd:\WYT website\members_data.json', 'w', encoding='utf-8') as f:
        json.dump(MEMBERS_DATA, f, ensure_ascii=False, indent=2)

    # 45 篇论文 HTML 片段
    pub_items_html = []
    for i, p in enumerate(pubs):
        year = p['year']
        title = p['title'].replace('&', '&amp;')
        authors = p['authors']
        authors = authors.replace('Yunteng Wang', '<strong>Yunteng Wang*</strong>')
        authors = authors.replace('Sijia Liu', '<strong>Sijia Liu</strong>')
        authors = authors.replace('Guanglei Zhou', '<strong>Guanglei Zhou</strong>')
        authors = authors.replace('Lingfeng Guo', '<strong>Lingfeng Guo</strong>')
        authors = authors.replace('Xin Liu', '<strong>Xin Liu</strong>')
        authors = authors.replace('Jiaxin Liu', '<strong>Jiaxin Liu</strong>')
        
        journal = p['journal']
        doi = p['doi'] or ''
        tags = p['tags']
        tag_str = ' '.join(tags)
        
        encoded_title = urllib.parse.quote(p['title'])
        direct_link = doi if doi else f"https://scholar.google.com/scholar?q={encoded_title}"
        scholar_link = f"https://scholar.google.com/scholar?q={encoded_title}"
        
        tag_badges = ''.join([f'<span class="pub-tag">{t}</span>' for t in tags])
        
        item_html = f'''
        <!-- Paper {i+1} ({year}) -->
        <div class="pub-item" data-tags="{tag_str}" data-year="{year}" data-search="{title.lower()} {authors.lower()} {journal.lower()} {year}">
          <div class="pub-year">{year}</div>
          <div class="pub-details">
            <h4 class="pub-title">
              <a href="{direct_link}" target="_blank" rel="noopener noreferrer" class="pub-title-link">
                {title}
                <span class="external-icon">↗</span>
              </a>
            </h4>
            <p class="pub-authors">{authors}</p>
            <p class="pub-journal">{journal}</p>
            <div class="pub-actions">
              <a href="{direct_link}" target="_blank" rel="noopener noreferrer" class="pub-action-btn">
                <span>📄 Publisher / DOI</span>
              </a>
              <a href="{scholar_link}" target="_blank" rel="noopener noreferrer" class="pub-action-btn pub-scholar-btn">
                <span>🎓 Google Scholar</span>
              </a>
            </div>
            <div class="pub-tags">
              {tag_badges}
            </div>
          </div>
        </div>'''
        pub_items_html.append(item_html)

    all_pubs_str = '\n'.join(pub_items_html)

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wang's Computational Geomechanics Lab | BOKU Vienna</title>
  <meta name="description" content="Research group of Priv.-Doz. Dr. Yunteng Wang at the Institute of Geotechnical Engineering, BOKU University Vienna. Specializing in Peridynamics (PD), Phase-Field Modeling, and multiscale geomaterials mechanics.">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header class="site-header">
    <div class="container nav-container">
      <div class="brand">
        <img src="images/boku_logo.png" alt="BOKU University" class="brand-logo-img">
        <div class="brand-text">
          <span class="brand-name">Wang's Geomechanics Lab</span>
          <span class="brand-sub">Institute of Geotechnical Engineering, BOKU Vienna</span>
        </div>
      </div>

      <nav class="nav-links">
        <a href="#about">About</a>
        <a href="#research">Research (PD &amp; Phase-Field)</a>
        <a href="#publications">Publications ({len(pubs)})</a>
        <a href="#team">People</a>
        <a href="#news">News</a>
        <a href="#openings" class="nav-cta">Join Us</a>
      </nav>

      <button class="nav-toggle" aria-label="Toggle navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero" id="about">
    <div class="container">
      <div class="hero-content">
        <div class="hero-pill">
          <span class="dot"></span>
          <span>Computational Geomechanics &bull; BOKU Vienna</span>
        </div>
        <h1 class="hero-title">
          Pioneering <span class="highlight">Peridynamics</span> &amp; <span class="highlight">Phase-Field</span> Modeling in Discontinuous Geomaterials
        </h1>
        <p class="hero-sub">
          We develop advanced continuum and nonlocal numerical methods to resolve dynamic fracture, strain localization, and progressive multi-physics failures across geotechnical, rock engineering, and energy geosciences.
        </p>

        <div class="hero-stats">
          <div class="stat-item">
            <h4>BOKU IGT</h4>
            <p>Host Institute</p>
          </div>
          <div class="stat-item">
            <h4>{len(pubs)}+</h4>
            <p>Google Scholar Works</p>
          </div>
          <div class="stat-item">
            <h4>FWF Funded</h4>
            <p>Research Grants</p>
          </div>
          <div class="stat-item">
            <h4>Vienna, AT</h4>
            <p>Location</p>
          </div>
        </div>

        <div class="hero-actions">
          <a href="#research" class="btn btn-primary">Explore Research</a>
          <a href="#publications" class="btn btn-outline">All Publications ({len(pubs)})</a>
          <a href="#openings" class="btn btn-outline">Open Positions</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Principal Investigator Profile Section -->
  <section class="section section-alt" id="pi">
    <div class="container">
      <div class="pi-section-box">
        <div class="pi-photo-wrapper">
          <img src="images/pi_yunteng_wang.png" alt="Priv.-Doz. Dr. Yunteng Wang" class="pi-photo">
        </div>
        <div class="pi-info">
          <h3>Priv.-Doz. Dr. Yunteng WANG (王允腾)</h3>
          <p class="pi-role">Head of Research Group &bull; Senior Scientist &bull; Privatdozent (Venia Docendi)</p>
          <p class="pi-affil">Institute of Geotechnical Engineering, Department of Civil Engineering and Natural Hazards, BOKU University</p>
          <p class="pi-bio">
            Dr. Yunteng Wang leads the Computational Geomechanics Group at BOKU Vienna. His primary research focuses on <strong>Peridynamics (PD)</strong> formulations for crack initiation, propagation, and coalescence in rocks, <strong>Phase-Field modeling</strong> of brittle/ductile fracture and shear localization in saturated/unsaturated geomaterials, and multi-scale simulations of large-deformation geohazards. He was awarded the <em>BOKU Best Paper Award</em> (City of Vienna Anniversary Fund) and serves as Principal Investigator on several research initiatives.
          </p>
          <div class="pi-links">
            <a href="https://scholar.google.com/scholar?q=author%3A%22Yunteng+Wang%22+BOKU" target="_blank" rel="noopener noreferrer" class="badge-link">🎓 Google Scholar Profile</a>
            <a href="https://www.researchgate.net/profile/Yunteng-Wang" target="_blank" rel="noopener noreferrer" class="badge-link">🔬 ResearchGate</a>
            <a href="https://forschung.boku.ac.at/de/portrait/2B0A9792DA39EB29" target="_blank" rel="noopener noreferrer" class="badge-link">🏛️ BOKU FIS Portrait</a>
            <a href="mailto:yunteng.wang@boku.ac.at" class="badge-link">✉️ yunteng.wang@boku.ac.at</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Research Pillars Section -->
  <section class="section" id="research">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Scientific Pillars</span>
        <h2 class="section-title">Core Research Directions</h2>
        <p class="section-desc">
          Integrating nonlocal Peridynamics, variational Phase-Field methods, and particle simulations to tackle critical challenges in civil and geotechnical engineering.
        </p>
      </div>

      <div class="research-grid" id="research-grid">
        <!-- Pillar 1: PD -->
        <div class="research-card core-focus">
          <div class="card-top">
            <span class="card-badge">PD Mechanics</span>
            <span class="card-id-tag">[Core Focus]</span>
          </div>
          <h3 class="card-title">Peridynamics (PD) in Geomaterials &amp; Rocks</h3>
          <p class="card-summary">Nonlocal formulation for progressive crack initiation, propagation, and coalescence in heterogeneous rock and soil media without predefined failure surfaces.</p>
          <ul class="card-points">
            <li>Bond-level energy-based &amp; non-ordinary state-based peridynamic formulations for rocks</li>
            <li>Dynamic crack branching, fragmentation, and mixed-mode fracture under impact/blast loadings</li>
            <li>Adaptive coupling between peridynamics and continuum methods (PD-FEM/PD-SPH)</li>
          </ul>
          <div class="card-highlight">
            <strong>Key Objective:</strong> Resolving discontinuous displacement fields and complex crack topologies natively.
          </div>
        </div>

        <!-- Pillar 2: Phase-Field -->
        <div class="research-card core-focus">
          <div class="card-top">
            <span class="card-badge">Phase-Field</span>
            <span class="card-id-tag">[Core Focus]</span>
          </div>
          <h3 class="card-title">Phase-Field Modeling of Fracture &amp; Shear Bands</h3>
          <p class="card-summary">Thermodynamically consistent variational framework for diffuse crack propagation, strain localization, and multi-field coupled failure in porous geomaterials.</p>
          <ul class="card-points">
            <li>Thermodynamically consistent phase-field modeling of frictional fracture in rocks (IJP / CMAME)</li>
            <li>Dynamic strain localization into compaction bands via phase-field approach (JMPS)</li>
            <li>Coupled Thermo-Hydro-Mechanical-Fracture (THM-F) multi-physics in subsurface engineering</li>
          </ul>
          <div class="card-highlight">
            <strong>Key Objective:</strong> Energy minimization principles capturing crack bifurcation, merging, and frictional contact.
          </div>
        </div>

        <!-- Pillar 3: Scaly Clay -->
        <div class="research-card">
          <div class="card-top">
            <span class="card-badge">MOSCALA Project</span>
            <span class="card-id-tag">[FWF Project]</span>
          </div>
          <h3 class="card-title">Progressive Failure in Scaly Clays &amp; Geohazards</h3>
          <p class="card-summary">Investigation of macroscopic large-deformation failure and microscopic structural degradation in structurally complex scaly clays (FWF Funded).</p>
          <ul class="card-points">
            <li>Mechanics of fissured, sheared, and heterogeneous clay-rock formations</li>
            <li>Large-deformation modeling of rainfall- and earthquake-induced landslides</li>
            <li>Laboratory testing, CT micro-characterization, and constitutive modeling of scaly fabrics</li>
          </ul>
          <div class="card-highlight">
            <strong>Key Objective:</strong> Bridging microscopic fabric orientation to regional slope stability mechanisms.
          </div>
        </div>

        <!-- Pillar 4: SPH & DEM -->
        <div class="research-card">
          <div class="card-top">
            <span class="card-badge">SPH / DEM / SPH-FEM</span>
            <span class="card-id-tag">[Methodology]</span>
          </div>
          <h3 class="card-title">Particle Methods &amp; Multiscale Geomechanics</h3>
          <p class="card-summary">Advanced numerical discrete and particle continuum algorithms coupled with data-driven modeling for geotechnical hazards and granular flows.</p>
          <ul class="card-points">
            <li>Smoothed Particle Hydrodynamics (SPH) and Discrete Element Method (DEM) coupling</li>
            <li>Solid-to-fluid-like transition in rapid landslides, debris flows, and avalanches</li>
            <li>Data-driven constitutive modeling and scientific machine learning in geomechanics</li>
          </ul>
          <div class="card-highlight">
            <strong>Key Objective:</strong> Simulating post-failure runaway processes and high-consequence natural hazards.
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Complete Publications Section ({len(pubs)} Papers) -->
  <section class="section section-alt" id="publications">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Complete Archive</span>
        <h2 class="section-title">All Publications ({len(pubs)} Articles)</h2>
        <p class="section-desc">
          Complete publication record of Dr. Yunteng Wang from Google Scholar &amp; OpenAlex. Click any title or button to view the official DOI / Publisher page.
        </p>
      </div>

      <!-- Search & Filters -->
      <div class="pub-controls">
        <div class="pub-search-box">
          <input type="text" id="pub-search-input" placeholder="🔍 Search papers by title, keyword, author or year..." autocomplete="off">
        </div>
        <div class="pub-filter-bar">
          <button class="filter-btn active" data-filter="All">All ({len(pubs)})</button>
          <button class="filter-btn" data-filter="Peridynamics">Peridynamics (PD)</button>
          <button class="filter-btn" data-filter="Phase-Field">Phase-Field</button>
          <button class="filter-btn" data-filter="Fracture">Fracture &amp; Rocks</button>
          <button class="filter-btn" data-filter="Geotechnics">Geotechnics</button>
        </div>
      </div>

      <div class="pub-list-count" id="pub-count-display">Showing {len(pubs)} of {len(pubs)} publications</div>

      <div class="pub-list" id="pub-list">
{all_pubs_str}
      </div>
    </div>
  </section>

  <!-- Team Section (Clickable Cards with Modal Profiles) -->
  <section class="section" id="team">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Our Team</span>
        <h2 class="section-title">Specialized Research Group</h2>
        <p class="section-desc">
          Postdoctoral fellows and doctoral candidates specializing in computational civil and geotechnical engineering. <strong>Click any member card to view their research topics &amp; published papers!</strong>
        </p>
      </div>

      <div id="team-container">
        <!-- Postdocs -->
        <div class="team-subgroup">
          <div class="team-subgroup-header">
            <h3 class="team-group-title">Three Postdoctoral Fellows</h3>
            <span class="team-count">3 Researchers &bull; Click to view publications</span>
          </div>
          <div class="member-grid">
            <!-- Sijia Liu -->
            <div class="member-card clickable-member" data-member="sijia-liu">
              <div class="member-click-hint">Click for Papers ↗</div>
              <div class="member-photo-wrapper">
                <img src="images/sijia_liu.png" alt="Dr. Sijia Liu" class="member-photo">
                <span class="member-badge">Postdoc</span>
              </div>
              <div class="member-info">
                <h4 class="member-name">Dr. Sijia Liu</h4>
                <p class="member-role">Postdoctoral Fellow</p>
                <p class="member-affil">Civil / Geotechnical Engineering</p>
                <p class="member-topic">Phase-field modeling of frictional fracture, nonlocal mechanics (JMPS / IJP / CMAME)</p>
              </div>
            </div>

            <!-- Guanglei Zhou -->
            <div class="member-card clickable-member" data-member="guanglei-zhou">
              <div class="member-click-hint">Click for Papers ↗</div>
              <div class="member-photo-wrapper">
                <img src="images/guanglei_zhou.png" alt="Dr. Guanglei Zhou" class="member-photo">
                <span class="member-badge">Postdoc</span>
              </div>
              <div class="member-info">
                <h4 class="member-name">Dr. Guanglei Zhou</h4>
                <p class="member-role">Postdoctoral Fellow</p>
                <p class="member-affil">Civil / Geotechnical Engineering</p>
                <p class="member-topic">THM coupled processes, creep deformation and underground energy storage</p>
              </div>
            </div>

            <!-- Lingfeng Guo -->
            <div class="member-card clickable-member" data-member="lingfeng-guo">
              <div class="member-click-hint">Click for Papers ↗</div>
              <div class="member-photo-wrapper">
                <img src="images/lingfeng_guo.png" alt="Dr. Lingfeng Guo" class="member-photo">
                <span class="member-badge">Postdoc</span>
              </div>
              <div class="member-info">
                <h4 class="member-name">Dr. Lingfeng Guo</h4>
                <p class="member-role">Postdoctoral Fellow</p>
                <p class="member-affil">Civil / Geotechnical Engineering</p>
                <p class="member-topic">Peridynamic formulations, multiscale granular mechanics (IJP / Acta Geotechnica)</p>
              </div>
            </div>
          </div>
        </div>

        <!-- PhD Candidates -->
        <div class="team-subgroup" style="margin-top: 3rem;">
          <div class="team-subgroup-header">
            <h3 class="team-group-title">Four PhD Students</h3>
            <span class="team-count">4 Doctoral Candidates &bull; Click to view research &amp; papers</span>
          </div>
          <div class="member-grid phd-grid">
            <!-- Jiaxin Liu -->
            <div class="member-card clickable-member" data-member="jiaxin-liu">
              <div class="member-click-hint">Click for Bio ↗</div>
              <div class="member-photo-wrapper">
                <img src="images/jiaxin_liu.png" alt="Jiaxin Liu" class="member-photo">
                <span class="member-badge" style="background:#0f172a;">PhD</span>
              </div>
              <div class="member-info">
                <h4 class="member-name">Jiaxin Liu</h4>
                <p class="member-role">PhD Candidate &amp; Project Staff</p>
                <p class="member-affil">Civil / Geotechnical Engineering</p>
                <p class="member-topic">Progressive failure in scaly clay and slope instability modeling (FWF Project)</p>
              </div>
            </div>

            <!-- Xinying Han -->
            <div class="member-card clickable-member" data-member="xinying-han">
              <div class="member-click-hint">Click for Bio ↗</div>
              <div class="member-photo-wrapper">
                <img src="images/xinying_han.png" alt="Xinying Han" class="member-photo">
                <span class="member-badge" style="background:#0f172a;">PhD</span>
              </div>
              <div class="member-info">
                <h4 class="member-name">Xinying Han</h4>
                <p class="member-role">PhD Candidate</p>
                <p class="member-affil">Civil / Geotechnical Engineering</p>
                <p class="member-topic">Desiccation cracking and phase-field modeling in unsaturated soils</p>
              </div>
            </div>

            <!-- Xin Liu -->
            <div class="member-card clickable-member" data-member="xin-liu">
              <div class="member-click-hint">Click for Papers ↗</div>
              <div class="member-photo-wrapper">
                <img src="images/xin_liu.png" alt="Xin Liu" class="member-photo">
                <span class="member-badge" style="background:#0f172a;">PhD</span>
              </div>
              <div class="member-info">
                <h4 class="member-name">Xin Liu</h4>
                <p class="member-role">PhD Candidate</p>
                <p class="member-affil">Civil / Geotechnical Engineering</p>
                <p class="member-topic">Wellbore integrity &amp; phase-field hydro-mechanical modeling (IJRMMS 2026)</p>
              </div>
            </div>

            <!-- Open Position -->
            <div class="member-card">
              <div class="member-photo-wrapper">
                <img src="images/phd_open.png" alt="Open Position" class="member-photo">
                <span class="member-badge" style="background:#0f172a;">Open</span>
              </div>
              <div class="member-info">
                <h4 class="member-name">Open Position (TBD)</h4>
                <p class="member-role">PhD Candidate / Researcher</p>
                <p class="member-affil">Civil / Geotechnical Engineering</p>
                <p class="member-topic">Computational geomechanics / Peridynamics (Open for applications)</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Member Profile Modal (Pop-up Window) -->
  <div class="member-modal-overlay" id="member-modal-overlay">
    <div class="member-modal-container">
      <button class="modal-close-btn" id="modal-close-btn" aria-label="Close modal">&times;</button>
      <div id="modal-content-body">
        <!-- Rendered dynamically by main.js -->
      </div>
    </div>
  </div>

  <!-- News Section -->
  <section class="section section-alt" id="news">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Updates</span>
        <h2 class="section-title">Latest Group News</h2>
        <p class="section-desc">
          Recent research accomplishments, project grants, paper acceptances, and group announcements.
        </p>
      </div>

      <div class="news-grid">
        <div class="news-card">
          <div class="news-meta">
            <span class="news-date">2026</span>
            <span class="news-badge">Group Update</span>
          </div>
          <p class="news-text">Wang's Computational Geomechanics Research Group expands with 3 Postdoctoral Fellows and 4 PhD Candidates dedicated to computational civil and geomechanics.</p>
        </div>

        <div class="news-card">
          <div class="news-meta">
            <span class="news-date">2025</span>
            <span class="news-badge">Paper in IJP</span>
          </div>
          <p class="news-text">Our work on thermodynamically consistent phase-field modeling of frictional fracture in rocks is published in International Journal of Plasticity (Sijia Liu &amp; Yunteng Wang et al.).</p>
        </div>

        <div class="news-card">
          <div class="news-meta">
            <span class="news-date">2024</span>
            <span class="news-badge">Springer Book</span>
          </div>
          <p class="news-text">The Springer monograph 'Recent Geotechnical Research at BOKU' co-edited by Prof. Wei Wu and Dr. Yunteng Wang has been officially released.</p>
        </div>

        <div class="news-card">
          <div class="news-meta">
            <span class="news-date">2024</span>
            <span class="news-badge">Award</span>
          </div>
          <p class="news-text">Dr. Yunteng Wang received the prestigious BOKU Best Paper Award from the Anniversary Fund of the City of Vienna.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Openings & Join Us -->
  <section class="section" id="openings">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Opportunities</span>
        <h2 class="section-title">Join Our Group</h2>
        <p class="section-desc">
          We welcome enthusiastic students and visiting scholars in civil and geotechnical engineering to join our research efforts in Vienna.
        </p>
      </div>

      <div class="openings-box">
        <div class="opening-item">
          <h4 class="opening-title">
            PhD Candidate Positions (Computational Geomechanics)
            <span class="opening-type">Fully Funded / CSC Candidates Welcome</span>
          </h4>
          <p class="opening-desc">We are seeking motivated graduate students with background in Civil Engineering, Computational Mechanics, or Rock/Soil Mechanics. Research focuses on Peridynamics and Phase-Field fracture modeling.</p>
        </div>

        <div class="opening-item">
          <h4 class="opening-title">
            Postdoctoral &amp; Visiting Scholar Fellowship
            <span class="opening-type">FWF / International Mobility</span>
          </h4>
          <p class="opening-desc">Researchers interested in nonlocal continuum mechanics, THM coupled phase-field modeling, or particle methods are warmly invited to contact Dr. Yunteng Wang.</p>
        </div>
      </div>

      <!-- Contact Block -->
      <div class="contact-layout" id="contact">
        <div class="contact-info">
          <h3>Get in Touch</h3>
          <p>
            Interested in PhD positions, joint research, or academic visits? Feel free to contact Dr. Yunteng Wang via email or visit our institute in Vienna.
          </p>
          <ul class="contact-details">
            <li><strong>Affiliation:</strong> Institute of Geotechnical Engineering (IGT), BOKU</li>
            <li><strong>Address:</strong> Muthgasse 107, 1190 Vienna, Austria</li>
            <li><strong>Email:</strong> yunteng.wang@boku.ac.at</li>
            <li><strong>University:</strong> BOKU University (Universität für Bodenkultur Wien)</li>
          </ul>
        </div>
        <div style="display:flex; flex-direction:column; justify-content:center; background:rgba(255,255,255,0.05); padding:2rem; border-radius:12px; border:1px solid rgba(255,255,255,0.1);">
          <h4 style="color:#a7f3d0; margin-bottom: 0.75rem;">Vienna - Academic Excellence &amp; Livability</h4>
          <p style="font-size:0.9rem; color:#94a3b8; line-height:1.6;">
            BOKU University is located in Vienna, Austria. Our group offers state-of-the-art computational facilities, high-performance computing clusters, and a collaborative international atmosphere.
          </p>
          <div style="margin-top: 1.5rem;">
            <a href="mailto:yunteng.wang@boku.ac.at" class="btn btn-primary" style="display:inline-block;">Send an Inquiry</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container footer-inner">
      <p>&copy; 2026 Wang's Geomechanics Lab &bull; Institute of Geotechnical Engineering &bull; BOKU Vienna</p>
      <p>Designed for academic excellence &bull; Powered by clean static architecture</p>
    </div>
  </footer>

  <!-- Scripts -->
  <script src="main.js"></script>
</body>
</html>'''

    with open(r'd:\WYT website\index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Rebuilt index.html with interactive member cards & modal setup!")

if __name__ == '__main__':
    build()
