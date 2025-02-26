from fastapi import FastAPI, APIRouter, Depends
import handlers.linux
from utils import validate_os  # Your existing OS validation
import handlers

app = FastAPI(title="SPWNPT Dev Environment", version="0.1.0")

def os_specific_router(os_name: str):
    """Create router with OS-specific prefix and validation"""
    return APIRouter(
        prefix=f"/{os_name}",
        tags=[os_name.capitalize()],
        dependencies=[Depends(validate_os)]  # Ensures route only works on correct OS
    )

# Create OS-specific routers
linux_router = os_specific_router("linux")
# mac_router = os_specific_router("mac")
# windows_router = os_specific_router("windows")

@app.get("/linux/fullstack", summary="Initialize Linux fullstack")
async def linux_fullstack_fullstack():
    return handlers.linux.handle_fullstack()

@linux_router.post("/linux/frontend", summary="Initialize Linux fullstack")
async def linux_fullstack_fullstack():
    return handlers.linux.handle_frontend()

@linux_router.post("/linux/backend", summary="Initialize Linux fullstack")
async def linux_fullstack_fullstack():
    return handlers.linux.handle_backend()

# @mac_router.post("/init", summary="Initialize macOS fullstack")
# async def mac_fullstack_init():
#     return handle_fullstack()  # Add macOS-specific logic as needed

# @windows_router.post("/init", summary="Initialize Windows fullstack")
# async def windows_fullstack_init():
#     return handle_fullstack()  # Add Windows-specific logic as needed
