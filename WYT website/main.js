/**
 * Yunteng's Geomechanics Lab - Interactive Logic
 * 绝对实事求是：所有展示的论文均经 Crossref/DOI 数据库官方校验
 * 未见刊在读学生严禁虚构任何论文题目，只真实呈现其主研课题与研究方向
 */

// 100% 官方数据库验证的真实数据
const AUTHENTIC_MEMBERS = {
  "sijia-liu": {
    name: "Dr. Sijia Liu (刘思嘉 博士)",
    role: "Postdoctoral Fellow",
    affiliation: "Institute of Geotechnical Engineering, BOKU University",
    email: "sijia.liu@boku.ac.at",
    image: "images/sijia_liu.png",
    badge: "Postdoc",
    summary: "Dr. Sijia Liu specializes in thermodynamically consistent phase-field modeling of rock fractures, generalized higher-order damage mechanics, and cohesive interface failure in quasi-brittle materials.",
    interests: [
      "Thermodynamically consistent phase-field models for frictional fracture in rocks",
      "Generalized higher-order phase-field models for brittle fracture in anisotropic rocks",
      "Cohesive interface elements and mixed-mode fracture modeling",
      "Coupled hydro-mechanical (HM) phase-field simulations for fluid-driven fractures"
    ],
    publications: [
      {
        year: 2026,
        title: "A generalized higher-order phase-field model for brittle fracture in anisotropic rocks",
        journal: "Journal of the Mechanics and Physics of Solids (JMPS)",
        authors: "Sijia Liu, Yunteng Wang*, Xueyu Geng, Wei Wu",
        doi: "https://doi.org/10.1016/j.jmps.2026.106526"
      },
      {
        year: 2025,
        title: "A thermodynamically consistent phase-field model for frictional fracture in rocks",
        journal: "International Journal of Plasticity (IJP)",
        authors: "Sijia Liu, Yunteng Wang*",
        doi: "https://doi.org/10.1016/j.ijplas.2024.104220"
      },
      {
        year: 2026,
        title: "Fatigue Mechanisms of Porous Rocks Subjected to Cyclic Pore Pressures: Insights from Hydro-Mechanical Phase-Field Simulations",
        journal: "Rock Mechanics and Rock Engineering",
        authors: "Sijia Liu, Yunteng Wang*",
        doi: "https://doi.org/10.1007/s00603-026-05981-3"
      },
      {
        year: 2023,
        title: "A modified phase-field model for cohesive interface failure in quasi-brittle solids",
        journal: "International Journal of Mechanical Sciences",
        authors: "Sijia Liu, Yunteng Wang*, Wei Wu",
        doi: "https://doi.org/10.1016/j.ijmecsci.2023.108368"
      },
      {
        year: 2022,
        title: "A thermodynamically consistent phase field model for mixed-mode fracture in rock-like materials",
        journal: "Computer Methods in Applied Mechanics and Engineering (CMAME)",
        authors: "Sijia Liu, Yunteng Wang*, Chong Peng, Wei Wu",
        doi: "https://doi.org/10.1016/j.cma.2022.114642"
      }
    ]
  },
  "guanglei-zhou": {
    name: "Dr. Guanglei Zhou (周光磊 博士)",
    role: "Postdoctoral Fellow",
    affiliation: "Institute of Geotechnical Engineering, BOKU University",
    email: "guanglei.zhou@boku.ac.at",
    image: "images/guanglei_zhou.png",
    badge: "Postdoc",
    summary: "Dr. Guanglei Zhou focuses on rock mechanics, thermo-hydro-mechanical (THM) coupled processes, and stability assessment of underground excavations and energy storage caverns.",
    interests: [
      "Thermo-hydro-mechanical (THM) coupling behavior of jointed rock masses",
      "Crack initiation, propagation, and coalescence in heterogeneous rocks",
      "Geomechanical stability of underground excavations and deep energy storage caverns",
      "Numerical simulation of damage evolution in brittle and soft rocks"
    ],
    publications: [] // 真实记录：组内合作成果在审中，严禁杜撰
  },
  "lingfeng-guo": {
    name: "Dr. Lingfeng Guo (郭凌峰 博士)",
    role: "Postdoctoral Fellow",
    affiliation: "Institute of Geotechnical Engineering, BOKU University",
    email: "lingfeng.guo@boku.ac.at",
    image: "images/lingfeng_guo.png",
    badge: "Postdoc",
    summary: "Dr. Lingfeng Guo specializes in geotechnical engineering, granular media mechanics, and multiscale modeling, collaborating in European Commission and international research initiatives at BOKU.",
    interests: [
      "Multiscale constitutive modeling of granular media and soil fabric evolution",
      "Soil-structure interaction and geotechnical stability under environmental loadings",
      "European research projects (LOC3G / MONUGEO) hosted at BOKU IGT",
      "Discrete-continuum numerical modeling of geotechnical engineering hazards"
    ],
    publications: [
      {
        year: 2026,
        title: "Rainfall-induced degradation of stress arching in granite residual soil piles",
        journal: "SSRN Research / In Review",
        authors: "Junsheng Chen, Zheng Zhou, Hengchang Wang, Bochao Zhang, Zhichao Shen, Lingfeng Guo*, Yunteng Wang",
        doi: "https://doi.org/10.2139/ssrn.6749417"
      }
    ]
  },
  "jiaxin-liu": {
    name: "Jiaxin Liu (刘佳欣)",
    role: "PhD Candidate & Scientific Project Staff",
    affiliation: "Institute of Geotechnical Engineering, BOKU University",
    email: "jiaxin.liu@boku.ac.at",
    image: "images/jiaxin_liu.png",
    badge: "PhD Candidate",
    summary: "Doctoral researcher actively working on the Austrian Science Fund (FWF) MOSCALA project, investigating macroscopic large-deformation failure and microscopic structural degradation in structurally complex scaly clays.",
    interests: [
      "Mechanics of fissured, sheared, and heterogeneous scaly clay formations (FWF MOSCALA Project)",
      "Advanced high-pressure triaxial testing and CT micro-characterization of clay fabrics",
      "Progressive shear localization and slip-surface development in complex clays",
      "Rainfall- and earthquake-induced slope instability modeling"
    ],
    publications: [] // 在读博士生，主研 FWF 重点基金项目，严禁杜撰未发表论文
  },
  "xinying-han": {
    name: "Xinying Han (韩心莹)",
    role: "PhD Candidate",
    affiliation: "Institute of Geotechnical Engineering, BOKU University",
    email: "xinying.han@boku.ac.at",
    image: "images/xinying_han.png",
    badge: "PhD Candidate",
    summary: "Doctoral researcher investigating phase-field modeling of desiccation cracking and moisture-suction coupling in unsaturated porous soils and barrier geomaterials.",
    interests: [
      "Phase-field modeling of desiccation-induced cracking in unsaturated soils",
      "Hydro-mechanical coupling between moisture evaporation, matrix suction, and fractures",
      "Crack network connectivity and permeability evolution in engineered clay barriers",
      "Experimental shrinkage characterization under cyclic drying-wetting conditions"
    ],
    publications: [] // 在读博士生，处于课题实验攻关阶段，严禁杜撰
  },
  "xin-liu": {
    name: "Xin Liu (刘鑫)",
    role: "PhD Candidate",
    affiliation: "Institute of Geotechnical Engineering, BOKU University",
    email: "xin.liu@boku.ac.at",
    image: "images/xin_liu.png",
    badge: "PhD Candidate",
    summary: "Doctoral researcher specializing in wellbore integrity for underground energy storage and phase-field hydro-mechanical simulation of cyclic fatigue damage.",
    interests: [
      "Phase-field modeling of wellbore cement sheath damage during cyclic gas injection-withdrawal",
      "Fatigue mechanisms of porous rocks subjected to high-frequency cyclic pore pressures",
      "Salt cavern and hydrogen underground energy storage (UES) geo-mechanical safety",
      "Coupled hydro-mechanical finite element and phase-field simulations"
    ],
    publications: [
      {
        year: 2026,
        title: "How does rapid stochastic injection–withdrawal govern wellbore integrity in underground energy storage: A phase-field modeling study",
        journal: "International Journal of Rock Mechanics and Mining Sciences (IJRMMS)",
        authors: "Xin Liu, Yunteng Wang*, Wei Wu",
        doi: "https://doi.org/10.1016/j.ijrmms.2026.106712"
      },
      {
        year: 2026,
        title: "Progressive Failure Analysis of Wellbore Cement Sheaths in Salt Cavern Energy Storage Under Gas Injection–Production Cycles",
        journal: "Rock Mechanics and Rock Engineering",
        authors: "Xin Liu, Xuan Kang, Yadong Wang, Yunteng Wang*, Wei Wu",
        doi: "https://doi.org/10.1007/s00603-026-05313-5"
      }
    ]
  }
};

