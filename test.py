from Modules.clear_sky import clear_sky_model
import matplotlib.pyplot as plt

params = {
    "longitude": -100.255,
    "latitude": 25.750,
    "timezone": -6,
    "date": "2012-03-02",
    "hour initial": 7,
    "hour final": 20,
}

model = clear_sky_model()
results = model.run(params)
plt.plot(results)
plt.show()
