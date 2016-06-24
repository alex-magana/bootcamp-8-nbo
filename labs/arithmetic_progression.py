def arith_geo(lst):
  if lst == []:
    return 0
  else:
    is_arithmetic = []
    is_geometric = []
    bool_arith = False
    bool_geo = False

    for i in range(len(lst) - 1):
      if lst[i] == 0 or lst[i + 1] == 0:
        is_geometric.append(0)
      else:
        is_geometric.append(lst[i+1] / float(lst[i]))
      is_arithmetic.append(lst[i+1] - lst[i])
      
    if min(is_arithmetic) == max(is_arithmetic):
      bool_arith = True
    
    if min(is_geometric) == max(is_geometric):
      bool_geo = True
    
    if bool_arith == True:
      return "Arithmetic"
    elif bool_geo == True:
      return "Geometric"
    else:
      return -1