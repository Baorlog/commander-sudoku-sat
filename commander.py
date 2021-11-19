from pysat.solvers import Glucose3


def commander_exact_one(var_list, group_list, g):
    # g must be a Glucose3 object

    # Number of this group clause
    num_clause = 0

    # Divide elements in var_list to groups
    number_of_item_in_group = len(var_list) // len(group_list)
    if len(var_list) % len(group_list):
        number_of_item_in_group += 1

    group_array = [[var_list[0]]]

    for i in range(1, len(var_list)):
        # print(group_array)
        if i % number_of_item_in_group == 0:
            group_array.append([])
        group_array[i // number_of_item_in_group].append(var_list[i])

    # print(group_array)

    # ALO for commander vars
    g.add_clause(group_list)
    num_clause += 1

    # AMO for commander vars
    for i in range(len(group_list) - 1):
        for j in range(i + 1, len(group_list)):
            g.add_clause([-group_list[i], -group_list[j]])
            num_clause += 1

    if len(group_array) != len(group_list):
        return False

    # Iterate through each group
    for i in range(len(group_array)):
        # ALO if commander var true
        current_group = list(group_array[i])
        current_group.append(-group_list[i])
        g.add_clause(current_group)
        num_clause += 1

        for j in range(len(group_array[i])):
            if j < len(group_array[i]) - 1:
                for k in range(j + 1, len(group_array[i])):
                    # AMO if commander var true
                    g.add_clause([-group_list[i], -group_array[i][j], -group_array[i][k]])
                    num_clause += 1

            # If commander var false
            g.add_clause([group_list[i], -group_array[i][j]])
            num_clause += 1

    # Show results
    # print(g.solve())
    # print(g.get_model())

    return num_clause


# g = Glucose3()
# commander_exact_one([1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16], [17,18,19,20], g)

