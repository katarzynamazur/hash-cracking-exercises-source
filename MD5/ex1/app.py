import hashlib
import random
import re

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# Global state
current_word = None


# Wordlist management
def load_wordlist():
    """Load words from wordlist.txt with fallback"""
    try:
        with open("wordlist.txt", "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        return words if words else get_fallback_words()
    except FileNotFoundError:
        return get_fallback_words()


def get_fallback_words():
    """Default wordlist if file not found"""
    return [
        "python",
        "flask",
        "security",
        "hash",
        "password",
        "admin",
        "letmein",
        "welcome",
        "qwerty",
        "crypto",
    ]


def get_md5_hash(text):
    """Generate MD5 hash"""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def validate_word(word):
    """Validate and sanitize input word"""
    if not word or not isinstance(word, str):
        return None
    word = word.strip()
    if not word or len(word) > 100:
        return None
    if not re.match(r"^[\w\-\.]+$", word, re.UNICODE):
        return None
    return word


# API Endpoints
@app.route("/hash", methods=["GET"])
def hash_endpoint():
    """Generate new hash challenge"""
    global current_word
    try:
        wordlist = load_wordlist()
        current_word = random.choice(wordlist)
        hash_value = get_md5_hash(current_word)

        return jsonify({"hash": hash_value, "message": "Try to crack this hash!"})
    except Exception as e:
        app.logger.error(f"Hash generation error: {e}")
        return jsonify({"error": "Failed to generate hash"}), 500


@app.route("/submit", methods=["POST"])
def submit_endpoint():
    """Verify submitted word"""
    global current_word

    if current_word is None:
        return (
            jsonify(
                {"success": False, "message": "Get a hash first from /hash endpoint"}
            ),
            400,
        )

    # Extract word from request
    submitted_word = None
    if request.is_json:
        try:
            data = request.get_json(force=True)
            submitted_word = data.get("word", "")
        except:
            return jsonify({"success": False, "message": "Invalid JSON format"}), 400
    else:
        submitted_word = request.form.get("word", "")

    # Validate input
    submitted_word = validate_word(submitted_word)
    if not submitted_word:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Invalid word format (1-100 chars, alphanumeric only)",
                }
            ),
            400,
        )

    # Check if correct
    if submitted_word == current_word:
        return jsonify(
            {
                "success": True,
                "message": "Congratulations! Hash cracked!",
                "word": current_word,
                "hash": get_md5_hash(current_word),
            }
        )
    else:
        return jsonify({"success": False, "message": "Incorrect word. Try again!"})


@app.route("/openapi.json", methods=["GET"])
def openapi_spec():
    """OpenAPI specification"""
    return jsonify(
        {
            "openapi": "3.0.3",
            "info": {
                "title": "MD5 Crack Playground API",
                "version": "1.0.0",
                "description": "Simple MD5 hash cracking challenge API",
            },
            "paths": {
                "/hash": {
                    "get": {
                        "summary": "Get new hash challenge",
                        "responses": {
                            "200": {
                                "description": "Hash generated successfully",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "object",
                                            "properties": {
                                                "hash": {"type": "string"},
                                                "message": {"type": "string"},
                                            },
                                        }
                                    }
                                },
                            }
                        },
                    }
                },
                "/submit": {
                    "post": {
                        "summary": "Submit word guess",
                        "requestBody": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {"word": {"type": "string"}},
                                        "required": ["word"],
                                    }
                                }
                            }
                        },
                        "responses": {
                            "200": {
                                "description": "Verification result",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "object",
                                            "properties": {
                                                "success": {"type": "boolean"},
                                                "message": {"type": "string"},
                                            },
                                        }
                                    }
                                },
                            }
                        },
                    }
                },
            },
        }
    )


@app.route("/docs", methods=["GET"])
def docs():
    """API documentation with Swagger UI"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>API Documentation - MD5 Crack Playground</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script>
        SwaggerUIBundle({
            url: '/openapi.json',
            dom_id: '#swagger-ui',
            deepLinking: true,
            presets: [SwaggerUIBundle.presets.apis]
        });
    </script>
</body>
</html>"""


