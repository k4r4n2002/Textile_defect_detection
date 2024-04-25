import json
import base64
import logging
from datetime import datetime

from flask_socketio import emit
from flask import request

logger = logging.getLogger(__name__)

def register_events(socketio):
    @socketio.on('connect', namespace='/stream')
    def handle_connect():
        logger.info(f"Client connected: {request.sid}")

    @socketio.on('disconnect', namespace='/stream')
    def handle_disconnect():
        logger.info(f"Client disconnected: {request.sid}")

    @socketio.on('detect', namespace='/stream')
    def detect(data):
        logger.debug(data)
        image = data['image']
        logger.debug(image)
        # raw_image = base64.b64decode(image)


        logger.info(f"Detection from: {request.sid}")

        emit('output', {
            "image": image,
            "from": data['from']
        }, room=request.sid)