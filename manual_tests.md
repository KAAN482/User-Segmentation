# Manual Test Scripts (Curl)

These commands test the 3 required scenarios. You can run them in your terminal (PowerShell or Bash).

## 1. Basic Comparison (Numeric)
Tests if `level` is greater than 10.

```bash
curl -X POST http://localhost:3000/evaluate ^
-H "Content-Type: application/json" ^
-d '{
    "user": {"level": 15},
    "segments": {
        "is_high_level": "level > 10"
    }
}'
```

## 2. Case Sensitivity (String equality)
Tests implicit case sensitivity of SQL strings. (Note: SQLite string comparisons are generally case-sensitive unless specified otherwise).

```bash
curl -X POST http://localhost:3000/evaluate ^
-H "Content-Type: application/json" ^
-d '{
    "user": {"country": "Turkey"},
    "segments": {
        "is_turkey": "country = ''Turkey''",
        "is_turkey_lowercase": "country = ''turkey''"
    }
}'
```

## 3. Multiple Conditions (Logical AND/OR)
Tests complex logic with multiple fields.

```bash
curl -X POST http://localhost:3000/evaluate ^
-H "Content-Type: application/json" ^
-d '{
    "user": {"country": "Turkey", "purchase_amount": 12000},
    "segments": {
        "turkish_vip": "country = ''Turkey'' AND purchase_amount >= 10000"
    }
}'
```
