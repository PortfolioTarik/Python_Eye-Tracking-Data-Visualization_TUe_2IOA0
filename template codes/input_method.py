
# will need to find and note application name and table name in order for those to properly work 


#overall input query
for i in FixationData.objects.raw(''' SELECT StimuliName, FixationIndex, FixationDuration,
                                        MappedFixationPointX, MappedFixationPointY, user
                                        FROM data  ''')

#Stimuli name query
for s in FixationData.objects.raw(''' SELECT StimuliName FROM data ''')

#user centered query
# u and s will be defined in their dropdown options beforehand
#(e.g. user dropdown set to '1', stimuli dropdown set to '02_Berlin_S1.jpg')
# for 2 or more users on the same graph do the amount of queries separate per user 
# then concatenate the data
viz_data = FixationData.objects.raw(''' SELECT FixationIndex, FixationDuration, 
                                            MappedFixationPointX, MappedFixationPointY 
                                            FROM Fixation datas
                                            WHERE user = u AND StimuliName = s''')

#index lookups
viz_data = FixationData.objects.raw('SELECT FixationDuration, MappedFixationPointX, MappedFixationPointY FROM myapp')[0]



viz_data = FixationData.objects.raw('''SELECT FixationDuration, User
                                    MappedFixationPointX, MappedFixationPointY
                                    FROM Fixation_data''')
    x_value1 = viz_data[(viz_data['user'] == 'p1')]['MappedFixationPointX']
    y_value1 = viz_data[(viz_data['user'] == 'p1')]['MappedFixationPointY']

    x_value2 = viz_data[(viz_data['user'] == 'p9')]['MappedFixationPointX']
    y_value2 = viz_data[(viz_data['user'] == 'p9')]['MappedFixationPointY']




# Make list of distinct stimuli names
columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']

    columns_sql = ', '.join(columns)
    query_maps = FixationData.objects.raw(
        "SELECT DISTINCT StimuliName, 1 as id FROM Fixation_data ")
    
    for stimulidata in query_maps: 
        stimuli_list.append(stimulidata.StimuliName)

    