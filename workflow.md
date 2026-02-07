## Airframe (Starter) | An Airflow DAG Template

### Overview

This DAG template follows **Airflow best practices** with a modular, scalable, and maintainable architecture.
Designed as a foundation for production-ready data pipelines that can be easily customized and extended.

---

### Design Highlights

- 🎯 **Orchestration-first** - Airflow triggers BigQuery jobs
- 🔧 **Environment-based config** - YAML configs for dev/prod via `WOP_STAGE` env variable
- 🧩 **Separation of concerns**: Configuration, logic, and orchestration are decoupled
- 📝 **Template SQL** - Version-controlled queries in `/sql` directory

### Workflow

```
first_sql_task → second_sql_task
```

---

**Repository:** [Git Repository](<Your Git Repository Link>)
