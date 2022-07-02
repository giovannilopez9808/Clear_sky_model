from Modules.clear_sky import clear_sky_model
import matplotlib.pyplot as plt

params = {
    "clear sky models": [
        "GHI",
        "RS",
    ],
    "longitude": -100.255,
    "latitude": 25.750,
    "timezone": -6,
    "date": "2012-03-02",
    "hour initial": 7,
    "hour final": 20,
}

model = clear_sky_model()
for model_name in params["clear sky models"]:
    params["clear sky model"] = model_name
    results = model.run(params)
    plt.plot(results,
             label=model_name)
plt.legend(ncol=len(params["clear sky models"]),
           frameon=False)
plt.show()
