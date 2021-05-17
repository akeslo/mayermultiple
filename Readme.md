# Summary
A custom component to display the [BTC Mayer Multiple ](https://mayermultiple.info/)

# Installation
This can be installed by copying all the files from custom_components/mayermultiple/ to <config directory>/custom_components/mayermultiple/.

# Configuration
Add the following to *configuration.yaml*

    # Example configuration.yaml entry
    mayermultiple:

The above configuration will generate an entity with the id sensor.mayer_multiple_btc and current value as the state along with these attributes:

    percentage_time_higer: The percentage of the time the mayer multiple has historically been higher than today's value
    btc_price: The current btc price
    average_multiple: The average mayer multiple since creation of bitcoin
