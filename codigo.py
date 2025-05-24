def f(x):
  return (x**2 - 2)

def fl(x):
  return 2 * x

def newton(xi, epsilon, iterations):
  x = xi

  for i in range(iterations):
    x_newton = x - f(x) / fl(x)

    print(f'x = {x} | f(x) = {f(x)} | fl(x) = {fl(x)} | x_newton = {x_newton}')

    if abs(x_newton - x) < epsilon:
      return x_newton, i

    x = x_newton

  return x, i

x, i = newton(2, 0.00001, 100)
print(f'\nSolução: {x} \nIterações: {i}')
