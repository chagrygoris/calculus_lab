

def f_paraboloid(x, y):
    return - (x - 5)**2 - (y - 2)**2

def go_surface_plot_arrows(descent_pts, f=f_paraboloid, save_html=False):
    ''' 
        Go vegan, plot arrows
    '''
    import plotly.graph_objects as go
    import numpy as np
    # Create a grid of x and y values
    x = np.linspace(-7, 17, 100)
    y = np.linspace(-10, 14, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # Define arrow data: list of (start, end) points and direction vectors
    arrows = [
        # Arrow from (3, 0, -10) to (5, 2, 0) (points to max at (5, 2, 0))
        {
            'start': [3, 0, -10],
            'end': [5, 2, 0],
        },
        # Arrow from (7, 4, -10) to (5, 2, 0)
        {
            'start': [7, 4, -10],
            'end': [5, 2, 0],
        }
    ]

    arrows = []
    for i in range(1, len(descent_pts)):
        arrows.append({
            'start': descent_pts[i-1],
            'end': descent_pts[i] + np.array([-0.5, -0.5, 0.5])
        })

    # Create traces for arrows (shafts and heads)
    arrow_traces = []
    for arrow in arrows:
        start = arrow['start']
        end = arrow['end']
        # Direction vector (u, v, w) for the cone
        u = [end[0] - start[0]]
        v = [end[1] - start[1]]
        w = [end[2] - start[2]]

        # Arrow shaft (line)
        shaft = go.Scatter3d(
            x=[start[0], end[0]],
            y=[start[1], end[1]],
            z=[start[2], end[2]],
            mode='lines',
            line=dict(color='red', width=4),
            showlegend=False
            # name='Arrow shaft'
        )
        
        # Arrowhead (cone)
        head = go.Cone(
            x=[end[0]],  # Cone base at arrow end
            y=[end[1]],
            z=[end[2]],
            u=u,  # Direction vector
            v=v,
            w=w,
            sizemode='scaled',
            sizeref=0.3,  # Size of cone
            anchor='tip',  # Cone tip at end point
            colorscale=[[0, 'red'], [1, 'red']],
            showscale=False,
            name='Arrowhead',
            showlegend=False
        )
        
        arrow_traces.extend([shaft, head])

    # Create the figure with surface and arrows
    fig = go.Figure(data=[
        go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', name='Surface')
    ] + arrow_traces)

    # Update layout
    fig.update_layout(
        title='Градиентный спуск (подъем) к локальному максимуму',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='f(x, y)',
            aspectratio=dict(x=1, y=1, z=0.5),
            camera=dict(
                eye=dict(x=-0.7, y=-0.4, z=0.5),  # Camera position
                center=dict(x=0, y=0, z=0),      # Look-at point
                up=dict(x=0, y=0, z=1)
            )
        ),
        autosize=False,
        width=800,
        height=600
    )

    if save_html:
        # # Save as HTML
        fig.write_html('../surface_with_arrows.html')
        print("Plot saved as 'surface_with_arrows.html'. Open it in a web browser.")
    return fig