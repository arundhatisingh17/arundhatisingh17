# Arundhati Singh <img src="https://github.com/TheDudeThatCode/TheDudeThatCode/blob/master/Assets/Mario_Hello_Big.gif" width="55" />

<p align="left">
  <a href="https://www.linkedin.com/in/arundhati-singh171003/" target="blank"><img align="center" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>&nbsp;
  <a href="https://github.com/arundhatisingh17" target="blank"><img align="center" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>&nbsp;
  <a href="https://medium.com/@arundhatisingh171003" target="blank"><img align="center" src="https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white" alt="Medium" /></a>&nbsp;
  <a href="https://arundhati17.netlify.app/" target="blank"><img align="center" src="https://img.shields.io/badge/Website-D87093?style=for-the-badge&logo=netlify&logoColor=white" alt="Website" /></a>&nbsp;
  <a href="https://drive.google.com/file/d/1oQdrTvDp9yzpgVMg3a8FCJeHFV5-oUYc/view?usp=sharing" target="blank"><img align="center" src="https://img.shields.io/badge/Resume-4285F4?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white" alt="Resume" /></a>
</p>

Computer Science and Data Science graduate from **UW–Madison** (Honors in Big Data Systems, Mathematics Certificate) and incoming **M.S. in Computer Science and Engineering at UC San Diego** (Sep 2026). I build distributed systems and data infrastructure, with a focus on fault tolerance, throughput, and energy-efficient computing.

I care about the layers where systems and data meet: distributed execution engines, storage and query optimization, and measuring what compute actually costs. Below is a snapshot of the work I find most interesting.

---

<!--START:activity-->
## Last 7 Commits

