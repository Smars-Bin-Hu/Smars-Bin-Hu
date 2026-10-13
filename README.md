<a href="https://github.com/Smars-Bin-Hu/copilot-agentic-harness">
  <img src="./card/card.svg" alt="Smars Hu: data engineer building AI agent harnesses in Toronto" width="100%" />
</a>

I'm Smars, a data engineer in Toronto. I work in banking, where an AI agent is only useful if you can prove what it did and stop it from doing what it shouldn't. That is the problem I build for.

## What I'm building

### [copilot-agentic-harness](https://github.com/Smars-Bin-Hu/copilot-agentic-harness)

A harness that wraps GitHub Copilot in VS Code so a team can let an agent work on real repositories.

- **Rules enforced by code.** Hooks check every tool call before it runs. Out-of-scope writes, `.git` changes and dangerous commands are rejected, whatever the prompt says.
- **Tasks that survive a new session.** Each task is a directory holding the requirement, plan, progress and result, so a fresh session picks up where the last one stopped.
- **Independent review.** The agent that did the work does not grade it. A separate reviewer and coded acceptance checks do.
- **Human-approved write-back.** The agent works in a task directory and reads the target repository's `main`. Changes reach the target only through a promote you approve, on a new branch.

Python standard library only, no `pip install`. Runs on macOS and Windows.

## Earlier work: data engineering