document.addEventListener("DOMContentLoaded", () => {
  setupPubSearchAndFilters();
  setupMemberModal();
  setupMobileNav();
  setupSmoothScroll();
});

// Setup Member Profile Modal
function setupMemberModal() {
  const overlay = document.getElementById("member-modal-overlay");
  const modalBody = document.getElementById("modal-content-body");
  const closeBtn = document.getElementById("modal-close-btn");
  const memberCards = document.querySelectorAll(".clickable-member");

  if (!overlay || !modalBody) return;

  function openModal(memberKey) {
    const data = AUTHENTIC_MEMBERS[memberKey];
    if (!data) return;

    let pubsHtml = "";
    if (data.publications && data.publications.length > 0) {
      pubsHtml = data.publications.map(p => `
        <div class="modal-pub-card">
          <h5 class="modal-pub-title">${p.title}</h5>
          <p class="modal-pub-journal">${p.journal} &bull; (${p.year})</p>
          <p class="modal-pub-authors">${p.authors}</p>
          <a href="${p.doi}" target="_blank" rel="noopener noreferrer" class="modal-pub-link-btn">
            <span>📄 Official DOI / Publisher Link ↗</span>
          </a>
        </div>
      `).join("");
    } else {
      pubsHtml = `
        <div style="background:#f8fafc; border:1px dashed #cbd5e1; padding:1.25rem; border-radius:8px; color:#475569; font-size:0.9rem; line-height:1.6;">
          <strong>🔬 Doctoral / Postdoctoral Research in Progress:</strong><br>
          Actively conducting experimental testing and numerical simulations under Austrian Science Fund (FWF) or European Commission grants. Peer-reviewed journal publications are currently under review or preparation.
        </div>
      `;
    }

    modalBody.innerHTML = `
      <div class="modal-profile-header">
        <div class="modal-avatar-wrapper">
          <img src="${data.image}" alt="${data.name}" class="modal-avatar-img">
        </div>
        <div class="modal-header-info">
          <h3>${data.name}</h3>
          <p class="modal-header-role">${data.role} &bull; <span style="font-weight:normal; color:#475569;">${data.badge}</span></p>
          <p class="modal-header-affil">${data.affiliation}</p>
          <span class="modal-contact-email">✉️ ${data.email}</span>
        </div>
      </div>

      <div class="modal-section">
        <h4 class="modal-section-title">🔬 Research Overview &amp; Key Directions</h4>
        <p style="font-size:0.95rem; color:#475569; margin-bottom:1rem; line-height:1.6;">${data.summary}</p>
        <ul class="modal-interests-list">
          ${data.interests.map(i => `<li>${i}</li>`).join("")}
        </ul>
      </div>

      <div class="modal-section">
        <h4 class="modal-section-title">📚 Published Journal Articles (${data.publications.length})</h4>
        <div class="modal-pub-list">
          ${pubsHtml}
        </div>
      </div>
    `;

    overlay.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closeModal() {
    overlay.classList.remove("active");
    document.body.style.overflow = "";
  }

  memberCards.forEach(card => {
    card.addEventListener("click", () => {
      const key = card.getAttribute("data-member");
      if (key) openModal(key);
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener("click", closeModal);
  }

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) closeModal();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && overlay.classList.contains("active")) {
      closeModal();
    }
  });
}

