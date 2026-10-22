"""UV photon energies, E = hc/lambda, in eV. CC0.
Band edges per ISO 21348 / CIE: UV-A 315-400 nm, UV-B 280-315 nm, UV-C 100-280 nm.
Reference lines: 365 nm (UV-A blacklight / Hg line), 254 nm (low-pressure Hg germicidal line),
260 nm (approximate DNA absorption peak).
"""
h = 6.62607015e-34   # J s (exact, SI 2019)
c = 299792458.0      # m/s (exact)
e = 1.602176634e-19  # J/eV (exact)

lines = [
    (400, "UV-A upper edge (visible boundary)"),
    (365, "UV-A reference: blacklight / Hg 365 nm"),
    (315, "UV-A / UV-B boundary"),
    (280, "UV-B / UV-C boundary"),
    (260, "DNA absorption peak (approx.)"),
    (254, "Low-pressure Hg germicidal line"),
    (100, "UV-C lower edge (vacuum-UV boundary)"),
]

print("E = hc/lambda;  hc = %.6f eV nm" % (h * c / e * 1e9))
print("%8s  %8s  %s" % ("nm", "eV", "label"))
for nm, label in lines:
    E = h * c / (nm * 1e-9) / e
    print("%8d  %8.3f  %s" % (nm, E, label))
print("Bands: UV-A 3.10-3.94 eV; UV-B 3.94-4.43 eV; UV-C 4.43-12.40 eV")
