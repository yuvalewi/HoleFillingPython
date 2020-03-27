def create_euclidean_weight(z=2, eps=0):
    def euclidean_weight(u, v):
        dist = calculate_distance(u,v)
        return 1. / (dist ** z + eps)

    return euclidean_weight


def calculate_distance(u, v):
    return ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** .5
