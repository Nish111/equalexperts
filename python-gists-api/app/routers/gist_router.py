from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()


@router.get("/{username}")
async def get_gists(username: str):
    async with httpx.AsyncClient() as client:
        url = f"https://api.github.com/users/{username}/gists"
        headers = {"Accept": "application/vnd.github+json"}
        response = await client.get(url, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="GitHub user not found")

        gists_data = response.json()
        simplified_gists = [
            {
                "id": gist["id"],
                "description": gist["description"],
                "url": gist["html_url"],
                "files": list(gist["files"].keys())
            }
            for gist in gists_data
        ]
        return simplified_gists