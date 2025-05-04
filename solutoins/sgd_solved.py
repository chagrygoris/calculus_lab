import numpy as np

def grad_descent_for_paraboloid(initial_state, learning_rate, eps, N, f, grad):
    ''' 
    Parameters:
    initial_state : numpy.ndarray
        Initial (x, y) coordinates as a 1D array of shape (2,). Represents the
        starting point for gradient descent.
    learning_rate : float
        Learning rate controlling the step size of each iteration. Must be positive.
    eps : float
        Convergence threshold. Iteration stops when the Euclidean norm of the
        position update is less than eps. Must be positive.
    N   :  integer
        Stop if the algorithm does not converge in N iteratons
    f : callable
        The objective function to minimize. Must take a numpy.ndarray of shape (2,)
        as input and return a float. 
    grad : callable
        The gradient function of `f`. Must take a numpy.ndarray of shape (2,) as
        input and return a numpy.ndarray of shape (2,) representing the gradient
        at that point.
    Outputs:
        final_state: minima, found by algorithm,
        descent_pts: (x, y, z) coordinates of visited points

    '''
    import numpy as np
    points = []

    previous_state = np.array((np.inf, np.inf))
    current_state = initial_state
    counter = 0
    while np.linalg.norm(current_state - previous_state) > eps and counter < N:
        counter += 1
        points.append((current_state[0], current_state[1], f(*current_state)))
        current_state, previous_state = current_state + learning_rate * grad(current_state), current_state
    return current_state, points



def randomize(compute_grad):
    ''' 
        Decorator to add some random noise to our gradient
        input: 
            function that computers real gradient
        output:
            function that computes gradient with some noise
        
        Важно: значение "шума" по каждой координате должно быть разным
        Подсказка: можно пользоваться функциями из модуля np.random
    '''
    def randomized(x):
        return np.random.rand(2) * compute_grad(x)
    return randomized


def compute_gradient_paraboloid(x:np.typing.ArrayLike):
    return np.array([-2 * x[0] + 10, -2 * x[1] + 4])