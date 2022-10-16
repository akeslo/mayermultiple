# Summary
A custom component to display the [BTC Mayer Multiple ](https://mayermultiple.info/)

# Installation
This can be installed via HACS or by copying all the files from custom_components/mayermultiple/ to <config directory>/custom_components/mayermultiple/.

# Configuration
Add the following to *configuration.yaml*

    # Example configuration.yaml entry
    mayermultiple:

The above configuration will generate an entity with the id sensor.mayer_multiple_btc and current value as the state along with these attributes:

    percentage_time_higer: The percentage of the time the mayer multiple has historically been higher than today's value
    btc_price: The current btc price
    average_multiple: The average mayer multiple since creation of bitcoin

# Example Use
*The below is using mini-graph-card*

![image](https://user-images.githubusercontent.com/3003773/118531771-31f06880-b714-11eb-9e39-376dbef2690f.png)
