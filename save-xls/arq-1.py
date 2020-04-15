import pandas as pd

'''
#Uma forma de salvar dados em xls
new_list= [["first","second"],["third","four"],["five","six"]] 
df = pd.DataFrame(new_list)
print(df)
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()
'''

new_list= [["first","second"],["third","four"],["five","six"]] 
df = pd.DataFrame(new_list)
print(df)
writer = pd.ExcelWriter('test-one.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', startrow=0, header=False, index=False)
writer.save()

dict1 = {'20200306': ['20200306-21:05:08.726000', 1321, 1171, 2864, 2832, 485.0], '20200305': ['20200305-21:06:28.866000', 1255, 1240, 2842, 2846, 3305.0], '20200303': ['20200303-21:06:25.248000', 1026, 1181, 2292, 2344, 15350.0], '20200304': ['20200304-21:11:51.516000', 1085, 1213, 3147, 3297, -55275.0], '20200302': ['20200302-21:12:31.998000', 614, 680, 1268, 1257, -490.0]}

'''
          0     1     2      3      4      5      6        7
a  20200303  8535  8473  17008  23033  23038  46071  27501.0
b  20200306  8229  8495  16724  26266  26275  52541  27855.0
c  20200304  6134  6059  12193  20457  20447  40904   -669.0
d  20200302  7204  7077  14281  23401  23361  46762  24282.0
e  20200305  7079  7372  14451  28489  28501  56990  31924.0
'''



print(sorted(dict1))

#Importante saber disso
'''
print('sheet of pnl')
print(sheet_pnl)

rena = ['a', 'b', 'c', 'd', 'e']

df = pd.DataFrame(sheet_win, index=rena)
df2 = pd.DataFrame(sheet_wdo)
rena = ['a', 'b', 'c', 'd', '3']
print(df.sort_values([0]))

#fazer o merge de dois data frames
df3 = pd.concat([df, df2])

print(df)

#somar todas as colunas
print(df.loc[:,1:].sum(axis = 0))

#adicionar uma linha
serie = df.loc[:,:].sum(axis = 0)
print(type(serie))

#calcular a media de umas colunas
mean_val = df.loc[:,:].mean(axis = 0)


#trocando um elemento de uma serie no pandas
serie[:1] = 'soma'
print(serie)

#adicionando mais uma linha na tabela



#converter panda to list
list_from_pandas = df.values.tolist()
#print(list_from_pandas)



#mudar primeiro elemento
mean_val[:1] = 'media'

#Selecionar um range specifico de coisas
print('iloc',df.iloc[:-2])


df = add_sum_mean_to_df(df)
print(df)

parara = conv_lst_df_win_wdo(sheet_win)
azul_caneta = parara[:-2]
print(azul_caneta)
'''

