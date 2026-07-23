# dbo.Employees

## Система-источник

_TODO: указать систему-источник_

## Описание таблицы

Справочник сотрудников (аналитиков, ОКК и др.).

## Связи с другими таблицами

- `Email` — ключ связи практически со всеми остальными ODS-таблицами процесса (например, `dbo.Reports.Analytic`, `dbo.GetDocCompareReport.analytic`/`okk`, `dbo.GetSupportMailReport.analytic`/`okk`).

## Описание колонок

| Колонка | Тип | Описание | Пример данных |
| :--- | :--- | :--- | :--- |
| `FullName` | nvarchar(100) | _TODO_ | Гребенкина Надежда (oper145@pssolution.ru), Левченкова Анастасия (oper130@pssolution.ru), TCC1104Хамзатов Сабур (TCC1104@pssolution.ru), TCC5040Смирнов  Антон (TCC5040@pssolution.ru), TCC4007Забродская Василина  (TCC4007@pssolution.ru) |
| `Name` | nvarchar(100) | _TODO_ | Хашиева Хади, Ларин Алексей, Рожкова Гульназ, Золотилина Елена, Осокина Олеся |
| `Email` | nvarchar(100) | _TODO_ | TCC310@pssolution.ru, TCC614@pssolution.ru, oper35@pssolution.ru, TCC4004@pssolution.ru, TCC911@pssolution.ru |
| `Status` | nvarchar(100) | _TODO_ | тсс 1400, тсс 1100, тсс 1700, штат, тсс 2500 |
| `Position` | nvarchar(100) | _TODO_ | ТСС, ТСС, ТСС, ТСС, ТСС |
| `IncludedInProcessing` | nvarchar(100) | _TODO_ | да, да, да, да, да |
| `Id` | int | _TODO_ | 143, 105, 126, 61, 215 |

## Дата создания документа

23.07.2026

## Кем создан

_TODO_
