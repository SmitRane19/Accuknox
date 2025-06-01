# Accuknox
# 🔧 Django Signals: Execution Behavior Explained

This repository explores how Django signals behave with respect to:

1. Synchronous vs Asynchronous execution  
2. Threading  
3. Database transactions  

---

## ✅ Q1: Are Django signals synchronous?

**✔️ Answer:** Yes

**💡 Proof:**
- The view does not return until the signal finishes its 5-second `sleep`.
- The delay is visible in the browser response time.

---

## ✅ Q2: Do Django signals run in the same thread?

**✔️ Answer:** Yes

**💡 Proof:**
- `threading.get_ident()` inside the view and signal show the same thread ID.
- This confirms both run in the same thread.


---

## ✅ Q3: Do Django signals run in the same database transaction?

**✔️ Answer:** Yes

**💡 Proof:**
- We printed `transaction.get_connection().in_atomic_block` inside the signal.
- It returned `True`, showing it's part of the same transaction.

---

## 🔎 Summary

| Question          | Answer  | Confirmed By |
|-------------------|---------|---------------|
| Synchronous?      | ✅ Yes | View delay via sleep |
| Same Thread?      | ✅ Yes | `threading.get_ident()` match |
| Same Transaction? | ✅ Yes | `in_atomic_block = True` |

---
