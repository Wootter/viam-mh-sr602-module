"""
This file registers the model with the Python SDK.
"""

from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .MH_SR602 import MH_SR602

Registry.register_resource_creator(Sensor.API, MH_SR602.MODEL, ResourceCreatorRegistration(MH_SR602.new, MH_SR602.validate))