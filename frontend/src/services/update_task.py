import httpx
from src.models.models import TaskUpdateModel


async def update_task(
    url: str,
    task_id: int,
    token: str,
    json_data: TaskUpdateModel,
) -> bool:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(
                url=f"{url}/{task_id}",
                json=json_data.model_dump(),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
            )
            if response.status_code == 200:
                return True
            else:
                print(f"Error updating task: {response.text}")
                return False
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
