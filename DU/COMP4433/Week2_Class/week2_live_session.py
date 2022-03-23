""" Week 2 Live Session

Pandas topics.
"""
import numpy as np
import pandas as pd
from pandas import DataFrame

# create a Dataframe from random draws, specifying index and cols
df = DataFrame(np.random.randn(10, 5),
               index=[i for i in 'IN OH MI KY IL CO WY NM CA OR'.split(' ')],
               columns=['feat_' + str(i) for i in range(1, 6)])

more_data = {'state': [i for i in 'IN OH MI KY IL CO WY NM CA OR'.split(' ')],
             'is_big': [False, True, True, False, np.nan, True, False, True, True, True],
             'nickname': ['Hoosier', 'Buckeye', 'Wolverine', 'Bluegrass', 'Prairie',
                          'Centennial', 'Equality', 'Enchantment', 'Golden', 'Beaver']}

# notice we're not setting an index value here.
df2 = DataFrame(more_data)

# Let's join these DataFrames
big_df = df.merge(df2, how='left', left_index=True, right_on='state')

# Notice the resulting indices
print(big_df.index)

# Let's merge them again, this time we'll specify indices for df2.
# This will introduce some redundancy into our DataFrame
# df2.set_index('state', inplace = True) is a better alternative.
df2 = DataFrame(more_data, index=more_data['state'])
df2.drop(columns='state', inplace=True)

# Executing the merge again.
big_df = df.merge(df2, how='left', left_index=True, right_index=True)

# Now notice the resulting indices.
print(big_df.index)

# Perhaps we want the state code as a feature and not the index
big_df.reset_index(drop=False, inplace=True)

# notice the name of the state code feature
print(big_df.columns)

# renaming cols inplace
big_df.rename(columns={'index': 'state'}, inplace=True)

# setting index back to state code
big_df.set_index('state', inplace=True)

print(big_df)

# notice that the index now has a name attribute
print(big_df.index)

# Let's add another feature.
big_df['year'] = '1997'

# And we'll augment this DataFrame a bit...
# Let's make another df to concat.
another_df = DataFrame(np.random.randn(10, 5),
                       index=[i for i in 'IN OH MI KY IL CO WY NM CA OR'.split(' ')],
                       columns=['feat_' + str(i) for i in range(1, 6)])

another_df = another_df.merge(df2, how='left', left_index=True, right_index=True)
another_df['year'] = '2001'

# and we'll add another column to this df.
another_df['quarter'] = 'q1'

# concatenate the two dataframes
# axis arg is 0 by default
final_df = pd.concat([big_df, another_df], axis=0)

# fillna for quarter...this wasn't a feature in big_df.
final_df['quarter'].fillna(value='q1', inplace=True)

# now we're going to double the length of our primary DataFrame.
# Be cautious with aliasing...
copied = final_df
copied['quarter'] = 'q2'

print(final_df['quarter'])

final_df['quarter'] = 'q1'

# Use the .copy() instead.
copied = final_df.copy()
copied['quarter'] = 'q2'

# confirming that the change to copied
# had no impact on final_df
print(final_df['quarter'])

# iterating over the feature columns and modifying them randomly
for i in ['feat_1', 'feat_2', 'feat_3', 'feat_4', 'feat_5']:
    copied[i] = np.vectorize(lambda arg: np.random.randn())(copied[i])

final_df = pd.concat([final_df, copied], axis=0)

# Let's pivot this and join an aggregate field to our final_df.
# Say, for some reason, we need the max across annual quarters of the feature values by year
pivoted = final_df.pivot_table(index=final_df.index,
                               columns='year',
                               values=['feat_1', 'feat_2', 'feat_3', 'feat_4', 'feat_5'],
                               aggfunc=np.max)

# we now have MultiIndexed columns where column indices are represented as tuples
print(pivoted.columns)
print(pivoted.index)
print(pivoted)

# if we want to flatten them out...
pivoted.columns = ['_'.join(col) for col in pivoted.columns]

print(pivoted)

# Maybe it makes more sense to pivot this way, if we want to join these data.
pivoted = final_df.pivot_table(index=[final_df.index, 'year'],
                               values=['feat_1', 'feat_2', 'feat_3', 'feat_4', 'feat_5'],
                               aggfunc=np.max)

# now we have MultiIndexed rows.
print(pivoted.columns)
print(pivoted.index)
print(pivoted)

# note that our pivoted data contains the same feature names as were in our primary data
# Pandas will handle this by appending an _x and _y to these feature names.
# We'll change these names first.
pivoted.columns = [i + '_ann_max' for i in pivoted.columns]

final_df = final_df.merge(pivoted,
                          how='left',
                          left_on=[final_df.index, 'year'],
                          right_index=True)

# sorting index
final_df.sort_index(ascending=True,
                    inplace=True)

# sorting on additional cols
final_df.sort_values(['year', 'quarter'],
                     ascending=[False, True],
                     inplace=True)

# maybe we want to drop records with a certain nickname
# we can send the indices of the data with certain properties to a list
location = final_df.index[(final_df['nickname'].isin(['Buckeye', 'Bluegrass']))].tolist()
final_df.drop(index=location, inplace=True)

# drop rows with missing values
final_df.dropna(axis=0, inplace=True)