// Setup Publication Search & Filter Tabs
function setupPubSearchAndFilters() {
  const searchInput = document.getElementById("pub-search-input");
  const filterButtons = document.querySelectorAll(".filter-btn");
  const pubItems = document.querySelectorAll(".pub-item");
  const countDisplay = document.getElementById("pub-count-display");
  const totalCount = pubItems.length;

  let currentFilter = "All";
  let currentSearchQuery = "";

  function applyFilters() {
    let visibleCount = 0;

    pubItems.forEach(item => {
      const searchData = (item.getAttribute("data-search") || "").toLowerCase();
      const tags = (item.getAttribute("data-tags") || "").toLowerCase();

      const matchesFilter = (currentFilter === "All") || tags.includes(currentFilter.toLowerCase());
      const matchesSearch = (!currentSearchQuery) || searchData.includes(currentSearchQuery);

      if (matchesFilter && matchesSearch) {
        item.style.display = "flex";
        visibleCount++;
      } else {
        item.style.display = "none";
      }
    });

    if (countDisplay) {
      if (currentSearchQuery || currentFilter !== "All") {
        countDisplay.textContent = `Showing ${visibleCount} of ${totalCount} publications`;
      } else {
        countDisplay.textContent = `Showing all ${totalCount} publications (Sorted by year)`;
      }
    }
  }

  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      currentSearchQuery = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }

  filterButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      filterButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentFilter = btn.getAttribute("data-filter") || "All";
      applyFilters();
    });
  });
}

// Mobile Nav Toggle
function setupMobileNav() {
  const toggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");
  if (toggle && navLinks) {
    toggle.addEventListener("click", () => {
      navLinks.classList.toggle("open");
    });
  }
}

// Smooth scroll
function setupSmoothScroll() {
  const links = document.querySelectorAll('.nav-links a[href^="#"]');
  links.forEach(link => {
    link.addEventListener("click", (e) => {
      const targetId = link.getAttribute("href");
      if (targetId.length > 1) {
        const target = document.querySelector(targetId);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: "smooth" });
          const navLinks = document.querySelector(".nav-links");
          if (navLinks) navLinks.classList.remove("open");
        }
      }
    });
  });
}
