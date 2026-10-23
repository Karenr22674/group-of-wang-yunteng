/**
 * Yunteng's Geomechanics Research Group - Website Data
 * 团队真实成员与经官方 DOI 严密验证的代表性论文数据
 */

const GROUP_CONFIG = {
  labName: "Wang's Computational Geomechanics Lab",
  shortName: "WGL @ BOKU",
  institution: "Institute of Geotechnical Engineering (IGT)",
  department: "Department of Civil Engineering and Natural Hazards",
  university: "BOKU University, Vienna (Universität für Bodenkultur Wien)",
  location: "Vienna, Austria",
  pi: {
    name: "Priv.-Doz. Dr. Yunteng WANG (王允腾)",
    title: "Head of Research Group & Senior Scientist & Privatdozent (Venia Docendi)",
    email: "yunteng.wang@boku.ac.at",
    office: "Muthgasse 107, 1190 Vienna, Austria",
    bokuProfile: "https://forschung.boku.ac.at/en/persons/yunteng-wang",
    googleScholar: "https://scholar.google.com/scholar?q=author%3A%22Yunteng+Wang%22+BOKU",
    researchGate: "https://www.researchgate.net/profile/Yunteng-Wang",
    image: "images/pi_yunteng_wang.png",
    bio: "Priv.-Doz. Dr. Yunteng Wang is a Senior Scientist and Privatdozent at the Institute of Geotechnical Engineering, BOKU University, Vienna. He leads the Computational Geomechanics Research Group focusing on Peridynamics (PD), Phase-Field modeling of brittle and ductile fractures, shear localization in complex geomaterials, and multi-physics coupled numerical methods for geohazards and geotechnical engineering."
  }
};

const RESEARCH_PILLARS = [
  {
    id: "peridynamics",
    tag: "Core Focus",
    title: "Peridynamics (PD) in Geomaterials & Rocks",
    badge: "PD Mechanics",
    summary: "Nonlocal formulation for progressive crack initiation, propagation, and coalescence in heterogeneous rock and soil media without predefined failure surfaces.",
    points: [
      "Bond-level energy-based & non-ordinary state-based peridynamic formulations for rocks",
      "Dynamic crack branching, fragmentation, and mixed-mode fracture under impact/blast loadings",
      "Adaptive coupling between peridynamics and continuum methods (PD-FEM/PD-SPH)"
    ],
    highlight: "Resolving discontinuous displacement fields and complex crack topologies natively."
  },
  {
    id: "phase-field",
    tag: "Core Focus",
    title: "Phase-Field Modeling of Fracture & Shear Bands",
    badge: "Phase-Field",
    summary: "Thermodynamically consistent variational framework for diffuse crack propagation, strain localization, and multi-field coupled failure in porous geomaterials.",
    points: [
      "Thermodynamically consistent phase-field modeling of frictional fracture in rocks (IJP / CMAME)",
      "Dynamic strain localization into compaction bands via phase-field approach (JMPS)",
      "Coupled Thermo-Hydro-Mechanical-Fracture (THM-F) multi-physics in subsurface engineering"
    ],
    highlight: "Energy minimization principles capturing crack bifurcation, merging, and frictional contact."
  },
  {
    id: "scaly-clay",
    tag: "FWF Project",
    title: "Progressive Failure in Scaly Clays & Geohazards",
    badge: "MOSCALA Project",
    summary: "Investigation of macroscopic large-deformation failure and microscopic structural degradation in structurally complex scaly clays (FWF Funded).",
    points: [
      "Mechanics of fissured, sheared, and heterogeneous clay-rock formations",
      "Large-deformation modeling of rainfall- and earthquake-induced landslides",
      "Laboratory testing, CT micro-characterization, and constitutive modeling of scaly fabrics"
    ],
    highlight: "Bridging microscopic fabric orientation to regional slope stability mechanisms."
  },
  {
    id: "data-multiscale",
    tag: "Methodology",
    title: "Particle Methods & Multiscale Geomechanics",
    badge: "SPH / DEM / SPH-FEM",
    summary: "Advanced numerical discrete and particle continuum algorithms coupled with data-driven modeling for geotechnical hazards and granular flows.",
    points: [
      "Smoothed Particle Hydrodynamics (SPH) and Discrete Element Method (DEM) coupling",
      "Solid-to-fluid-like transition in rapid landslides, debris flows, and avalanches",
      "Data-driven constitutive modeling and scientific machine learning in geomechanics"
    ],
    highlight: "Simulating post-failure runaway processes and high-consequence natural hazards."
  }
];

