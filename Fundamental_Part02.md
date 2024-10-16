# Fundamentals Part Two: Partial Differential Equations (PDEs)

## What is a PDE?

A Partial Differential Equation (PDE) involves partial derivatives of a function with respect to multiple variables. PDEs are essential for describing various physical phenomena such as heat, sound, fluid flow, and quantum mechanics.

## Types of PDEs

### Elliptic PDEs
- **Characteristics**: No real characteristics; solutions are smooth and well-behaved.
- **Example**: Laplace's Equation
  - **Formula**: \( \nabla^2 \phi = 0 \)

### Parabolic PDEs
- **Characteristics**: Describes diffusion-like processes; solutions propagate within a limited domain.
- **Example**: Heat Equation
  - **Formula**: \( \frac{\partial u}{\partial t} = \alpha \nabla^2 u \)
    - \( \alpha \) is the thermal diffusivity.

### Hyperbolic PDEs
- **Characteristics**: Describes wave-like phenomena; solutions propagate along characteristics.
- **Example**: Wave Equation
  - **Formula**: \( \frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u \)
    - \( c \) is the wave speed.

## Numerical Methods

### Finite Difference Method (FDM)
- **Concept**: Approximates derivatives using differences between function values at discrete points.
- **Example**: Central Difference for the second derivative
  - **Formula**: \( \frac{\partial^2 u}{\partial x^2} \approx \frac{u_{i+1} - 2u_i + u_{i-1}}{\Delta x^2} \)

### Finite Element Method (FEM)
- **Concept**: Divides the domain into smaller sub-domains (elements) and uses interpolation functions.
- **Process**:
  1. Discretize the domain into elements.
  2. Choose interpolation functions.
  3. Formulate element equations.
  4. Assemble the global system of equations.
  5. Apply boundary conditions and solve.

### Finite Volume Method (FVM)
- **Concept**: Integrates governing equations over control volumes, ensuring conservation of fluxes.
- **Example**: Discretization of a conservation law
  - **Formula**: \( \frac{\partial }{\partial t} \int_V \rho dV + \int_A \rho \mathbf{u} \cdot d\mathbf{A} = 0 \)

### Finite Point Method (FPM)
- **Concept**: Uses scattered points in the domain to approximate the differential equations.
- **Process**:
  1. Generate points within the domain.
  2. Construct shape or basis functions around each point.
  3. Formulate and solve the system of equations.

## Differentiation Schemes

### Forward Difference
- **Formula**: \( \frac{\partial u}{\partial x} \approx \frac{u_{i+1} - u_i}{\Delta x} \)

### Backward Difference
- **Formula**: \( \frac{\partial u}{\partial x} \approx \frac{u_i - u_{i-1}}{\Delta x} \)

### Central Difference
- **Formula**: \( \frac{\partial u}{\partial x} \approx \frac{u_{i+1} - u_{i-1}}{2\Delta x} \)

---

Prev: [Fundamentals - Part I](Fundamental_Part01.md)  
Next: [Fundamentals - Part III](Fundamental_Part03.md)
