import plotly.express as px
import numpy as np

df = {
    "x": np.random.rand(50),
    "y": np.random.rand(50),
    "z": np.random.rand(50),
    "color": np.random.randint(0, 10, 50)
}

fig = px.scatter_3d(df, x="x", y="y", z="z", color="color", title="3D Scatter Plot Example")
fig.show()