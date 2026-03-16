# Fundamentals Part Two: Partial Differential Equations (PDEs)

## What is a PDE?

A **Partial Differential Equation (PDE)** involves partial derivatives of a function with respect to two or more independent variables.

PDEs are used to describe many physical phenomena, including:

- heat transfer
- sound propagation
- fluid flow
- quantum mechanics

---

## Types of PDEs

### 1. Elliptic PDEs

**Characteristics**

- No real characteristic directions
- Solutions are typically smooth and well-behaved

**Example: Laplace's Equation**

$$
\nabla^2 \phi = 0
$$

---

### 2. Parabolic PDEs

**Characteristics**

- Describe diffusion-dominated processes
- Information spreads gradually over time

**Example: Heat Equation**

$$
\frac{\partial u}{\partial t} = \alpha \nabla^2 u
$$

Where:

- $u$ is the dependent variable
- $\alpha$ is the thermal diffusivity

---

### 3. Hyperbolic PDEs

**Characteristics**

- Describe wave-like phenomena
- Solutions propagate along characteristic lines

**Example: Wave Equation**

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u
$$

Where:

- $u$ is the dependent variable
- $c$ is the wave speed

---

## Numerical Methods

### 1. Finite Difference Method (FDM)

**Concept**

Approximates derivatives using differences between function values at discrete grid points.

**Example: Central Difference for the Second Derivative**

$$
\frac{\partial^2 u}{\partial x^2}
\approx
\frac{u_{i+1} - 2u_i + u_{i-1}}{\Delta x^2}
$$

---

### 2. Finite Element Method (FEM)

**Concept**

Divides the domain into smaller subdomains called *elements* and approximates the solution using interpolation functions.

**Typical workflow**

1. Discretize the domain into elements
2. Choose interpolation functions
3. Formulate element equations
4. Assemble the global system
5. Apply boundary conditions and solve

---

### 3. Finite Volume Method (FVM)

**Concept**

Integrates the governing equations over control volumes to enforce conservation.

**Example: Conservation Law in Integral Form**

$$
\frac{\partial}{\partial t} \int_V \rho \, dV
+
\int_A \rho \mathbf{u} \cdot d\mathbf{A}
= 0
$$

---

### 4. Finite Point Method (FPM)

**Concept**

Uses scattered points in the domain to approximate the governing differential equations without requiring a mesh.

**Typical workflow**

1. Generate points within the domain
2. Construct local shape or basis functions
3. Formulate and solve the resulting system

---

## Differentiation Schemes

### Forward Difference

$$
\frac{\partial u}{\partial x}
\approx
\frac{u_{i+1} - u_i}{\Delta x}
$$

### Backward Difference

$$
\frac{\partial u}{\partial x}
\approx
\frac{u_i - u_{i-1}}{\Delta x}
$$

### Central Difference

$$
\frac{\partial u}{\partial x}
\approx
\frac{u_{i+1} - u_{i-1}}{2\Delta x}
$$

---

Previous: [Fundamentals - Part I](Fundamental_Part01.md)  
Next: [Fundamentals - Part III](Fundamental_Part03.md)
