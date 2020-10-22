
def triangle_area(vertices):
    x = []
    y = []
    for i in range(len(vertices)):      # Putter x-verdiene og y-verdiene i to lister
        x.append(vertices[i][0])
        y.append(vertices[i][1])

    A = 0.5*abs(x[1]*y[2]-x[2]*y[1]-x[0]*y[2]+x[2]*y[0]+x[0]*y[1]-x[1]*y[0])
    return A

def test_triangle_area():
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area = {computed}, expected area = {expected}"
    assert success, msg

v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
vertices = [v1, v2, v3]

test_triangle_area()


"""
Terminal> python triangle_area.py

"""