- [`neetcode-submissions`](https://github.com/arundhatisingh17/neetcode-submissions) — [Add: longest-repeating-substring-with-replacement - submission-0](https://github.com/arundhatisingh17/neetcode-submissions/commit/e8c898e55651fdb0560b45f6b39e2e2f42fac5d0) · 2 days ago
- [`neetcode-submissions`](https://github.com/arundhatisingh17/neetcode-submissions) — [Add: word-break - submission-5](https://github.com/arundhatisingh17/neetcode-submissions/commit/2039e00f351b62d052689906256945b46cba6289) · 15 hours ago
- [`neetcode-submissions`](https://github.com/arundhatisingh17/neetcode-submissions) — [Add: count-paths - submission-6](https://github.com/arundhatisingh17/neetcode-submissions/commit/a79dcb8712ed155b75d1e6b25f097ea6c5c46425) · 16 hours ago
- [`neetcode-submissions`](https://github.com/arundhatisingh17/neetcode-submissions) — [Add: longest-common-subsequence - submission-3](https://github.com/arundhatisingh17/neetcode-submissions/commit/9ac6d3ba1a6f10d8bcb7078f6b49ab0fb63116c1) · 23 hours ago
- [`neetcode-submissions`](https://github.com/arundhatisingh17/neetcode-submissions) — [Add: products-of-array-discluding-self - submission-4](https://github.com/arundhatisingh17/neetcode-submissions/commit/7dce7faa4b40b0427690cf9883a7093f22388ca6) · 16 hours ago
- [`neetcode-submissions`](https://github.com/arundhatisingh17/neetcode-submissions) — [Add: products-of-array-discluding-self - submission-1](https://github.com/arundhatisingh17/neetcode-submissions/commit/6d6eca9df4695381e72438d34f3c055a7333caf2) · 16 hours ago
- [`neetcode-submissions`](https://github.com/arundhatisingh17/neetcode-submissions) — [Add: palindromic-substrings - submission-0](https://github.com/arundhatisingh17/neetcode-submissions/commit/2ef637f5e222ff4588c082cf320ea2d6f89abb53) · 1 day ago
<!--END:activity-->

---

## Education

- **University of California, San Diego** — M.S., Computer Science and Engineering *(Sep 2026 – May 2028)*
- **University of Wisconsin–Madison** — B.S., Computer Science & Data Science, Mathematics Certificate, Honors in Big Data Systems *(Aug 2022 – May 2026)*
  - Cumulative GPA 3.73 · 4.0 across the last three semesters

---

## Experience & Research

**Research Assistant — Prof. Remzi Arpaci-Dusseau** *(Jul 2025 – May 2026)*
- Designed and ran real-hardware experiments on NVIDIA V100S GPUs (CloudLab), building an instrumentation pipeline with NVML energy profiling and PyTorch GEMM-FLOP tracking across five system configurations.
- Showed that Energy-per-FLOP is far more consistent than per-token pricing (a 29% spread versus 146%) across prefill and decode workloads — arguing for energy as a fairer unit for inference cost.

**Software Developer — Traffic Operations & Safety Laboratory** *(Sep 2025 – May 2026)*
- Built a RESTful Java backend with Spring Boot (Model-Repository-Controller) and parameterized SQL for a statewide traffic-safety analytics dashboard, enabling year-over-year crash trend analysis with region, county, and municipality filters.
- Extended a statewide crash-analytics platform (Java, PostgreSQL) with new API endpoints and filtered, parameterized queries to speed up data access for government users.

**Research Assistant — Prof. Kevin Eliceiri, FabLab** *(Sep 2024 – Sep 2025)*
- Engineered a real-time monitoring pipeline for electron-beam manufacturing equipment, processing 50K+ daily log entries for proactive anomaly detection.
- Cut end-to-end ingestion latency by 30% using buffered batch transfers and asynchronous HTTP requests.
- Reverse-engineered a binary RS-232 protocol to build a low-level Python driver for legacy hardware, with automated handshake and error-recovery logic for 24/7 reliability.

---

## Selected Projects

**[Speculative Retrieval](https://github.com/arundhatisingh17/speculative-retrieval)** · *Python, FastAPI, PyTorch, SPECTER2, React*
- Aspect-aware retrieval over research papers that separates work by *contribution* rather than surface topic, addressing the aspect-conflation failure of standard dense RAG on vocabulary-saturated corpora.
- Built a two-tier retriever that fuses SPECTER2 paper embeddings, BGE passage embeddings, and a cross-encoder reranker via reciprocal-rank fusion, with section-aware "aspect lenses" that bias ranking toward the part of a paper (method, gaps) that answers the question.
- Added a query-reformulation layer that decomposes long, multi-part questions into fused sub-queries, plus a grounded LLM step returning a cited "why this matches" summary per result — surfaced through a React/Vite interface with drag-to-workspace refocusing over the live FastAPI backend.

**Custom MapReduce Engine** · *Python, gRPC, Docker, HDFS*
- Distributed computing engine on a Master-Worker topology, using gRPC for low-latency inter-node communication and HDFS for distributed storage of Parquet datasets.
- Fault-tolerant execution via a heartbeat monitor that detects worker failures and performs atomic task reassignment, reaching eventual consistency without manual intervention.
- Reduced shuffle-phase network I/O through columnar Parquet storage and map-side combiners.

**Open-Source Contribution — Superduper** · *Python*
- Proposed a fix for an unsafe pickle/dill deserialization vulnerability, introducing an `Auto` datatype that serializes JSON-safe fields as plain text while preserving dill only for genuinely non-serializable objects.

---

## Teaching

Peer Mentor for **CS 320, CS 564, and CS 574** at UW–Madison *(Jun 2024 – May 2026)* — mentoring students in algorithm analysis, object-oriented design, query optimization, and ETL/ELT pipeline design.

---

## Technical Skills

| Category | Tools |
| :--- | :--- |
| **Languages** | Go, Java, C/C++, Python, SQL, JavaScript |
| **Systems & Distributed Computing** | gRPC, RPC, TCP/IP, HDFS, Docker, multithreading & concurrency, fault tolerance |
| **Databases** | MySQL, PostgreSQL, MongoDB, Elasticsearch |
| **Frameworks & Tools** | Spring Boot, React, Flask, Git, JIRA, Google Cloud, AWS |
| **ML / Systems** | PyTorch, CUDA, OpenMP, vLLM, GPU performance profiling |

<p align="left">
      <img src="https://www.vectorlogo.zone/logos/golang/golang-icon.svg" alt="go" width="55" height="55"/>
      <img src="https://www.vectorlogo.zone/logos/java/java-icon.svg" alt="java" width="60" height="60"/>
      <img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="python" width="50" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/nodejs/nodejs-icon.svg" alt="nodejs" width="50" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="50" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/docker/docker-official.svg" alt="docker" width="55" height="45"/>
      <img src="https://www.vectorlogo.zone/logos/kubernetes/kubernetes-icon.svg" alt="kubernetes" width="50" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/amazon_aws/amazon_aws-icon.svg" alt="aws" width="50" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="50" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg" alt="postgresql" width="45" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/mysql/mysql-icon.svg" alt="mysql" width="45" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/mongodb/mongodb-icon.svg" alt="mongodb" width="42" height="50"/>
      <img src="https://www.vectorlogo.zone/logos/elastic/elastic-icon.svg" alt="elasticsearch" width="42" height="50"/>
</p>

---

## Awards & Activities

- **Akuna Capital 2026 Virtual Quant Trading Challenge** — selected participant; built and tested a market-making bot in a simulated exchange environment.
- **300+ LeetCode problems solved**, including 140+ Medium-difficulty.

---

## LeetCode Activity

<p align="center">
  <img src="https://leetcard.jacoblin.cool/lolly_171003?theme=light&font=Karma&ext=heatmap" alt="LeetCode activity grid" />
</p>

---

## Contact

I am always open to discussing distributed systems, data infrastructure, research, or collaboration.

<p align="left">
<a href="mailto:asingh278@wisc.edu">
  <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
</a>
</p>
