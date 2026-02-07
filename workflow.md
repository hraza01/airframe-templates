## Airframe (Advanced) | An Airflow DAG Template

### Overview

This DAG template follows **Airflow best practices** with a modular, scalable, and maintainable architecture.
Designed as a foundation for production-ready data pipelines that can be easily customized and extended.

---

### Design Highlights

- ✨ **TaskFlow API** for clean, Pythonic task definitions with automatic XCom handling
- 🎯 **Orchestration-first** - Airflow triggers external services (APIs, BigQuery) rather than processing data
- 🔧 **Environment-based config** - YAML configs for dev/prod via `WOP_STAGE` env variable
- 🧩 **Separation of concerns**: Configuration, logic, and orchestration are decoupled
- 📝 **Template SQL** - Version-controlled queries in `/sql` directory
- 🏗️ **Modular architecture** - Reusable task definitions outside DAG context

### Workflow

```
call_external_api → sql_task → templated_sql_task
```

---

**Repository:** [Git Repository](<Your Git Repository Link>)
