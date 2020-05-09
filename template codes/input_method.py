
# will need to find and note application name and table name in order for those to properly work 


#overall input query
for i in FixationData.objects.raw(''' SELECT StimuliName, FixationIndex, FixationDuration,
                                        MappedFixationPointX, MappedFixationPointY, user
                                        FROM TABLE_NAME  ''')

#Stimuli name query
for s in FixationData.objects.raw(''' SELECT StimuliName FROM TABLE_NAME ''')

#user centered query
# u and s will be defined in their dropdown options beforehand
#(e.g. user dropdown set to '1', stimuli dropdown set to '02_Berlin_S1.jpg')
# for 2 or more users on the same graph do the amount of queries separate per user 
# then concatenate the data
data_for_viz = FixationData.objects.raw(''' SELECT FixationIndex, FixationDuration, 
                                            MappedFixationPointX, MappedFixationPointY 
                                            FROM TABLE_NAME
                                            WHERE user = u AND StimuliName = s''')

