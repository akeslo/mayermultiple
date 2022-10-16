"""Platform for sensor integration."""
import requests
from datetime import datetime, date, timedelta
from homeassistant.helpers.entity import Entity


ATTR_HIGHER_PERCENTAGE = "percentage_time_higer"
ATTR_BTC_PRICE = "btc_price"
ATTR_AVERAGE_MULTIPLE = "average_multiple"

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([mayerMultiple()])


class mayerMultiple(Entity):

    """Representation of a Sensor."""


    def __init__(self):
        """Initialize the sensor."""
        self._state = None
        self._percentageTimeHigher = None
        self._btcPrice = None
        self._averageMayerMultiple = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Mayer Multiple (BTC)'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return the state of the sensor."""
        return "mdi:currency-btc"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return ""

    @property
    def extra_state_attributes(self):
        return { ATTR_HIGHER_PERCENTAGE: self._percentageTimeHigher, ATTR_BTC_PRICE:self._btcPrice , ATTR_AVERAGE_MULTIPLE: self._averageMayerMultiple }

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        url = ("https://bitcoinition.com/current.json")
        # sending get request
        r = requests.get(url=url)
        # extracting response json
        self._state = r.json()["data"]["current_mayer_multiple"]
        self._percentageTimeHigher = r.json()["data"]["percentage_time_higher"]
        self._btcPrice = r.json()["data"]["btc_price"]
        self._averageMayerMultiple = r.json()["data"]["average_mayer_multiple"]
