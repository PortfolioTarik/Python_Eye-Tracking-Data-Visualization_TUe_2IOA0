#---- Start Coding by Tarik Hacialiogullari
def getSortedUserData(user, mapName, color, order):
    columns = ['ID', 'Timestamp', 'StimuliName', 'FixationIndex', 'FixationDuration',
               'MappedFixationPointX', 'MappedFixationPointY', 'user', 'description']
    columns_sql = ', '.join(columns)
#---- End Coding by Tarik Hacialiogullari

#---- Start Coding by Tarik Hacialiogullari & Updated by Andrada Pancu
    query_asc = "SELECT " + columns_sql + " FROM Fixation_data WHERE user = '" + user + "' AND StimuliName LIKE '%" + mapName.split('_')[1] + "%' AND description = '" + color + "' ORDER BY FixationDuration "
    query_desc = "SELECT " + columns_sql + " FROM Fixation_data WHERE user = '" + user + "' AND StimuliName LIKE '%" + mapName.split('_')[1] + "%' AND description = '" + color + "' ORDER BY FixationDuration DESC "
#---- End Coding by Tarik Hacialiogullari & Updated by Andrada Pancu

#Start of code by Andrada Pancu - in models homepage - also needs order='ASC'
    if order == 'ASC' :
        queryset_userData = FixationData.objects.raw(query_asc)
    if order == 'DESC' :
        queryset_userData = FixationData.objects.raw(query_desc)
    
    return querySetToPandas(queryset_userData)
#End of code by Andrada Pancu

#Start of code by Andrada Pancu - in barchart views
    order = 'ASC'
    df_user = getSortedUserData('p1', '06_Hamburg_S1.jpg', 'color', order)

    menu = Select(options=['ASC','DESC'], value = 'ASC', title = 'Order')
    def callback(attr, old, new):
        if menu.value == 'ASC' : order = 'ASC'
        elif menu.value == 'DESC' : order = 'DESC' 
        df_user = getSortedUserData('p1', '06_Hamburg_S1.jpg', 'color', order)
    menu.on_change('value', callback)
#End of code by Andrada Pancu