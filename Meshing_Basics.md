# Meshing Basics

## Mesh Quality

### Typical Mesh Shapes

- **2D Shapes**: Triangles, quadrilaterals
- **3D Shapes**: Tetrahedrons, hexahedrons, polyhedrons

### Mesh Quality Metrics

- **Aspect Ratio**
- **Skewness**
- **Non-orthogonality**
- **Mesh Density**
- **Smoothness**

## Types of Mesh

### Structured Mesh
- Regular grid pattern

### Unstructured Mesh
- Irregular grid pattern

### Curvilinear Mesh
- **H-Grid**
- **O-Grid**
- **C-Grid**

## Time Discretization

### Euler Method
- **Explicit Euler Method**
  \[ u^{n+1} = u^n + \Delta t f(u^n, t^n) \]

- **Implicit Euler Method**
  \[ u^{n+1} = u^n + \Delta t f(u^{n+1}, t^{n+1}) \]

### Crank-Nicolson Method
- **Formula**: 
  \[ u^{n+1} = u^n + \frac{\Delta t}{2} [f(u^n, t^n) + f(u^{n+1}, t^{n+1})] \]

### Other Methods
- **Cliff-Rock Method**

---

Prev :[Effects](Effects)
Next :[Solution for Navier Stokes](Solution_for_Navier_Stokes.md)
