# -*- coding: utf-8 -*-
import logging
import asyncio
from cbpi.api import *


@parameters(
    [
        Property.Text(label="Topic", configurable=True,
                      description="MQTT Topic"),
        Property.Text(
            label="Payload",
            configurable=True,
            description="Payload that is sent as MQTT message. Defaults to \"PRESS\""
        )
    ])
class MQTTButton(CBPiActor):
    def __init__(self, cbpi, id, props):
        super(MQTTButton, self).__init__(cbpi, id, props)

    async def on_start(self):
        self.topic = self.props.get("Topic", None)
        self.payload = self.props.get("Payload", "PRESS")

    async def on(self, power=None):
        await self.cbpi.satellite.publish(
            self.topic, self.payload, False
        )
        self.state = True

    async def off(self):
        self.state = False

    async def run(self):
        while self.running:
            if self.state:
                await self.cbpi.actor.off(self.id)
            await asyncio.sleep(1)

    def get_state(self):
        return self.state
    

def setup(cbpi):
    if str(cbpi.static_config.get("mqtt", False)).lower() == "true":
        cbpi.plugin.register("MQTTButton", MQTTButton)
