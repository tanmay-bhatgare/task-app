import httpx


async def delete_task(
    url: str,
    token: str,
    task_id: int,
):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                url=f"{url}/{task_id}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
            )
            if response.status_code == 204:
                return True
            else:
                print(f"Failed to delete task: {response.status_code} {response.text}")
                return False
    except httpx.HTTPStatusError as e:
        print(e)
        return False
    except Exception as e:
        print(e)
        return False
