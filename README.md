-- Добавление новой записки/напоминания 
curl -X POST -H 'Content-Type:application/json' -d '{"description":"You added me!"}' http://localhost:8000/todos/
-- Запрос всех созданных напоминаний 
curl -X POST -H 'Content-Type:application/json'
-- Удаление записи (добавление id в ссылке)
 curl -X DELETE -H 'Content-Type:application/json' -d '{"description":"test11"}' http://localhost:8000/todos/1 
 -- Изменение записи (добавление id в ссылке)
 curl -X PUT -H 'Content-Type:application/json' -d '{"description":"test12", "is_done":"True"}' http://localhost:8000/todos/2
