# Properties of Numerical Solution Methods

## Consistency
A method is considered **consistent** if the discretized equations exhibit no truncation error as the mesh size and time step approach zero (i.e., as \(\Delta x \to 0\) and \(\Delta t \to 0\)).

## Stability
A solution process is considered **stable** if a time-dependent solution remains bounded, or if, in an iterative process, the error decreases with an increasing number of iteration steps.

## Convergence
A numerical method is deemed **convergent** if the solution to the differential equation can be accurately obtained with sufficiently small mesh spacings and/or time steps. Stability is both a necessary and sufficient condition for convergence.

## Conservation
The properties of the solution process should be conserved, meaning that what is input into the system should be reflected in the output.

## Boundedness
The properties in the solution process should be bounded. For instance, physical values such as concentration should fall within a range of 0 to 1, while density must always remain greater than 0.

## Solution of Systems of Linear Equations

### Direct Methods
- **Guass Elimination**
- **Tri-Diagonal Matrix Algorithm (TDMA)(for tridiagonal matrices)**
- **LU Decomposition**

#### Iterative Methods

- **Jacobi Method**
- **Gauss-Seidel Method**
- **SOR (Successive Over-Relaxation)**
- **LU Decomposition**
- **Incomplete LU Decomposition**

### Conjugate Gradient Method

### Multi-Grid Methods

---
<p align="left">Previous: [Introduction](introduction.md)</p> <p align="right">Next: [Fundamentals - Part II](Fundamental_Part02.md)</p>


<p align="right">text</p>
