SET NOCOUNT ON;

IF OBJECT_ID('tempdb..#ColumnInfo') IS NOT NULL DROP TABLE #ColumnInfo;

CREATE TABLE #ColumnInfo
(
    SchemaName        SYSNAME,
    TableName         SYSNAME,
    ColumnName        SYSNAME,
    ColumnPosition    INT,
    DataType          NVARCHAR(128),
    MaxLength         INT,
    NumericPrecision  TINYINT,
    NumericScale      INT,
    IsNullable        NVARCHAR(3),
    DefaultValue      NVARCHAR(4000),
    SampleValues      NVARCHAR(1000)
);

INSERT INTO #ColumnInfo
    (SchemaName, TableName, ColumnName, ColumnPosition, DataType,
     MaxLength, NumericPrecision, NumericScale, IsNullable, DefaultValue)
SELECT
    t.TABLE_SCHEMA,
    t.TABLE_NAME,
    c.COLUMN_NAME,
    c.ORDINAL_POSITION,
    c.DATA_TYPE,
    c.CHARACTER_MAXIMUM_LENGTH,
    c.NUMERIC_PRECISION,
    c.NUMERIC_SCALE,
    c.IS_NULLABLE,
    c.COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.TABLES t
JOIN INFORMATION_SCHEMA.COLUMNS c
    ON t.TABLE_SCHEMA = c.TABLE_SCHEMA
    AND t.TABLE_NAME = c.TABLE_NAME
WHERE t.TABLE_TYPE = 'BASE TABLE';

-- Заполняем примеры значений (динамический SQL, т.к. имена объектов заранее неизвестны)
DECLARE @SchemaName SYSNAME, @TableName SYSNAME, @ColumnName SYSNAME, @DataType NVARCHAR(128);
DECLARE @sql NVARCHAR(MAX), @result NVARCHAR(1000);

DECLARE col_cursor CURSOR LOCAL FAST_FORWARD FOR
    SELECT SchemaName, TableName, ColumnName, DataType FROM #ColumnInfo;

OPEN col_cursor;
FETCH NEXT FROM col_cursor INTO @SchemaName, @TableName, @ColumnName, @DataType;

WHILE @@FETCH_STATUS = 0
BEGIN
    SET @result = NULL;

    IF @DataType NOT IN ('xml','geography','geometry','hierarchyid','sql_variant','image','timestamp','rowversion')
    BEGIN
        BEGIN TRY
            SET @sql = N'
                SELECT @res = (
                    SELECT STRING_AGG(CAST(val AS NVARCHAR(200)), '', '')
                    FROM (
                        SELECT TOP 5 ' + QUOTENAME(@ColumnName) + N' AS val
                        FROM ' + QUOTENAME(@SchemaName) + N'.' + QUOTENAME(@TableName) + N'
                        WHERE ' + QUOTENAME(@ColumnName) + N' IS NOT NULL
                        ORDER BY NEWID()
                    ) x
                );';

            EXEC sp_executesql @sql, N'@res NVARCHAR(1000) OUTPUT', @res = @result OUTPUT;
        END TRY
        BEGIN CATCH
            SET @result = 'N/A (' + ERROR_MESSAGE() + ')';
        END CATCH
    END
    ELSE
        SET @result = 'N/A (unsupported type)';

    UPDATE #ColumnInfo
    SET SampleValues = @result
    WHERE SchemaName = @SchemaName AND TableName = @TableName AND ColumnName = @ColumnName;

    FETCH NEXT FROM col_cursor INTO @SchemaName, @TableName, @ColumnName, @DataType;
END

CLOSE col_cursor;
DEALLOCATE col_cursor;

SELECT *
FROM #ColumnInfo
ORDER BY SchemaName, TableName, ColumnPosition;