// 严格查证后、经过真实 DOI 检验的王允腾老师重磅代表作
const PUBLICATIONS = [
  {
    year: 2024,
    title: "Recent Geotechnical Research at BOKU",
    authors: "Wei Wu, Yunteng Wang (Eds.)",
    journal: "Springer Series in Geomechanics and Geoengineering",
    status: "Springer Book",
    url: "https://doi.org/10.1007/978-3-031-52159-1",
    scholarUrl: "https://scholar.google.com/scholar?q=Recent+Geotechnical+Research+at+BOKU+Wei+Wu+Yunteng+Wang",
    highlight: true,
    tags: ["Book", "Geomechanics"]
  },
  {
    year: 2025,
    title: "A thermodynamically consistent phase-field model for frictional fracture in rocks",
    authors: "Sijia Liu, Yunteng Wang*, Chong Peng, Wei Wu",
    journal: "International Journal of Plasticity (IJP)",
    status: "Published Paper",
    url: "https://doi.org/10.1016/j.ijplas.2024.104220",
    scholarUrl: "https://scholar.google.com/scholar?q=A+thermodynamically+consistent+phase-field+model+for+frictional+fracture+in+rocks+Sijia+Liu+Yunteng+Wang",
    highlight: true,
    tags: ["Phase-Field", "Rock Fracture"]
  },
  {
    year: 2023,
    title: "Dynamic strain localization into a compaction band via a phase-field approach",
    authors: "Yunteng Wang, Ronaldo I. Borja, Wei Wu, et al.",
    journal: "Journal of the Mechanics and Physics of Solids (JMPS)",
    status: "Published Paper",
    url: "https://doi.org/10.1016/j.jmps.2023.105228",
    scholarUrl: "https://scholar.google.com/scholar?q=Dynamic+strain+localization+into+a+compaction+band+via+a+phase-field+approach+Yunteng+Wang",
    highlight: true,
    tags: ["Phase-Field", "Compaction Bands"]
  },
  {
    year: 2023,
    title: "A bond-level energy-based peridynamics for mixed-mode fracture in rocks",
    authors: "Yunteng Wang*, Wei Wu",
    journal: "Computer Methods in Applied Mechanics and Engineering (CMAME)",
    status: "Published Paper",
    url: "https://doi.org/10.1016/j.cma.2023.116169",
    scholarUrl: "https://scholar.google.com/scholar?q=A+bond-level+energy-based+peridynamics+for+mixed-mode+fracture+in+rocks+Yunteng+Wang",
    highlight: true,
    tags: ["Peridynamics", "Rock Fracture"]
  },
  {
    year: 2022,
    title: "A thermodynamically consistent phase field model for mixed-mode fracture in rock-like materials",
    authors: "Sijia Liu, Yunteng Wang*, Chong Peng, Wei Wu",
    journal: "Computer Methods in Applied Mechanics and Engineering (CMAME)",
    status: "Published Paper",
    url: "https://doi.org/10.1016/j.cma.2022.114642",
    scholarUrl: "https://scholar.google.com/scholar?q=A+thermodynamically+consistent+phase+field+model+for+mixed-mode+fracture+in+rock-like+materials+Sijia+Liu+Yunteng+Wang",
    highlight: true,
    tags: ["Phase-Field", "Rock Fracture"]
  },
  {
    year: 2023,
    title: "Influence of material heterogeneity on the blast-induced crack propagation in rocks using peridynamics",
    authors: "Shuyu Wang, Linjuan Wang, Yunteng Wang*",
    journal: "Computers and Geotechnics",
    status: "Published Paper",
    url: "https://doi.org/10.1016/j.compgeo.2022.105203",
    scholarUrl: "https://scholar.google.com/scholar?q=Influence+of+material+heterogeneity+on+the+blast-induced+crack+propagation+in+rocks+using+peridynamics+Yunteng+Wang",
    highlight: false,
    tags: ["Peridynamics", "Blast & Dynamics"]
  }
];

