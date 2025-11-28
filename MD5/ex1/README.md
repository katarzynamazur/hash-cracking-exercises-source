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
docker run -d -p 4001:4001 --name md5-crack ghcr.io/katarzynamazur/md5-crack-ex1:latest
```

The API will be available at: **http://localhost:4001**

---

## 📚 Exercise Instructions

### Step 1: Get the Hash

Request a new hash challenge:

```bash
curl http://localhost:4001/hash
```

**Response:**
```json
{
  "hash": "5f4dcc3b5aa765d61d8327deb882cf99",
  "message": "Try to crack this hash!"
}
```

### Step 2: Crack the Hash

> 💡 **HINT**: The password is one of the **most common passwords** used worldwide!

### Step 3: Submit Your Answer

```bash
curl -X POST http://localhost:4001/submit \
  -H "Content-Type: application/json" \
  -d '{"word":"password"}'
```

**Success Response:**
```json
{
  "success": true,
  "message": "Congratulations! Hash cracked!",
  "word": "password",
  "hash": "5f4dcc3b5aa765d61d8327deb882cf99"
}
```

## 📖 Further Reading

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [MD5 Collision Attacks](https://en.wikipedia.org/wiki/MD5#Security)
- [Hashcat Documentation](https://hashcat.net/wiki/)
- [John the Ripper Guide](https://www.openwall.com/john/doc/)
- [Common Password Lists](https://github.com/danielmiessler/SecLists)

---
