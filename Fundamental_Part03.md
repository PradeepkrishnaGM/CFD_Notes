# Fundamentals Part Three: Conservation Principles

## Conservation Laws in Fluid Dynamics

In CFD, the governing equations are based on conservation principles. These describe how mass, momentum, scalar quantities, and energy are preserved within a flow field.

---

## 1. Mass Conservation

The principle of mass conservation states that mass cannot be created or destroyed.

### Continuity Equation

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0
$$

Where:

- $\rho$ is the fluid density
- $\mathbf{u}$ is the velocity vector

---

## 2. Momentum Conservation

Momentum conservation in fluid dynamics is described by the Navier–Stokes equations. These account for pressure forces, viscous effects, and external body forces.

### Navier–Stokes Equation

$$
\frac{\partial (\rho \mathbf{u})}{\partial t}
+
\nabla \cdot (\rho \mathbf{u}\mathbf{u})
=
-\nabla p
+
\nabla \cdot \boldsymbol{\tau}
+
\rho \mathbf{f}
$$

Where:

- $p$ is the pressure
- $\boldsymbol{\tau}$ is the stress tensor
- $\mathbf{f}$ is the body force per unit volume

---

## 3. Conservation of Scalar Quantities

In CFD, scalar quantities such as temperature, concentration, or species mass fraction are also governed by conservation equations.

### Scalar Transport Equation

$$
\frac{\partial (\rho \phi)}{\partial t}
+
\nabla \cdot (\rho \phi \mathbf{u})
=
\nabla \cdot (\Gamma_\phi \nabla \phi)
+
S_\phi
$$

Where:

- $\phi$ is the scalar quantity
- $\Gamma_\phi$ is the diffusion coefficient
- $S_\phi$ is the source term

---

## 4. Energy Conservation

Energy conservation accounts for changes in internal, kinetic, and thermal energy due to conduction, convection, and dissipation.

### Energy Equation

$$
\frac{\partial (\rho E)}{\partial t}
+
\nabla \cdot (\rho E \mathbf{u})
=
\nabla \cdot (k \nabla T)
+
\Phi
$$

Where:

- $E$ is the total energy per unit mass
- $k$ is the thermal conductivity
- $T$ is the temperature
- $\Phi$ represents viscous dissipation

---

Previous: [Fundamentals - Part II](Fundamental_Part02.md)  
Next: [Discretization](Discretization.md)
