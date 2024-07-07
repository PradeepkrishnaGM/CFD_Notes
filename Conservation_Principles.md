# Conservation Principles

## Mass Conservation (Continuity Equation)

The principle of mass conservation states that mass cannot be created or destroyed. In fluid dynamics, this is expressed as the continuity equation.

### Continuity Equation
\[ \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0 \]
Where:
- \( \rho \) is the fluid density
- \( \mathbf{u} \) is the velocity vector

## Momentum Conservation

Momentum conservation in fluid dynamics is described by the Navier-Stokes equations. These equations account for the forces acting on the fluid, including pressure, viscous, and external forces.

### Navier-Stokes Equations
\[ \frac{\partial (\rho \mathbf{u})}{\partial t} + \nabla \cdot (\rho \mathbf{u} \mathbf{u}) = -\nabla p + \nabla \cdot \mathbf{\tau} + \rho \mathbf{f} \]
Where:
- \( p \) is the pressure
- \( \mathbf{\tau} \) is the stress tensor
- \( \mathbf{f} \) is the body force per unit volume

## Conservation of Scalar Quantities

In CFD, scalar quantities such as temperature, concentration, or species mass fractions are also conserved.

### Scalar Transport Equation
\[ \frac{\partial (\rho \phi)}{\partial t} + \nabla \cdot (\rho \phi \mathbf{u}) = \nabla \cdot (\Gamma_\phi \nabla \phi) + S_\phi \]
Where:
- \( \phi \) is the scalar quantity
- \( \Gamma_\phi \) is the diffusion coefficient
- \( S_\phi \) is the source term

## Energy Conservation

Energy conservation in fluid dynamics accounts for the internal energy changes due to conduction, convection, and other energy sources.

### Energy Equation
\[ \frac{\partial (\rho E)}{\partial t} + \nabla \cdot (\rho E \mathbf{u}) = \nabla \cdot (k \nabla T) + \Phi \]
Where:
- \( E \) is the total energy per unit mass
- \( k \) is the thermal conductivity
- \( T \) is the temperature
- \( \Phi \) represents viscous dissipation

---

Next: [Numerical Solutions and Spatial Discretization](Numerical_Solutions_and_Spatial_Discretization.md)

