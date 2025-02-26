from fastapi import FastAPI, APIRouter, Depends
import handlers.linux
import handlers.macos
import handlers.windows

app = FastAPI(title="SPWNPT Dev Environment", version="0.1.0")

def os_specific_router(os_name: str):
    """Create router with OS-specific prefix and validation"""
    return APIRouter(
        prefix=f"/{os_name}",
        tags=[os_name.capitalize()],
    )

# Create OS-specific routers
linux_router = os_specific_router("linux")
# mac_router = os_specific_router("mac")
# windows_router = os_specific_router("windows")

#! Linux routes
@app.get("/linux/fullstack", summary="Initialize Linux fullstack")
async def linux_fullstack():
    return handlers.linux.handle_fullstack()

@linux_router.post("/linux/frontend", summary="Initialize Linux fullstack")
async def linux_frontend():
    return handlers.linux.handle_frontend()

@linux_router.post("/linux/backend", summary="Initialize Linux fullstack")
async def linux_backend():
    return handlers.linux.handle_backend()

# #! Mac routes
# @linux_router.post("/macos/backend", summary="Initialize Linux fullstack")
# async def macos_fullstack():
#     return handlers.macos.handle_backend()
# @linux_router.post("/macos/backend", summary="Initialize Linux fullstack")
# async def macos_frontend():
#     return handlers.macos.handle_backend()
# @linux_router.post("/macos/backend", summary="Initialize Linux fullstack")
# async def macos_backend():
#     return handlers.macos.handle_backend()

# #! Windows routes
# @linux_router.post("/windows/backend", summary="Initialize Linux fullstack")
# async def windows_fullstack():
#     return handlers.linux.handle_backend()
# @linux_router.post("/windows/backend", summary="Initialize Linux fullstack")
# async def windows_frontend():
#     return handlers.linux.handle_backend()
# @linux_router.post("/windows/backend", summary="Initialize Linux fullstack")
# async def windows_frontend():
#     return handlers.linux.handle_backend()
