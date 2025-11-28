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
docker run -d -p 4002:4002 --name md5-crack ghcr.io/katarzynamazur/md5-crack-ex2:latest
```

The API will be available at: **http://localhost:4002**

---

## 📚 Exercise Instructions

### Step 1: Get the Hash

Request a new hash challenge:

```bash
curl http://localhost:4002/hash
```

**Response:**
```json
{
  "hash": "76a2173be6393254e72ffa4d6df1030a",
  "message": "Try to crack this hash!"
}
```

### Step 2: Crack the Hash

> 💡 **HINT**: The correct password is hidden somewhere among all 4-letter lowercase combinations.

### Step 3: Submit Your Answer

```bash
curl -X POST http://localhost:4002/submit \
  -H "Content-Type: application/json" \
  -d '{"word":"passwd"}'
```

**Success Response:**
```json
{
  "success": true,
  "message": "Congratulations! Hash cracked!",
  "word": "passwd",
  "hash": "76a2173be6393254e72ffa4d6df1030a"
}
```

## 📖 Further Reading

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [MD5 Collision Attacks](https://en.wikipedia.org/wiki/MD5#Security)
- [Hashcat Documentation](https://hashcat.net/wiki/)
- [John the Ripper Guide](https://www.openwall.com/john/doc/)
- [Common Password Lists](https://github.com/danielmiessler/SecLists)

---
