# Meshing Basics

## Mesh Quality

Mesh quality plays a major role in the accuracy, stability, and convergence of CFD simulations.

### Typical Mesh Shapes

- **2D Shapes**: Triangles, quadrilaterals
- **3D Shapes**: Tetrahedrons, hexahedrons, polyhedrons

### Mesh Quality Metrics

Common mesh quality metrics include:

- **Aspect Ratio**
- **Skewness**
- **Non-orthogonality**
- **Mesh Density**
- **Smoothness**

## Types of Mesh

### Structured Mesh
A structured mesh follows a regular grid pattern.

### Unstructured Mesh
An unstructured mesh follows an irregular grid pattern.

### Curvilinear Mesh
Common curvilinear mesh topologies include:

- **H-Grid**
- **O-Grid**
- **C-Grid**

## Time Discretization

Time discretization methods are used to advance the solution in time.

### Euler Method

**Explicit Euler Method**

$u^{n+1} = u^n + \Delta t \, f(u^n, t^n)$

**Implicit Euler Method**

$u^{n+1} = u^n + \Delta t \, f(u^{n+1}, t^{n+1})$

### Crank-Nicolson Method

**Formula**

$u^{n+1} = u^n + \frac{\Delta t}{2}\left[f(u^n, t^n) + f(u^{n+1}, t^{n+1})\right]$

### Other Methods

- **Cliff-Rock Method**

---

Prev: [Effects](Effects.md)  
Next: [Solution for Navier Stokes](Solution_for_Navier_Stokes.md)
