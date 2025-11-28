# 🔐 MD5 Crack Playground

A hands-on Flask-based API that teaches hash cracking fundamentals through interactive exercises. Students learn to crack MD5 hashes using various techniques and tools.

---

## 🎯 Learning Objectives

By completing this exercise, you will learn:

- ✅ Dictionary attack techniques
- ✅ Using tools like `hashcat`, `john`, and `curl`
- ✅ REST API interaction and JSON handling
- ✅ Bash scripting for automation
- ✅ Why weak passwords are dangerous

---

## 🚀 Quick Start

### Run with Docker

```bash 
docker run -d -p 4003:4003 --name md5-crack ghcr.io/katarzynamazur/md5-crack-ex3:latest
```

The API will be available at: **http://localhost:4003**

---

## 📚 Exercise Instructions

### Step 1: Get the Hash

Request a new hash challenge:

```bash
curl http://localhost:4003/hash
```

**Response:**
```json
{
  "hash": "202cb962ac59075b964b07152d234b70",
  "message": "Try to crack this hash!"
}
```

### Step 2: Crack the Hash

> 💡 **HINT**: Think of a short, 3‑digit numeric code - nothing more, nothing less..

### Step 3: Submit Your Answer

```bash
curl -X POST http://localhost:4003/submit \
  -H "Content-Type: application/json" \
  -d '{"word":"123"}'
```

**Success Response:**
```json
{
  "success": true,
  "message": "Congratulations! Hash cracked!",
  "word": "123",
  "hash": "202cb962ac59075b964b07152d234b70"
}
```

## 📖 Further Reading

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [MD5 Collision Attacks](https://en.wikipedia.org/wiki/MD5#Security)
- [Hashcat Documentation](https://hashcat.net/wiki/)
- [John the Ripper Guide](https://www.openwall.com/john/doc/)
- [Common Password Lists](https://github.com/danielmiessler/SecLists)

---