| Project | What it is | |
| --- | --- | --- |
| [EComDWH-BatchDataProcessingPlatform](https://github.com/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform) | A five-layer data warehouse for e-commerce orders on a self-managed cluster: Spark, Airflow, ClickHouse, with CI/CD and monitoring. | ![stars](https://img.shields.io/github/stars/Smars-Bin-Hu/EComDWH-BatchDataProcessingPlatform?style=flat-square) |
| [azure-cloud-datapipeline-EDA](https://github.com/Smars-Bin-Hu/azure-cloud-datapipeline-EDA) | A lakehouse pipeline on Azure Databricks with Delta Lake, Unity Catalog and Data Factory. | ![stars](https://img.shields.io/github/stars/Smars-Bin-Hu/azure-cloud-datapipeline-EDA?style=flat-square) |

## Tech stack

### AI agent engineering

**Coding agents**

![Claude Code](https://img.shields.io/badge/Claude_Code-d97757?style=for-the-badge&logo=claude&logoColor=white) ![GitHub Copilot Agent Mode](https://img.shields.io/badge/GitHub_Copilot_Agent_Mode-24292f?style=for-the-badge&logo=githubcopilot&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge)

**Harness engineering**

![Agent Harness](https://img.shields.io/badge/Agent_Harness-6e40c9?style=for-the-badge) ![Tool-Call Hooks](https://img.shields.io/badge/Tool--Call_Hooks-6e40c9?style=for-the-badge) ![Permission Gates](https://img.shields.io/badge/Permission_Gates-6e40c9?style=for-the-badge) ![Human-in-the-Loop Approval](https://img.shields.io/badge/Human--in--the--Loop_Approval-6e40c9?style=for-the-badge) ![Persistent Task State](https://img.shields.io/badge/Persistent_Task_State-6e40c9?style=for-the-badge) ![Agent Observability](https://img.shields.io/badge/Agent_Observability-6e40c9?style=for-the-badge)

**Context engineering**

![MCP](https://img.shields.io/badge/MCP-1f6feb?style=for-the-badge&logo=modelcontextprotocol&logoColor=white) ![Agent Skills](https://img.shields.io/badge/Agent_Skills-1f6feb?style=for-the-badge) ![Custom Instructions](https://img.shields.io/badge/Custom_Instructions-1f6feb?style=for-the-badge) ![AGENTS.md](https://img.shields.io/badge/AGENTS.md-1f6feb?style=for-the-badge) ![Knowledge Base](https://img.shields.io/badge/Knowledge_Base-1f6feb?style=for-the-badge) ![Progressive Disclosure](https://img.shields.io/badge/Progressive_Disclosure-1f6feb?style=for-the-badge)

**Multi-agent workflow**

![Subagents](https://img.shields.io/badge/Subagents-0e8a6a?style=for-the-badge) ![Independent Reviewer](https://img.shields.io/badge/Independent_Reviewer-0e8a6a?style=for-the-badge) ![Plan Approval](https://img.shields.io/badge/Plan_Approval-0e8a6a?style=for-the-badge) ![Map-Reduce Tasks](https://img.shields.io/badge/Map--Reduce_Tasks-0e8a6a?style=for-the-badge) ![Autonomous Runs](https://img.shields.io/badge/Autonomous_Runs-0e8a6a?style=for-the-badge)

**Evals and verification**

![Evals](https://img.shields.io/badge/Evals-b08800?style=for-the-badge) ![Acceptance Checks](https://img.shields.io/badge/Acceptance_Checks-b08800?style=for-the-badge) ![Simulation Runs](https://img.shields.io/badge/Simulation_Runs-b08800?style=for-the-badge) ![Golden Baselines](https://img.shields.io/badge/Golden_Baselines-b08800?style=for-the-badge)

### Data engineering

**Languages**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![SQL](https://img.shields.io/badge/SQL-2f302e?style=for-the-badge&logoColor=white) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)

**Data processing and lakehouse**

![Apache Spark](https://img.shields.io/badge/Spark-2f302e?style=for-the-badge&logo=apachespark&logoColor=red) ![Databricks](https://img.shields.io/badge/databricks-fdad0d?style=for-the-badge&logo=databricks&logoColor=white) ![Delta Lake](https://img.shields.io/badge/delta_lake-FDEE21?style=for-the-badge&logo=databricks&logoColor=red) ![Apache Kafka](https://img.shields.io/badge/Kafka-000?style=for-the-badge&logo=apachekafka) ![Structured Streaming](https://img.shields.io/badge/spark-structured_streaming-red?style=for-the-badge&logo=apachespark&logoColor=red) ![ClickHouse](https://img.shields.io/badge/ClickHouse-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=white)

**Orchestration, quality and governance**

![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white) ![Azure Data Factory](https://img.shields.io/badge/azure_data_factory-017CEE?style=for-the-badge) ![Delta Live Tables](https://img.shields.io/badge/delta_live_tables-red?style=for-the-badge) ![Unity Catalog](https://img.shields.io/badge/unity_catalog-red?style=for-the-badge) ![Dimensional Modelling](https://img.shields.io/badge/dimensional_modelling-07b483?style=for-the-badge) ![Lakehouse Architecture](https://img.shields.io/badge/lakehouse_architecture-07b483?style=for-the-badge)

**Cloud and DevOps**

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-0d0435?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%23181717.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## Certificates

<a href="https://api.accredible.com/v1/frontend/credential_website_embed_image/certificate/154927293"><img alt="Databricks Certified Data Engineer Associate" src="https://github.com/user-attachments/assets/40e58694-cf95-41e1-954d-e2b4b741db31" width="12%"/></a>
<a href="https://learn.microsoft.com/zh-cn/users/smarshu-4262/credentials/cff5977467245b87"><img alt="Microsoft Certified: Fabric Data Engineer Associate" src="https://github.com/user-attachments/assets/a9e376ec-9521-4b05-8539-bfb53d72f66c" width="18%"/></a>

## Find me

<a href="https://www.linkedin.com/in/smars-hu/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="https://x.com/SmarsBHu"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X"/></a>
<a href="https://www.smarshu.com/"><img src="https://img.shields.io/badge/smarshu.com-222222?style=for-the-badge" alt="Website"/></a>
<a href="https://cal.com/smars-hu"><img src="https://img.shields.io/badge/book_a_meeting-292929?style=for-the-badge&logo=caldotcom&logoColor=white" alt="Book a meeting"/></a>
