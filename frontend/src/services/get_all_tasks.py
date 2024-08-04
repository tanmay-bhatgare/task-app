from typing import Dict, NoReturn
import httpx

from src.constants.constants import Url


async def get_all_tasks(token: str) -> Dict | NoReturn:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=f"{Url.task_base_url}/",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
            )
            if response.status_code == 200:
                tasks = response.json()
                return tasks
            else:
                print(f"Failed to fetch tasks: {response.status_code} {response.text}")
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
