"""Checks for share 5811b022 (Sphinx / Giza). CC0. Standard library only.
Coordinates are approximate public gazetteer values (degrees-minutes-seconds as listed
on common references) and are [to verify] against a survey; they are good to ~30 m."""
import math

def dms(d, m, s): return d + m/60 + s/3600
sites = {
    "Sphinx":    (dms(29, 58, 31), dms(31, 8, 16)),
    "Khufu G1":  (dms(29, 58, 45), dms(31, 8, 3)),
    "Khafre G2": (dms(29, 58, 34), dms(31, 7, 51)),
    "Menkaure G3": (dms(29, 58, 21), dms(31, 7, 41)),
}
R = 6371000.0
def dist(a, b):
    (la1, lo1), (la2, lo2) = map(lambda p: (math.radians(p[0]), math.radians(p[1])), (a, b))
    x = (lo2 - lo1) * math.cos((la1 + la2) / 2); y = la2 - la1
    return R * math.hypot(x, y)
print("== Sphinx to pyramid centres (approx.) ==")
half = {"Khufu G1": 230.3/2, "Khafre G2": 215.3/2, "Menkaure G3": 103.4/2}
for k in ("Khufu G1", "Khafre G2", "Menkaure G3"):
    d = dist(sites["Sphinx"], sites[k])
    print(f"Sphinx -> {k:12s}: centre {d:5.0f} m, nearest base edge roughly {d-half[k]:5.0f} m")

print("\n== Great Pyramid 'squaring the circle' ==")
h, b = 146.6, 230.33
print(f"perimeter 4b = {4*b:.1f} m; 2*pi*h = {2*math.pi*h:.1f} m; ratio = {4*b/(2*math.pi*h):.4f}")
seked = 5.5  # palms run per cubit (7 palms) rise
slope = 7 / seked
print(f"seked 5 1/2 palms -> slope {slope:.4f} (tan {math.degrees(math.atan(slope)):.2f} deg); "
      f"perimeter/height = 8/slope = {8/slope:.4f} = 2 x {4/slope:.4f} (22/7 = {22/7:.4f})")
print("-> the 2*pi match follows from the 5 1/2-palm seked; whether pi was intended is debated.")

print("\n== Sphinx proportions vs golden ratio ==")
L, H, W = 73.5, 20.2, 19.1
for name, r in (("length/height", L/H), ("length/width", L/W), ("height/width", H/W)):
    print(f"{name:14s} = {r:.3f}  (phi = 1.618)")
