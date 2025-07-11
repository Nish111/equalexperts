# GitHub Gists API - Python (FastAPI)

## Setup Instructions

### Prerequisites
- Python 3.11+
- Docker

### Install & Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker

```bash
docker build -t python-gists-api .
docker run -p 8080:8080 python-gists-api
```

### Test

```bash
pytest tests/
```

### API Usage
```
GET /{username}
Example: http://localhost:8080/octocat
```

### Response Format
```json
[
  {
    "id": "a1b2c3d4e5",
    "description": "Example Gist",
    "url": "https://gist.github.com/octocat/a1b2c3d4e5",
    "files": ["file1.txt", "file2.py"]
  },
  ...
]
```