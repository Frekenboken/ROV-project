import plotly.graph_objs as go
import numpy as np


def get_value(x, y):
    if x > 0 and y > 0:
        if abs(x) > abs(y):
            return x - y  # "Первый октант"
        else:
            return y - x  # "Второй октант"
    elif x < 0 and y > 0:
        if not (abs(x) < abs(y)):
            return 2 ** 0.5 * y  # "Четвертый октант"
    elif x < 0 and y < 0:
        if abs(x) > abs(y):
            return 0  # "Пятый октант"
        else:
            return 0  # "Шестой октант"
    elif x > 0 and y < 0:
        if abs(x) < abs(y):
            return 2 ** 0.5 * x  # "Седьмой октант"
    elif x == 0 and y == 0:
        return 0
    elif x == 0 and y < 0:
        return 0
    elif y == 0 and x < 0:
        return 0
    return (x ** 2 + y ** 2) ** 0.5


# Создаём список для хранения данных точек
scatter_data = []

for x in range(-100, 105, 5):
    for y in range(-100, 105, 5):
        z = get_value(x, y)
        print(x, y, z)
        # Отображаем точки
        scatter_data.append(go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode='markers',
            marker=dict(
                size=5,
                color='red',
                symbol='circle',
                line=dict(
                    color='rgb(204, 204, 204)',
                    width=1
                ),
                opacity=0.8
            )
        ))


# Создаём график
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=scatter_data, layout=layout)

# Показываем график
fig.show()

