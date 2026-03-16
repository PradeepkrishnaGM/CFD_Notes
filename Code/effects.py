import numpy as np
import matplotlib.pyplot as plt

def corner_inflow_profile(s, sigma=0.14):
    """
    Scalar inflow profile concentrated near the lower-left corner.
    """
    return np.exp(-(s / sigma) ** 2)

def apply_boundary_conditions(phi, x, y, sigma):
    """
    Boundary conditions:
    - West boundary  : Dirichlet inflow, concentrated near y = 0
    - South boundary : Dirichlet inflow, concentrated near x = 0
    - East boundary  : zero-gradient outflow
    - North boundary : zero-gradient outflow

    phi includes one ghost-cell layer on each side.
    """
    left_bc = corner_inflow_profile(y, sigma)
    bottom_bc = corner_inflow_profile(x, sigma)

    # Dirichlet inflow on west and south boundaries
    # Ghost-cell formulation so the boundary face value is exactly the prescribed BC
    phi[0, 1:-1] = 2.0 * left_bc - phi[1, 1:-1]
    phi[1:-1, 0] = 2.0 * bottom_bc - phi[1:-1, 1]

    # Zero-gradient outflow on east and north boundaries
    phi[-1, 1:-1] = phi[-2, 1:-1]
    phi[1:-1, -1] = phi[1:-1, -2]

    # Corner ghosts
    phi[0, 0] = 0.5 * (phi[0, 1] + phi[1, 0])
    phi[0, -1] = phi[1, -1]
    phi[-1, 0] = phi[-1, 1]
    phi[-1, -1] = phi[-2, -1]

    return left_bc, bottom_bc

def power_law_factor(Pe):
    """
    Patankar power-law weighting factor.
    """
    return max(0.0, (1.0 - 0.1 * abs(Pe)) ** 5)

def face_flux(up, down, far_up, vel, gamma, h, scheme):
    """
    Compute the face flux:
        J = u * phi_f - gamma_eff * d(phi)/dn

    For positive velocity, 'up' is the upstream cell value,
    'down' is the downstream cell value,
    'far_up' is the far-upstream value used by QUICK.
    """
    if scheme == "UDS":
        phi_face = up
        gamma_eff = gamma

    elif scheme == "CDS":
        phi_face = 0.5 * (up + down)
        gamma_eff = gamma

    elif scheme == "QUICK":
        phi_face = (6.0 * up + 3.0 * down - far_up) / 8.0
        gamma_eff = gamma

    elif scheme == "POWER":
        Pe = vel * h / max(gamma, 1.0e-14)
        phi_face = up
        gamma_eff = gamma * power_law_factor(Pe)

    else:
        raise ValueError(f"Unknown scheme: {scheme}")

    return vel * phi_face - gamma_eff * (down - up) / h

def solve_scheme(
    scheme,
    N=80,
    L=1.0,
    u=1.0,
    v=1.0,
    gamma=0.003,
    final_time=0.8,
    sigma=0.14,
):
    """
    Solve the transient 2D advection-diffusion equation on a uniform grid:

        d(phi)/dt + d(u phi)/dx + d(v phi)/dy
        = gamma * (d2(phi)/dx2 + d2(phi)/dy2)

    using an explicit finite-volume update.

    Parameters
    ----------
    scheme : str
        One of ["UDS", "CDS", "QUICK", "POWER"]
    N : int
        Number of interior cells in each direction
    L : float
        Domain size (square domain: 0 <= x,y <= L)
    u, v : float
        Constant velocity components
    gamma : float
        Diffusion coefficient
    final_time : float
        End time for the transient run
    sigma : float
        Width of the corner inflow distribution
    """
    dx = L / N
    dy = L / N

    x = (np.arange(N) + 0.5) * dx
    y = (np.arange(N) + 0.5) * dy

    # Field with one ghost-cell layer around the domain
    phi = np.zeros((N + 2, N + 2), dtype=float)

    # Stable explicit time step estimate
    conv_limit = 1.0 / (abs(u) / dx + abs(v) / dy)

    if gamma > 0.0:
        diff_limit = 0.5 / (gamma * (1.0 / dx**2 + 1.0 / dy**2))
    else:
        diff_limit = np.inf

    dt = 0.35 * min(conv_limit, diff_limit)
    nsteps = int(np.ceil(final_time / dt))
    dt = final_time / nsteps

    for _ in range(nsteps):
        left_bc, bottom_bc = apply_boundary_conditions(phi, x, y, sigma)
        phi_new = phi.copy()

        for i in range(1, N + 1):
            for j in range(1, N + 1):
                # West face flux
                if i == 1:
                    # Inflow boundary at x = 0
                    bc = left_bc[j - 1]
                    Jw = u * bc - gamma * (phi[i, j] - bc) / (0.5 * dx)
                else:
                    Jw = face_flux(
                        up=phi[i - 1, j],
                        down=phi[i, j],
                        far_up=phi[i - 2, j],
                        vel=u,
                        gamma=gamma,
                        h=dx,
                        scheme=scheme,
                    )

                # East face flux
                if i == N:
                    # Zero-gradient outflow
                    Je = u * phi[i, j]
                else:
                    Je = face_flux(
                        up=phi[i, j],
                        down=phi[i + 1, j],
                        far_up=phi[i - 1, j],
                        vel=u,
                        gamma=gamma,
                        h=dx,
                        scheme=scheme,
                    )

                # South face flux
                if j == 1:
                    # Inflow boundary at y = 0
                    bc = bottom_bc[i - 1]
                    Js = v * bc - gamma * (phi[i, j] - bc) / (0.5 * dy)
                else:
                    Js = face_flux(
                        up=phi[i, j - 1],
                        down=phi[i, j],
                        far_up=phi[i, j - 2],
                        vel=v,
                        gamma=gamma,
                        h=dy,
                        scheme=scheme,
                    )

                # North face flux
                if j == N:
                    # Zero-gradient outflow
                    Jn = v * phi[i, j]
                else:
                    Jn = face_flux(
                        up=phi[i, j],
                        down=phi[i, j + 1],
                        far_up=phi[i, j - 1],
                        vel=v,
                        gamma=gamma,
                        h=dy,
                        scheme=scheme,
                    )

                phi_new[i, j] = phi[i, j] - dt * (
                    (Je - Jw) / dx + (Jn - Js) / dy
                )

        phi = phi_new

    return x, y, phi[1:-1, 1:-1]

def main():
    schemes = ["UDS", "CDS", "QUICK", "POWER"]
    results = {}

    for scheme in schemes:
        x, y, phi = solve_scheme(scheme=scheme)
        results[scheme] = phi
        print(
            f"{scheme:>5s}  "
            f"min = {phi.min(): .5f}, "
            f"max = {phi.max(): .5f}"
        )

    X, Y = np.meshgrid(x, y, indexing="ij")

    # Contour plots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10), constrained_layout=True)

    for ax, scheme in zip(axes.ravel(), schemes):
        cf = ax.contourf(X, Y, results[scheme], levels=30)
        fig.colorbar(cf, ax=ax)
        ax.set_title(scheme)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_aspect("equal")

    plt.show()

    # Diagonal profile x = y
    plt.figure(figsize=(8, 5))
    for scheme in schemes:
        plt.plot(x, results[scheme].diagonal(), label=scheme)

    plt.xlabel("Distance along diagonal (x = y)")
    plt.ylabel("Scalar value")
    plt.title("Comparison along the main diagonal")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
