import texttable
table = texttable.Texttable()
table.set_cols_align(["l" , "r" , "c"])
table.set_cols_align(["b" , "b" , "b"])
table.set_chars(["-" , "|" , "+" , "-"])
row1 = [" " , " " , " "]
row2 = [" " , " " , " "]
row3 = [" " , " " , " "]
table.add_rows([row1 , row2 , row3])
print(table.draw())