# -*- encoding: UTF-8

import pandas as pd

# select * from data;
# equivalent to df
def select_all():
	a = [['2', '1.2', '4.2'], ['0', '10', '0.3'], ['1', '5', '0']]
	df = pd.DataFrame(a, columns=['one', 'two', 'three'])
	print(df)

# select * from data limit 10
# equivalent to df
def select_by_limit():
	a = [['2', '1.2', '4.2'], ['0', '10', '0.3'], ['1', '5', '0']]
	df = pd.DataFrame(a, columns=['one', 'two', 'three'])
	print(df[:2])

# select id from data
# equivalent to df
def select_id():
	a = [['2', '1.2', '4.2'], ['0', '10', '0.3'], ['1', '5', '0']]
	df = pd.DataFrame(a, columns=['one', 'two', 'three'])
	print(df['two'])

# select count(id) from data
# equivalent to df
def select_count_id():
	a = [['2', '1.2', '4.2'], ['0', '10', '0.3'], ['1', '5', '0']]
	df = pd.DataFrame(a, columns=['one', 'two', 'three'])
	print(df['two'].count())	

# select id, count(distinct order_id) from table group by id
# order_id重复的算1个
def select_group_by():
	a = [['10', '1.2', '0.3'], ['10', '10', '0.3'], ['11', '5', '0'], ['11', '15', '0.3']]
	df = pd.DataFrame(a, columns=['id', 'two', 'order_id'])
	group_df = df.groupby('id').agg({'order_id': 'nunique'})
	group_df = group_df.reset_index()
	print(group_df)

# select * from data where id < 1000 and age > 30
# equivalent to df
def select_where():
	df = pd.DataFrame([[100, 31],
					   [101, 29],
					   [10000, 31]], columns=['id', 'age'])
	where_df = df.loc[(df['id'] < 1000) & (df['age'] > 30)]
	print(where_df)

# select * from table1 t1 inner join table2 t2 on t1.id = t2.id
# equivalent to df
def select_table_inner_join():
	t1 = pd.DataFrame([[100,31],
					   [101,29],
					   [10000, 31]], columns=['id', 'age'])
	t2 = pd.DataFrame([[101,31],
					   [101,29],
					   [10100, 31]], columns=['id', 'age'])
	join_df = pd.merge(t1, t2, how='inner', on=['id'])
	print(join_df)

# select * from table1 union select * from table2
# equivalent to df
def select_table_union():
	t1 = pd.DataFrame([[100,31],	
					   [101,29],
					   [10000, 31]], columns=['id', 'age'])

	t2 = pd.DataFrame([[101,31],	
					   [101,29],
					   [10100, 31]], columns=['id', 'age'])
	union_df = pd.merge(t1, t2, how='outer')
	print(union_df)

# delete from table1 where id=10
def delete_where():
	t1 = pd.DataFrame([[100,31],	
					   [101,29],
					   [10000, 31]], columns=['id', 'age'])
	del_df = t1.loc[t1['id'] != 100]
	print(del_df)

# alter table table1 drop column column_name
def alter_table():
	t1 = pd.DataFrame([[100,31],	
					   [101,29],
					   [10000, 31]], columns=['id', 'age'])
	alter_df = t1.drop(columns=['id'])
	print(alter_df)
	
if __name__ == "__main__":
	# select_all()
	# select_by_limit()
	# select_id()
	# select_count_id()
	# select_group_by()
	# select_where()
	# select_table_inner_join()
	# select_table_union()
	# delete_where()
	alter_table()
