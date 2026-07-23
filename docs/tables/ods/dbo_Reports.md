# dbo.Reports

## Система-источник

_TODO: указать систему-источник_

## Описание таблицы

_TODO: заполнить описание таблицы_

## Описание колонок

| Колонка | Тип | Описание | Пример данных |
| :--- | :--- | :--- | :--- |
| `DocId` | int | _TODO_ | 9496883, 9611947, 9614303, 9640083, 9424332 |
| `DocDate` | date | _TODO_ | 2026-05-14, 2026-06-06, 2026-06-19, 2026-05-02, 2026-05-07 |
| `StartWorkDateTime` | datetime | _TODO_ | июл 21 2026  5:06PM, май 15 2026  5:50AM, июн 14 2026  2:40PM, май 21 2026  1:46PM, июн 13 2026  7:25PM |
| `Analytic` | varchar(50) | _TODO_ | TCC7002@pssolution.ru, oper105@pssolution.ru, TCC431@pssolution.ru, TCC715@pssolution.ru, TCC1225@pssolution.ru |
| `Company` | varchar(50) | _TODO_ | ЛУНП, ЛЮНП, ЛЦНП, ЛУНП, ЛЮНП |
| `SubdivisionType` | varchar(10) | _TODO_ | RBA, RBA, RBA, RBA, RBA |
| `Subdivision` | varchar(70) | _TODO_ | 52100, 47253, 30669, 12013, 33215 |
| `TimeSlotType` | varchar(50) | _TODO_ | ЗапД, Опер Кафе, Помощник, Опер Кафе, Опер Кафе |
| `DocStatus` | varchar(50) | _TODO_ | Передан в ЛК, Невозможно обработать, Невозможно обработать, Невозможно обработать, Невозможно обработать |
| `DocType` | varchar(50) | _TODO_ | Рабочий, Рабочий, Рабочий, Рабочий, Рабочий |
| `Reason` | varchar(200) | _TODO_ | Аналитик - нет клиентов,  нет видеоархива,  разрывы/зависания видео,  нет видеоархива,  Подтв. отсутствие сотрудника |
| `WorkTime` | float | _TODO_ | 0, 0, 0.07, 0.17, 2.28 |
| `InfrCount` | int | _TODO_ | 1, 0, 5, 2, 0 |
| `ConsultCount` | int | _TODO_ | 3, 0, 3, 0, 2 |
| `TimeSlotBeg` | datetime | _TODO_ | май 26 2026  3:51AM, июн  4 2026  2:43AM, май 21 2026 11:09AM, июл  6 2026  9:12AM, июн 27 2026  8:50PM |
| `TimeSlotEnd` | datetime | _TODO_ | май 21 2026  1:47AM, июл 16 2026  4:40PM, июн 23 2026 10:27AM, май 12 2026  6:30PM, июл  2 2026 10:04AM |
| `TimeSlotDuration` | varchar(50) | _TODO_ | 60, 60, 60, 60, 60 |
| `AnalyticRemark` | varchar(1024) | _TODO_ | 17:22:03 нет топлива, нет топлива, разрывы, 19:12:50*улыбка в 19:13:20, ускоренная речь |
| `AnalyticGroup` | varchar(50) | _TODO_ | штат, ТСС, ТСС, ТСС, ТСС |
| `SubdivisionGroup` | varchar(50) | _TODO_ | 2, 3, 2, 3, 1 |
| `Period2` | varchar(4) | _TODO_ | День, День, День, День, День |
| `SubdivisionId` | bigint | _TODO_ | 5234, 2890, 3616, 3970, 4657 |
| `key2` | varchar(120) | _TODO_ | ЛУНП86643, ЛУНП74432, TEBOIL11175, TEBOIL11077, ЛУНП72319 |

## Дата создания документа

23.07.2026

## Кем создан

_TODO_
