# Contributing

Keep changes small, reproducible, and focused on one concern. Do not commit competition data, generated models, credentials, or notebook checkpoints.

Before opening a pull request:

```bash
pip install -r requirements-dev.txt
python -m compileall -q app2.py tests
pytest -q
```

For experiment changes, document the data split, random seed, metric, and comparison baseline. Clear unnecessary notebook output while retaining concise tables or plots that support a stated conclusion.
