from math import sqrt


def get_roots(a_coef, b_coef, c_coef):
    discriminant = b_coef ** 2 - 4 * a_coef * c_coef
    if discriminant < 0:
        return None, None
    root1 = (-b_coef - sqrt(discriminant)) / (2 * a_coef)
    root2 = (-b_coef + sqrt(discriminant)) / (2 * a_coef)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