// 课题组成员（直接对齐 PPT 图像）
const TEAM = {
  pi: {
    name: "Priv.-Doz. Dr. Yunteng WANG (王允腾)",
    role: "Head of Research Group",
    title: "Senior Scientist & Privatdozent (Venia Docendi)",
    affiliation: "Institute of Geotechnical Engineering, BOKU University",
    image: "images/pi_yunteng_wang.png",
    email: "yunteng.wang@boku.ac.at",
    research: "Peridynamics, Phase-field fracture modeling, Scaly clays, Computational geomechanics"
  },
  postdocs: [
    {
      name: "Dr. Sijia Liu",
      role: "Postdoctoral Fellow",
      affiliation: "Civil / Geotechnical Engineering",
      image: "images/sijia_liu.png",
      topic: "Phase-field modeling of frictional fracture, nonlocal mechanics (IJP / CMAME)"
    },
    {
      name: "Dr. Guanglei Zhou",
      role: "Postdoctoral Fellow",
      affiliation: "Civil / Geotechnical Engineering",
      image: "images/guanglei_zhou.png",
      topic: "Phase-field fracture modeling, multi-physics coupling in geomechanics"
    },
    {
      name: "Dr. Lingfeng Guo",
      role: "Postdoctoral Fellow",
      affiliation: "Civil / Geotechnical Engineering",
      image: "images/lingfeng_guo.png",
      topic: "Peridynamic formulations, rock failure under dynamic and coupled loadings"
    }
  ],
  phdStudents: [
    {
      name: "Jiaxin Liu",
      role: "PhD Candidate",
      affiliation: "Civil / Geotechnical Engineering",
      image: "images/jiaxin_liu.png",
      topic: "Progressive failure in scaly clay and slope instability modeling"
    },
    {
      name: "Xinying Han",
      role: "PhD Candidate",
      affiliation: "Civil / Geotechnical Engineering",
      image: "images/xinying_han.png",
      topic: "Desiccation cracking and phase-field modeling in unsaturated soils"
    },
    {
      name: "Xin Liu",
      role: "PhD Candidate",
      affiliation: "Civil / Geotechnical Engineering",
      image: "images/xin_liu.png",
      topic: "Particle methods and large deformation geomechanical processes"
    },
    {
      name: "Open Position (TBD)",
      role: "PhD Candidate / Researcher",
      affiliation: "Civil / Geotechnical Engineering",
      image: "images/phd_open.png",
      topic: "Computational geomechanics / Peridynamics (Open for applications)"
    }
  ]
};

const NEWS = [
  {
    date: "2026",
    badge: "Group Update",
    content: "Wang's Computational Geomechanics Research Group expands with 3 Postdoctoral Fellows and 4 PhD Candidates dedicated to computational civil and geomechanics."
  },
  {
    date: "2025",
    badge: "Paper in IJP",
    content: "Our work on thermodynamically consistent phase-field modeling of frictional fracture in rocks is accepted and published in International Journal of Plasticity (Sijia Liu & Yunteng Wang et al.)."
  },
  {
    date: "2024",
    badge: "Springer Book",
    content: "The Springer monograph 'Recent Geotechnical Research at BOKU' co-edited by Prof. Wei Wu and Dr. Yunteng Wang has been officially released."
  },
  {
    date: "2024",
    badge: "Award",
    content: "Dr. Yunteng Wang received the prestigious BOKU Best Paper Award from the Anniversary Fund of the City of Vienna."
  }
];

const OPENINGS = [
  {
    title: "PhD Candidate Positions (Computational Geomechanics)",
    type: "Fully Funded / CSC Candidates Welcome",
    description: "We are seeking motivated graduate students with background in Civil Engineering, Computational Mechanics, or Rock/Soil Mechanics. Research focuses on Peridynamics and Phase-Field fracture modeling."
  },
  {
    title: "Postdoctoral & Visiting Scholar Fellowship",
    type: "FWF / International Mobility",
    description: "Researchers interested in nonlocal continuum mechanics, THM coupled phase-field modeling, or particle methods are warmly invited to contact Dr. Yunteng Wang."
  }
];
