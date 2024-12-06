
#desc procedure RCM.RCM_BUSINESS_DV.COMPARING_TABLES(VARCHAR, VARCHAR, VARCHAR) ;

def run(session, from_table, compare_table, to_table):

    import re
    
    """
    Dict with functions to apply to each data Type
    """
    numDictFunctions = {'COUNT DISTICT':'COUNT(DISTINCT(CHN_COL))', 'MAX':'MAX(CHN_COL)', 'MIN':'MIN(CHN_COL)', 'SUM':'SUM(CHN_COL)',
                        'AVG':'AVG(CHN_COL)', 'NULLS COUNT':'SUM(IFF(CHN_COL IS NULL,1,0))'}
    charDictFunctions = {'COUNT DISTICT':'COUNT(DISTINCT(CHN_COL))', 'MAX':'MAX(CHN_COL)', 'MIN':'MIN(CHN_COL)', 'SUM CHAR':'SUM(LEN(CHN_COL))',
                        'AVG CHAR':'AVG(LEN(CHN_COL))', 'WORD COUNT':"SUM(ARRAY_SIZE(SPLIT(CHN_COL,' ')))", 
                        'AVG WORD':"AVG(ARRAY_SIZE(SPLIT(CHN_COL,' ')))",'NULLS COUNT':'SUM(IFF(CHN_COL IS NULL,1,0))'}
    dateDictFunctions = {'COUNT DISTICT':'COUNT(DISTINCT(CHN_COL))','MAX':'MAX(CHN_COL)','MIN':'MIN(CHN_COL)', 'NULLS COUNT':'SUM(IFF(CHN_COL IS NULL,1,0))'}
    
    def getSQLSplitted(tableName):
        """
        Getting the attributes for each table
        """
        SQLText = session.sql(f"SELECT GET_DDL('TABLE','{tableName}') AS DDL").collect()
        SQLText = SQLText[0].as_dict()['DDL']
        SQLTextList = SQLText.split('\n')[1:-1]
        return SQLTextList

    def splitTextDict(SqlText):
        """
        Classifying each attribute for data type
        """
        dictTypes = {'NUM':[], 'VARCHAR':[], 'DATE':[], 'OTHER':[], 'TOTAL':0}
        def transformColumn(column):
            """
            Creating a list with name and data type of each column (attribute)
            """
            transformedColumn = re.split('[^\w+]',column.strip())
            #column.upper().split()[0].strip()
            return transformedColumn
        """
        Iterating over each column of table and classifying by data type
        """        
        for column in SqlText:
            transformedColumn = transformColumn(column=column)
            if transformedColumn[1] in {'NUMBER','FLOAT'}:
                dictTypes['NUM'].append(transformedColumn[0])
            elif transformedColumn[1] in {'CHAR','VARCHAR','STRING'}:
                dictTypes['VARCHAR'].append(transformedColumn[0])
            elif transformedColumn[1] in ('DATE','TIME','TIMESTAMP','TIMESTAMP_NTZ'):
                dictTypes['DATE'].append(transformedColumn[0])
            else:
                dictTypes['OTHER'].append(transformedColumn[0])
            dictTypes['TOTAL'] += 1

        return dictTypes

    def constructFunction(_function,_functionName, listCols, tableName, isNum):
        """
        Constructing query for each function in list of functions to apply
        """
        tableNameNoContext = tableName.split('.')[-1]
        
        header = f"SELECT '{tableNameNoContext}' AS TABLE_FROM, '{_functionName}' AS OPERATION,"
        if isNum:
            functionBody = [' ' + re.sub('CHN_COL',x,_function) + f' AS {x}' for x in listCols]
        else:
            functionBody = [' ' + re.sub('CHN_COL',x,_function) + f'::VARCHAR AS {x}' for x in listCols]
        functionBody = ','.join(functionBody)
        fromClause = f'\n FROM {tableName}'
        finalFunction = header + functionBody + fromClause
        return finalFunction

    def FunctionGenerator(listCols, tableName, dictFunctions, isNum):
        """
        Constructing final query combining all functions in functions to apply to create one big table with all
        columns with same data type
        """
        listSQLFunctions = [constructFunction(dictFunctions[_functionName], _functionName, listCols, tableName, isNum) for _functionName in dictFunctions]
        SQLText = '\nUNION ALL \n'.join(listSQLFunctions)
        return SQLText

    # Getting DDL
    textColumnsFromTable    = getSQLSplitted(from_table)
    textColumnsCompareTable = getSQLSplitted(compare_table)
    

    # Classifying columns of table
    dictColumnsFromTable    = splitTextDict(textColumnsFromTable)   
    dictColumnsCompareTable = splitTextDict(textColumnsCompareTable) 
    
    # Numeric columns generation
    textSQLNumTablesFromTable       =   FunctionGenerator(listCols = dictColumnsFromTable['NUM'],tableName = from_table, dictFunctions = numDictFunctions, isNum = True)
    textSQLNumTablesCompareTable    =   FunctionGenerator(listCols = dictColumnsCompareTable['NUM'],tableName = compare_table, dictFunctions = numDictFunctions, isNum = True)
    NumTableName = f'RCM.RCM_BUSINESS_DV.COMPARING_{to_table}_NUM'
    """
    createNumTable = f'CREATE OR REPLACE TABLE {NumTableName} AS \n WITH BASE AS (\
                    \n {textSQLNumTablesFromTable} \n UNION ALL \n {textSQLNumTablesCompareTable} \n) \n \
                    SELECT * FROM BASE ORDER BY OPERATION, TABLE_FROM'
    """    
    createNumFromTable = f'CREATE OR REPLACE TABLE {NumTableName}_FROM AS \n {textSQLNumTablesFromTable}'
    createNumCompareTable = f'CREATE OR REPLACE TABLE {NumTableName}_COMPARE AS \n {textSQLNumTablesCompareTable}'
    session.sql(createNumFromTable).collect()
    session.sql(createNumCompareTable).collect()
    
    # Varchar columns generation
    textSQLCharTablesFromTable =   FunctionGenerator(listCols = dictColumnsFromTable['VARCHAR'],tableName = from_table, dictFunctions = charDictFunctions, isNum = False)
    textSQLCharTablesCompareTable =   FunctionGenerator(listCols = dictColumnsCompareTable['VARCHAR'],tableName = compare_table, dictFunctions = charDictFunctions, isNum = False)
    CharTableName = f'RCM.RCM_BUSINESS_DV.COMPARING_{to_table}_VARCHAR'
    """
    createCharTable = f'CREATE OR REPLACE TABLE {CharTableName} AS \n WITH BASE AS (\
                    \n {textSQLCharTablesFromTable} \n UNION ALL \n {textSQLCharTablesCompareTable} \n) \n \
                    SELECT * FROM BASE ORDER BY OPERATION, TABLE_FROM'
    """
    createCharFromTable = f'CREATE OR REPLACE TABLE {CharTableName}_FROM AS \n {textSQLCharTablesFromTable}'
    createCharCompareTable = f'CREATE OR REPLACE TABLE {CharTableName}_COMPARE AS \n {textSQLCharTablesCompareTable}'
    session.sql(createCharFromTable).collect()
    session.sql(createCharCompareTable).collect()
    
    # Date columns generation
    textSQLDateTablesFromTable =   FunctionGenerator(listCols = dictColumnsFromTable['DATE'],tableName = from_table, dictFunctions = dateDictFunctions, isNum = False)
    textSQLDateTablesCompareTable =   FunctionGenerator(listCols = dictColumnsCompareTable['DATE'],tableName = compare_table, dictFunctions = dateDictFunctions, isNum = False)
    DateTableName = f'RCM.RCM_BUSINESS_DV.COMPARING_{to_table}_DATE'
    """
    createDateTable = f'CREATE OR REPLACE TABLE {DateTableName} AS \n WITH BASE AS (\
                    \n {textSQLDateTablesFromTable} \n UNION ALL \n {textSQLDateTablesCompareTable} \n) \n \
                    SELECT * FROM BASE ORDER BY OPERATION, TABLE_FROM'
    """
    createDateFromTable = f'CREATE OR REPLACE TABLE {DateTableName}_FROM AS \n {textSQLDateTablesFromTable}'
    createDateCompareTable = f'CREATE OR REPLACE TABLE {DateTableName}_COMPARE AS \n {textSQLDateTablesCompareTable}'
    session.sql(createDateFromTable).collect()
    session.sql(createDateCompareTable).collect()
    


    return DateTableName
