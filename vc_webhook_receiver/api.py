from fastapi import APIRouter, HTTPException, Request
import config
from discord_interactions import verify_key as webhook_verify
from webhook_class import WebhookPost
from time import time

router = APIRouter()

@router.post("/webhook")
async def Webhook_post(request: Request, webhook: WebhookPost):
    print(request.headers)
    request_signature = request.headers['X-Signature-Ed25519']
    request_timestamp = request.headers['X-Signature-Timestamp']
    request_body = await request.body()

    if not webhook_verify(request_body, request_signature, request_timestamp, config.VirtualCrypto.PUBLIC_KEY):
        raise HTTPException(401, "Bad request signature")

    time_diff = time() - float(request_timestamp)
    timestamp_error = abs(time_diff) > 15
    
    if timestamp_error:
        raise HTTPException(401, f"Your watch is broken ({int(time_diff)})")

    if webhook.type == 1: # PING
        return {"type":1} # PONG
