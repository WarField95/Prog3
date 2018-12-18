from Prog3.Blatt9 import TSP_Rösch as TSP


def create_argument_list(path_completed, path_ahead, r_depth, l):
    if len(path_completed) == r_depth:
        l.append((path_completed, path_ahead))
    else:
        for i in range(len(path_ahead)):
            create_argument_list(path_completed + (path_ahead[i],) ,
                                path_ahead[:i] + path_ahead[i+1:],
                                r_depth, l)


nr_of_cities = 10
r_depth = 2
l = []
create_argument_list((TSP.staedte_positionen[0], ),
            TSP.staedte_positionen[1:nr_of_cities], r_depth, l)


l[:2]


def worker_TSP(q_in, q_out):
    while True:
        arguments = q_in.get()
        result = TSP.shortest_closed_path(*arguments)
        q_out.put(result)
        q_in.task_done()