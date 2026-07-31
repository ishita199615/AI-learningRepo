# AI-learningRepo
<!-- generated from resources.yml — do not edit by hand -->

# AI & Data Science Learning Path

**A curated, opinionated path through the courses, tools, and references worth your time.**

![resources](https://img.shields.io/badge/resources-23-blue) ![vetted](https://img.shields.io/badge/personally%20vetted-18-green) ![license](https://img.shields.io/badge/license-MIT-lightgrey)

Not a link dump. Every entry answers three questions: what is it, who is it for, and how long will it actually take.
Anything I haven't personally worked through is marked as such.

Entries live in `resources.yml`. 
The README is generated — see CONTRIBUTING.md.

---

## Contents

- [Start here](#start-here) — 3 entries
- [Courses](#courses) — 8 entries
- [Tools](#tools) — 8 entries
- [References](#references) — 4 entries
- [How to read this](#how-to-read-this)

---

## Start here

*If you're new and want one thing to open first, open the first one.*

### [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)

**Microsoft** · free · beginner · ~20 hours · 21 lessons, Python + TypeScript

The best free on-ramp to building with LLMs. Lessons split cleanly into "Learn" (concepts) and "Build" (code you run). Needs an Azure OpenAI, GitHub Models, or OpenAI key — GitHub Models is the free path.

`completed`  ·  `genai` `llm` `prompt-engineering` `rag`

### [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)

**Andrej Karpathy** · free · intermediate · ~25 hours · Video lectures + notebooks

Builds backprop, then a transformer, from scratch in plain Python. The single best way to stop treating models as magic. Slow down and type the code rather than watching it.

`completed`  ·  `deep-learning` `transformers` `fundamentals`

### [Practical Deep Learning for Coders](https://course.fast.ai)

**fast.ai** · free · beginner · ~40 hours · Video course + fastbook

Top-down: you train a working model in lesson one and learn the theory afterwards. The opposite order to Karpathy, and a good complement to it.

`partly done`  ·  `deep-learning` `computer-vision` `nlp`

---

## Courses

*Longer structured programmes. Costs and time estimates are the realistic ones, not the marketing ones.*

### [Machine Learning for Beginners](https://github.com/microsoft/ML-For-Beginners)

**Microsoft** · free · beginner · ~24 hours · 26 lessons, Python + R

Classical ML, not deep learning. Regression, clustering, NLP, time series.

`reviewed`  ·  `machine-learning` `python` `r`

### [Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners)

**Microsoft** · free · beginner · ~20 hours · 20 lessons

Ethics, data prep, visualisation, lifecycle. Good for non-CS backgrounds.

`reviewed`  ·  `data-science` `visualization`

### [AI for Beginners](https://github.com/microsoft/AI-For-Beginners)

**Microsoft** · free · beginner · ~24 hours · 12 weeks, 24 lessons

Broader and more theoretical than the GenAI course. Symbolic AI through neural networks.

`reviewed`  ·  `ai` `deep-learning` `fundamentals`

### [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)

**Microsoft** · free · intermediate · ~12 hours · Lessons + code

Agent design patterns, tool use, planning. Do the GenAI course first.

`in progress`  ·  `agents` `llm`

### [MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)

**Microsoft** · free · intermediate · ~8 hours · Lessons + code

Model Context Protocol is becoming the standard way tools attach to models. Worth understanding before you write another bespoke tool schema.

`not yet reviewed`  ·  `mcp` `agents` `tooling`

### [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp)

**DataTalks.Club** · free · beginner · ~4 months · Cohort course + projects

Deployment-focused. You ship models, not just train them. Runs as a cohort with deadlines.

`reviewed`  ·  `machine-learning` `mlops` `deployment`

### [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)

**DataTalks.Club** · free · intermediate · ~4 months · Cohort course + projects

dbt, Spark, Kafka, orchestration, warehousing. The gap most data scientists have.

`not yet reviewed`  ·  `data-engineering` `spark` `dbt`

### [Open Source Society University — Data Science](https://github.com/ossu/data-science)

**OSSU** · free · beginner · 2+ years · Full curriculum

A complete degree-equivalent path. Realistically nobody finishes it, but it's an excellent map for finding the gaps in your own knowledge.

`reference`  ·  `curriculum` `data-science` `mathematics`

---

## Tools

*Free, open source, and worth the install. Each line says what it replaces.*

### [ollama](https://github.com/ollama/ollama)

**Ollama** · free · beginner · 5 minutes · CLI

Run open language models locally. One command to install, one to pull a model.

`daily driver`  ·  `llm` `local-ai`

### [vLLM](https://github.com/vllm-project/vllm)

**vLLM project** · free · advanced · ~1 hour · Python library / server

Production inference. Continuous batching and an OpenAI-compatible endpoint, which matters more than the throughput — swapping providers becomes a base-URL change.

`reviewed`  ·  `llm` `serving` `gpu`

### [DuckDB](https://github.com/duckdb/duckdb)

**DuckDB Labs** · free · beginner · 15 minutes · Embedded database

Query millions of rows straight from CSV or Parquet with no server. Benchmarks in my duckdb-vs-pandas repo if you want numbers.

`daily driver`  ·  `analytics` `sql` `data`

### [Whisper](https://github.com/openai/whisper)

**OpenAI** · free · beginner · 20 minutes · Python library

Speech to text, offline, 90+ languages. Use faster-whisper for real workloads.

`daily driver`  ·  `speech` `transcription`

### [LangGraph](https://github.com/langchain-ai/langgraph)

**LangChain** · free · intermediate · ~3 hours · Python library

Agent loops as state machines, with checkpointing and interrupt points. The distinction that matters: a chain runs steps you defined, an agent runs a loop where the model decides.

`in progress`  ·  `agents` `orchestration`

### [Langfuse](https://github.com/langfuse/langfuse)

**Langfuse** · free · intermediate · ~1 hour · Self-hosted service

Token cost per run, latency per node, prompt versioning. Grafana understands CPU; it does not understand tokens. You need both.

`reviewed`  ·  `observability` `evals` `llmops`

### [Supabase](https://github.com/supabase/supabase)

**Supabase** · free tier · beginner · ~1 hour · Hosted or self-hosted

Postgres with auth, storage, realtime and pgvector. One dependency instead of four.

`reviewed`  ·  `database` `backend` `pgvector`

### [Docling](https://github.com/docling-project/docling)

**IBM** · free · intermediate · ~1 hour · Python library

Document parsing that preserves table structure. Mangled tables are the most common silent cause of confidently wrong RAG answers.

`not yet reviewed`  ·  `rag` `parsing` `documents`

---

## References

*Things I reopen rather than read once.*

### [The fastai book](https://github.com/fastai/fastbook)

**Howard & Gugger** · free · beginner · reference · Jupyter notebooks

Full text of the O'Reilly book as runnable notebooks.

`reference`  ·  `deep-learning` `book`

### [LLM101n](https://github.com/karpathy/LLM101n)

**Andrej Karpathy** · free · intermediate · reference · Course repo

Build a storyteller LLM from scratch. Still evolving — check activity before committing.

`not yet reviewed`  ·  `llm` `from-scratch`

### [System Design Primer](https://github.com/donnemartin/system-design-primer)

**Donne Martin** · free · intermediate · reference · Markdown + flashcards

Not AI-specific, but the vocabulary you need the moment a model goes to production.

`reference`  ·  `system-design` `interviews`

### [smol-course](https://github.com/huggingface/smol-course)

**Hugging Face** · free · intermediate · ~10 hours · Notebooks

Aligning and fine-tuning small models on modest hardware.

`not yet reviewed`  ·  `fine-tuning` `small-models`

---

## How to read this

**Status** tells you how much weight to give my opinion:

| Status | Means |
|---|---|
| `daily driver` | I use this regularly |
| `completed` | I finished it |
| `in progress` | I'm working through it now |
| `partly done` | I did some of it |
| `reviewed` | I've used or read enough to judge it |
| `reference` | I reopen it rather than read it through |
| `not yet reviewed` | On my list — included for completeness, not endorsed |

**Time estimates are realistic, not promotional.** If a course says "6 hours" and actually takes 20 once you run the code, the number here is 20.

**Most common tags:** `llm` (5), `deep-learning` (4), `agents` (3), `rag` (2), `fundamentals` (2), `machine-learning` (2), `data-science` (2), `genai` (1)

---

## Contributing

Edit `resources.yml`, not this file. See [CONTRIBUTING.md](CONTRIBUTING.md).

Links are checked weekly by CI. If one rots, an issue opens automatically.

## License

MIT. Curation is opinion, not endorsement — check licences on the linked projects themselves.

Maintained by [Ishita Sharma](https://github.com/IshitaSharmaDS).