@app.route("/", methods=["GET"])
def index():
    """Homepage with modern minimalistic design"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MD5 Crack Playground</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #0f0f0f;
            color: #e0e0e0;
            line-height: 1.6;
            padding: 2rem;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem 0;
        }
        
        h1 {
            font-size: 2.5rem;
            font-weight: 700;
            color: #fff;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }
        
        .subtitle {
            color: #888;
            font-size: 1rem;
            margin-bottom: 2rem;
        }
        
        .btn {
            display: inline-block;
            padding: 0.75rem 2rem;
            background: #fff;
            color: #000;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            transition: all 0.2s;
        }
        
        .btn:hover {
            background: #e0e0e0;
            transform: translateY(-1px);
        }
        
        .main-layout {
            display: grid;
            grid-template-columns: 1fr 400px;
            gap: 2rem;
        }
        
        .left-panel {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }
        
        .right-panel {
            position: sticky;
            top: 2rem;
            height: fit-content;
        }
        
        .card {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 8px;
            padding: 2rem;
        }
        
        h2 {
            font-size: 1.25rem;
            color: #fff;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }
        
        .endpoint {
            display: flex;
            align-items: center;
            padding: 1rem;
            background: #0f0f0f;
            border-radius: 6px;
            margin-bottom: 0.75rem;
            border: 1px solid #2a2a2a;
        }
        
        .method {
            padding: 0.25rem 0.75rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
            margin-right: 1rem;
            min-width: 60px;
            text-align: center;
        }
        
        .method-get {
            background: #1a4d2e;
            color: #4ade80;
        }
        
        .method-post {
            background: #1e3a5f;
            color: #60a5fa;
        }
        
        .path {
            font-family: 'Courier New', monospace;
            color: #e0e0e0;
            font-size: 0.9rem;
            flex: 1;
        }
        
        .path a {
            color: #60a5fa;
            text-decoration: none;
            transition: color 0.2s;
        }
        
        .path a:hover {
            color: #93c5fd;
            text-decoration: underline;
        }
        
        .desc {
            color: #888;
            font-size: 0.875rem;
            margin-top: 0.5rem;
        }
        
        .info-text {
            color: #888;
            font-size: 0.95rem;
            line-height: 1.8;
        }
        
        .code-block {
            background: #0a0a0a;
            border: 1px solid #2a2a2a;
            border-radius: 6px;
            padding: 1rem;
            margin-top: 1rem;
            overflow-x: auto;
        }
        
        code {
            font-family: 'Courier New', monospace;
            color: #4ade80;
            font-size: 0.875rem;
        }
        
        .badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: #2a2a2a;
            border-radius: 4px;
            font-size: 0.8rem;
            margin: 0.25rem;
            color: #888;
        }
        
        @media (max-width: 768px) {
            body {
                padding: 1rem;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            .main-layout {
                grid-template-columns: 1fr;
            }
            
            .right-panel {
                position: static;
            }
            
            .endpoint {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .method {
                margin-bottom: 0.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>MD5 Crack Playground</h1>
            <a href="/docs" class="btn">API Documentation</a>
        </header>
        
        <div class="main-layout">
            <div class="left-panel">
                <div class="card">
                    <h2>How It Works</h2>
                    <p class="info-text">
                        The server randomly selects a word and generates its MD5 hash. 
                        Your challenge is to crack the hash using techniques like dictionary 
                        attacks, brute force, or tools such as <strong>hashcat</strong> 
                        or <strong>john</strong>.
                    </p>
                    <div class="code-block">
                        <code># Example usage<br>
curl http://localhost:4001/hash<br>
curl -X POST http://localhost:4001/submit -H "Content-Type: application/json" -d '{"word":"python"}'
                        </code>
                    </div>
                </div>
                
                <div class="card">
                    <h2>Quick Start</h2>
                    <p class="info-text">
                        1. Request a hash from <code>/hash</code><br>
                        2. Use your favorite cracking tool or script<br>
                        3. Submit your guess to <code>/submit</code><br>
                        4. Verify if you cracked it successfully
                    </p>
                </div>
            </div>
            
            <div class="right-panel">
                <div class="card">
                    <h2>Available Endpoints</h2>
                    
                    <div class="endpoint">
                        <span class="method method-get">GET</span>
                        <div>
                            <div class="path"><a href="/hash">/hash</a></div>
                            <div class="desc">Generate new hash challenge</div>
                        </div>
                    </div>
                    
                    <div class="endpoint">
                        <span class="method method-post">POST</span>
                        <div>
                            <div class="path">/submit</div>
                            <div class="desc">Submit word guess for verification</div>
                        </div>
                    </div>
                    
                    <div class="endpoint">
                        <span class="method method-get">GET</span>
                        <div>
                            <div class="path"><a href="/docs">/docs</a></div>
                            <div class="desc">Interactive API documentation</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4001)
