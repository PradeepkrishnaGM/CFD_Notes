# Discretization

## Spatial Discretization

Spatial discretization involves dividing the spatial domain into discrete elements or volumes to approximate the continuous equations.

### Time Discretization

Time discretization involves breaking the time domain into discrete intervals for numerical simulation.

## Approximation of Integrals

### Approximation of Surface Integrals

Surface integrals can be approximated using various numerical methods such as:
- **Midpoint Rule**
- **Trapezoidal Rule**
- **Simpson's Rule**

### Approximation of Volume Integrals

Volume integrals are typically approximated using:
- **Gaussian Quadrature**
- **Midpoint Rule**
- **Trapezoidal Rule**

## Interpolation Methods

### Upwind Differencing Scheme (UDS)
- **First-order UDS**: 
  $\[ \phi_i = \phi_{i-1} \]$

### Second-order Upwind Differencing Scheme (Second-order UDS)
- **Formula**: 
  $\[ \phi_i = 2\phi_{i-1} - \phi_{i-2} \]$

### Central Differencing Scheme (CDS)
- **Formula**: 
  $\[ \phi_i = \frac{\phi_{i+1} + \phi_{i-1}}{2} \]$

### QUICK Scheme
- **Formula**: 
  $\[ \phi_i = \frac{3}{8}\phi_{i+1} + \frac{6}{8}\phi_i - \frac{1}{8}\phi_{i-1} \]$

### Power Law Interpolation
- **Formula**: 
  $\[ \phi_i = \phi_P + \frac{\phi_E - \phi_P}{\exp(Pe) - 1} \]$

## Boundary Conditions

Boundary conditions specify the values or behavior of the solution at the boundaries of the domain.

### Types of Boundary Conditions

- **Dirichlet Boundary Condition**: Specifies the value of a variable on the boundary.
- **Neumann Boundary Condition**: Specifies the gradient of a variable on the boundary.
- **Mixed Boundary Condition**: Combines Dirichlet and Neumann conditions.

---

Prev :[Fundamentals - Part III](Fundamental_Part01.md)
Next :[Discretization](Discretization.md)
