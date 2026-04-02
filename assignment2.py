import pandas as pd

data = pd.DataFrame([{'id':0, 'follows':1}, {'id':0, 'follows':2},{'id':0, 'follows':3}, {'id':2, 'follows':0}, {'id':2, 'follows':1}, {'id':3, 'follows':0}, {'id':3, 'follows':2}])

def find_triangle(data):
    cpy = data.copy()
    ind = pd.merge(data, cpy, left_on = "follows", right_on = "id")
    df_final = pd.merge(ind, data, left_on = "follows_y", right_on = "id")
    ret = df_final[df_final["id_x"] == df_final["follows"]][["id_x", "follows_x", "follows_y", "follows"]]
    return ret

print(find_triangle(data))
